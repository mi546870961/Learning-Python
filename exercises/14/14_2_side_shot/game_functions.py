import sys
import pygame

from time import sleep
from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ai_settings,screen,stats,sb,ship,aliens,
        bullets):
    '''响应按键'''
    if event.key == pygame.K_DOWN:
        #向下移动飞船
        ship.moving_down = True
    elif event.key == pygame.K_UP:
        #向上移动飞船
        ship.moving_up = True
    elif event.key == pygame.K_SPACE:
        #发射子弹
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        #Q键退出
        sys.exit()
    elif event.key == pygame.K_p and not stats.game_active:
        #P键开始
        start_game(ai_settings,screen,stats,sb,ship,aliens,bullets)
        
def fire_bullet(ai_settings,screen,ship,bullets):
    '''如果没有到极限，就发射一颗子弹'''
    #创建一颗子弹，并加到编组bullets中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet) 
        

def check_keyup_events(event,ship):
    '''响应松开'''
    if event.key == pygame.K_DOWN:
        #向下移动飞船
        ship.moving_down = False            
    if event.key == pygame.K_UP:
        #向上移动飞船
        ship.moving_up = False
        

def check_play_botton(ai_settings,screen,stats,sb,play_button,ship,
        aliens,bullets,mouse_x, mouse_y):
    '''在玩家单击Play按钮时开始新游戏'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_settings,screen,stats,sb,ship,aliens,bullets)     
        
        
def start_game(ai_settings,screen,stats,sb,ship,aliens,bullets):
    '''开始游戏'''      
    #重置游戏设置
    ai_settings.initialize_dynamic_settings()
    
    #隐藏光标
    pygame.mouse.set_visible(False)
    
    #重置游戏统计信息
    stats.reset_stats()
    stats.game_active = True
    
    #重置记分牌图像
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()
    
    #清空外星人列表和子弹列表
    aliens.empty()
    bullets.empty()
    
    #创建一群新的外星人，并将飞船放到屏幕底端中央
    create_fleet(ai_settings,screen,aliens)
    ship.center_ship()
        

def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,
        bullets):
    '''响应键盘和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,stats,sb,ship,
                aliens,bullets)            
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_botton(ai_settings,screen,stats,sb,play_button,ship,
        aliens,bullets,mouse_x, mouse_y)
                
    

def create_alien(ai_settings,screen,aliens):
    '''创建一个外星人并放在右侧中央'''
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.rect.right = alien.screen_rect.right
    alien.rect.centery = alien.screen_rect.centery
    aliens.add(alien)

            
def create_fleet(ai_settings,screen,aliens):
    '''创建一个外星人群'''
    create_alien(ai_settings,screen,aliens)

            
def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
        play_button):
    '''更新屏幕图像，并切换到新屏幕'''
    
    #每次循环都会重绘屏幕
    screen.fill(ai_settings.bg_color)
    
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()
    aliens.draw(screen)
    
    #显示得分
    sb.show_score()
    
    #如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()    
            
    #让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    '''更新子弹位置，并删除已消失子弹'''
    #更新子弹位置
    bullets.update()    
    
    #检测是否击中目标
    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,
        aliens,bullets)
    
    #检测子弹是否超出屏幕    
    check_bullet_miss(stats,sb,bullets)   
        
def check_bullet_miss(stats,sb,bullets):
    '''检测是否有子弹没有击中靶子，到达右侧'''
    for bullet in bullets.sprites(): 
        if bullet.rect.left >= bullet.screen_rect.right:
            bullets.remove(bullet)
            bullet_miss(stats,sb)
            
            
def bullet_miss(stats,sb):
    '''响应子弹没有击中靶子'''
    if stats.ships_left >0:
        #将所剩飞船减少1
        stats.ships_left -= 1
        
        #更新剩余次数
        sb.prep_ships()

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
             

def check_high_score(stats,sb):
    '''检测是否诞生最高分'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()  
          

def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,
        aliens,bullets):            
    '''检查是否有子弹击中外星人'''
    #如果击中，就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)
        
    if len(aliens) == 0:
        #如果整群外星人被消灭，就提高一个等级
        #删除现有的子弹
        bullets.empty()
        ai_settings.increase_speed()
        
        #提高等级
        stats.level += 1
        sb.prep_level()        
        
        #新建一群外星人
        create_fleet(ai_settings,screen,aliens) 
            
            
def check_fleet_edge(ai_settings,aliens):
    '''如果有外星人到达边缘就变方向'''
    for alien in aliens.sprites():
        if alien.check_edges():
            ai_settings.fleet_direction *= -1
            break 
  
def update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets):
    '''检测是否有外星人到达边缘，然后更新外星人群中所有外星人位置'''
    check_fleet_edge(ai_settings,aliens)
    aliens.update()

    

