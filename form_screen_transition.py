from forms import *

class FormScreenTransition(Form):
    '''
    This class represents the screen transition form  
    '''
    def __init__(self,name:str,master_surface:object,x:int,y:int,level_num:int,music_name:str,active:bool,speed:int,direction:int)->None:
        super().__init__(name,master_surface,x,y,active,level_num,music_name)

        self.surface = master_surface
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y

        self.speed = speed
        self.transition_is_over = False
        
        self.timer = 600
        
        self.transition_rect = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.transition_rect_rect = self.transition_rect.get_rect()
        self.transition_rect.fill(BLACK)
        self.title = TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2,text="NIVEL {0}".format(level_num+1),screen=master_surface,font_size=75)

    def transition(self)->None:
        '''
        Sets transition os over flag as True if the timer reaches 0 
        Arguments: None
        Returns: None
        '''
        self.transition_is_over = False
              
        if (self.timer==0):
            self.transition_is_over = True
            self.timer = 600

    def timer_update(self)->None:
        '''
        Counts down the timer
        Arguments: None
        Returns: None
        '''
        if(self.timer > 0):
            self.timer -= 1

    def update(self)->None:
        '''
        Executes the methods that need update 
        Arguments: None
        Returns: None
        '''
        self.master_surface.blit(self.transition_rect,(self.transition_rect_rect.x,self.transition_rect_rect.y))
        self.title.draw()
        self.transition()
        self.timer_update()
