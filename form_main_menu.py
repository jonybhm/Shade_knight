from forms import *

class FormMainMenu(Form):
    '''
    This class represents the main menu form  
    '''
    def __init__(self,name:str,master_surface:object,x:int,y:int,active:bool,level_num:int,music_name:str)->None:
        super().__init__(name,master_surface,x,y,active,level_num,music_name)
        
        self.start_first_level = False
        self.music_update() 

        self.surface = pygame.image.load(PATH + r"\\menu\\menu_widget.png").convert_alpha()
        self.surface = pygame.transform.scale(self.surface,(SCREEN_WIDTH,SCREEN_HEIGHT))
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        
        self.menu_ppal_title = TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-300,text="SHADE KNIGHT",screen=master_surface,font_size=75)
        self.menu_ppal_subtitle = TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-200,text="MENU PRINCIPAL",screen=master_surface,font_size=50)

        self.button_start = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-75,text="COMENZAR",screen=master_surface
        ,on_click=self.click_start)
        self.button_level_select = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2,text="SELECCIONAR NIVEL",screen=master_surface
        ,on_click=self.click_level_select,on_click_param="form_level_select")
        self.button_options = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+75,text="OPCIONES",screen=master_surface
        ,on_click=self.click_options,on_click_param="form_options")
        self.button_rankings = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+150,text="RANKINGS",screen=master_surface
        ,on_click=self.click_rankings,on_click_param="form_rankings")
        self.button_exit = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+225,text="SALIR",screen=master_surface
        ,on_click=self.click_exit)
        
        self.widget_list = [self.menu_ppal_subtitle,self.menu_ppal_title,self.button_start,
        self.button_level_select,self.button_options,self.button_exit,self.button_rankings]
           
       
    def click_start(self,parametro)->None:
        '''
        Sets star level flag as True 
        Arguments: parametro (str)  
        Returns: None
        '''  
        self.start_first_level = True
        
    def click_level_select(self,parametro)->None: 
        '''
        Sets active level selct form 
        Arguments: parametro (str)  
        Returns: None
        '''  
        self.set_active(parametro)
        
    def click_options(self,parametro)->None:
        '''
        Sets active options form 
        Arguments: parametro (str)  
        Returns: None
        '''  
        self.set_active(parametro)
        
    def click_exit(self,parametro)->None: 
        '''
        Sets active exit form 
        Arguments: parametro (str)  
        Returns: None
        '''  
        self.set_active(parametro)

    def click_rankings(self,parametro)->None:
        '''
        Sets active rankings form 
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