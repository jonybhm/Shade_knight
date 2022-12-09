import pygame
import random
from constantes import *
from spell import *
from auxiliar_2 import MetodoAuxiliar



class Character(pygame.sprite.Sprite):
    '''
    This class represents the player character
    '''
    def __init__(self,char_type:str,x:int,y:int,speed:int,magic:int,health:int=100)->None:
        pygame.sprite.Sprite.__init__(self)
        self.is_alive = True
                
        self.health = health
        self.max_health = health

        self.magic = magic
        self.start_magic = magic
        self.spell_cooldown = 0
        self.spell_small_cooldown = 0
        

        self.money = 0
        self.dmg_count = 0
        self.kill_count = 0
        self.score = 0

        self.char_type = char_type 
        self.speed = speed 
        self.x = x
        self.y = y
        
        self.animation_list = []
        self.frame_index = 0
        self.character_action_index = 0
        self.time_update = pygame.time.get_ticks()

        self.big_spell_sfx = pygame.mixer.Sound(PATH + r"\\sfx\\player_spell.wav")
        self.small_spell_sfx = pygame.mixer.Sound(PATH + r"\\sfx\\enemy_spell.wav")
        

        if(self.char_type=="player"):
            
            animation_folders_dic = {"idle":16,"death":6,"move":15} 
            
            for type_folder in animation_folders_dic:
                buffer_list = []     
            
                buffer_list =  MetodoAuxiliar.getSurfaceFromSpriteSheet(
                PATH + r"\\{}\\{}.png".format(char_type,type_folder),
                animation_folders_dic.get(type_folder),1,scale=0.75)

                self.animation_list.append(buffer_list)
      
                
        self.image = self.animation_list[self.character_action_index][self.frame_index] 
        
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.is_move_left = False
        self.is_move_right = False
        self.is_move_up = False
        self.is_move_down = False
        self.is_shoot_spell = False
        self.is_shoot_spell_small = False
    
    def move_update (self,platform_group:object)->None:
        '''
        Given some movement flags (bool) it adds speed to the enemies, in both x and y axis. It detects collitions with platforms and adds its movement to he players
        Arguments: sprite group (object) containing platforms
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
     
        for platform in platform_group:
            if platform.rect.colliderect(self.rect.x + delta_x,self.rect.y,self.width,self.height): 
                delta_x =  -self.speed 
            if platform.rect.colliderect(self.rect.x + delta_x,self.rect.y,self.width,self.height): 
                delta_x =  platform.speed
             
            if platform.rect.colliderect(self.rect.x,self.rect.y + delta_y,self.width,self.height):    
                delta_y = -platform.speed
            if platform.rect.colliderect(self.rect.x,self.rect.y + delta_y,self.width,self.height):    
                delta_y = platform.speed
                
        self.rect.x += delta_x
        self.rect.y += delta_y

    def shooting_spell(self,spell_group:object)->None:
        '''
        Generates instances of the spells and adds them to sprite groups
        Arguments: sprite group (object) containing spells
        Returns: None
        '''
        if (self.spell_cooldown == 0 and self.magic > 0 ):
            self.spell_cooldown = 100   
            
            spell_big = Spell(self.rect.centerx + (self.rect.size[0]),self.rect.centery,speed=30,type_spell="big",spell_dmg=50)
            spell_group.add(spell_big)
            self.magic -= 1 
            self.big_spell_sfx.set_volume(0.1)
            self.big_spell_sfx.play()

    def shooting_spell_small(self,spell_group:object)->None:
        '''
        Generates instances of the spells and adds them to sprite groups 
        Arguments: sprite group (object) containing spells
        Returns: None
        '''
        if (self.spell_small_cooldown == 0):
            self.spell_small_cooldown = 20   
            spell_small = Spell(self.rect.centerx,self.rect.centery,speed=20,type_spell="small",spell_dmg=10)
            spell_group.add(spell_small)
            self.small_spell_sfx.set_volume(0.05)
            self.small_spell_sfx.play()
            
            

    def verify_is_alive_update(self)->None:
        '''
        Verifys if the player is alive or dead 
        Arguments: None
        Returns: None
        '''
        if (self.health <= 0):
            self.health = 0
            self.speed = 0
            self.is_alive = False
            self.action_update(1)
            
    def cooldown_update(self)->None:
        '''
        Counts down the cooldown timer
        Arguments: None
        Returns: None
        '''
        if (self.spell_cooldown > 0): 
            self.spell_cooldown -= 1
        if (self.spell_small_cooldown > 0):
            self.spell_small_cooldown -= 1
        
        
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
    
    def events(self,event_list)->None:
        '''
        Verifys the buttons that are being pressed and activates different flags 
        Arguments: list containing the game events 
        Returns: None
        '''
        
        for event in event_list:
            
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_a):
                    self.is_move_left = True
                if (event.key == pygame.K_d):
                    self.is_move_right = True
                if (event.key == pygame.K_w):
                    self.is_move_up = True
                if (event.key == pygame.K_s):
                    self.is_move_down = True
                if (event.key == pygame.K_SPACE):
                    self.is_shoot_spell = True
                if (event.key == pygame.K_LSHIFT):
                    self.is_shoot_spell_small = True
                              
            if (event.type == pygame.KEYUP):
                if (event.key == pygame.K_a):
                    self.is_move_left = False
                if (event.key == pygame.K_d):
                    self.is_move_right = False              
                if (event.key == pygame.K_w):
                    self.is_move_up = False
                if (event.key == pygame.K_s):
                    self.is_move_down = False
                if (event.key == pygame.K_SPACE):
                    self.is_shoot_spell = False
                if (event.key == pygame.K_LSHIFT):
                    self.is_shoot_spell_small = False
        
    def action_update(self,new_ation)->None:
        '''
        Verifys if the new action is different and updates the action frame in the animation list
        Arguments: new_action represented by an int value, representing different type of animation
        Returns: None
        '''
        if (new_ation != self.character_action_index):
            self.character_action_index = new_ation
            self.frame_index = 0 
            self.time_update = pygame.time.get_ticks()

    def draw (self,screen)->None:
        '''
        Merges the surface representing the player with the one from the main screen
        Arguments: The surface from the main screen (object) 
        Returns: None
        '''
        if (DEBUG_MODE):
            pygame.draw.rect(screen,RED,self.rect,1)
        screen.blit(self.image,self.rect)

    def update(self,platform_group,event_list)->None:
        '''
        Executes the methods that need update 
        Arguments: None
        Returns: None
        '''
        self.animation_update()
        self.cooldown_update()
        self.move_update(platform_group)
        self.verify_is_alive_update()
        self.events(event_list)
        
