

from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import GyroSensor, INPUT_2


gyro_sensor = GyroSensor(INPUT_2)
move_tank = MoveTank(OUTPUT_B, OUTPUT_C)

# repeat 4 times.
# Make it move with while loop (in a forward motion for about a second)
# Get current gyro sensor measurment
# Stop. Start accelerating one wheel, stopping the second
# While loop to check gyro sensor - previous (if 90 stop)
