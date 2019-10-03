class Settings():
	"""储存所有设置的类"""

	def __init__(self):
		"""初始化游戏设置"""
		#屏幕设置
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)

		#飞船的设置
		self.ship_speed_factor = 20

		#子弹设置
		self.bullet_speed_factor = 40
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullets_allowed = 10

		#外星人设置
		self.alien_speed_factor = 20
		self.fleet_drop_speed = 20	#撞到边缘时 向下移动速度
		#fleet_direction为1表示向右移，为-1表示向左移
		self.fleet_direction = 1


		#飞船设置
		self.ship_speed_factor = 30
		self.ship_limit = 3

		#以什么样的速度加快游戏节奏
		self.speedup_scale = 1.5
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""初始化随游戏进行而变化的设置"""
		self.ship_speed_factor = 25
		self.bullet_speed_factor = 25
		self.alien_speed_factor = 20

		#fleet_direction为1表示向右；为-1表示向左
		#self.fleet_direction = 1

		#记分
		self.alien_points = 50

	def increase_speed(self):
		"""提高速度设置"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

































