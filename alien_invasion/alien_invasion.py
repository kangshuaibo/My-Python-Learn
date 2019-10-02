#coding=utf-8
#创建一个空的Pygame窗口
import sys	#包含功能 用sys来退出游戏

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()	#初始化背景设置
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))	#调用函数 创建一个名为screen的显示窗口
	pygame.display.set_caption("Alien Invasion Yun")	#设置窗口标题

	#创建一艘飞船、一个子弹编组、一个外星人编组
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group()

			#创建一个用于储存子弹的编组
			#bullets = Group()	#创建一个group实例 命名为bullets

	#创建一个外星人
	alien = Alien(ai_settings,screen)

	#创建外星人群
	gf.create_fleet(ai_settings,screen,ship,aliens)


	#开始游戏主循环
	while True:
		
		#监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		#gf.update_bullets(bullets)
		#gf.update_screen(ai_settings,screen,ship,alien,bullets)
		
		gf.update_aliens(ai_settings,aliens)
		gf.update_bullets(aliens,bullets)
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)


run_game()	#调用函数



