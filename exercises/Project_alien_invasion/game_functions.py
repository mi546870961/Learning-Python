import sys
import pygame

from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	'''响应按键'''
	if event.key == pygame.K_RIGHT:
		#向右移动飞船
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		#向右移动飞船
		ship.moving_left = True	
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
		
def fire_bullet(ai_settings,screen,ship,bullets):
	'''如果没有到极限，就发射一颗子弹'''
	#创建一颗子弹，并加到编组bullets中
	if len(bullets) < ai_settings.bullet_allowed:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)	

def check_keyup_events(event,ship):
	'''响应松开'''
	if event.key == pygame.K_RIGHT:
		#向右移动飞船
		ship.moving_right = False			
	if event.key == pygame.K_LEFT:
		#向右移动飞船
		ship.moving_left = False


def check_events(ai_settings,screen,ship,bullets):
	'''响应键盘和鼠标事件'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)				
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)				
	
			
def update_screen(ai_setting,screen,ship,bullets):
	'''更新屏幕图像，并切换到新屏幕'''
	
	#每次循环都会重绘屏幕
	screen.fill(ai_setting.bg_color)
	
	#在飞船和外星人后面重绘所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	ship.blitme()
			
	#让最近绘制的屏幕可见
	pygame.display.flip()


def update_bullets(bullets):
	'''更新子弹位置，并删除已消失子弹'''
	#更新子弹位置
	bullets.update()	
	
	#删除已消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
		
