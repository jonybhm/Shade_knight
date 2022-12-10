import pygame
from auxiliar import *
from constantes import *
from button import *


class Form:
    '''
    This class represents any form that's active on screen 
    '''
    forms_dict = {}
    def __init__(self,name:str,master_surface:object,x:int,y:int,active:bool,level_num:int,music_name:str) -> None:
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.active = active
        self.x = x
        self.y = y
        self.level_num = level_num
        self.music_name = music_name
                
    def set_active(self,name:str)->None:
        '''
        Set active the form 
        Arguments: name of the form (str)
        Returns: None
        '''
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.forms_dict[name].active = True

    def music_update(self)->None:
        '''
        Loads and plays music for each form
        Arguments: None
        Returns: None
        '''
        pygame.mixer.music.stop()
        pygame.mixer.music.load(PATH + r"\\music\\{}.wav".format(self.music_name))
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1,0.0,7000) 
        
        
    def draw(self)->None:
        '''
        Merges the form with the one from the main screen
        Arguments: None
        Returns: None
        '''
        self.master_surface.blit(self.surface,self.slave_rect)

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
    
class FormStartLevel(Form):
    def __init__(self,name:str,master_surface:object,x:int,y:int,active:bool,level_num:int,music_name:str)->None:
        '''
        This class represents the start level form  
        '''
        super().__init__(name,master_surface,x,y,active,level_num,music_name)
        self.level_restart = False
        self.advance_level = False
        self.game_ending = False
        self.level_timer = 120
        self.first_last_timer = pygame.time.get_ticks()
               
        self.screen = master_surface
              
        self.music_update()
        self.player = Character(char_type="player",x=200,y=200,speed=8,magic=5,health=100)
        self.spell_group_player = pygame.sprite.Group()

        self.level_info = load_json(PATH + r"\\level\\level_info.json")

        self.level = Level(total_items=self.level_info[level_num]["number_max_items"],background=self.level_info[level_num]["background"],
        max_platforms=self.level_info[level_num]["number_max_platform"],platform_type=self.level_info[level_num]["platform_type"],
        platform_height=self.level_info[level_num]["platform_height"],platform_width=self.level_info[level_num]["platform_width"],
        music=self.level_info[level_num]["music"])

        self.imagen_scroll = self.level.generate_background()

        self.health=self.level.generate_health_update()
        self.magic=self.level.generate_magic_update()
        self.money=self.level.generate_money_update()
        self.trap=self.level.generate_trap_update()
        self.items_group = self.level.items_group

        self.level.generate_platforms()
        self.platform_group = self.level.platform_group

        self.enemies = EnemyManager(total_enemies=self.level_info[level_num]["number_max_enemies"],
        enemy_type=self.level_info[level_num]["enemy_type"],enemy_timer=self.level_info[level_num]["enemy_timer"],
        enemy_health=self.level_info[level_num]["enemy_health"],enemy_scale=self.level_info[level_num]["enemy_scale"])
        self.enemies.manage_enemies_update(self.player)
        self.enemy_group = self.enemies.managed_enemy_group
        self.spell_group_enemy = self.level.spell_group_enemy    

        self.health_image = pygame.image.load(PATH + r"\\items\\health_icon.png")
        self.health_image = pygame.transform.scale(self.health_image,(25,25)).convert_alpha()
        
        self.magic_image = pygame.image.load(PATH + r"\\items\\magic_icon.png")
        self.magic_image = pygame.transform.scale(self.magic_image,(25,25)).convert_alpha()
        
        self.money_image = pygame.image.load(PATH + r"\\items\\money_icon.png")
        self.money_image = pygame.transform.scale(self.money_image,(25,25)).convert_alpha()  

        self.clock = pygame.time.Clock()

        self.scroll = 0 
        self.tiles = math.ceil(SCREEN_WIDTH /self.imagen_scroll.get_width()) + 1 
        
        pygame.mixer.music.stop()
        self.level.generate_music()
        
        
    def draw(self)->None:
        '''
        Merges the elements of the form with the one from the main screen
        Arguments: None
        Returns: None
        '''
        for widget in self.widget_list:    
            widget.draw()

        if(DEBUG_MODE):
            for debug_text in self.widget_list_debug:    
                debug_text.draw()
            
        
        self.player.draw(screen=self.screen)

        for enemy in self.enemy_group:
            enemy.draw(screen=self.screen)

        for platform in self.platform_group:
            platform.draw(screen=self.screen)

        self.spell_group_player.draw(self.screen)
        self.spell_group_enemy.draw(self.screen)
        self.items_group.draw(self.screen)

        self.screen.blit(self.money_image,(2.5,55))
        self.screen.blit(self.magic_image,(2.5,30))
        self.screen.blit(self.health_image,(2.5,5))

    def update(self,event_list:list)->None:
        '''
        Executes the methods that need update 
        Arguments: event list (list)
        Returns: None
        '''
        
        if (DEBUG_MODE):
           
            self.game_info_total_enemigos = TextTitle(x=150,y=SCREEN_HEIGHT-225,
            text="TOTAL ENEMIGOS: {0}".format(self.enemies.total_enemies),screen=self.screen,font_size=25)
            self.game_info_vencidos = TextTitle(x=150,y=SCREEN_HEIGHT-200,
            text="TOTAL VENCIDOS: {0}".format(self.player.kill_count),screen=self.screen,font_size=25)
            self.game_info_small_spell = TextTitle(x=150,y=SCREEN_HEIGHT-175,
            text="SMALL SPELL COOLDOWN: {0}".format(self.player.spell_small_cooldown),screen=self.screen,font_size=25)
            self.game_info_bog_spell = TextTitle(x=150,y=SCREEN_HEIGHT-150,
            text="BIG SPELL COOLDOWN: {0}".format(self.player.spell_cooldown),screen=self.screen,font_size=25)
            self.game_info_score = TextTitle(x=150,y=SCREEN_HEIGHT-125,
            text="SCORE: {0}".format(self.player.score),screen=self.screen,font_size=25)
            self.game_info_enemy_timer = TextTitle(x=150,y=SCREEN_HEIGHT-100,
            text="ENEMY TIMER: {0}".format(self.enemies.timer),screen=self.screen,font_size=25)
            self.game_info_money_timer = TextTitle(x=150,y=SCREEN_HEIGHT-75,
            text="MONEY TIMER: {0}".format(self.level.timer_money),screen=self.screen,font_size=25)
            self.game_info_health_timer = TextTitle(x=150,y=SCREEN_HEIGHT-50,
            text="HEALTH TIMER: {0}".format(self.level.timer_health),screen=self.screen,font_size=25)
            self.game_info_magic_timer = TextTitle(x=150,y=SCREEN_HEIGHT-25,
            text="MAGIC TIMER: {0}".format(self.level.timer_magic),screen=self.screen,font_size=25)
            
            self.widget_list_debug = [self.game_info_total_enemigos,self.game_info_vencidos,self.game_info_bog_spell,self.game_info_small_spell,
            self.game_info_enemy_timer,self.game_info_health_timer,self.game_info_magic_timer,self.game_info_money_timer,self.game_info_score]

        self.info_timer = TextTitle(x=SCREEN_WIDTH-150,y=20,text="TIEMPO RESTANTE: {0}".format(self.level_timer),screen=self.screen,font_size=25)
        
        self.info_salud_player = TextTitle(x=100,y=20,text="SALUD: {0}%".format(self.player.health),screen=self.screen,font_size=25)
        
        self.info_magia_player = TextTitle(x=100,y=45,text="MAGIA: X{0}".format(self.player.magic),screen=self.screen,font_size=25)
        
        self.info_dinero_player = TextTitle(x=100,y=70,text="DINERO: X{0}".format(self.player.money),screen=self.screen,font_size=25)
       
        self.widget_list = [self.info_salud_player,self.info_magia_player,self.info_dinero_player,self.info_timer]

        self.clock.tick(FPS)
         
        i = 0
        while(i < self.tiles):
            self.screen.blit(self.imagen_scroll, (self.imagen_scroll.get_width()*i+ self.scroll, 0)) 
            i += 1
        self.scroll -= 6  
        if abs(self.scroll) > self.imagen_scroll.get_width():
            self.scroll = 0 

                
        self.player.update(self.platform_group,event_list) 
    
        for enemy in self.enemy_group:
            enemy.update()
            enemy.enemy_actions(self.player,self.spell_group_enemy)

        for platform in self.platform_group:
            platform.update(self.spell_group_enemy,self.spell_group_player,self.platform_group)
                    
        self.spell_group_player.update(self.player,self.spell_group_player,self.spell_group_enemy,self.enemy_group)

        self.spell_group_enemy.update(self.player,self.spell_group_player,self.spell_group_enemy,self.enemy_group)

        self.items_group.update(self.player)
        self.level.update() 
        self.enemies.update(self.player)

        if(self.level_timer >0):
            current_timer = pygame.time.get_ticks()
            if (current_timer - self.first_last_timer > 1000):
                self.level_timer -=1
                self.first_last_timer = current_timer

        
        if (self.player.is_alive):
            if (self.player.is_shoot_spell):
                self.player.shooting_spell(self.spell_group_player)
            if (self.player.is_shoot_spell_small):
                self.player.shooting_spell_small(self.spell_group_player)
                
            if (self.player.is_move_left or self.player.is_move_right or
            self.player.is_move_up or self.player.is_move_down):
                self.player.action_update(2)#"2" = "move"
            else:
                self.player.action_update(0)#"0" = "idle"

    def level_advance(self)->None:    
        '''
        Verifys if the level needs to advance and then empties all the groups
        Arguments: None
        Returns: None
        '''        
        if(self.player.kill_count == self.enemies.total_enemies or self.level_timer == 0):
            
            if(self.level_num < len(self.level_info)-1):
                self.advance_level = True
                self.spell_group_player.empty()
                self.spell_group_enemy.empty()
                self.platform_group.empty()
                self.items_group.empty()
                self.enemy_group.empty()
            else:
                self.game_ending = True
                
    
    def restart_level(self)->None:
        '''
        Verifys if the level needs to restart and then empties all the groups
        Arguments: None
        Returns: None
        '''
        self.player = Character(char_type="player",x=200,y=200,speed=8,magic=5,health=100) 
        self.spell_group_player.empty()
        self.spell_group_enemy.empty()
        self.platform_group.empty()
        self.items_group.empty()
        self.enemy_group.empty()
        self.level_restart = True

           

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
