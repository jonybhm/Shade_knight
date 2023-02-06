from forms import *

class FormRanking(Form):
    '''
    This class represents the ranking form  
    '''
    def __init__(self,name:str,master_surface:object,x:int,y:int,active:bool,level_num:int,music_name:str,ranking_list:list)->None:
        super().__init__(name,master_surface,x,y,active,level_num,music_name)

        self.surface = pygame.image.load(PATH + r"\\menu\\menu_widget.png").convert_alpha()
        self.surface = pygame.transform.scale(self.surface,(SCREEN_WIDTH,SCREEN_HEIGHT))
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y

        self.ranking_on_screen = []
        self.ranking_list=ranking_list

        self.title = TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-300,text="SHADE KNIGHT",screen=master_surface,font_size=75)
        self.subtitle = TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-200,text="TOP 10 RANKINGS",screen=master_surface,font_size=50)
        self.button_return_menu = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+200,text="VOLVER AL MENU",screen=master_surface
        ,on_click=self.click_return_menu,on_click_param="form_main_menu")
                
               
        for i in range(len(ranking_list)):
            self.ranking_on_screen.append(TextTitle(x=SCREEN_WIDTH//2-100,y=SCREEN_HEIGHT//2.5+i*25,text="{0}".format(i+1),screen=master_surface,font_size=25))
            self.ranking_on_screen.append(TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2.5+i*25,text="{0}".format(ranking_list[i][1]),screen=master_surface,font_size=25))
            self.ranking_on_screen.append(TextTitle(x=SCREEN_WIDTH//2+100,y=SCREEN_HEIGHT//2.5+i*25,text="{0}".format(ranking_list[i][2]),screen=master_surface,font_size=25))
                 
        self.widget_list = [self.title,self.subtitle,self.button_return_menu]
    
   
    def click_return_menu(self,parametro:str)->None:
        '''
        Sets active main menu form  
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
        super().draw()
        for widget in self.widget_list:    
            widget.draw()
        for ranking in self.ranking_on_screen:    
            ranking.draw()
            

    def update(self)->None:
        '''
        Executes the methods that need update 
        Arguments: event list (list)
        Returns: None
        '''
        super().draw()
        for widget in self.widget_list:    
            widget.update()
