import pygame
import json
from constantes import *
from auxiliar import *
from SQLITE import *
from forms import *

class FormManager:
    def __init__ (self,screen,ranking_info_db):
        '''
        A class that represents the manager of the forms
        '''
        
        self.main_screen = screen
        self.global_score = 0
        self.current_level = 0
        
        self.ranking_info_db = ranking_info_db
        
        self.form_main_menu = FormMainMenu(name="form_main_menu",master_surface=self.main_screen,x=0,y=0,active=True,level_num=1,music_name="main_menu")
        self.form_options = FormOptions(name="form_options",master_surface=self.main_screen,x=0,y=0,active=True,level_num=1,music_name="main_menu")
        self.form_level_select = FormLevelSelect(name="form_level_select",master_surface=self.main_screen,x=0,y=0,active=True,level_num=1,music_name="main_menu")
        self.form_start_level = FormStartLevel(name="form_start_level",master_surface=self.main_screen,x=0,y=0,active=True,level_num=self.current_level,music_name="main_menu")
        self.form_pause = FormPause(name="form_pause",master_surface=self.main_screen,x=0,y=0,active=True,level_num=self.current_level,music_name="main_menu")
        self.form_rankings = FormRanking(name="form_rankings",master_surface=self.main_screen,x=0,y=0,active=True,level_num=1,music_name="main_menu",ranking_list=self.ranking_info_db)
        self.form_enter_name = FormEnterName(name="form_enter_name",master_surface=self.main_screen,x=0,y=0,active=True,level_num=1,music_name="main_menu",score=self.global_score)
        self.form_screen_transition_reset = FormScreenTransition(name="form_screen_transition_reset",master_surface=self.main_screen,x=0,y=0,active=True,speed=4,direction=1,level_num=self.current_level,music_name="main_menu")
        self.form_screen_transition_advance = FormScreenTransition(name="form_screen_transition_advance",master_surface=self.main_screen,x=0,y=0,active=True,speed=4,direction=1,level_num=self.current_level+1,music_name="main_menu")

    def keys_update(self,event_list:list)->None:
        '''
        Checks if ESC key is pressed to acces the Pause form
        Arguments: event list (list)
        Returns: None
        '''

        for event in event_list:
        
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    self.form_pause.set_active("form_pause")
    
    def forms_update(self,event_list:list)->None:
        '''
        Updates and draw the forms given the specific conditions
        Arguments: event list (list)
        Returns: None
        '''

        if(self.form_main_menu.active):
            self.form_main_menu.update()
            self.form_main_menu.draw()
            if(self.form_main_menu.start_first_level == True): 
                self.current_level=0
                self.form_main_menu.start_first_level = False
                self.form_start_level = FormStartLevel(name="form_start_level",master_surface=self.main_screen,x=0,y=0,active=True,level_num=self.current_level,music_name="other_1")
                self.form_start_level.set_active("form_start_level")
            
        elif(self.form_options.active): 
            self.form_options.update()
            self.form_options.draw()

        elif(self.form_level_select.active): 
            self.form_level_select.update()
            self.form_level_select.draw()
            if(self.form_level_select.is_selected == True): 
                self.current_level=self.form_level_select.level_selected
                self.form_level_select.is_selected = False
                self.form_start_level = FormStartLevel(name="form_start_level",master_surface=self.main_screen,x=0,y=0,active=True,level_num=self.current_level,music_name="other_1")
                self.form_start_level.set_active("form_start_level")

        elif(self.form_start_level.active): 
            self.form_start_level.update(event_list)
            self.form_start_level.draw()
            self.form_start_level.level_advance()
                        
            
            if (self.form_start_level.advance_level == True ): 
                self.global_score += self.form_start_level.player.score 
                if(self.current_level < len(self.form_start_level.level_info)-1):
                    self.form_screen_transition_advance = FormScreenTransition(name="form_screen_transition_advance",master_surface=self.main_screen,x=0,y=0,active=True,speed=4,direction=1,level_num=self.current_level+1,music_name="main_menu")
                    self.form_screen_transition_advance.set_active("form_screen_transition_advance")
                    

            if(self.form_start_level.game_ending == True): 
                self.form_start_level.game_ending = False
                self.form_enter_name = FormEnterName(name="form_enter_name",master_surface=self.main_screen,x=0,y=0,active=True,level_num=1,music_name="ending",score=self.global_score)
                self.form_enter_name.set_active("form_enter_name")
            
            if (self.form_pause.level_restart == True or self.form_start_level.player.is_alive == False): 
                self.form_screen_transition_reset = FormScreenTransition(name="form_screen_transition_reset",master_surface=self.main_screen,x=0,y=0,active=True,speed=4,direction=1,level_num=self.current_level,music_name="main_menu")
                self.form_screen_transition_reset.set_active("form_screen_transition_reset")

        elif(self.form_pause.active):
            self.form_pause.update()
            self.form_pause.draw()

        elif(self.form_enter_name.active):
            self.form_enter_name.update(event_list)
            self.form_enter_name.draw()
            if(self.form_enter_name.confirm_name == True):            
                
                self.form_enter_name.confirm_name = False                    
                add_rows_sqlite(self.form_enter_name.text_box._wrting,self.global_score)
                self.ranking_info_db = view_rows_sqlite()
                 
                self.form_rankings = FormRanking(name="form_rankings",master_surface=self.main_screen,x=0,y=0,active=True,level_num=1,music_name="ending",
                ranking_list=self.ranking_info_db)
                self.form_rankings.set_active("form_rankings")

        elif(self.form_rankings.active):
            self.form_rankings.update()
            self.form_rankings.draw()
    
        elif(self.form_screen_transition_reset.active):
            self.form_screen_transition_reset.update()
            self.form_screen_transition_reset.draw()
            if(self.form_screen_transition_reset.transition_is_over == True):
                self.form_start_level.restart_level()
                self.form_pause.level_restart = False
                self.form_start_level = FormStartLevel(name="form_start_level",master_surface=self.main_screen,x=0,y=0,active=True,level_num=self.current_level,music_name="other_1")
                self.form_start_level.set_active("form_start_level")
        
        elif(self.form_screen_transition_advance.active):
            self.form_screen_transition_advance.update()
            self.form_screen_transition_advance.draw()
            if(self.form_screen_transition_advance.transition_is_over == True):
                self.form_start_level.advance_level = False
                self.current_level += 1         
                self.form_start_level = FormStartLevel(name="form_start_level",master_surface=self.main_screen,x=0,y=0,active=True,level_num=self.current_level,music_name="other_1")
                self.form_start_level.set_active("form_start_level")

    def update(self,event_list:list)->None:
        '''
        Executes the methods that need update 
        Arguments: event list (list)
        Returns: None
        '''
        self.keys_update(event_list)
        self.forms_update(event_list)