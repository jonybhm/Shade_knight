from forms import *

class FormPause(Form):
    def __init__(self,name:str,master_surface:object,x:int,y:int,active:bool,level_num:int,music_name:str)->None:
        '''
        This class represents the pause form  
        '''
        super().__init__(name,master_surface,x,y,active,level_num,music_name)
        self.level_restart = False
        self.current_level_number = level_num
        self.paused = pygame.mixer.music.get_busy() 

        self.surface = master_surface
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y

        self.menu_ppal_title = TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-300,text="SHADE KNIGHT",screen=master_surface,font_size=75)
        self.menu_ppal_subtitle = TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-200,text="PAUSA",screen=master_surface,font_size=50)

        self.button_resume = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-100,text="VOLVER AL NIVEL",screen=master_surface
        ,on_click=self.click_resume,on_click_param="form_start_level")
        self.button_restart = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2,text="REINICIAR NIVEL",screen=master_surface
        ,on_click=self.click_restart,on_click_param="form_start_level")
        self.button_music = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+100,text="MUSICA: ON/OFF",screen=master_surface
        ,on_click=self.click_music)
        self.button_return_menu = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+200,text="VOLVER AL MENU",screen=master_surface
        ,on_click=self.click_return_menu,on_click_param="form_main_menu")
        
        self.widget_list = [self.menu_ppal_subtitle,self.menu_ppal_title,self.button_resume,
        self.button_restart,self.button_music,self.button_return_menu]
           
       
    def click_resume(self,parametro:str)->None:  
        '''
        Sets active start level form and sets level number 
        Arguments: parametro (str)  
        Returns: None
        '''  
        self.set_active(parametro)
        
        
    def click_restart(self,parametro:str)->None:
        '''
        Sets active start level form and sets level number 
        Arguments: parametro (str)  
        Returns: None
        '''   
        self.set_active(parametro)
        self.level_restart = True
                

    def click_music(self,parametro:str)->None:
        '''
        Sets active start level form and sets level number 
        Arguments: parametro (str)  
        Returns: None
        '''  
        if (self.paused):
            pygame.mixer.music.unpause()
        if (not self.paused):
            pygame.mixer.music.pause()
        self.paused = not self.paused
        
    def click_return_menu(self,parametro:str)->None: 
        '''
        Sets active start level form and sets level number 
        Arguments: parametro (str)  
        Returns: None
        '''  
        self.set_active(parametro)
            
    def draw(self)->None:
        '''
        Merges the elements of the form with the one from the main screen
        Arguments: None
        Returns: None
        '''
        for widget in self.widget_list:    
            widget.draw()

    def update(self)->None:
        '''
        Executes the methods that need update 
        Arguments: event list (list)
        Returns: None
        '''
        super().draw()
        for widget in self.widget_list:    
            widget.update()
