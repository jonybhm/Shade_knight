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
    def __init__ (self,x,y,text,screen,on_click=None,on_click_param=None,font_size=25):
        super().__init__(x,y,text,screen,font_size)
        self.font = pygame.font.Font(PATH + r"\\font\\alagard.ttf",self.font_size)
        self.image = self.font.render(self.text,True,(255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.click_option_sfx = pygame.mixer.Sound(PATH +r"\\sfx\\menu_select.wav")
        self.on_click = on_click
        self.on_click_param = on_click_param
        self.write_on = False
        #self.state = M_STATE_NORMAL
        self._wrting = ""
        self.image_wrting = self.font.render(self._wrting,True,(255,255,255))
        self.rect_wrting = self.image_wrting.get_rect()
        self.rect_wrting.center = (x,y)
        
        
        
    def box_pressed(self):
        
        #posicion del mouse
        pos = pygame.mouse.get_pos()
        event_list = pygame.event.get()
        
        #colision mouse/boton
        for event in event_list:
            if (event.type == pygame.MOUSEBUTTONDOWN):
                self.click_option_sfx.set_volume(0.2)
                self.click_option_sfx.play()
                self.write_on = self.rect.collidepoint(pos)
            if (event.type == pygame.KEYDOWN and self.write_on):
                if event.key == pygame.K_RETURN:
                    self.write_on = False
                elif event.key == pygame.K_BACKSPACE:
                    self._wrting = self._wrting[:-1]
                else:
                    self._wrting += event.unicode
    
    def draw(self):
        super().draw()
        self.image.blit(self.screen,(self.rect_wrting.x,self.rect_wrting.y))
        #mostrar wrtingo en pantalla       
        
    def update(self):
        self.draw()
        self.box_pressed()
        #print(self._wrting)
        #print(self.write_on)
