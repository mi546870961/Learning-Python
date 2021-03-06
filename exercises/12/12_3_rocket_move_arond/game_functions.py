import sys
import pygame

def check_keydown_events(event,ship):
	'''响应按键'''
	if event.key == pygame.K_RIGHT:
		#向右移动飞船
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		#向左移动飞船
		ship.moving_left = True	
	elif event.key == pygame.K_UP:
		#向上移动飞船
		ship.moving_up = True	
	elif event.key == pygame.K_DOWN:
		#向下移动飞船
		ship.moving_down = True		

def check_keyup_events(event,ship):
	'''响应松开'''
	if event.key == pygame.K_RIGHT:
		#向右移动飞船
		ship.moving_right = False			
	elif event.key == pygame.K_LEFT:
		#向右移动飞船
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		#向右移动飞船
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		#向右移动飞船
		ship.moving_down = False


def check_events(ship):
	'''响应键盘和鼠标事件'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ship)				
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)				
	
			
def update_sceen(ai_setting,screen,ship):
	'''更新屏幕图像，并切换到新屏幕'''
	
	#每次循环都会重绘屏幕
	screen.fill(ai_setting.bg_color)
	ship.blitme()
			
	#让最近绘制的屏幕可见
	pygame.display.flip()

