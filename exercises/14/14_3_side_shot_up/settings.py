class Settings():
    def __init__(self):     
        '''初始化游戏设置静态类'''
        
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800        
        self.bg_color = (230,230,230)   
        
        #飞船设置
        self.ship_limit = 2
        
        #子弹设置
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3
        
        #外星人设置
        self.fleet_drop_speed = 100
        
        #计分
        self.alien_points = 50
        
        #加快游戏节奏
        self.speedup_scale = 1.1
        
        #外星人点数的提高速度
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的量'''
        self.ship_speed_factor = 1.5        
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
        # fleet_direction为1表示向左，为-1表示向右
        self.fleet_direction = 1
        
    def increase_speed(self):
        '''提高速度设置'''
        self.alien_speed_factor *= self.speedup_scale
        #提高分数
        self.alien_points = int(self.alien_points*self.score_scale)
