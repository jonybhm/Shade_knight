from forms import *

class FormEnterName(Form):
    '''
    This class represents the enter name form  
    '''
    def __init__(self,name:str,master_surface:object,x:int,y:int,active:bool,level_num:int,music_name:str,score:int)->None:
        super().__init__(name,master_surface,x,y,active,level_num,music_name)

        self.surface = pygame.image.load(PATH + r"\\menu\\menu_widget.png").convert_alpha()
        self.surface = pygame.transform.scale(self.surface,(SCREEN_WIDTH,SCREEN_HEIGHT))
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
      
        self.music_update()
        self.confirm_name = False
                   
        self.title = TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-300,text="SHADE KNIGHT",screen=master_surface,font_size=75)
        self.subtitle = TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-200,text="INGRESE SU NOMBRE:",screen=master_surface,font_size=50)
        self.subtitle_score = TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-100,text="PUNTAJE:{0}".format(score),screen=master_surface,font_size=30)
        
        self.text_box = TextBox(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2,text="_________________",screen=master_surface)
        self.button_confirm_name = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+100,text="CONFIRMAR NOMBRE",screen=master_surface
        ,on_click=self.click_confirm_name)
        
        self.widget_list = [self.title,self.subtitle,self.subtitle_score,self.button_confirm_name]

        
    
    def click_confirm_name(self,parametro:str)->None: 
        '''
        Sets confirm name flag as True 
        Arguments: parametro (str)  
        Returns: None
        '''  
        self.confirm_name = True
        
    def draw(self)->None:
        '''
        Merges the elements of the form with the one from the main screen
        Arguments: None
        Returns: None
        '''
        super().draw()
        for widget in self.widget_list:    
            widget.draw()
        self.text_box.draw()
        self.writing_text  = TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-20,text="{0}".format(self.text_box._wrting.upper()),
        screen=self.master_surface,font_size=30)
        self.writing_text.draw()

    def update(self,event_list)->None:
        '''
        Executes the methods that need update 
        Arguments: event list (list)
        Returns: None
        '''
        super().draw()
        self.text_box.update(event_list)
        for widget in self.widget_list:    
            widget.update()  
