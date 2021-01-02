from implementation import *

def collision_no_acceleration_test():
    forces_input = [ 0 for _ in range( 1000 ) ]
    distance_input = 600 # meters
    velocity_input = 40  # meters per second 

    time_of_collision =  predict_collision( distance_input, velocity_input, forces_input )

    if time_of_collision == None:
        print( 'Test Failed: Expected a collision' )
        return False

    if 16.6 <= time_of_collision and 17.0 >= time_of_collision:
        return True
    else:
        print( 'Test Failed: Expected time of collision near 16.8 seconds' )
        return False

def collision_no_acceleration_no_collision_test():
    forces_input = [ 0 for _ in range( 10 ) ]
    distance_input = 60 # meters
    velocity_input = 20 # meters per second 

    time_of_collision = predict_collision( distance_input, velocity_input, forces_input )

    if time_of_collision == None:
        return True
    else:
        print( 'Test Failed: Expected no collision at all' )
        return False

def collision_uniform_acceleration_test():
    forces_input = [ 4 for _ in range( 1000 ) ]
    distance_input = 1200 # meters
    velocity_input = 20   # meters per second 

    time_of_collision = predict_collision( distance_input, velocity_input, forces_input )

    if time_of_collision == None:
        print( 'Test Failed: Expected a collision' )
        return False

    if 21.0 <= time_of_collision and 21.4 >= time_of_collision:
        return True
    else:
        print( 'Test Failed: Expected time of collision near 21.2 seconds' )
        return False

def collision_negative_acceleration_test():
    forces_input = [ -0.3 for _ in range( 1000 ) ]
    distance_input = 600 # meters
    velocity_input = 40  # meters per second 

    time_of_collision = predict_collision( distance_input, velocity_input, forces_input )

    if time_of_collision == None:
        print( 'Test Failed: Expected a collision' )
        return False

    if 18.0 <= time_of_collision and 18.4 >= time_of_collision:
        return True
    else:
        print( 'Test Failed: Expected time of collision near 18.2 seconds' )
        return False

def collision_increasing_acceleration_test():
    forces_input = [ 0.007 * i for i in range( 1000 ) ]
    distance_input = 600 # meters
    velocity_input = 20  # meters per second 

    time_of_collision = predict_collision( distance_input, velocity_input, forces_input )

    if time_of_collision == None:
        print( 'Test Failed: Expected a collision' )
        return False

    if 29.0 <= time_of_collision and 29.4 >= time_of_collision:
        return True
    else:
        print( 'Test Failed: Expected time of collision near 29.2 seconds' )
        return False

