import os
import sys
import unittest
import tempfile
import shutil

current_path = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_path, os.pardir))
sys.path.insert(0, parent_dir)

import motor_drive


class MotorDriveTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
    