import json
import pygame
from constantes import *
from level import Level
from enemy_manager import *
from character import *




def show_text_on_screen(x:int,y:int,text:str,screen:object,font_size:int)->None:
    '''
    Shows text on the main screen of the game 
    Arguments: text to be shown (string), position in screen x (int) and y (int), the main screen (Surface), and the font size  (int)
    Returns: None
    '''
    font = pygame.font.Font(PATH + r"\\font\\alagard.ttf",font_size)
    image_text = font.render(text,True,(255,255,255))
    screen.blit(image_text,(x,y))

def load_json(path:str)->list:
    '''
    It loads a file .json and returns the info inside a list
    Arguments: path to a .json file (string)
    Returns: a list containing the info from that .json (list)
    '''
    with open(path,"r") as file:
        dic_file = json.load(file)

    return dic_file["levels"]

