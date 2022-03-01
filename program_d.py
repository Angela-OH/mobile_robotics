from ev3dev2.sensor.lego import TouchSensor, ColorSensor, UltrasonicSensor, GyroSensor
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sound import Sound
from ev3dev2.display import Display
from ev3dev2.button import Button


def main():
    """Declare all inputs and outputs we are using."""
    # Outputs
    left_wheel = OUTPUT_A
    right_wheel = OUTPUT_B
    # Inputs
    input_color = INPUT_1
    input_gyro = INPUT_2
    input_touch = INPUT_3
    input_ultrasonic = INPUT_4

    """Create classes"""
    move = MoveTank(left_wheel, right_wheel)
    gyro = GyroSensor(input_gyro)
    color = ColorSensor(input_color)
    touch = TouchSensor(input_touch)
    ultrasonic = UltrasonicSensor(input_ultrasonic)

    """For feedback from the robot"""
    display = Display()
    sound = Sound()
    button = Button()

    while ultrasonic.distance_centimeters() > 25:
        move.on(20, 20)

    while gyro.angle() < 180:
        move.on(50, 0)


if __name__ == '__main__':
    main()
