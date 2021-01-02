import numpy as np

def predict_collision( initial_distance, initial_velocity, list_of_forces):
    '''
        Given an initial distance between the two cars and an initial velocity of your car, this function 
        should predict the time of collision between your car and the car in front of you if your car is 
        subject to the force in "list_of_forces[n]" at each time step "n". This force is given in the units 
        of "car mass . m / s^2". The car in front of you is assumed to at rest. If there has been no collision 
        and the list of forces has been exhausted, the function should return 'None'.
    '''
    m = 1
    delT = 0.2
    bpm = 0.01
    b = 0.01
    mu = 0.01
    g = 10
    duration = len(list_of_forces)
    velocity = [0]*duration
    distance = [0]*duration
    F_adj = [0]*duration

    for i in range(duration):
        F_adj[i] = list_of_forces[i]-mu*m*g

    velocity[0] = initial_velocity
    distance[0] = initial_distance

    for i in range(duration-1):
        velocity[i+1] = (1-b*delT/m)*velocity[i]+(delT/m)*F_adj[i]
        distance[i+1] = distance[i]-delT*velocity[i]-(delT)**2*F_adj[i]/(2*m)+b*delT**2*velocity[i]/(2*m)
    for i in range (duration):
        if distance[i] <= 0:
            return i*delT
    return None


def run_control_simulation( alpha, setpoint, initial_distance, initial_velocity_ours, their_velocities ):
    '''
        Given a value for alpha and setpoint (in m) as well as the initial velocity of the controlled 
        vehicle (m/s) and initial distance between the controlled vehicle and the vehicle in front of it,
        use the state space model and the control law developed in the Assignment 2 document to calculate 
        d[n] given the trace v[n]. If v[n] (their_velocities) is a list of length N, then the function should
        return a list of length N where return_value[n] = d[n].
    '''
    m = 1
    delT = 0.2
    bpm = 0.01
    b = 0.01
    mu = 0.01
    g = 10
    c1 = 2*m*alpha/(delT)**2  #0.5
    c2 = 1-b*delT/(2*m)  #0.999
    duration = len(their_velocities)
    velocity = [0] * (duration+1)
    distance = [0] * (duration+1)
    F_adj = [0] * (duration)
    velocity[0] = initial_velocity_ours
    distance[0] = initial_distance
    for i in range(duration):
        F_adj[i] = c1*((distance[i]-setpoint)+(their_velocities[i]-c2*velocity[i])*delT)
        distance[i+1] = distance[i]+delT*their_velocities[i]-delT*velocity[i]-(delT)**2*F_adj[i]/(2*m)+b*delT**2*velocity[i]/(2*m)
        velocity[i+1] = (1-b*delT/m)*velocity[i]+(delT/m)*F_adj[i]

    return distance

def run_clipped_control_simulation( alpha, setpoint, initial_distance, initial_velocity_ours, their_velocities ):
    '''
        Implement the description of 'run_control_simulation' with the additional feature that if the force
        determined by the control law (F_tilde) is greater than 7 car mass . m / s^2 or less than -10 car mass . m / s^2
        then it should be 'clipped' to 7 car mass . m / s^2 or -10 car mass . m / s^2 respectively.
        (this simulates a scenario where a vehicle has a maximum amount of acceleration/braking power)
    '''
    upperLimit = 7
    lowerLimit = -10
    m = 1
    delT = 0.2
    bpm = 0.01
    b = 0.01
    mu = 0.01
    g = 10
    c1 = 2 * m * alpha / (delT) ** 2  # 0.5
    c2 = 1 - b * delT / (2 * m)  # 0.999
    duration = len(their_velocities)
    velocity = [0] * (duration + 1)
    distance = [0] * (duration + 1)
    F_adj = [0] * (duration)
    velocity[0] = initial_velocity_ours
    distance[0] = initial_distance
    for i in range(duration):
        F_adj[i] = c1 * ((distance[i] - setpoint) + (their_velocities[i] - c2 * velocity[i]) * delT)
        F_adj[i] = min(upperLimit*m,F_adj[i])
        F_adj[i] = max(lowerLimit*m, F_adj[i])
        distance[i + 1] = distance[i] + delT * their_velocities[i] - delT * velocity[i] - (delT) ** 2 * F_adj[i] / (
                    2 * m) + b * delT ** 2 * velocity[i] / (2 * m)
        velocity[i + 1] = (1 - b * delT / m) * velocity[i] + (delT / m) * F_adj[i]

    return distance

def run_noisy_control_simulation( alpha, setpoint, initial_distance, initial_velocity_ours, their_velocities, noise_level ):
    '''
        Implement the description of 'run_clipped_control_simulation' with the addition of sensor noise. In 
        the control law, multiply their velocity by exp(X) where X is a Gaussian random variable with a mean of 0 
        and a standard deviation of `noise_level`. You can use the `numpy.random.randn()` function which 
        generates a random variable with mean of 0 and a standard deviation of 1 and multiply that value by 
        `noise_level` to get a random value which is a Gaussian random variable with a mean of 0 and a standard deviation
        of `noise_level`.

        Within the state space model, you should use the "real" value of their velocity (i.e. without the random multiplication factor)
    '''
    their_velocities = [i * np.exp(np.random.randn()) * noise_level for i in their_velocities]
    distance = run_clipped_control_simulation(alpha,setpoint,initial_distance,initial_velocity_ours,their_velocities)
    return distance