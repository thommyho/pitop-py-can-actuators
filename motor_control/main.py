from pitop.robotics.drive_controller import DriveController
from time import sleep
_drive_controller = DriveController(left_motor_port="M3", right_motor_port="M0")
_drive_controller.target_lock_drive_angle(30)
sleep(10)