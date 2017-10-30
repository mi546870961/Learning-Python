import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	'''对发射子弹管理的类'''
	
	def __init__(self,ai_settings,screen,ship):
		'''在飞船所在位置创建一个子弹'''
		
		super(Bullet,self).__init__()
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		
		#在0,0处创建一个表示子弹矩形，再设置正确位置
		self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
			ai_settings.bullet_height)
		self.rect.right = ship.rect.right
		self.rect.centery = ship.rect.centery
		
		#存储用小数表示的子弹位置
		self.x = float(self.rect.x)
		
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
		
	def update(self):
		'''向上移动子弹'''
		#更新表示子弹位置的小数值
		self.x += self.speed_factor
		#更新表示子弹位置的rect的位置
		self.rect.x = self.x
		
	def draw_bullet(self):
		'''在屏幕上绘制子弹'''
		pygame.draw.rect(self.screen,self.color,self.rect)
