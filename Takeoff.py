#import libraries
from dronekit import *
import time

#connect to vehicle
vehicle = connect('127.0.0.1:14551',baud=921600,wait_ready=True)

#takeoff function
def arm_takeoff(height):
    #check if drone is ready
    while not vehicle.is_armable:
        print("waiting for drone")
        time.sleep(1)

    #change mode and arm
    print("arming")
    vehicle.mode=VehicleMode('GUIDED')
    vehicle.armed=True
    
    #check if drone is armed
    while not vehicle.armed:
        print("Waiting for arm")
        time.sleep(1)

    #takeoff
    print("takeoff")
    vehicle.simple_takeoff(height)

    #report values back every 1s and finally break out
    while True:
        print('Reached ',vehicle.location.global_relative_frame.alt)
        if(vehicle.location.global_relative_frame.alt>=height*0.95):
            print("Reached Target Altitude")
            break
        time.sleep(1)

arm_takeoff(10)

#hover for 10sec
time.sleep(10)

#landing
print('Land')
vehicle.mode=VehicleMode('RTL')
time.sleep(20)

#close vehicle
vehicle.close()