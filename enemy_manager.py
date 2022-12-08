from enemigos import Enemy
import random
from constantes import *
import pygame
from auxiliar import *

class EnemyManager:
    def __init__(self,total_enemies,enemy_health,enemy_timer,enemy_type,enemy_scale):
        self.current_enemies = 0
        self.timer = 0
        self.random_pos_y = random.randint(0,SCREEN_HEIGHT)

        self.managed_enemy_group = pygame.sprite.Group()
        #datos del json
        self.total_enemies = total_enemies
        self.enemy_type = enemy_type
        self.enemy_health = enemy_health
        self.enemy_timer = enemy_timer
        self.enemy_scale = enemy_scale

    def manage_enemies_update(self,player):
        if(self.timer == 0 and self.current_enemies < self.total_enemies and player.is_alive):
            self.timer = self.enemy_timer
            enemy = Enemy(char_type=self.enemy_type,speed=2,health=self.enemy_health,img_scale=self.enemy_scale)
            self.managed_enemy_group.add(enemy)
            self.current_enemies += 1 

        
    def timer_update(self):
        if(self.timer > 0):
            self.timer -= 1


    def update(self,player):
        self.manage_enemies_update(player)
        self.timer_update()
