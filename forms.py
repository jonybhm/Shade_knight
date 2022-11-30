import pygame
from auxiliar import *
from constantes import *
from button import *


class Form:
    forms_dict = {}
    def __init__(self,name,master_surface,x,y,active,level_num,music_name) -> None:
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.active = active
        self.x = x
        self.y = y
        self.level_num = level_num
        self.music_name = music_name
                
        #FONDO menu ppal
        self.surface = pygame.image.load(PATH + r"\\menu\\menu_widget.png").convert_alpha()
        self.surface = pygame.transform.scale(self.surface,(SCREEN_WIDTH,SCREEN_HEIGHT))
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y

    def set_active(self,name):
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.forms_dict[name].active = True

    def music_update(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(PATH + r"\\music\\{}.wav".format(self.music_name))
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1,0.0,7000) 
        
        
        
    def draw(self):
        self.master_surface.blit(self.surface,self.slave_rect)

class FormMainMenu(Form):
    def __init__(self,name,master_surface,x,y,active,level_num,music_name):
        super().__init__(name,master_surface,x,y,active,level_num,music_name)
        
              
        self.music_update()
        #BOTONES instancio y dibujo en pantalla que toma la imagen del menu
        self.menu_ppal_title = TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-300,text="SHADE KNIGHT",screen=master_surface,font_size=75)
        self.menu_ppal_subtitle = TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-200,text="MENU PRINCIPAL",screen=master_surface,font_size=50)

        self.button_start = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-100,text="COMENZAR",screen=master_surface
        ,on_click=self.click_start,on_click_param="form_start_level")
        self.button_level_select = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2,text="SELECCIONAR NIVEL",screen=master_surface
        ,on_click=self.click_level_select,on_click_param="form_level_select")
        self.button_options = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+100,text="OPCIONES",screen=master_surface
        ,on_click=self.click_options,on_click_param="form_options")
        self.button_exit = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+200,text="SALIR",screen=master_surface
        ,on_click=self.click_exit)
        self.button_rankings = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+300,text="RANKINGS",screen=master_surface
        ,on_click=self.click_rankings,on_click_param="form_rankings")
        
        self.widget_list = [self.menu_ppal_subtitle,self.menu_ppal_title,self.button_start,
        self.button_level_select,self.button_options,self.button_exit,self.button_rankings]
           
        #ACCIONES DE BOTONES
        
    def click_start(self,parametro):  
        self.set_active(parametro)
        

    def click_level_select(self,parametro): 
        self.set_active(parametro)
        
    def click_options(self,parametro):
        self.set_active(parametro)
        
    def click_exit(self,parametro): 
        self.set_active(parametro)

    def click_rankings(self,parametro):
        self.set_active(parametro)

            
    def draw(self):
        super().draw()
        for widget in self.widget_list:    
            widget.draw()

    def update(self):
        super().draw()
        for widget in self.widget_list:    
            widget.update()
           


class FormOptions(Form):
    def __init__(self,name,master_surface,x,y,active,level_num,music_name):
        super().__init__(name,master_surface,x,y,active,level_num,music_name)
        
        #BOTONES instancio y dibujo en pantalla que toma la imagen del menu
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
    
    def click_music_on(self,parametro): 
        pygame.mixer.music.unpause()
    
    def click_music_off(self,parametro): 
        pygame.mixer.music.pause()
    
    def click_full_screen(self,parametro): 
        pass

    def click_back(self,parametro): 
        self.set_active(parametro)

    def draw(self):
        super().draw()
        for widget in self.widget_list:    
            widget.draw()

    def update(self):
        super().draw()
        for widget in self.widget_list:    
            widget.update()
    


