from forms import *

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

           