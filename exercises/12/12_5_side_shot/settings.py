class Settings():
	def __init__(self):		
		'''存储游戏所有设置的类'''
		
		#设置背景色
		self.screen_width = 1200
		self.screen_height = 800		
		self.bg_color = (230,230,230) 	
		
		#飞船的设置
		self.ship_speed_factor = 1.5
		
		#子弹设置
		self.bullet_speed_factor = 1
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = 60,60,60
		self.bullet_allowed = 3