class FormLevelSelect(Form):
    def __init__(self,name,master_surface,x,y,active,level_num,music_name):
        super().__init__(name,master_surface,x,y,active,level_num,music_name)
                   
              
        #BOTONES instancio y dibujo en pantalla que toma la imagen del menu
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
    
    def click_level_1(self,parametro): 
        self.set_active(parametro)
    
    def click_level_2(self,parametro): 
        self.set_active(parametro)
    
    def click_level_3(self,parametro): 
        self.set_active(parametro)

    def click_back(self,parametro): 
        self.set_active(parametro)

    def draw(self):
        super().draw()
        for widget in self.widget_list:    
            widget.draw()

    def update(self):
        super().draw()
        for widget in self.widget_list:    
            widget.update()
    
class FormStartLevel(Form):
    def __init__(self,name,master_surface,x,y,active,level_num,music_name):
        super().__init__(name,master_surface,x,y,active,level_num,music_name)
        self.level_restart = False
        self.advance_level = False
        self.screen = master_surface
        
        self.music_update()
        self.player = Character(char_type="player",x=200,y=200,speed=8,magic=5,health=100)
        self.spell_group_player = pygame.sprite.Group()

        #self.level_number = level_num
        self.level_info = load_json(PATH + r"\\level\\level_info.json")

        self.level = Level(total_items=self.level_info[level_num]["number_max_items"],background=self.level_info[level_num]["background"],
        max_platforms=self.level_info[level_num]["number_max_platform"],platform_type=self.level_info[level_num]["platform_type"],
        platform_height=self.level_info[level_num]["platform_height"],platform_width=self.level_info[level_num]["platform_width"],
        music=self.level_info[level_num]["music"])
        #background
        self.imagen_scroll = self.level.generate_background()
        #items
        self.health=self.level.generate_health_update()
        self.magic=self.level.generate_magic_update()
        self.money=self.level.generate_money_update()
        self.trap=self.level.generate_trap_update()
        self.items_group = self.level.items_group
        #platformas
        self.level.generate_platforms()
        self.platform_group = self.level.platform_group
        #enemigos
        self.enemies = EnemyManager(total_enemies=self.level_info[level_num]["number_max_enemies"],
        enemy_type=self.level_info[level_num]["enemy_type"],enemy_timer=self.level_info[level_num]["enemy_timer"],
        enemy_health=self.level_info[level_num]["enemy_health"],enemy_scale=self.level_info[level_num]["enemy_scale"])
        self.enemies.manage_enemies_update(self.player)
        self.enemy_group = self.enemies.managed_enemy_group
        self.spell_group_enemy = self.level.spell_group_enemy    

        #imagenes pantalla
        self.health_image = pygame.image.load(PATH + r"\\items\\health_icon.png")
        self.health_image = pygame.transform.scale(self.health_image,(25,25)).convert_alpha()
        
        self.magic_image = pygame.image.load(PATH + r"\\items\\magic_icon.png")
        self.magic_image = pygame.transform.scale(self.magic_image,(25,25)).convert_alpha()
        
        self.money_image = pygame.image.load(PATH + r"\\items\\money_icon.png")
        self.money_image = pygame.transform.scale(self.money_image,(25,25)).convert_alpha()  


        #setear framerate 
        self.clock = pygame.time.Clock()

        self.scroll = 0 #variable scrolling
        self.tiles = math.ceil(SCREEN_WIDTH /self.imagen_scroll.get_width()) + 1 #eliminar buffering
        
        pygame.mixer.music.stop()
        self.level.generate_music()
        
        
    def draw(self):
        for widget in self.widget_list:    
            widget.draw()
        
        self.player.draw(screen=self.screen)

        for enemy in self.enemy_group:
            enemy.draw(screen=self.screen)

        for platform in self.platform_group:
            platform.draw(screen=self.screen)

        self.spell_group_player.draw(self.screen)
        self.spell_group_enemy.draw(self.screen)
        self.items_group.draw(self.screen)

        self.screen.blit(self.money_image,(0,50))
        self.screen.blit(self.magic_image,(0,25))
        self.screen.blit(self.health_image,(0,0))

    def update(self,event_list):

        #texto en pantalla
        #mostrar info en pantalla / MODO DEBUG
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
        
        #salud personaje en pantalla 
        self.info_salud_player = TextTitle(x=100,y=20,text="SALUD: {0}%".format(self.player.health),screen=self.screen,font_size=25)
        
        #magia personaje en pantalla 
        self.info_magia_player = TextTitle(x=100,y=45,text="MAGIA: X{0}".format(self.player.magic),screen=self.screen,font_size=25)
        
        #dinero personaje en pantalla
        self.info_dinero_player = TextTitle(x=100,y=70,text="DINERO: X{0}".format(self.player.money),screen=self.screen,font_size=25)
       
        self.widget_list = [self.game_info_total_enemigos,self.game_info_vencidos,self.game_info_bog_spell,self.game_info_small_spell,
        self.game_info_enemy_timer,self.game_info_health_timer,self.game_info_magic_timer,self.game_info_money_timer,self.game_info_score,
        self.info_salud_player,self.info_magia_player,self.info_dinero_player]

        self.clock.tick(FPS)
         
        #pantalla scrolling en el fondo
        i = 0
        while(i < self.tiles):
            self.screen.blit(self.imagen_scroll, (self.imagen_scroll.get_width()*i+ self.scroll, 0)) #appendea la imagen de fondo al final de la misma imagen
            i += 1
        self.scroll -= 6  #frame para el scrolling
        if abs(self.scroll) > self.imagen_scroll.get_width():
            self.scroll = 0 #resetear el frame de scroll

                
        self.player.update(self.platform_group,event_list) 
    
        for enemy in self.enemy_group:
            enemy.update()
            enemy.enemy_actions(self.player,self.spell_group_enemy)

        for platform in self.platform_group:
            platform.update(self.spell_group_enemy,self.spell_group_player,self.platform_group)
                    
        self.spell_group_player.update(self.player,self.spell_group_player,self.spell_group_enemy,self.enemy_group)

        self.spell_group_enemy.update(self.player,self.spell_group_player,self.spell_group_enemy,self.enemy_group)

        self.items_group.update(self.player)
        #actualiza timer de items
        self.level.update() 
        #update timer enemigos
        self.enemies.update(self.player)

        

        #actualizar las acciones del personaje
        if (self.player.is_alive):
            if (self.player.is_shoot_spell):
                self.player.shooting_spell(self.spell_group_player)
            if (self.player.is_shoot_spell_small):
                self.player.shooting_spell_small(self.spell_group_player)
                
            if (self.player.is_move_left or self.player.is_move_right or
            self.player.is_move_up or self.player.is_move_down):
                self.player.action_update(2)#actualiza la accion a "2" = "move"
            else:
                self.player.action_update(0)#actualiza la accion a "0" = "idle"

    def level_advance(self):    
        #avanzar de nivel
        if(self.player.kill_count == self.enemies.total_enemies):
            
            if(self.level_num < len(self.level_info)):
                self.player = Character(char_type="player",x=200,y=200,speed=8,magic=5,health=100) #restart_player
                self.spell_group_player.empty()
                self.spell_group_enemy.empty()
                self.platform_group.empty()
                self.items_group.empty()
                self.enemy_group.empty()
                self.advance_level = True

                
            '''else:
                ingresar_score = True
                name_title = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-300,text="INGRESE SU NOMBRE:",screen=main_screen,font_size=50)
                
                name_input = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-200,text="{0}".format(ingreso_teclado),screen=main_screen,font_size=75)
                score_title = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-100,text="PUNTAJE:",screen=main_screen)
                score = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2,text="{0}".format(player.score),screen=main_screen)
                enter_button = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+100,text="ENTER".format(player.score),screen=main_screen)
                name_title.draw()
                name_input.draw()
                score_title.draw()
                score.draw()
                enter_button.draw()
                
                #ACCIONES DE BOTONES
                if(enter_button.button_pressed()):
                    ingresar_score = False
                    create_table_sqlite()
                    add_rows_sqlite(ingreso_teclado,player.score)
                    view_rows_sqlite()
                pygame.mixer.music.stop()
                pygame.mixer.music.load(PATH + r"\\music\\main_menu.wav")
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(-1,0.0,7000)'''
    
    def restart_level(self):

        self.player = Character(char_type="player",x=200,y=200,speed=8,magic=5,health=100) #restart_player
        self.spell_group_player.empty()
        self.spell_group_enemy.empty()
        self.platform_group.empty()
        self.items_group.empty()
        self.enemy_group.empty()
        self.level_restart = True
        

        
        
        
    

