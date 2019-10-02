#coding=utf-8
#创建alien类
import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
	"""表示单个外星人的类"""
	def __init__(self,ai_settings,screen):
		"""初始化外星人 并设置外星人的起始位置"""
		super(Alien,self).__init__()#这是python3的写法
		self.screen = screen
		self.ai_settings = ai_settings

		#家在外星人图像，并设置其rect属性
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		#每个外星人的图像都在屏幕左上角	
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#储存外星人的准确位置
		self.x = float(self.rect.x)

	def blitme(self):
		"""在指定位置绘制外星人"""
		self.screen.blit(self.image,self.rect)
	
	def update(self):
		"""向右移动外星人"""
		self.x += self.ai_settings.alien_speed_factor
		self.rect.x = self.x

	def check_edges(self):
		"""如果外星人位于屏幕边缘，就返回True"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True

	def update(self):
		"""向左或向右移动外星人"""
		self.x += (self.ai_settings.alien_speed_factor* self.ai_settings.fleet_direction)
		self.rect.x = self.x