def control_step_test():
    setpoint         = 80
    initial_velocity = 30
    initial_distance = 120
    alpha            = 0.01

    velocity_trace = [ 20 for _ in range( 1000 ) ]

    distance_trace = run_control_simulation( alpha, setpoint, initial_distance, initial_velocity, velocity_trace )
    expected_trace = [120, 117.63, 114.54, 110.8, 106.5, 101.73, 96.59, 91.19, 85.64, 80.05, 74.53, 69.19, 64.15, 59.49, 55.3, 51.67, 48.65, 46.31, 44.67, 43.77, 43.61, 44.19, 45.49, 47.47, 50.08, 53.27, 56.96, 61.08, 65.54, 70.24, 75.08, 79.98, 84.82, 89.52, 93.97, 98.11, 101.84, 105.09, 107.82, 109.96, 111.48, 112.37, 112.61, 112.19, 111.15, 109.5, 107.3, 104.58, 101.41, 97.85, 93.99, 89.91, 85.68, 81.4, 77.15, 73.02, 69.08, 65.41, 62.09, 59.18, 56.72, 54.77, 53.36, 52.5, 52.21, 52.48, 53.31, 54.68, 56.54, 58.86, 61.57, 64.64, 67.98, 71.53, 75.21, 78.96, 82.69, 86.32, 89.8, 93.05, 96.0, 98.61, 100.82, 102.59, 103.9, 104.73, 105.06, 104.89, 104.23, 103.11, 101.54, 99.57, 97.24, 94.6, 91.71, 88.63, 85.42, 82.14, 78.87, 75.68, 72.61, 69.74, 67.11, 64.78, 62.79, 61.18, 59.97, 59.18, 58.83, 58.91, 59.43, 60.35, 61.67, 63.34, 65.33, 67.61, 70.11, 72.78, 75.58, 78.44, 81.3, 84.12, 86.82, 89.36, 91.7, 93.77, 95.56, 97.02, 98.14, 98.88, 99.24, 99.23, 98.84, 98.08, 96.98, 95.56, 93.85, 91.9, 89.74, 87.41, 84.98, 82.48, 79.97, 77.5, 75.12, 72.87, 70.8, 68.94, 67.34, 66.02, 65.0, 64.3, 63.93, 63.89, 64.19, 64.8, 65.72, 66.93, 68.38, 70.06, 71.93, 73.94, 76.06, 78.24, 80.44, 82.61, 84.71, 86.7, 88.53, 90.19, 91.63, 92.82, 93.75, 94.41, 94.78, 94.85, 94.64, 94.14, 93.37, 92.35, 91.11, 89.67, 88.06, 86.31, 84.47, 82.57, 80.64, 78.74, 76.89, 75.13, 73.5, 72.03, 70.74, 69.66, 68.81, 68.2, 67.84, 67.74, 67.89, 68.29, 68.93, 69.79, 70.85, 72.08, 73.47, 74.99, 76.59, 78.25, 79.93, 81.6, 83.23, 84.78, 86.22, 87.53, 88.69, 89.66, 90.43, 91.0, 91.35, 91.47, 91.37, 91.05, 90.53, 89.8, 88.9, 87.84, 86.64, 85.33, 83.94, 82.5, 81.02, 79.56, 78.13, 76.76, 75.48, 74.31, 73.28, 72.41, 71.7, 71.18, 70.85, 70.71, 70.77, 71.02, 71.45, 72.06, 72.83, 73.74, 74.77, 75.9, 77.11, 78.37, 79.65, 80.94, 82.2, 83.4, 84.54, 85.57, 86.49, 87.28, 87.92, 88.4, 88.72, 88.87, 88.84, 88.65, 88.29, 87.78, 87.13, 86.35, 85.46, 84.48, 83.43, 82.34, 81.21, 80.09, 78.98, 77.92, 76.92, 75.99, 75.17, 74.47, 73.89, 73.44, 73.14, 72.99, 72.99, 73.14, 73.43, 73.86, 74.41, 75.08, 75.84, 76.69, 77.6, 78.55, 79.53, 80.52, 81.49, 82.43, 83.32, 84.13, 84.87, 85.5, 86.02, 86.43, 86.71, 86.86, 86.88, 86.77, 86.53, 86.18, 85.71, 85.14, 84.49, 83.75, 82.97, 82.13, 81.28, 80.42, 79.56, 78.74, 77.95, 77.23, 76.58, 76.01, 75.53, 75.16, 74.9, 74.75, 74.72, 74.8, 74.99, 75.28, 75.68, 76.16, 76.73, 77.36, 78.04, 78.76, 79.51, 80.27, 81.01, 81.74, 82.43, 83.08, 83.66, 84.17, 84.6, 84.93, 85.18, 85.32, 85.37, 85.31, 85.16, 84.91, 84.58, 84.17, 83.68, 83.14, 82.55, 81.92, 81.27, 80.61, 79.95, 79.31, 78.7, 78.13, 77.61, 77.16, 76.77, 76.46, 76.24, 76.1, 76.05, 76.08, 76.2, 76.41, 76.69, 77.04, 77.45, 77.92, 78.43, 78.98, 79.55, 80.12, 80.7, 81.26, 81.8, 82.31, 82.77, 83.17, 83.52, 83.8, 84.01, 84.14, 84.2, 84.18, 84.09, 83.92, 83.68, 83.38, 83.03, 82.63, 82.18, 81.71, 81.21, 80.71, 80.2, 79.71, 79.23, 78.79, 78.38, 78.02, 77.7, 77.45, 77.26, 77.13, 77.07, 77.08, 77.15, 77.29, 77.49, 77.74, 78.04, 78.39, 78.77, 79.18, 79.61, 80.06, 80.5, 80.93, 81.35, 81.75, 82.11, 82.43, 82.71, 82.94, 83.12, 83.24, 83.3, 83.31, 83.25, 83.14, 82.97, 82.76, 82.5, 82.2, 81.87, 81.51, 81.14, 80.75, 80.36, 79.98, 79.61, 79.26, 78.94, 78.65, 78.4, 78.19, 78.03, 77.92, 77.86, 77.85, 77.89, 77.98, 78.12, 78.3, 78.52, 78.78, 79.06, 79.37, 79.7, 80.03, 80.37, 80.71, 81.03, 81.34, 81.63, 81.89, 82.11, 82.3, 82.45, 82.55, 82.61, 82.63, 82.6, 82.53, 82.41, 82.26, 82.07, 81.85, 81.6, 81.33, 81.05, 80.76, 80.46, 80.17, 79.88, 79.61, 79.35, 79.12, 78.92, 78.75, 78.62, 78.52, 78.46, 78.44, 78.46, 78.52, 78.62, 78.75, 78.91, 79.1, 79.31, 79.54, 79.79, 80.04, 80.3, 80.56, 80.81, 81.05, 81.28, 81.48, 81.66, 81.81, 81.94, 82.03, 82.08, 82.1, 82.09, 82.05, 81.97, 81.86, 81.72, 81.56, 81.38, 81.18, 80.96, 80.74, 80.51, 80.29, 80.06, 79.85, 79.65, 79.47, 79.31, 79.17, 79.06, 78.98, 78.93, 78.9, 78.91, 78.94, 79.01, 79.1, 79.22, 79.36, 79.51, 79.69, 79.87, 80.07, 80.26, 80.46, 80.66, 80.84, 81.02, 81.18, 81.33, 81.45, 81.55, 81.63, 81.68, 81.7, 81.7, 81.67, 81.62, 81.54, 81.44, 81.33, 81.19, 81.04, 80.88, 80.71, 80.54, 80.36, 80.19, 80.03, 79.87, 79.73, 79.6, 79.49, 79.4, 79.33, 79.28, 79.25, 79.25, 79.27, 79.32, 79.38, 79.46, 79.57, 79.68, 79.81, 79.95, 80.1, 80.25, 80.4, 80.55, 80.7, 80.84, 80.96, 81.08, 81.18, 81.26, 81.32, 81.37, 81.39, 81.4, 81.38, 81.35, 81.29, 81.22, 81.14, 81.04, 80.92, 80.8, 80.68, 80.54, 80.41, 80.28, 80.15, 80.03, 79.92, 79.81, 79.73, 79.65, 79.59, 79.55, 79.53, 79.52, 79.53, 79.56, 79.6, 79.66, 79.74, 79.82, 79.92, 80.02, 80.13, 80.25, 80.37, 80.48, 80.59, 80.7, 80.8, 80.89, 80.97, 81.04, 81.09, 81.13, 81.16, 81.16, 81.16, 81.13, 81.1, 81.05, 80.98, 80.91, 80.83, 80.74, 80.64, 80.54, 80.44, 80.34, 80.24, 80.14, 80.05, 79.97, 79.9, 79.84, 79.79, 79.76, 79.73, 79.72, 79.73, 79.75, 79.78, 79.82, 79.87, 79.94, 80.01, 80.09, 80.17, 80.26, 80.35, 80.44, 80.52, 80.61, 80.68, 80.76, 80.82, 80.87, 80.92, 80.95, 80.97, 80.98, 80.98, 80.97, 80.94, 80.91, 80.86, 80.81, 80.75, 80.68, 80.6, 80.53, 80.45, 80.37, 80.3, 80.22, 80.15, 80.09, 80.03, 79.98, 79.94, 79.91, 79.89, 79.88, 79.88, 79.89, 79.91, 79.94, 79.98, 80.03, 80.08, 80.14, 80.2, 80.27, 80.34, 80.41, 80.47, 80.54, 80.6, 80.66, 80.71, 80.75, 80.79, 80.81, 80.83, 80.84, 80.85, 80.84, 80.82, 80.8, 80.76, 80.72, 80.68, 80.63, 80.57, 80.52, 80.46, 80.4, 80.34, 80.28, 80.23, 80.18, 80.13, 80.09, 80.06, 80.03, 80.01, 80.0, 80.0, 80.01, 80.02, 80.04, 80.07, 80.1, 80.14, 80.19, 80.23, 80.28, 80.34, 80.39, 80.44, 80.49, 80.54, 80.58, 80.62, 80.66, 80.69, 80.71, 80.73, 80.74, 80.74, 80.74, 80.73, 80.71, 80.69, 80.66, 80.62, 80.59, 80.54, 80.5, 80.46, 80.41, 80.36, 80.32, 80.28, 80.24, 80.2, 80.17, 80.14, 80.12, 80.11, 80.1, 80.09, 80.1, 80.11, 80.12, 80.14, 80.16, 80.19, 80.23, 80.26, 80.3, 80.34, 80.38, 80.42, 80.46, 80.49, 80.53, 80.56, 80.59, 80.61, 80.63, 80.65, 80.66, 80.66, 80.66, 80.65, 80.64, 80.62, 80.6, 80.58, 80.55, 80.52, 80.49, 80.45, 80.42, 80.38, 80.35, 80.31, 80.28, 80.26, 80.23, 80.21, 80.19, 80.18, 80.17, 80.17, 80.17, 80.17, 80.18, 80.19, 80.21, 80.23, 80.26, 80.28, 80.31, 80.34, 80.37, 80.4, 80.43, 80.46, 80.49, 80.52, 80.54, 80.56, 80.57, 80.59, 80.59, 80.6, 80.6, 80.59, 80.59, 80.57, 80.56, 80.54, 80.52, 80.5, 80.47, 80.45, 80.42, 80.39, 80.37, 80.34, 80.32, 80.29, 80.27, 80.26, 80.24, 80.23, 80.22, 80.22, 80.22, 80.22, 80.23, 80.24, 80.25, 80.27, 80.28, 80.3, 80.33, 80.35, 80.37, 80.39, 80.42, 80.44, 80.46, 80.48, 80.5, 80.52, 80.53, 80.54, 80.55, 80.55, 80.55, 80.55, 80.54, 80.54, 80.52, 80.51, 80.5, 80.48, 80.46, 80.44, 80.42, 80.4, 80.38, 80.36, 80.34, 80.32, 80.31, 80.29, 80.28, 80.27, 80.27, 80.26, 80.26, 80.26, 80.27, 80.27, 80.28, 80.29, 80.31, 80.32, 80.34, 80.35, 80.37, 80.39, 80.41, 80.43, 80.44, 80.46, 80.47, 80.48, 80.49, 80.5, 80.51, 80.51, 80.51, 80.51, 80.51, 80.5, 80.5, 80.49, 80.48, 80.46, 80.45, 80.43, 80.42, 80.4, 80.39, 80.37, 80.36, 80.34, 80.33, 80.32, 80.31, 80.3, 80.3, 80.29, 80.29, 80.29, 80.3, 80.3, 80.31, 80.31, 80.32] 

    if distance_trace == None or len( distance_trace ) != len( expected_trace ):
        print( f'Test Failed: Length of return value did not match expected length of {len( expected_trace )}' )
        return False

    total_error = sum( [ a - b for a, b in zip( distance_trace, expected_trace ) ] )

    if( total_error <= -2.0 or total_error >= 2.0 ):
        print( 'Test Failed: Error in distance trace exceeded the programmed tolerance' )
        return False

    return True

