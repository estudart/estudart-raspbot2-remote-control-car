import time, math

from Raspbot_Lib import Raspbot, LightShow


class RemoteControlAdapter:
	def __init__(self):
		self.bot = Raspbot()
	
	def get_ir_value(self):
		data = self.bot.read_data_array(0x0c, 1)
		data_to_hex = hex(data[0])
		return data_to_hex
	
	def enable_ir_receiver(self):
		self.bot.Ctrl_IR_Switch(1)
	
	def disbale_ir_receiver(self):
		self.bot.Ctrl_IR_Switch(0)
