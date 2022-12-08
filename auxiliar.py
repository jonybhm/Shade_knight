import json
import pygame
from constantes import *
from level import Level
from enemy_manager import *
from character import *




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

