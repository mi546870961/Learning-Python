import sys
import pygame

from star import Star
from pygame.sprite import Group


pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Stars")
bg_color =(255,255,255) #白色

#创建一组星星
stars = Group()

def get_number_star_x(star):
    '''计算一行能容纳多少星星'''
    available_space_x = star.screen_rect.width - 1 * star.rect.width
    number_star_x = int(available_space_x / (2*star.rect.width))
    return number_star_x

def get_number_rows(star):
    '''计算屏幕容纳多少行星星'''
    available_space_y = star.screen_rect.height - 2 * star.rect.height
    number_rows = int(available_space_y / (2*star.rect.height))
    return number_rows

def create_alien(stars,star_number,row_number):
    '''创建一组星星'''
    star = Star(screen)
    star_width = star.rect.width
    star_height = star.rect.height
    star.x = star_width + 2*star_width * star_number    
    star.rect.x = star.x
    star.rect.y = star_height + 2*star_height * row_number
    stars.add(star)

            
def create_stars(screen,stars):
    '''创建一组星星'''
    star = Star(screen)
    number_star_x = get_number_star_x(star)
    number_rows = get_number_rows(star)
    for row_number in range(number_rows):
        for star_number in range(number_star_x):
            create_alien(stars,star_number,row_number)


while True:    
    
    #监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill(bg_color)        
    create_stars(screen,stars)    
    stars.draw(screen)   
       
    #让最近绘制的屏幕可见
    pygame.display.flip()
