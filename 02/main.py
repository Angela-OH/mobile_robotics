# # Demo of a simple proportional line follower using two sensors
# # It's deliberately flawed and will exit with errors in some circumstances;
# # try fixing it!

# import math
# from time import sleep

from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import
# from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
# from ev3dev2.sensor.lego import ColorSensor, GyroSensor, UltrasonicSensor

import math
move_tank = MoveTank(OUTPUT_B, OUTPUT_C)

# colorLeft = ColorSensor(INPUT_2)
# colorRight = ColorSensor(INPUT_3)
# gyro = GyroSensor(INPUT_4)
# ultrasonic = UltrasonicSensor(INPUT_1)

# GAIN = 0.5


wheel_size = 56
distance_beteween_wheels = 180

outer_wheel_travel = (math.pi * distance_beteween_wheels * 2)/4
distance_per_rotation = math.pi * wheel_size * 2

rotations_of_outer_wheel = outer_wheel_travel/distance_per_rotation

print(rotations_of_outer_wheel)

while True:
    move_tank.on_for_rotations(100, 0, rotations_of_outer_wheel)
    move_tank.on_for_rotations(100, 10, 1)
