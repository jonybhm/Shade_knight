import json
import pygame
from constantes import *
from level import *
from manager import *



@staticmethod
class MetodoAuxiliar:
    def getSurfaceFromSprite(path,columnas,filas,flip=False, step = 1,scale=1):
        lista = []
        surface_imagen = pygame.image.load(path).convert_alpha()
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


def show_text_on_screen(x,y,text,screen,font_size):
    font = pygame.font.Font(PATH + r"\\font\\alagard.ttf",font_size)
    image_text = font.render(text,True,(255,255,255))
    screen.blit(image_text,(x,y))




def draw_bg(screen):
    screen.fill((0,0,0))

def load_json(path:str)->list:
    with open(path,"r") as file:
        dic_file = json.load(file)

    return dic_file["levels"]

'''def restart_level(group_spells_player,group_spells_enemies,group_platforms,group_items,level_number):
    group_spells_player.empty()
    group_spells_enemies.empty()
    group_platforms.empty()
    group_items.empty()
    

    level_info = load_json(PATH + r"\\level\\level_info.json")

    level = Level(total_items=level_info[level_number]["number_max_items"],background=level_info[level_number]["background"],
    max_platforms=level_info[level_number]["number_max_platform"],platform_type=level_info[level_number]["platform_type"],
    platform_height=level_info[level_number]["platform_height"],platform_width=level_info[level_number]["platform_width"],
    music=level_info[level_number]["music"])
    
    return level

def restart_enemies(group_enemies,level_number):
    group_enemies.empty()

    level_info = load_json(PATH + r"\\level\\level_info.json")

    enemies = EnemyManager(total_enemies=level_info[level_number]["number_max_enemies"],
    enemy_type=level_info[level_number]["enemy_type"],enemy_timer=level_info[level_number]["enemy_timer"],
    enemy_health=level_info[level_number]["enemy_health"],enemy_scale=level_info[level_number]["enemy_scale"])

    return enemies'''