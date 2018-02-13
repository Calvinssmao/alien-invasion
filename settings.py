#encoding=utf-8
class Settings(object):
	"""存储alien invasion的所有设置的类"""

	def __init__(self):
		"""初始化游戏的静态设置"""
		self.screen_width = 1000        #屏幕长
		self.screen_height = 600        #屏幕宽
		self.bg_color = (230, 230, 230) #设置背景颜色

		"""飞船设置"""
		self.ship_limit = 3             #飞船的数量设置

		"""子弹设置""" 
		self.bullet_width = 3           #子弹的宽
		self.bullet_height = 15         #子弹的长
		self.bullet_color = 60, 60, 60  #子弹的颜色
		self.bullets_allowed = 3        #屏幕上允许的最大子弹数量

		"""外星人设置"""
		self.fleet_drop_speed = 10      #外星人的下落速度设置

		# 加快游戏节奏的速度
		self.speedup_scale = 1.1
		# 外星人点数的提高速度
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""初始化随游戏进行而变化的设置"""
		self.ship_speed_factor = 1.5    #飞船的速度设置
		self.bullet_speed_factor = 3    #子弹的速度设置
		self.alien_speed_factor = 1     #外星人的速度设置

		self.fleet_direction = 1        #外星人的移动方向, 1表示向右;-1表示向左
		# 计分
		self.alien_points = 50

	def increase_speed(self):
		"""提高速度设置和外星人点数"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale) 
		print(self.alien_points)


		