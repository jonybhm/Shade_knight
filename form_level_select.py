from forms import *

class FormLevelSelect(Form):
    def __init__(self,name:str,master_surface:object,x:int,y:int,active:bool,level_num,music_name:str)->None:
        '''
        This class represents the level select form  
        '''
        super().__init__(name,master_surface,x,y,active,level_num,music_name)
       
        self.surface = pygame.image.load(PATH + r"\\menu\\menu_widget.png").convert_alpha()
        self.surface = pygame.transform.scale(self.surface,(SCREEN_WIDTH,SCREEN_HEIGHT))
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y

        self.level_selected = 0
        self.is_selected = False           
        
        self.levels_title = TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-300,text="SHADE KNIGHT",screen=master_surface,font_size=75)
        self.levels_subtitle = TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-200,text="ELEGIR NIVEL",screen=master_surface,font_size=50)
        
        self.button_level_1 = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-100,text="NIVEL 1",screen=master_surface,
        on_click=self.click_level_1,on_click_param="form_start_level")
        self.button_level_2 = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2,text="NIVEL 2",screen=master_surface,
        on_click=self.click_level_2,on_click_param="form_start_level")
        self.button_level_3 = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+100,text="NIVEL 3",screen=master_surface,
        on_click=self.click_level_3,on_click_param="form_start_level")
        self.button_back = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+200,text="VOLVER",screen=master_surface,
        on_click=self.click_back,on_click_param="form_main_menu")

                  
        self.widget_list = [self.levels_subtitle,self.levels_title,self.button_level_1,
        self.button_level_2,self.button_level_3,self.button_back]
    
    def click_level_1(self,parametro:str)->None: 
        '''
        Sets active start level form and sets level number 
        Arguments: parametro (str)  
        Returns: None
        '''  
        self.set_active(parametro)
        self.level_selected = 0
        self.is_selected = True  

    def click_level_2(self,parametro:str)->None: 
        '''
        Sets active start level form and sets level number 
        Arguments: parametro (str)  
        Returns: None
        '''  
        self.set_active(parametro)
        self.level_selected = 1
        self.is_selected = True

    def click_level_3(self,parametro:str)->None: 
        '''
        Sets active start level form and sets level number 
        Arguments: parametro (str)  
        Returns: None
        '''  
        self.set_active(parametro)
        self.level_selected = 2
        self.is_selected = True

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
