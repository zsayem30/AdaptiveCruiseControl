# AdaptiveCruiseControl
The dynamics of a vehicle can be viewed as a system that transforms the force applied to the vehicle (via the
engine) into the velocity of the vehicle. This is another way of saying that as long as other factors such as the drag
coefcient and the rolling coefcient of friction are constant, only the initial speed and the force of the engine for
all time thereafter are necessary to determine the velocity of the vehicle for all time.
This is an implementation of a 1D cruise control using continuous time and discrete time state space functions and control law. Non ideal behaviours where also accounted for where there were limitations on the maximum velocity and acceleration that vehicles can acheive.
