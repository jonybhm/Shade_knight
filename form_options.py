from forms import *

class FormOptions(Form):
    def __init__(self,name:str,master_surface:object,x:int,y:int,active:bool,level_num:int,music_name:str)->None:
        '''
        This class represents the options form  
        '''
        super().__init__(name,master_surface,x,y,active,level_num,music_name)

        self.surface = pygame.image.load(PATH + r"\\menu\\menu_widget.png").convert_alpha()
        self.surface = pygame.transform.scale(self.surface,(SCREEN_WIDTH,SCREEN_HEIGHT))
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        

        self.options_title = TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-300,text="SHADE KNIGHT",screen=master_surface,font_size=75)
        self.options_subtitle = TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-200,text="OPCIONES",screen=master_surface,font_size=50)

        self.button_music_on = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-100,text="MUSIC ON",screen=master_surface,
        on_click=self.click_music_on)
        self.button_music_off = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2,text="MUSIC OFF",screen=master_surface,
        on_click=self.click_music_off)
        self.button_full_screen = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+100,text="PANTALLA COMPLETA",screen=master_surface,
        on_click=self.click_full_screen)
       
        self.button_back = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+200,text="VOLVER",screen=master_surface,
        on_click=self.click_back,on_click_param="form_main_menu")
        
        self.widget_list = [self.options_subtitle,self.options_title,self.button_music_on,
        self.button_music_off,self.button_full_screen,self.button_back]
    
    def click_music_on(self,parametro:str)->None: 
        '''
        Unpauses music
        Arguments: parametro (str)  
        Returns: None
        '''  
        pygame.mixer.music.unpause()
    
    def click_music_off(self,parametro:str)->None: 
        '''
        Pauses music
        Arguments: parametro (str)  
        Returns: None
        '''  
        pygame.mixer.music.pause()
    
    def click_full_screen(self,parametro:str)->None:
        '''
        Sets full screen mode 
        Arguments: parametro (str)  
        Returns: None
        '''   
        pygame.display.toggle_fullscreen()

    def click_back(self,parametro:str)->None: 
        '''
        Sets active main menu form 
        Arguments: parametro (str)  
        Returns: None
        '''  
        self.set_active(parametro)

    def draw(self)->None:
        '''
        Merges the form with the one from the main screen
        Arguments: None
        Returns: None
        '''
        super().draw()
        for widget in self.widget_list:    
            widget.draw()

    def update(self)->None:
        '''
        Executes the methods that need update 
        Arguments: None
        Returns: None
        '''
        super().draw()
        for widget in self.widget_list:    
            widget.update()