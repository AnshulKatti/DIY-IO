from curses import baudrate
from cv2 import connectedComponents

from dronekit import *

vehicle=connect("127.0.0.1:14551",baud=921600,wait_ready=True)

print(vehicle.mode)

print(vehicle.is_armable)

print(vehicle.armed)
