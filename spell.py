import pygame
import math
from auxiliar_2 import MetodoAuxiliar
from constantes import *



class Spell(pygame.sprite.Sprite):
    '''
    This class represent the spells that the player and enemies can use to attacks each other
    '''
    def __init__(self,x:int,y:int,speed:int,type_spell:str,spell_dmg:int,movement:str="straight")->None:
        pygame.sprite.Sprite.__init__(self)

        self.speed = speed 
        self.x = x
        self.y = y
        self.time_update = pygame.time.get_ticks()
        self.type_spell = type_spell
        self.movement = movement
        self.spell_dmg = spell_dmg

        self.wave_limit=0
        self.wave_direction=1

        
        self.damage_sfx_2 = pygame.mixer.Sound(PATH + r"\\sfx\\player_meele.wav")
        self.animation_list = []
        self.frame_index = 0
        if(type_spell == "big"):
            self.animation_list = MetodoAuxiliar.getSurfaceFromSpriteSheet(
            PATH + r"\\spells\\spell_player.png",6,1,scale=0.60)
        if(type_spell == "small"):
            self.animation_list = MetodoAuxiliar.getSurfaceFromSpriteSheet(
            PATH + r"\\spells\\spell_enemy.png",6,1,scale=0.50)
            

        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        

        self.direction = 1
    
    def animation_update(self)->None:
        '''
        Runs down the frames in the animation and resets it when it reaches the end
        Arguments: None
        Returns: None
        '''
        self.image = self.animation_list[self.frame_index]
        if (pygame.time.get_ticks() - self.time_update > ANIMATION_COOLDOWN):
            self.time_update =  pygame.time.get_ticks()
            self.frame_index += 1
        if (self.frame_index >= len(self.animation_list)):
            self.frame_index = 0

    def draw(self,screen:object)->None:
        '''
        Merges the surface representing the platform with the one from the main screen
        Arguments: The surface from the main screen (object) 
        Returns: None
        '''
        if(DEBUG_MODE):
            pygame.draw.rect(screen,RED,self.rect,1)

        screen.blit(self.image,self.rect)


    def move_update(self)->None:
        '''
        Given some movement parameters (str) it adds speed to the spell, in both x and y axis 
        Arguments: None
        Returns: None
        '''
        if(self.movement=="straight"):
            self.rect.x += self.speed
        elif(self.movement=="diag_up"):
            self.rect.y += self.speed//3
            self.rect.x += self.speed
        elif(self.movement=="diag_down"):
            self.rect.y -= self.speed//3
            self.rect.x += self.speed
        elif(self.movement=="wave_pattern"):
            self.rect.x += self.speed
            if(self.wave_direction==1):
                self.rect.y -= self.speed
            else:    
                self.rect.y += self.speed
            self.wave_limit+=1
            if(self.wave_limit>20):
                self.wave_direction *= -1
                self.wave_limit *= -1
        elif(self.movement=="flip_wave_pattern"):
            self.rect.x += self.speed
            if(self.wave_direction==-1):
                self.rect.y -= self.speed
            else:    
                self.rect.y += self.speed
            self.wave_limit+=1
            if(self.wave_limit>20):
                self.wave_direction *= -1
                self.wave_limit *= -1

    def collition_update(self,player:object,spell_group_player:object,spell_group_enemy:object,enemy_sprite_group:object)->None:
        '''
        Detects collisions between spells and enemies/player, and in case of collision or if the spells leaves the screen, the spell is destroyed
        Arguments: Three groups of sprites (object) which contains spells from players and enemies and platforms and player (object) 
        Returns: None
        '''
        if (self.rect.left > SCREEN_WIDTH or self.rect.right < 0):
            self.kill()
        
        for enemy in enemy_sprite_group:
            if (pygame.sprite.spritecollide(enemy,spell_group_player,False)): 
                if (enemy.is_alive):
                    enemy.health -= self.spell_dmg
                    player.dmg_count += 1
                    player.score += player.dmg_count
                    
                    self.kill()
                        
        if (pygame.sprite.spritecollide(player,spell_group_enemy,False)): 
            if (player.is_alive):
                player.health -= self.spell_dmg
                self.damage_sfx_2.set_volume(0.2)
                self.damage_sfx_2.play()
                self.kill()


    def update(self,player:object,spell_group_player:object,spell_group_enemy:object,enemy_sprite_group:object)->None:
        '''
        Executes the methods that need update 
        Arguments: Three groups of sprites (object) which contains spells from players and enemies and platforms and player (object) 
        Returns: None
        '''
        self.animation_update()
        self.move_update()
        self.collition_update(player,spell_group_player,spell_group_enemy,enemy_sprite_group)


        