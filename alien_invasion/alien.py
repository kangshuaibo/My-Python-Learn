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
        
