import pygame
from auxiliar import *
from constantes import *
from button import *


class Form:
    '''
    This class represents any form that's active on screen 
    '''
    forms_dict = {}
    def __init__(self,name:str,master_surface:object,x:int,y:int,active:bool,level_num:int,music_name:str) -> None:
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.active = active
        self.x = x
        self.y = y
        self.level_num = level_num
        self.music_name = music_name
                
    def set_active(self,name:str)->None:
        '''
        Set active the form 
        Arguments: name of the form (str)
        Returns: None
        '''
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.forms_dict[name].active = True

    def music_update(self)->None:
        '''
        Loads and plays music for each form
        Arguments: None
        Returns: None
        '''
        pygame.mixer.music.stop()
        pygame.mixer.music.load(PATH + r"\\music\\{}.wav".format(self.music_name))
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1,0.0,7000) 
        
        
    def draw(self)->None:
        '''
        Merges the form with the one from the main screen
        Arguments: None
        Returns: None
        '''
        self.master_surface.blit(self.surface,self.slave_rect)