class FormPause(Form):
    def __init__(self,name,master_surface,x,y,active,level_num,music_name):
        super().__init__(name,master_surface,x,y,active,level_num,music_name)
        self.level_restart = False
        self.current_level_number = level_num
        #BOTONES instancio y dibujo en pantalla que toma la imagen del menu
        self.menu_ppal_title = TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-300,text="SHADE KNIGHT",screen=master_surface,font_size=75)
        self.menu_ppal_subtitle = TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-200,text="PAUSA",screen=master_surface,font_size=50)

        self.button_resume = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-100,text="VOLVER AL NIVEL",screen=master_surface
        ,on_click=self.click_resume,on_click_param="form_start_level_{0}".format(self.current_level_number))
        self.button_restart = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2,text="REINICIAR NIVEL",screen=master_surface
        ,on_click=self.click_restart,on_click_param="form_start_level")
        self.button_music = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+100,text="MUSICA: ON/OFF",screen=master_surface
        ,on_click=self.click_music)
        self.button_return_menu = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+200,text="VOLVER AL MENU",screen=master_surface
        ,on_click=self.click_return_menu,on_click_param="form_main_menu")
        
        self.widget_list = [self.menu_ppal_subtitle,self.menu_ppal_title,self.button_resume,
        self.button_restart,self.button_music,self.button_return_menu]
           
        #ACCIONES DE BOTONES
        
    def click_resume(self,parametro):  
        self.set_active(parametro)
        
        
    def click_restart(self,parametro): 
        self.set_active(parametro)
        self.level_restart = True
                

    def click_music(self,parametro):
        pygame.mixer.music.pause()
        
    def click_return_menu(self,parametro): 
        self.set_active(parametro)
            
    def draw(self):
        for widget in self.widget_list:    
            widget.draw()

    def update(self):
        super().draw()
        for widget in self.widget_list:    
            widget.update()
        

