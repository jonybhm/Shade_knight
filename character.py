import pygame
import random
from constantes import *
from spell import *
from auxiliar_2 import MetodoAuxiliar



class Character(pygame.sprite.Sprite):
    def __init__(self,char_type,x,y,speed,magic,health=100):
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


        self.char_type = char_type #tipo de personaje player/enemigo/boss
        self.speed = speed #cantidad de pixeles que el personaje se va a mover
        self.x = x
        self.y = y
        
        self.animation_list = []
        self.frame_index = 0
        self.character_action_index = 0
        self.time_update = pygame.time.get_ticks()

        self.big_spell_sfx = pygame.mixer.Sound(PATH + r"\\sfx\\player_spell.wav")
        self.small_spell_sfx = pygame.mixer.Sound(PATH + r"\\sfx\\enemy_spell.wav")
        

        if(self.char_type=="player"):
            #diccionario con nombre de carpeta y cantidad de frames segun accion
            animation_folders_dic = {"idle":16,"death":6,"move":15} 
            #"meele":8,
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

        #acciones del jugador
        self.is_move_left = False
        self.is_move_right = False
        self.is_move_up = False
        self.is_move_down = False
        self.is_shoot_spell = False
        self.is_shoot_spell_small = False
    
    def move_update (self,platform_group):

        #reiniciar variables de movimiento
        delta_x = 0
        delta_y = 0  

        #variables de movimiento
        if (self.is_move_left):
            delta_x = -self.speed
              
        if (self.is_move_right):
            delta_x = self.speed

        if (self.is_move_up):
            delta_y = -self.speed

        if (self.is_move_down):
            delta_y = self.speed
        
        #chequear por colisiones con plataformas
        for platform in platform_group:
            if platform.rect.colliderect(self.rect.x + delta_x,self.rect.y,self.width,self.height): 
                delta_x =  -self.speed 
            if platform.rect.colliderect(self.rect.x + delta_x,self.rect.y,self.width,self.height): 
                delta_x =  platform.speed
             
            if platform.rect.colliderect(self.rect.x,self.rect.y + delta_y,self.width,self.height):    
                delta_y = -platform.speed
            if platform.rect.colliderect(self.rect.x,self.rect.y + delta_y,self.width,self.height):    
                delta_y = platform.speed
                
            

                
        #actualizar posicion del rectangulo
        self.rect.x += delta_x
        self.rect.y += delta_y

    def shooting_spell(self,spell_group):
        if (self.spell_cooldown == 0 and self.magic > 0 ):
            self.spell_cooldown = 100 #disparo una vez y hay que esperar hasta el siguiente  
            
            spell_big = Spell(self.rect.centerx + (self.rect.size[0]),self.rect.centery,speed=30,type_spell="big",spell_dmg=50)
            spell_group.add(spell_big)
            self.magic -= 1 #reduce la cantidad de hechizos en 1
            self.big_spell_sfx.set_volume(0.1)
            self.big_spell_sfx.play()

    def shooting_spell_small(self,spell_group):
        if (self.spell_small_cooldown == 0):
            self.spell_small_cooldown = 20 #disparo una vez y hay que esperar hasta el siguiente  
            spell_small = Spell(self.rect.centerx,self.rect.centery,speed=20,type_spell="small",spell_dmg=10)
            spell_group.add(spell_small)
            self.small_spell_sfx.set_volume(0.05)
            self.small_spell_sfx.play()
            
            
    def cooldown_update(self):
        if (self.spell_cooldown > 0): 
            self.spell_cooldown -= 1
        if (self.spell_small_cooldown > 0):
            self.spell_small_cooldown -= 1

    def verify_is_alive_update(self):
        if (self.health <= 0):
            self.health = 0
            self.speed = 0
            self.is_alive = False
            self.action_update(1)
            
        
    def animation_update(self):
        #avanzar el frame en la animacion
        self.image = self.animation_list[self.character_action_index][self.frame_index]
        #verificar si el tiempo que paso desde la ultima update es maor a la cte ANIMATION_COOLDOWN
        if (pygame.time.get_ticks() - self.time_update > ANIMATION_COOLDOWN):
            self.time_update =  pygame.time.get_ticks()
            self.frame_index += 1
        #loopear la lista de frames
        if (self.frame_index >= len(self.animation_list[self.character_action_index])):
            if (self.character_action_index == 1): #en caso de morir
                self.frame_index = len (self.animation_list[self.character_action_index]) - 1
            else:    
                self.frame_index = 0
    
    def events(self,event_list):
        
        
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
                              
                    
            #eventos de teclado al soltar  
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
        
    def action_update(self,new_ation):
        #verificar accion nueva es disntina a la anterior
        if (new_ation != self.character_action_index):
            self.character_action_index = new_ation
            self.frame_index = 0 #iniciar nueva accion en el frame 0
            self.time_update = pygame.time.get_ticks()

    def update(self,platform_group,event_list):
        self.animation_update()
        self.cooldown_update()
        self.move_update(platform_group)
        self.verify_is_alive_update()
        self.events(event_list)
        
    def draw (self,screen):
        if (DEBUG_MODE):
            pygame.draw.rect(screen,RED,self.rect,1)
        screen.blit(self.image,self.rect)
