import pygame
import json
from constantes import *
from auxiliar import *
from SQLITE import *
from forms import *

pygame.init()

#pantalla y nombre de ventana
main_screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Shade Knigth")

current_level = 1
run = True

#FORMULARIOS!!
form_main_menu = FormMainMenu(name="form_main_menu",master_surface=main_screen,x=0,y=0,active=True,level_num=1,music_name="main_menu")
form_options = FormOptions(name="form_options",master_surface=main_screen,x=0,y=0,active=True,level_num=1,music_name="main_menu")
form_level_select = FormLevelSelect(name="form_level_select",master_surface=main_screen,x=0,y=0,active=True,level_num=1,music_name="main_menu")
form_start_level_1 = FormStartLevel(name="form_start_level_1",master_surface=main_screen,x=0,y=0,active=True,level_num=0,music_name="other_1")
form_start_level_2 = FormStartLevel(name="form_start_level_2",master_surface=main_screen,x=0,y=0,active=True,level_num=1,music_name="level_1")
form_start_level_3 = FormStartLevel(name="form_start_level_3",master_surface=main_screen,x=0,y=0,active=True,level_num=2,music_name="level_2")
form_pause = FormPause(name="form_pause",master_surface=main_screen,x=0,y=0,active=True,level_num=current_level,music_name="main_menu")


while (run):

    event_list = pygame.event.get()
    for event in event_list:
        #salir del juego
        if (event.type == pygame.QUIT):
            run = False
        if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    form_pause.set_active("form_pause")
    
    #UPDATE Y DRAW DE FORMULARIOS
    if(form_main_menu.active):
        form_main_menu.update()
        form_main_menu.draw()
    elif(form_options.active):
        form_options.update()
        form_options.draw()
    elif(form_level_select.active):
        form_level_select.update()
        form_level_select.draw()
    elif(form_start_level_1.active):
        form_start_level_1.update(event_list)
        form_start_level_1.draw()
        current_level = 1
    elif(form_start_level_2.active):
        
        form_start_level_2.update(event_list)
        form_start_level_2.draw()
        current_level = 2
    elif(form_start_level_3.active):
        form_start_level_3.update(event_list)
        form_start_level_3.draw()
        current_level = 3
    elif(form_pause.active):
        form_pause.update()
        form_pause.draw()
                    
    pygame.display.update()



pygame.quit()
