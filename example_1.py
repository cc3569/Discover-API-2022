#!/usr/bin/env python3

from rover_api.discover_rover import Rover
from rover_api.discover_camera import Camera

def main_ex():
    rover1 = Rover()
    cam1 = Camera()
    rover1.move_forward(0.5, 5)
    rover1.move_backward(0.5, 5)
    rover1.turn_left(45, 0.5)
    rover1.turn_right(45, 0.5)
    
if __name__ == '__main__':
    main_ex()
