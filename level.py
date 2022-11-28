import pygame
from constantes import *
from character import *
from auxiliar import *
from spell import *
from items import *
from plataforma import *
from enemigos import *



class Level:
    def __init__ (self,total_items,background,max_platforms,platform_type,platform_width,platform_height,music):

        #grupos de sprites
        self.spell_group_enemy = pygame.sprite.Group()
        self.items_group = pygame.sprite.Group()
        self.platform_group = pygame.sprite.Group()
        
        #temporizadores de elementos hasta aparecer de neuevo en pantalla
        self.timer_money = 1000
        self.timer_magic = 500
        self.timer_health = 800
        self.timer_trap = 800
        self.current_items = 0

        self.timer_platform = 0
        #self.current_platforms = 0 

        #datos obtenidos del "json"
        self.total_items = total_items
        #self.max_platforms = max_platforms 
        self.background = background
        self.platform_type = platform_type
        self.platform_width = platform_width
        self.platform_height = platform_height
        self.music = music

        
        
        


        #-----------CARGA DE NIVEL-------------
    def generate_money_update(self):
        #items dinero
        if(self.timer_money == 0 and self.current_items < self.total_items):
            self.timer_money = 500
            money = Items(type=7)
            self.items_group.add(money)
            self.current_items += 1 
            return money
        
    def generate_magic_update(self):
        #items magia
        if(self.timer_magic == 0 and self.current_items < self.total_items):
            self.timer_magic = 300
            magic = Items(type=10)
            self.items_group.add(magic)
            self.current_items += 1 
            return magic
    
    def generate_health_update(self): 
        #items salud
        if(self.timer_health == 0 and self.current_items < self.total_items):
            self.timer_health = 400
            health = Items(type=1)
            self.items_group.add(health)
            self.current_items += 1 
            return health

    def generate_trap_update(self): 
        #items salud
        if(self.timer_trap == 0 and self.current_items < self.total_items):
            self.timer_trap = 600
            trap = Items(type=4)
            self.items_group.add(trap)
            self.current_items += 1 
            return trap


    
    def generate_platforms(self):
        #plataformas
        if(self.timer_platform == 0 ):
            self.timer_platform = 200
            platform = Platform(w=self.platform_width,h=self.platform_height,speed=1,type=self.platform_type)
            self.platform_group.add(platform)
            #self.current_platforms += 1 
            return platform

    def item_timer_update(self):
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
        

    def generate_background(self):
        #fondo
        imagen_scroll = pygame.image.load(PATH + r"\\level\\{}.png".format(self.background)).convert_alpha()
        imagen_scroll = pygame.transform.scale(imagen_scroll,(SCREEN_WIDTH,SCREEN_HEIGHT))
        
        return imagen_scroll

    def generate_music(self):
        #musica
        pygame.mixer.music.load(PATH + r"\\music\\{}.wav".format(self.music))
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1,0.0,7000)

    
    def update(self):
        self.generate_health_update()
        self.generate_magic_update()
        self.generate_money_update()
        self.generate_trap_update()
        self.item_timer_update()
        self.generate_platforms()


    