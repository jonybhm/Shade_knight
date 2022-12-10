import pygame
from SQLITE import *
from form_manager import *

pygame.init()

#pantalla y nombre de ventana
main_screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.SCALED)


pygame.display.set_caption("Shade Knigth")

run = True

ranking_info_db = view_rows_sqlite()
create_table_sqlite()
forms = FormManager(main_screen,ranking_info_db)


while (run):
    event_list = pygame.event.get()
    
    for event in event_list:
        if (event.type == pygame.QUIT):
            run = False

    forms.update(event_list)
        
                   
    pygame.display.update()

pygame.quit()