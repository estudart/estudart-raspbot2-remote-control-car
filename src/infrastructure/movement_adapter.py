import time, math

import sys
sys.path.append('/home/pi/project_demo/lib')
from McLumk_Wheel_Sports import *

'''
In the future the idea is code our own moving methods
out of Raspbot.Ctrl_Muto()
'''
class MovementAdapter:
	def move(self, direction, speed):
		if   direction == 'CarForward':   move_forward(speed)
		elif direction == 'CarBackward':  move_backward(speed)
		elif direction == 'CarLeft':      move_left(speed)
		elif direction == 'CarRight':     move_right(speed)
		elif direction == 'CarLeftSpin':  rotate_left(speed)
		elif direction == 'CarRightSpin': rotate_right(speed)

	def stop_robot(self):
		stop_robot()
