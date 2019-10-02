#coding=utf-8
#把check_events() 放在一个名为game_functons的模块中
import sys

import pygame

from bullet import Bullet
from alien import Alien

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



def update_screen(ai_settings,screen,ship,aliens,bullets):
	"""更新屏幕上的图像，并切换到新屏幕"""
	#每次循环时都重绘屏幕
	screen.fill(ai_settings.bg_color)	#背景

	#在飞船和外星人后面重绘所有子弹
	for bullet in bullets.sprites():	#这个方法返回一个列表
		bullet.draw_bullet()

	ship.blitme()	#draw绘制飞船
	aliens.draw(screen)   #调用draw() 绘制编组中每个元素 外星人

 	#让最近绘制的屏幕可见
	pygame.display.flip()

def update_bullets(aliens,bullets):
	bullets.update()
	#删除已消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	#检查是否有子弹击中了外星人
	#如果是这样，就删除相应的子弹和外星人
		collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

def fire_bullet(ai_settings,screen,ship,bullets):
	"""如果还没有达到限制，就发射一颗子弹"""
		#创建一颗子弹，并将其加入到编组bullets中
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)



#创建群外星人
def create_fleet(ai_settings,screen,ship,aliens):
	"""创建群外星人"""
	#创建一个外星人，并计算一行可容纳多少个外星人
	alien = Alien(ai_settings,screen)	#创建一个
	number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

	#创建一好几行外星人
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):	#从零数到要创建的外星人数
		#创建一个外星人并将其加入到前行
			create_alien(ai_settings,screen,aliens,alien_number,row_number)
		


def get_number_aliens_x(ai_settings,alien_width):
	"""计算每行可容纳多少个外星人"""
	available_space_x = ai_settings.screen_width - 2 * alien_width	#计算剩余水平空间 2*是因为有空隙
	number_aliens_x = int(available_space_x/(2*alien_width))	#计算剩余空间外星人数量
	return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	"""创建一个外星人并将其放在当前行"""
	alien = Alien(ai_settings,screen)	#在循环中创建一个
	alien_width = alien.rect.width	#获取一个宽度
	alien.x = alien_width + 2 * alien_width * alien_number	#得到目前 外星人占据的空间
	alien.rect.x = alien.x	#计算当前的位置
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)	#添加到编组


def get_number_rows(ai_settings,ship_height,alien_height):
	"""计算屏幕可容纳多少行外星人"""
	available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2* alien_height))
	return number_rows


def update_aliens(ai_settings,aliens):
	"""检查是否有外星人位于屏幕边缘
	更新外星人人群中所有外星人的位置"""
	check_fleet_edges(ai_settings,aliens)
	aliens.update()

def check_fleet_edges(ai_settings,aliens):
	"""有外星人到达边缘时采取相应措施"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break

def change_fleet_direction(ai_settings,aliens):
	"""将整群外星人下移，并改变他们的方向"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1
































	
