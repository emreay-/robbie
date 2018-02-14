import os

from pynput.keyboard import Key, Listener

from robbie.scripts.motor_drive import DifferentialDrive


class KeyCommand(object):
    forward = Key.up
    backward = Key.down
    left = Key.left
    right = Key.right
    stop = Key.esc
    commands = {forward: ((1, 250), (1, 250)), 
                backward: ((-1, 250), (-1, 250)),
                left: ((-1, 250), (1, 250)),
                right: ((1, 250), (-1, 250)),
                stop: ((0, 0), (0, 0))}


class Teleop(object):

    def __init__(self, pin_setup: str = None, drive_config: str = None):
        self.differential_driver = DifferentialDrive(pin_setup, drive_config)
        self.reset_motor_command()

    def reset_motor_command(self):
        self.motor_command = ((0, 0), (0, 0))

    def run(self):
        with Listener(on_press=self.key_pressed, 
                      on_release=self.key_released) as listener:
            listener.join()

    def key_pressed(self, key):
        self.motor_command = KeyCommand.commands[key]
        self.differential_driver.drive(self.motor_command)

    def key_released(self, key):
        self.reset_motor_command()
        self.differential_driver.drive(self.motor_command)


if __name__ == '__main__':
    param_dir = os.getenv('ROBBIE_PARAM_DIR')
    pin_setup = os.path.join(param_dir, 'pin_setup.json')
    drive_config = os.path.join(param_dir, 'drive_config.json')

    teleop = Teleop(pin_setup, drive_config)
    teleop.run()
    
