import pygame
import random
from constantes import *
#from auxiliar import MetodoAuxiliar


class Items(pygame.sprite.Sprite):
    def __init__(self,type,speed=5):
        pygame.sprite.Sprite.__init__(self)
        self.type = type #dada la cuadricula: health:1 , money:7 , magic:10
        self.image = MetodoAuxiliar.getSurfaceFromSpriteSheet(PATH + r"\\items\\items.png",3,4,scale=0.5)[type]
        self.rect = self.image.get_rect()
        self.x=SCREEN_WIDTH #random.randrange(0 + (self.rect.size[0]),SCREEN_WIDTH - (self.rect.size[0])) 
        self.y=random.randrange(0 + (self.rect.size[0]),SCREEN_HEIGHT - (self.rect.size[0]))
        self.rect.center = (self.x,self.y)

        self.pick_up_sfx = pygame.mixer.Sound(PATH +r"\\sfx\\menu_select.wav")

        self.speed = speed
        self.direction = 1
        self.is_move_left = True

    def move_update (self):
        #reiniciar variables de movimiento
        delta_x = 0
        #variables de movimiento
        if (self.is_move_left):
            delta_x = -self.speed
        #actualizar posicion del rectangulo
        self.rect.x += delta_x
    
    
    def pick_up_update(self,player):
        #verificar si el jugador colisiona con el item
        if (pygame.sprite.collide_rect(self,player)):
            self.pick_up_sfx.set_volume(0.2)
            self.pick_up_sfx.play()
            #verificar el tipo de item
            if (self.type == 1): #type health
                player.health += 10
                if (player.health > player.max_health):
                    player.health = player.max_health
            elif (self.type == 7): #type money
                player.money += 10
                player.score += player.money 
            elif (self.type == 10): #type magic
                player.magic += 1 
            elif (self.type == 4): #type magic
                player.health -= 10    
            self.kill()#borra el sprite del grupo

        #verificar si los items estan fuera de la pantalla
        if (self.rect.right < 0):
            self.kill() #elimina sprite del grupo




    def update(self,player):
        self.move_update()
        self.pick_up_update(player)
        
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

        