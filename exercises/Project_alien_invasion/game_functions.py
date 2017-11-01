import sys
import pygame

from time import sleep
from bullet import Bullet
from alien import Alien

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
    elif event.key == pygame.K_q:
        sys.exit()
        
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

def get_number_aliens_x(ai_settings,alien_width):
    '''计算一行能容纳多少外星人'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2*alien_width))
    return number_alien_x

def get_number_rows(ai_settings,ship_height,alien_height):
    '''计算屏幕容纳多少行外星人'''
    available_space_y = (ai_settings.screen_height -
        (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    '''创建一个外星人并放在首行'''
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2*alien_width * alien_number    
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 2*alien_height * row_number
    aliens.add(alien)

            
def create_fleet(ai_settings,screen,ship,aliens):
    '''创建一个外星人群'''
    alien = Alien(ai_settings,screen)
    number_alien_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,
        alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings,screen,aliens,alien_number,
                row_number)

            
def update_screen(ai_settings,screen,ship,bullets,aliens):
    '''更新屏幕图像，并切换到新屏幕'''
    
    #每次循环都会重绘屏幕
    screen.fill(ai_settings.bg_color)
    
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()
    aliens.draw(screen)
            
    #让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings,screen,ship,aliens,bullets):
    '''更新子弹位置，并删除已消失子弹'''
    #更新子弹位置
    bullets.update()    
    
    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets)        
    

def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):            
    '''检查是否有子弹击中外星人'''
    #如果击中，就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)    
    if len(aliens) == 0:
        #删除现有的子弹并新建一群外星人
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)

def check_fleet_edge(ai_settings,aliens):
    '''如果有外星人到达边缘就采取措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break     

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    '''响应被外星人撞到的飞船'''
    if stats.ships_left >0:
        #将所剩飞船减少1
        stats.ships_left -= 1
        
        #清空外星人和子弹
        aliens.empty()
        bullets.empty()
        
        #创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        
        #暂停
        sleep(0.5)
    else:
        stats.game_active = False

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
     for alien in aliens.sprites(): 
        if alien.rect.bottom >= ship.screen_rect.bottom:
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break

  
def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    '''检测是否有外星人到达边缘，然后更新外星人群中所有外星人位置'''
    check_fleet_edge(ai_settings,aliens)
    aliens.update()
    #检测是否有外星人到达底部
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)
    #检测外星人和飞船间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
    
        
def change_fleet_direction(ai_settings,aliens):
    '''将舰队整体下移，并改变运动方向'''   
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
