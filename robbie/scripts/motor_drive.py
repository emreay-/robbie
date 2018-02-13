import json
from typings import Tuple

import pigpio

direction_type = int
velocity_type = int
motor_command_type = Tuple[direction_type, velocity_type]
drive_command_type = Tuple[motor_command_type, motor_command_type]


class DifferentialDrive(object):

    def __init__(self, pin_setup: str, drive_config: str):
        self.load_pins(pin_setup)
        self.load_config(drive_config)
        self.setup_gpio()

    def load_pins(self, pin_setup: str):
        with open(pin_setup, 'r') as handle:
            self.pins = json.load(handle)

    def load_config(self, drive_config: str):
        with open(drive_config, 'r') as handle:
            self.config = json.load(handle)

    def setup_gpio(self):
        self.pi = pigpio.pi()
        for pin in self.pins.values():
            self.pi.set_mode(pin, pigpio.OUTPUT)
    
    def drive(self, command: drive_command_type):
        (left_motor_command, right_motor_command) = command
        send_motor_command(left_motor_command, motor='left')
        send_motor_command(right_motor_command, motor='right')

    def send_motor_command(self, command: motor_command, motor: str):
        if motor not in ['left', 'right']:
            return

        motor_enable = '{}_motor_enable'.format(motor)
        motor_A = '{}_motor_A'.format(motor)
        motor_B = '{}_motor_B'.format(motor)
        (direction, velocity) = command
        direction = self.direction_to_str(direction)

        self.pi.set_PWM_dutycycle(self.pins[enable], velocity)
        self.pi.write(self.pins[motor_A], self.config[motor][direction][motor_A])
        self.pi.write(self.pins[motor_B], self.config[motor][direction][motor_B])

    @staticmethod
    def direction_to_str(direction: direction_type):
        return {1: 'forward', -1: 'backward'}.get(direction, 'stationary')
    