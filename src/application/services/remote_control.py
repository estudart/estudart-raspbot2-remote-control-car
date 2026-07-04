from src.infrastructure.movement_adapter import MovementAdapter
from src.infrastructure.remote_control_adapter import RemoteControlAdapter


class RemoteControlService:
	def __init__(self):
		self.remote_control_adapter = RemoteControlAdapter()
		self.movement_adapter = MovementAdapter()
		self.speed = 20
		self.ir_to_string_map = {
			'0x1': 'CarForward',
			'0x9': 'CarBackward',
			'0x4': 'CarLeft',
			'0x6': 'CarRight',
			'0x8': 'CarLeftSpin',
			'0xa': 'CarRightSpin',
			'0x0': 'Power',
		}
		
	def run(self):
		try:
			self.remote_control_adapter.enable_ir_receiver()
			
			while True:
				ir_value = self.remote_control_adapter.get_ir_value()
				move_command = self.ir_to_string_map.get(ir_value)
				if move_command == 'Power':
					self.movement_adapter.stop_robot()
				self.movement_adapter.move(move_command, self.speed)
		
		except KeyboardInterrupt:
			self.movement_adapter.stop_robot()
				
