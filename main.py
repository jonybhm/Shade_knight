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

current_level = 0
run = True

ranking_info =[{"position":1,"name":"juan","score":1200},{"position":2,"name":"roberto","score":600}] #lista de prueba para form rankings


#FORMULARIOS!!
form_main_menu = FormMainMenu(name="form_main_menu",master_surface=main_screen,x=0,y=0,active=True,level_num=1,music_name="main_menu")
form_options = FormOptions(name="form_options",master_surface=main_screen,x=0,y=0,active=True,level_num=1,music_name="main_menu")
form_level_select = FormLevelSelect(name="form_level_select",master_surface=main_screen,x=0,y=0,active=True,level_num=1,music_name="main_menu")
form_start_level = FormStartLevel(name="form_start_level",master_surface=main_screen,x=0,y=0,active=True,level_num=current_level,music_name="other_1")
'''form_start_level_2 = FormStartLevel(name="form_start_level_2",master_surface=main_screen,x=0,y=0,active=True,level_num=1,music_name="level_1")
form_start_level_3 = FormStartLevel(name="form_start_level_3",master_surface=main_screen,x=0,y=0,active=True,level_num=2,music_name="level_2")'''
form_pause = FormPause(name="form_pause",master_surface=main_screen,x=0,y=0,active=True,level_num=current_level,music_name="main_menu")
form_rankings = FormRanking(name="form_rankings",master_surface=main_screen,x=0,y=0,active=True,level_num=1,music_name="main_menu",ranking_info_list=ranking_info)

#form_restart_level = FormStartLevel(name="form_start_level",master_surface=main_screen,x=0,y=0,active=True,level_num=0,music_name="other_1")

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
    elif(form_start_level.active):
        form_start_level.update(event_list)
        form_start_level.draw()
        form_start_level.level_advance()
        if (form_start_level.advance_level == True ):
            if(current_level < len(form_start_level.level_info)):
                form_start_level.advance_level = False
                current_level += 1         
                form_start_level = FormStartLevel(name="form_start_level",master_surface=main_screen,x=0,y=0,active=True,level_num=current_level,music_name="other_1")
                form_start_level.set_active("form_start_level")
        if (form_pause.level_restart == True ):
            form_start_level.restart_level()
            form_pause.level_restart = False
            form_start_level = FormStartLevel(name="form_start_level",master_surface=main_screen,x=0,y=0,active=True,level_num=current_level,music_name="other_1")
            form_start_level.set_active("form_start_level")

    
    elif(form_pause.active):
        form_pause.update()
        form_pause.draw()
    elif(form_rankings.active):
        form_rankings.update()
        form_rankings.draw()
    '''elif(form_start_level_2.active):
        
        form_start_level_2.update(event_list)
        form_start_level_2.draw()
        current_level = 2
    elif(form_start_level_3.active):
        form_start_level_3.update(event_list)
        form_start_level_3.draw()
        current_level = 3'''
                    
    pygame.display.update()



pygame.quit()
