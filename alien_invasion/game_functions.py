#coding=utf-8
#把check_events() 放在一个名为game_functons的模块中
import sys

import pygame

from bullet import Bullet 

def check_events(ai_settings,screen,ship,bullets):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:	#按下右按键
			check_keydown_events(event,ai_settings,screen,ship,bullets)

		elif event.type == pygame.KEYUP:	#松开右按键
			check_keyup_events(event,ship)

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	"""响应按键"""
	if event.key == pygame.K_RIGHT:
			ship.moving_right = True

	elif event.key == pygame.K_LEFT:
		ship.moving_left = True

	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	

def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False

	if event.key == pygame.K_LEFT:
		 ship.moving_left = False



def update_screen(ai_settings,screen,ship,alien,bullets):
	"""更新屏幕上的图像，并切换到新屏幕"""
	#每次循环时都重绘屏幕
	screen.fill(ai_settings.bg_color)	#背景

	#在飞船和外星人后面重绘所有子弹
	for bullet in bullets.sprites():	#这个方法返回一个列表
		bullet.draw_bullet()

	ship.blitme()	#draw绘制飞船
	alien.blitme()   #绘制外星人

 	#让最近绘制的屏幕可见
	pygame.display.flip()

def update_bullets(bullets):
	bullets.update()
		#删除已消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def fire_bullet(ai_settings,screen,ship,bullets):
	"""如果还没有达到限制，就发射一颗子弹"""
		#创建一颗子弹，并将其加入到编组bullets中
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)



	
