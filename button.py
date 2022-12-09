import pygame
from auxiliar import *
from constantes import *


class Widget:
    '''
    This class represents any graphic interface on the screen 
    '''
    def __init__ (self,x:int,y:int,text:str,screen:object,font_size:int=25)->None:
        self.font_size = font_size
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        
        
        
    def draw(self)->None:
        '''
        Merges the surface representing the widget with the one from the main screen
        Arguments: None
        Returns: None
        '''
        
        self.screen.blit(self.image,(self.rect.x,self.rect.y))

   

class Button(Widget):
    '''
    This class represents any button interactable on the screen 
    '''
    def __init__ (self,x:int,y:int,text:str,screen:object,on_click:object=None,on_click_param:str=None,font_size:int=25)->None:
        super().__init__(x,y,text,screen,font_size)
        self.font = pygame.font.Font(PATH + r"\\font\\alagard.ttf",self.font_size)
        self.image = self.font.render(self.text,True,(255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.click_option_sfx = pygame.mixer.Sound(PATH +r"\\sfx\\menu_select.wav")
        self.on_click = on_click
        self.on_click_param = on_click_param
        
    def button_pressed(self)->None:
        '''
        Detects if the button is pressed
        Arguments: None
        Returns: None
        '''
        
        pos = pygame.mouse.get_pos()
        
        if (self.rect.collidepoint(pos)):
            if (pygame.mouse.get_pressed()[0] == 1):
                pygame.time.delay(300)
                self.on_click(self.on_click_param)
                self.click_option_sfx.set_volume(0.2)
                self.click_option_sfx.play()
    
    def draw(self)->None:
        '''
        Merges the surface representing the player with the one from the main screen
        Arguments: None 
        Returns: None
        '''
        super().draw()
        #mostrar texto en pantalla       
        
    def update(self)->None:
        '''
        Executes the methods that need update 
        Arguments: None
        Returns: None
        '''
        self.draw()
        self.button_pressed()
        
class TextTitle(Widget):
    '''
    This class represents any non interactable text seen on the screen  
    '''
    def __init__ (self,x:int,y:int,text:str,screen:object,font_size:int=50)->None:
        super().__init__(x,y,text,screen,font_size)
        self.font = pygame.font.Font(PATH + r"\\font\\alagard.ttf",self.font_size)
        self.image = self.font.render(self.text,True,(255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
    def draw(self)->None:
        '''
        Merges the surface representing the player with the one from the main screen
        Arguments: None 
        Returns: None
        '''
        super().draw()
       
    
    def update(self)->None:
        '''
        Executes the methods that need update 
        Arguments: None
        Returns: None
        '''
        self.draw()
        
    
    

class TextBox(Widget):
    '''
    This class represents any text box on the screen where you can write
    '''
    def __init__ (self,x:int,y:int,text:str,screen:object,on_click:object=None,on_click_param:str=None,font_size:int=25)->None:
        super().__init__(x,y,text,screen,font_size)
        self.font = pygame.font.Font(PATH + r"\\font\\alagard.ttf",self.font_size)
        self.image = self.font.render(self.text,True,(255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.click_option_sfx = pygame.mixer.Sound(PATH +r"\\sfx\\menu_select.wav")
        self.on_click = on_click
        self.on_click_param = on_click_param
        self.write_on = True
        self._wrting = ""
        self.image_wrting = self.font.render(self._wrting,True,(255,255,255))
        self.rect_wrting = self.image_wrting.get_rect()
        self.rect_wrting.center = (x,y)
        
        
        
    def write_on_box(self,event_list:list)->None:
        '''
        Detects keys being pressed and generates text
        Arguments: event list (list)
        Returns: None
        '''
        
        for event in event_list:
            
            if (event.type == pygame.KEYDOWN and self.write_on):
                
                if event.key == pygame.K_BACKSPACE:
                    self._wrting = self._wrting[:-1]
                else:
                    self._wrting += event.unicode
    
    def draw(self)->None:
        '''
        Merges the surface representing the player with the one from the main screen
        Arguments: None 
        Returns: None
        '''
        super().draw()
        self.image.blit(self.screen,(self.rect_wrting.x,self.rect_wrting.y))
              
        
    def update(self,event_list:list)->None:
        '''
        Executes the methods that need update 
        Arguments: event list (list)
        Returns: None
        '''
        self.draw()
        self.write_on_box(event_list)
      



