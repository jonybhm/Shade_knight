import pygame
import random
from auxiliar_2 import MetodoAuxiliar
from constantes import *
from spell import *
from character import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self,char_type,speed,health,img_scale):
        pygame.sprite.Sprite.__init__(self)
        #propiedades de los enemigos
        self.is_alive = True
                
        self.health = health
        self.max_health = health
        self.img_scale = img_scale

        
        self.spell_cooldown = 0

        self.char_type = char_type #tipo de personaje player/enemigo/mid
        self.speed = speed #cantidad de pixeles que el personaje se va a mover
        
        self.animation_list = []
        self.frame_index = 0
        self.character_action_index = 0
        self.time_update = pygame.time.get_ticks()

        
        self.direction = 1 #"viendo" hacia arriba
        self.enemy_move_limit = 0 #contador de cuanto se mueve hacia un lado
        self.stop_move = False
        self.stop_move_limit_timer = 0 #contador de cuanto se queda quieto
        if(self.char_type=="enemy"):
            #diccionario con nombre de carpeta y cantidad de frames segun accion
            animation_folders_dic = {"idle":6,"death":6} 
            for type_folder in animation_folders_dic:
                buffer_list = []     
            
                buffer_list = MetodoAuxiliar.getSurfaceFromSpriteSheet(
                PATH + r"\\{}\\{}.png".format(self.char_type,type_folder),
                animation_folders_dic.get(type_folder),1,False,1,self.img_scale)

                self.animation_list.append(buffer_list)

        elif(self.char_type=="mid"):
            #diccionario con nombre de carpeta y cantidad de frames segun accion
            animation_folders_dic = {"mid":8,"death":6} 
            for type_folder in animation_folders_dic:
                buffer_list = []     
            
                buffer_list = MetodoAuxiliar.getSurfaceFromSpriteSheet(
                PATH + r"\\{}\\{}.png".format(char_type,type_folder),
                animation_folders_dic.get(type_folder),1,False,1,self.img_scale)

                self.animation_list.append(buffer_list)
        
        elif(self.char_type=="final"):
            #diccionario con nombre de carpeta y cantidad de frames segun accion
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


    def move_update (self):
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
       
        #actualizar posicion del rectangulo
        self.rect.x += delta_x
        self.rect.y += delta_y

    def shooting_spell(self,spell_group):
        if (self.spell_cooldown == 0 ):
            self.enemy_spell_sfx.set_volume(0.05)
            self.enemy_spell_sfx.play()
            self.spell_cooldown = 100 #disparo una vez y hay que esperar hasta el siguiente  
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
            
    
    def enemy_actions(self,player,spell_group):
        if (self.is_alive and player.is_alive):
            if(random.randint(1,20) == 1): #probabilidad de 1/20
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
            self.kill() #quita al enemigo de la pantalla y del grupo de sprites
            player.kill_count += 1

    def cooldown_update(self):
        if (self.spell_cooldown > 0):
            self.spell_cooldown -= 1

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
        
    def action_update(self,new_ation):
        #verificar accion nueva es disntina a la anterior
        if (new_ation != self.character_action_index):
            self.character_action_index = new_ation
            self.frame_index = 0 #iniciar nueva accion en el frame 0
            self.time_update = pygame.time.get_ticks()

    def update(self):
        self.animation_update()
        self.cooldown_update()
        self.move_update()
        self.verify_is_alive_update()
        
    def draw (self,screen):
        if (DEBUG_MODE):
            pygame.draw.rect(screen,RED,self.rect,1)
        screen.blit(self.image,self.rect)

        

'''class MetodoAuxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet(path,columnas,filas,flip=False, step = 1,scale=1):
        lista = []
        surface_imagen = pygame.image.load(path)
        fotograma_ancho = int(surface_imagen.get_width()/columnas)
        fotograma_alto = int(surface_imagen.get_height()/filas)
        fotograma_ancho_scaled = int(fotograma_ancho*scale)
        fotograma_alto_scaled = int(fotograma_alto*scale)
        x = 0
        
        for fila in range(filas):
            for columna in range(0,columnas,step):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
                if(scale != 1):                    
                    surface_fotograma = pygame.transform.scale(surface_fotograma,(fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha()
                if(flip):
                    surface_fotograma = pygame.transform.flip(surface_fotograma,True,False)
                lista.append(surface_fotograma)
        return lista'''



        

                