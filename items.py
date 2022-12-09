import pygame
import random
from constantes import *
from auxiliar_2 import MetodoAuxiliar


class Items(pygame.sprite.Sprite):
    '''
    This class represent the items that appear and help or harm the player
    '''
    def __init__(self,type,speed=5):
        pygame.sprite.Sprite.__init__(self)
        self.type = type 
        self.image = MetodoAuxiliar.getSurfaceFromSpriteSheet(PATH + r"\\items\\items.png",3,4,scale=0.5)[type]
        self.rect = self.image.get_rect()
        self.x=SCREEN_WIDTH 
        self.y=random.randrange(0 + (self.rect.size[0]),SCREEN_HEIGHT - (self.rect.size[0]))
        self.rect.center = (self.x,self.y)

        self.pick_up_sfx = pygame.mixer.Sound(PATH +r"\\sfx\\menu_select.wav")

        self.speed = speed
        self.direction = 1
        self.is_move_left = True

    def move_update (self)->None:
        '''
        Given some movement flags (bool) it adds speed to the enemies, in x axis 
        Arguments: None
        Returns: None
        '''
        
        delta_x = 0
        
        if (self.is_move_left):
            delta_x = -self.speed
        
        self.rect.x += delta_x
    
    
    def pick_up_update(self,player:object)->None:
        '''
        Detects collisions between items and player, and in case of collision or if the item leaves the screen, its destroyed
        Arguments: player (object) 
        Returns: None
        '''
        
        if (pygame.sprite.collide_rect(self,player)):
            self.pick_up_sfx.set_volume(0.2)
            self.pick_up_sfx.play()
            
            if (self.type == 1): #type health
                player.health += 10
                player.score += 5
                if (player.health > player.max_health):
                    player.health = player.max_health
            elif (self.type == 7): #type money
                player.money += 25
                player.score += player.money 
            elif (self.type == 10): #type magic
                player.magic += 1 
                player.score += 2
            elif (self.type == 4): #type magic
                player.health -= 10    
                player.score -= 5
            self.kill()

        if (self.rect.right < 0):
            self.kill() 


    def update(self,player:object)->None:
        '''
        Executes the methods that need update 
        Arguments: player (object)
        Returns: None
        '''
        self.move_update()
        self.pick_up_update(player)
 