import pygame
from auxiliar import *
from constantes import *


class Widget:
    def __init__ (self,x,y,text,screen,font_size=25):
        self.font_size = font_size
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        
        
        
    def draw(self):
        
        #mostrar texto en pantalla
        self.screen.blit(self.image,(self.rect.x,self.rect.y))

   

class Button(Widget):
    def __init__ (self,x,y,text,screen,on_click=None,on_click_param=None,font_size=25):
        super().__init__(x,y,text,screen,font_size)
        self.font = pygame.font.Font(PATH + r"\\font\\alagard.ttf",self.font_size)
        self.image = self.font.render(self.text,True,(255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.click_option_sfx = pygame.mixer.Sound(PATH +r"\\sfx\\menu_select.wav")
        self.on_click = on_click
        self.on_click_param = on_click_param
        
    def button_pressed(self):
        
        #posicion del mouse
        pos = pygame.mouse.get_pos()

        #colision mouse/boton
        if (self.rect.collidepoint(pos)):
            if (pygame.mouse.get_pressed()[0] == 1):
                self.on_click(self.on_click_param)
                self.click_option_sfx.set_volume(0.2)
                self.click_option_sfx.play()
    
    def draw(self):
        super().draw()
        #mostrar texto en pantalla       
        
    def update(self):
        self.draw()
        self.button_pressed()
        
class TextTitle(Widget):
    def __init__ (self,x,y,text,screen,font_size=50):
        super().__init__(x,y,text,screen,font_size)
        self.font = pygame.font.Font(PATH + r"\\font\\alagard.ttf",self.font_size)
        self.image = self.font.render(self.text,True,(255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
    def draw(self):
        super().draw()
        #mostrar texto en pantalla
    
    def update(self):
        self.draw()
        
    
    

class TextBox(Widget):
    def __init__ (self,x,y,text,screen,font_size=50):
        super().__init__(x,y,text,screen,font_size)
        
        self.image = pygame.image.load(PATH + r"\\menu\\text_box.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(500,100))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def draw(self):
        super().draw()
        #mostrar texto en pantalla

    '''def button_pressed(self):
        action = False
        #posicion del mouse
        pos = pygame.mouse.get_pos()

        #colision mouse/boton
        if (self.rect.collidepoint(pos)):
            if (pygame.mouse.get_pressed()[0] == 1 and self.click == False):
                action = True
                self.click = True
                self.click_option_sfx.set_volume(0.2)
                self.click_option_sfx.play()
            if (pygame.mouse.get_pressed()[0] == 0):
                action = False
        
        return action

    def update(self):
        self.draw()
        action = self.button_pressed()

        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN and action):
                if (event.key == pygame.K_BACKSPACE):
                    self._text = self._text[:-1]
                else:
                    self._text += event.unicode



'''