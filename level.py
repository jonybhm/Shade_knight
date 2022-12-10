import pygame
from constantes import *
from character import *
from auxiliar import *
from spell import *
from items import *
from plataforma import *
from enemigos import *


class Level:
    '''
    This class represents the level manager  
    '''
    def __init__ (self,total_items,background,max_platforms,platform_type,platform_width,platform_height,music):

        self.spell_group_enemy = pygame.sprite.Group()
        self.items_group = pygame.sprite.Group()
        self.platform_group = pygame.sprite.Group()
        
        self.timer_money = 1059
        self.timer_magic = 522
        self.timer_health = 953
        self.timer_trap = 755
        self.current_items = 0

        self.timer_platform = 0

        self.total_items = total_items
        self.background = background
        self.platform_type = platform_type
        self.platform_width = platform_width
        self.platform_height = platform_height
        self.music = music

        
        
    def generate_money_update(self)->None:
        '''
        Generates instances of the money item and adds them to the items group
        Arguments: None
        Returns: None
        '''
        if(self.timer_money == 0 and self.current_items < self.total_items):
            self.timer_money = 1000
            money = Items(type=7)
            self.items_group.add(money)
            self.current_items += 1 
            return money
        
    def generate_magic_update(self)->None:
        '''
        Generates instances of the magic item and adds them to the items group
        Arguments: None
        Returns: None
        '''
        if(self.timer_magic == 0 and self.current_items < self.total_items):
            self.timer_magic = 1000
            magic = Items(type=10)
            self.items_group.add(magic)
            self.current_items += 1 
            return magic
    
    def generate_health_update(self)->None: 
        '''
        Generates instances of the health item and adds them to the items group
        Arguments: None
        Returns: None
        '''
        if(self.timer_health == 0 and self.current_items < self.total_items):
            self.timer_health = 1000
            health = Items(type=1)
            self.items_group.add(health)
            self.current_items += 1 
            return health

    def generate_trap_update(self)->None: 
        '''
        Generates instances of the trap item and adds them to the items group
        Arguments: None
        Returns: None
        '''
        if(self.timer_trap == 0 and self.current_items < self.total_items):
            self.timer_trap = 1000
            trap = Items(type=4)
            self.items_group.add(trap)
            self.current_items += 1 
            return trap
    
    def generate_platforms(self)->None:
        '''
        Generates instances of platforms and adds them to the platform group
        Arguments: None
        Returns: None
        '''
        if(self.timer_platform == 0 ):
            self.timer_platform = 200
            platform = Platform(w=self.platform_width,h=self.platform_height,speed=1,type=self.platform_type)
            self.platform_group.add(platform)
            return platform

    def item_timer_update(self)->None:
        '''
        Counts down the cooldown timer
        Arguments: None
        Returns: None
        '''
        if(self.timer_health > 0):
            self.timer_health -= 1
        if(self.timer_magic > 0):
            self.timer_magic -= 1
        if(self.timer_money > 0):
            self.timer_money -= 1
        if(self.timer_trap > 0):
            self.timer_trap -= 1
        if(self.timer_platform > 0):
            self.timer_platform -= 1
        

    def generate_background(self)->None:
        '''
        Loads the background image that scrolls during the level 
        Arguments: None
        Returns: None
        '''
        imagen_scroll = pygame.image.load(PATH + r"\\level\\{}.png".format(self.background)).convert_alpha()
        imagen_scroll = pygame.transform.scale(imagen_scroll,(SCREEN_WIDTH,SCREEN_HEIGHT))
        
        return imagen_scroll

    def generate_music(self)->None:
        '''
        Loads and plays the music for each level
        Arguments: None
        Returns: None
        '''
        pygame.mixer.music.load(PATH + r"\\music\\{}.wav".format(self.music))
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1,0.0,7000)

    
    def update(self)->None:
        '''
        Executes the methods that need update 
        Arguments: None
        Returns: None
        '''
        self.generate_health_update()
        self.generate_magic_update()
        self.generate_money_update()
        self.generate_trap_update()
        self.item_timer_update()
        self.generate_platforms()


    