import sys

import pygame

def run_game():
	#初始化游戏
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption("Alien Invasion")
	
	#设置背景色
	#bg_color = (230,230,230) #灰色
	bg_color = (0,0,255) #蓝色
	
	
	#开始游戏
	while True:
		
		#监视键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		
		#每次循环都会重绘屏幕
		screen.fill(bg_color)
				
		#让最近绘制的屏幕可见
		pygame.display.flip()
		
		
run_game()
