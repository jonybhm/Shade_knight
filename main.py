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

global_score = 0
current_level = 0
run = True


ranking_info_db = view_rows_sqlite()
create_table_sqlite()


#FORMULARIOS!!
form_main_menu = FormMainMenu(name="form_main_menu",master_surface=main_screen,x=0,y=0,active=True,level_num=1,music_name="main_menu")
form_options = FormOptions(name="form_options",master_surface=main_screen,x=0,y=0,active=True,level_num=1,music_name="main_menu")
form_level_select = FormLevelSelect(name="form_level_select",master_surface=main_screen,x=0,y=0,active=True,level_num=1,music_name="main_menu")
form_start_level = FormStartLevel(name="form_start_level",master_surface=main_screen,x=0,y=0,active=True,level_num=current_level,music_name="main_menu")
form_pause = FormPause(name="form_pause",master_surface=main_screen,x=0,y=0,active=True,level_num=current_level,music_name="main_menu")
form_rankings = FormRanking(name="form_rankings",master_surface=main_screen,x=0,y=0,active=True,level_num=1,music_name="main_menu",
ranking_list=ranking_info_db)
form_enter_name = FormEnterName(name="form_enter_name",master_surface=main_screen,x=0,y=0,active=True,level_num=1,music_name="main_menu")
form_screen_transition_reset = FormScreenTransition(name="form_screen_transition_reset",master_surface=main_screen,x=0,y=0,active=True,speed=4,direction=1,level_num=current_level,music_name="main_menu")
form_screen_transition_advance = FormScreenTransition(name="form_screen_transition_advance",master_surface=main_screen,x=0,y=0,active=True,speed=4,direction=1,level_num=current_level+1,music_name="main_menu")


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
    if(form_main_menu.active):#MENU PRINCIPAL
        form_main_menu.update()
        form_main_menu.draw()
        if(form_main_menu.start_first_level == True): #COMENZAR DESDE EL PRIMER NIVEL
            current_level=0
            form_main_menu.start_first_level = False
            form_start_level = FormStartLevel(name="form_start_level",master_surface=main_screen,x=0,y=0,active=True,level_num=current_level,music_name="other_1")
            form_start_level.set_active("form_start_level")
        
    elif(form_options.active): #MENU OPCIONES
        form_options.update()
        form_options.draw()

    elif(form_level_select.active): #SELECCION DE NIVELES
        form_level_select.update()
        form_level_select.draw()
        if(form_level_select.is_selected == True): #SELECCION DE NIVELES
            current_level=form_level_select.level_selected
            form_level_select.is_selected = False
            form_start_level = FormStartLevel(name="form_start_level",master_surface=main_screen,x=0,y=0,active=True,level_num=current_level,music_name="other_1")
            form_start_level.set_active("form_start_level")

    elif(form_start_level.active): #INICIO DE NIVEL
        form_start_level.update(event_list)
        form_start_level.draw()
        form_start_level.level_advance()
        print(global_score)
        
        
        if (form_start_level.advance_level == True ): #AVANCE DE NIVELES
            global_score += form_start_level.player.score #puntaje global que se actuliza mientras los niveles avanzan
            if(current_level < len(form_start_level.level_info)-1):
                form_screen_transition_advance = FormScreenTransition(name="form_screen_transition_advance",master_surface=main_screen,x=0,y=0,active=True,speed=4,direction=1,level_num=current_level+1,music_name="main_menu")
                form_screen_transition_advance.set_active("form_screen_transition_advance")
                

        if(form_start_level.game_ending == True): #INGRESAR NOMBRE PARA RANKINGS
            form_start_level.game_ending = False
            form_enter_name = FormEnterName(name="form_enter_name",master_surface=main_screen,x=0,y=0,active=True,level_num=1,music_name="ending")
            form_enter_name.set_active("form_enter_name")
           
        if (form_pause.level_restart == True or form_start_level.player.is_alive == False): #REINICIO DE NIVELES
            form_screen_transition_reset = FormScreenTransition(name="form_screen_transition_reset",master_surface=main_screen,x=0,y=0,active=True,speed=4,direction=1,level_num=current_level,music_name="main_menu")
            form_screen_transition_reset.set_active("form_screen_transition_reset")

            

    
    elif(form_pause.active):
        form_pause.update()
        form_pause.draw()

    elif(form_enter_name.active):
        form_enter_name.update()
        form_enter_name.draw()
        if(form_enter_name.confirm_name == True):            
            #print(form_enter_name.text_box._wrting)
            #print(type(form_enter_name.text_box._wrting))
            form_enter_name.confirm_name = False                    
            add_rows_sqlite(form_enter_name.text_box._wrting,global_score) #agrega info a la base de datos
            ranking_info_db = view_rows_sqlite()
            print(ranking_info_db)          
            form_rankings = FormRanking(name="form_rankings",master_surface=main_screen,x=0,y=0,active=True,level_num=1,music_name="ending",
            ranking_list=ranking_info_db)
            form_rankings.set_active("form_rankings")

    elif(form_rankings.active):
        form_rankings.update()
        form_rankings.draw()
   
    elif(form_screen_transition_reset.active):
        form_screen_transition_reset.update()
        form_screen_transition_reset.draw()
        if(form_screen_transition_reset.transition_is_over == True):
            form_start_level.restart_level()
            form_pause.level_restart = False
            form_start_level = FormStartLevel(name="form_start_level",master_surface=main_screen,x=0,y=0,active=True,level_num=current_level,music_name="other_1")
            form_start_level.set_active("form_start_level")
    
    elif(form_screen_transition_advance.active):
        form_screen_transition_advance.update()
        form_screen_transition_advance.draw()
        if(form_screen_transition_advance.transition_is_over == True):
            form_start_level.advance_level = False
            current_level += 1         
            form_start_level = FormStartLevel(name="form_start_level",master_surface=main_screen,x=0,y=0,active=True,level_num=current_level,music_name="other_1")
            form_start_level.set_active("form_start_level")
                    
    pygame.display.update()



pygame.quit()
