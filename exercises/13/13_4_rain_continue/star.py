import pygame

from pygame.sprite import Sprite 

class Star(Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/rain.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        #star 最初都在左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        
    def blitme(self):
        #指定位置绘制star
        self.screen.blit(self.image,self.rect)
        
    def update(self,drop_speed):
        self.rect.y += drop_speed
        
    
