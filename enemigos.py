import pygame
import random
from auxiliar_2 import MetodoAuxiliar
from constantes import *
from spell import *
from character import *

class Enemy(pygame.sprite.Sprite):
    '''
    This class represent the enemies that appear and attack the player
    '''
    def __init__(self,char_type:str,speed:int,health:int,img_scale:float)->None:
        pygame.sprite.Sprite.__init__(self)
      
        self.is_alive = True
                
        self.health = health
        self.max_health = health
        self.img_scale = img_scale

        
        self.spell_cooldown = 0

        self.char_type = char_type 
        self.speed = speed 
        
        self.animation_list = []
        self.frame_index = 0
        self.character_action_index = 0
        self.time_update = pygame.time.get_ticks()

        self.direction = 1
        self.enemy_move_limit = 0 
        self.stop_move = False
        self.stop_move_limit_timer = 0 
        if(self.char_type=="enemy"):
           
            animation_folders_dic = {"idle":6,"death":6} 
            for type_folder in animation_folders_dic:
                buffer_list = []     
            
                buffer_list = MetodoAuxiliar.getSurfaceFromSpriteSheet(
                PATH + r"\\{}\\{}.png".format(self.char_type,type_folder),
                animation_folders_dic.get(type_folder),1,False,1,self.img_scale)

                self.animation_list.append(buffer_list)

        elif(self.char_type=="mid"):
            
            animation_folders_dic = {"mid":8,"death":6} 
            for type_folder in animation_folders_dic:
                buffer_list = []     
            
                buffer_list = MetodoAuxiliar.getSurfaceFromSpriteSheet(
                PATH + r"\\{}\\{}.png".format(char_type,type_folder),
                animation_folders_dic.get(type_folder),1,False,1,self.img_scale)

                self.animation_list.append(buffer_list)
        
        elif(self.char_type=="final"):
            
            animation_folders_dic = {"final":8,"death":6} 
            for type_folder in animation_folders_dic:
                buffer_list = []     
            
                buffer_list = MetodoAuxiliar.getSurfaceFromSpriteSheet(
                PATH + r"\\{}\\{}.png".format(char_type,type_folder),
                animation_folders_dic.get(type_folder),1,False,1,self.img_scale)

                self.animation_list.append(buffer_list)
        
        self.image = self.animation_list[self.character_action_index][self.frame_index] 
        
        self.rect = self.image.get_rect()
        self.x = SCREEN_WIDTH - (self.rect.size[0])//2
        if (self.char_type=="enemy" or self.char_type=="mid"):
            self.y = random.randrange(0 + (self.rect.size[0]),SCREEN_HEIGHT - (self.rect.size[0]))
        else:
            self.y = SCREEN_HEIGHT//2
        self.rect.center = (self.x,self.y)
        self.is_move_left = False
        self.is_move_right = False
        self.is_move_up = False
        self.is_move_down = False
        self.is_shoot_spell = False
        self.enemy_spell_sfx = pygame.mixer.Sound(PATH + r"\\sfx\\damage.wav")

    def enemy_actions(self,player:object,spell_group:object)->None:
        '''
        Given a certain limit it changes the direction in which the enemies move in the y axis 
        Arguments: Two groups of sprites (object) which contains spells and the player
        Returns: None
        '''
        if (self.is_alive and player.is_alive):
            if(random.randint(1,20) == 1): 
                self.shooting_spell(spell_group)
                      
            if(self.direction==-1):
                self.is_move_up = False
                self.is_move_down = True
            elif (self.direction==1):
                self.is_move_down = False
                self.is_move_up = True 
                                
            self.move_update()    
            self.enemy_move_limit += 1 

            if (self.enemy_move_limit > 20):
                self.direction *= -1
                self.enemy_move_limit *= -1

        elif(self.is_alive == False and self.spell_cooldown == 0):
            self.kill() 
            player.kill_count += 1


    def move_update (self)->None:
        '''
        Given some movement flags (bool) it adds speed to the enemies, in both x and y axis 
        Arguments: None
        Returns: None
        '''
       
        delta_x = 0
        delta_y = 0  

        if (self.is_move_left):
            delta_x = -self.speed
            
        if (self.is_move_right):
            delta_x = self.speed

        if (self.is_move_up):
            delta_y = -self.speed

        if (self.is_move_down):
            delta_y = self.speed
       
        self.rect.x += delta_x
        self.rect.y += delta_y

    def shooting_spell(self,spell_group):
        '''
        Generates instances of the spells and adds them to sprite groups 
        Arguments: None
        Returns: None
        '''
        if (self.spell_cooldown == 0 ):
            self.enemy_spell_sfx.set_volume(0.05)
            self.enemy_spell_sfx.play()
            self.spell_cooldown = 100 
            if(self.char_type == "enemy"):
                spell = Spell(self.rect.centerx - (self.rect.size[0]),self.rect.centery,speed=-15,type_spell="small",spell_dmg=10)
                spell_group.add(spell)
            if(self.char_type == "mid"):
                spell = Spell(self.rect.centerx ,self.rect.centery,speed=-10,type_spell="small",spell_dmg=10)
                spell_diag_1 = Spell(self.rect.centerx ,self.rect.centery,speed=-10,type_spell="small",movement="diag_up",spell_dmg=10)
                spell_diag_2 = Spell(self.rect.centerx ,self.rect.centery,speed=-10,type_spell="small",movement="diag_down",spell_dmg=10)
                spell_group.add(spell)
                spell_group.add(spell_diag_1)
                spell_group.add(spell_diag_2)
            if(self.char_type == "final"):
                spell_wave_1 = Spell(self.rect.centerx ,self.rect.centery,speed=-12,type_spell="small",movement="wave_pattern",spell_dmg=10)
                spell_wave_2 = Spell(self.rect.centerx ,self.rect.centery,speed=-12,type_spell="small",movement="flip_wave_pattern",spell_dmg=10)
                spell_diag_1 = Spell(self.rect.centerx ,self.rect.centery,speed=-12,type_spell="small",movement="diag_up",spell_dmg=10)
                spell_diag_2 = Spell(self.rect.centerx ,self.rect.centery,speed=-12,type_spell="small",movement="diag_down",spell_dmg=10)
                spell_group.add(spell_wave_1)
                spell_group.add(spell_wave_2)
                spell_group.add(spell_diag_1)
                spell_group.add(spell_diag_2)
               


    def cooldown_update(self)->None:
        '''
        Counts down the cooldown timer
        Arguments: None
        Returns: None
        '''
        if (self.spell_cooldown > 0):
            self.spell_cooldown -= 1

    def verify_is_alive_update(self)->None:
        '''
        Verifys if the enemy is alive or dead 
        Arguments: None
        Returns: None
        '''
        if (self.health <= 0):
            self.health = 0
            self.speed = 0
            self.is_alive = False
            self.action_update(1)
    
    
        
    def animation_update(self)->None:
        '''
        Runs down the frames in the animation and resets it when it reaches the end
        Arguments: None
        Returns: None
        '''
      
        self.image = self.animation_list[self.character_action_index][self.frame_index]
        
        if (pygame.time.get_ticks() - self.time_update > ANIMATION_COOLDOWN):
            self.time_update =  pygame.time.get_ticks()
            self.frame_index += 1
       
        if (self.frame_index >= len(self.animation_list[self.character_action_index])):
            if (self.character_action_index == 1): 
                self.frame_index = len (self.animation_list[self.character_action_index]) - 1
            else:    
                self.frame_index = 0
        
    def action_update(self,new_ation:int)->None:
        '''
        Updates the animation in the animation list
        Arguments: new_action represented by an int value, representing different type of animation
        Returns: None
        '''
       
        if (new_ation != self.character_action_index):
            self.character_action_index = new_ation
            self.frame_index = 0 
            self.time_update = pygame.time.get_ticks()

    def draw (self,screen:object)->None:
        '''
        Merges the surface representing the platform with the one from the main screen
        Arguments: The surface from the main screen (object) 
        Returns: None
        '''
        if (DEBUG_MODE):
            pygame.draw.rect(screen,RED,self.rect,1)
        screen.blit(self.image,self.rect)
    
    def update(self)->None:
        '''
        Executes the methods that need update 
        Arguments: None
        Returns: None
        '''
        self.animation_update()
        self.cooldown_update()
        self.move_update()
        self.verify_is_alive_update()
        
