#encoding=utf-8
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	
	def __init__(self, ai_settings, screen):
		"""初始化飞船并设置其初始位置"""
		super(Ship, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# 加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		# 将每艘新飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom  = self.screen_rect.bottom

		# 在飞船的属性center中存储小数值
		self.center_x = float(self.rect.centerx)
		self.center_y = float(self.rect.centery)

		# 移动标志
		self.moving_right  = False
		self.moving_left   = False
		self.moving_top    = False
		self.moving_bottom = False

	def update(self):
		"""根据移动标志调整飞船的位置"""
		# 更新飞船的center_x,center_y值，而不是rect
		if self.moving_right  and  self.rect.right  < self.screen_rect.right:
			self.center_x += self.ai_settings.ship_speed_factor
		if self.moving_left   and  self.rect.left   > self.screen_rect.left:
			self.center_x -= self.ai_settings.ship_speed_factor
		if self.moving_bottom and  self.rect.bottom < self.screen_rect.bottom:
			self.center_y += self.ai_settings.ship_speed_factor
		if self.moving_top    and  self.rect.top    > self.screen_rect.top:
			self.center_y -= self.ai_settings.ship_speed_factor
		
		# 根据center_x,center_y更新rect对象
		self.rect.centerx = self.center_x
		self.rect.centery = self.center_y

	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		"""让飞船在屏幕上居中"""
		self.center_x = self.screen_rect.centerx
		self.center_y = self.screen_rect.bottom - self.rect.height / 2