def control_ramp_test():
    setpoint         = 80
    initial_velocity = 30
    initial_distance = 120
    alpha            = 0.1

    velocity_trace  = [ 10 + 2 * i for i in range( 40 ) ]
    velocity_trace += [ 60 for _ in range( 80 ) ] 

    distance_trace = run_control_simulation( alpha, setpoint, initial_distance, initial_velocity, velocity_trace )
    expected_trace = [120, 112.41, 99.47, 84.32, 70.21, 59.86, 54.96, 55.94, 61.99, 71.4, 81.94, 91.39, 97.97, 100.66, 99.31, 94.61, 87.85, 80.57, 74.3, 70.18, 68.82, 70.21, 73.8, 78.64, 83.64, 87.78, 90.33, 90.93, 89.67, 86.98, 83.56, 80.16, 77.45, 75.92, 75.75, 76.83, 78.82, 81.24, 83.55, 85.3, 86.21, 80.78, 75.76, 72.12, 70.46, 70.89, 73.12, 76.52, 80.29, 83.65, 85.95, 86.85, 86.31, 84.58, 82.14, 79.54, 77.31, 75.88, 75.43, 75.97, 77.28, 79.02, 80.8, 82.26, 83.15, 83.33, 82.85, 81.87, 80.64, 79.43, 78.47, 77.94, 77.9, 78.3, 79.03, 79.89, 80.71, 81.33, 81.64, 81.61, 81.29, 80.76, 80.15, 79.6, 79.21, 79.03, 79.09, 79.35, 79.73, 80.15, 80.52, 80.76, 80.86, 80.79, 80.59, 80.32, 80.03, 79.79, 79.63, 79.59, 79.65, 79.8, 80.0, 80.19, 80.35, 80.45, 80.46, 80.41, 80.3, 80.16, 80.03, 79.92, 79.87, 79.86, 79.91, 79.99, 80.09, 80.18, 80.25, 80.28, 80.27] 

    if distance_trace == None or len( distance_trace ) != len( expected_trace ):
        print( f'Test Failed: Length of return value did not match expected length of {len( expected_trace )}' )
        return False

    total_error = sum( [ a - b for a, b in zip( distance_trace, expected_trace ) ] )

    if( total_error <= -2.0 or total_error >= 2.0 ):
        print( 'Test Failed: Error in distance trace exceeded the programmed tolerance' )
        return False

    return True

if __name__ == '__main__':
    from sys import argv
    argc = len( argv )

    if argc != 3:
        exit(1)

    if argv[1] == 'collision':
        if argv[2] == 'no_acceleration':
            exit( 0 if collision_no_acceleration_test() else 1 )
        elif argv[2] == 'no_acceleration_no_collision':
            exit( 0 if collision_no_acceleration_no_collision_test() else 1 )
        elif argv[2] == 'uniform_acceleration':
            exit( 0 if collision_uniform_acceleration_test() else 1 )
        elif argv[2] == 'negative_acceleration':
            exit( 0 if collision_negative_acceleration_test() else 1 )
        elif argv[2] == 'increasing_acceleration':
            exit( 0 if collision_increasing_acceleration_test() else 1 )

    if argv[1] == 'control':
        if argv[2] == 'step':
            exit( 0 if control_step_test() else 1 )
        elif argv[2] == 'ramp':
            exit( 0 if control_ramp_test() else 1 )
