import pygame
import random
from constantes import *
#from auxiliar import MetodoAuxiliar



class Platform(pygame.sprite.Sprite):
    
    def __init__(self,speed,w,h,type):
        pygame.sprite.Sprite.__init__(self)
        self.image = MetodoAuxiliar.getSurfaceFromSpriteSheet(PATH + r"\\platforms\\platforms.png",3,1)[type]
        self.image = pygame.transform.scale(self.image,(w,h))
        
        self.rect = self.image.get_rect()
        self.x=SCREEN_WIDTH
        self.y=random.randrange(0 + (self.rect.size[0]),SCREEN_HEIGHT - (self.rect.size[0]),(self.rect.size[0])*2)
        self.rect.center = (self.x,self.y)

        self.speed = speed
        self.direction = 1
        self.platform_move_limit = 0
        self.is_move_left = True
        
    def move_update (self):
        #reiniciar variables de movimiento
        delta_x = 0
        delta_y = 0  

        #variables de movimiento
        if (self.is_move_left):
            delta_x = -self.speed*2

        if (self.is_move_up):
            delta_y = -self.speed

        if (self.is_move_down):
            delta_y = self.speed

        #actualizar posicion del rectangulo
        self.rect.x += delta_x
        self.rect.y += delta_y

    def platform_wave(self):

        if (self.direction==-1):
            self.is_move_up = False
            self.is_move_down = True
        elif (self.direction==1):
            self.is_move_down = False
            self.is_move_up = True 
                            
        self.move_update()    
        self.platform_move_limit += 1 

        if (self.platform_move_limit > 25):
            self.direction *= -1
            self.platform_move_limit *= -1
            


    #colisiones con plataformas
    def collide_update (self,spell_group_enemy,spell_group_player,platform_group):
        for spell in spell_group_enemy:
            if (pygame.sprite.spritecollide(spell,platform_group,False)):
                spell.kill()   
        
        for spell in spell_group_player:
            if (pygame.sprite.spritecollide(spell,platform_group,False)):
                spell.kill() 
    

    def draw(self,screen):
        if(DEBUG_MODE):
            pygame.draw.rect(screen,RED,self.rect,1)

        screen.blit(self.image,self.rect)

    def update(self,spell_group_enemy,spell_group_player,platform_group):
        self.platform_wave()
        self.collide_update(spell_group_enemy,spell_group_player,platform_group)

class MetodoAuxiliar:
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
        return lista
      


        