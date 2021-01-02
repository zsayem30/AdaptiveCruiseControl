from implementation import *
import numpy as np
import matplotlib.pyplot as plt

set_alpha = [1,0.1,0.01,0.001]
d_target = 80
initial_d = 120
initial_v = 30
noise_lvl = 0.5
their_velocity =  [ 20 for _ in range( 1000 ) ]
time_step = np.linspace(0,1000,1)

for i in range(len(set_alpha)):
    none1 = "\images\none"+str(set_alpha[i])+".png"
    plt.plot(run_control_simulation(set_alpha[i],d_target,initial_d,initial_v,their_velocity))
    # naming the x axis
    plt.xlabel('Time Step')
    # naming the y axis
    plt.ylabel('Distance')
    # giving a title to my graph
    plt.title('None, alpha ='+str(set_alpha[i]))
    plt.show()
    # plt.savefig('C:\Users\sayem\Documents\ENPH 2020WT1\ELEC 221\Plots\runCtrSim_'+str(set_alpha[i])+'.png')

    plt.plot(run_clipped_control_simulation(set_alpha[i],d_target, initial_d, initial_v, their_velocity))
    # naming the x axis
    plt.xlabel('Time Step')
    # naming the y axis
    plt.ylabel('Distance')
    # giving a title to my graph
    plt.title('Clipped, alpha =' + str(set_alpha[i]))
    # plt.savefig('C:\Users\sayem\Documents\ENPH 2020WT1\ELEC 221\clippedCtrSim_' + str(set_alpha[i]) + '.png')
    plt.show()

    plt.plot(run_noisy_control_simulation(set_alpha[i],d_target, initial_d, initial_v, their_velocity,noise_lvl))
    # naming the x axis
    plt.xlabel('Time Step')
    # naming the y axis
    plt.ylabel('Distance')
    # giving a title to my graph
    plt.title('Noise Included, alpha =' + str(set_alpha[i]))
    plt.show()

    # # plt.savefig("C:\Users\sayem\Documents\ENPH 2020WT1\ELEC 221\Plots\noisyClippedRunCtrSim_" + str(set_alpha[i]) + ".png")