class FormRanking(Form):
    def __init__(self,name,master_surface,x,y,active,level_num,music_name,ranking_info_list):
        super().__init__(name,master_surface,x,y,active,level_num,music_name)
                   
        self.ranking_info_list = ranking_info_list
                   
        #BOTONES instancio y dibujo en pantalla que toma la imagen del menu
        self.title = TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-300,text="SHADE KNIGHT",screen=master_surface,font_size=75)
        self.subtitle = TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-200,text="TOP RANKINGS",screen=master_surface,font_size=50)
        for ranked_player in ranking_info_list:
            for i in range(len(ranking_info_list)):
                self.position_rank = TextTitle(x=SCREEN_WIDTH//2-100,y=SCREEN_HEIGHT//2+i*25,text="{0}".format(ranked_player["position"]),screen=master_surface,font_size=25)
                self.name_rank = TextTitle(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+i*25,text="{0}".format(ranked_player["name"]),screen=master_surface,font_size=25)
                self.score_rank = TextTitle(x=SCREEN_WIDTH//2+100,y=SCREEN_HEIGHT//2+i*25,text="{0}".format(ranked_player["score"]),screen=master_surface,font_size=25)

        self.button_return_menu = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-100,text="VOLVER AL MENU",screen=master_surface
        ,on_click=self.click_return_menu,on_click_param="form_main_menu")
                          
        self.widget_list = [self.title,self.subtitle,self.position_rank,self.name_rank,self.score_rank,self.button_return_menu]
    
   
    def click_return_menu(self,parametro): 
        self.set_active(parametro)

    def draw(self):
        super().draw()
        for widget in self.widget_list:    
            widget.draw()

    def update(self):
        super().draw()
        for widget in self.widget_list:    
            widget.update()

