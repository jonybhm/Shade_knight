import pygame
import math
from auxiliar_2 import MetodoAuxiliar
from constantes import *



class Spell(pygame.sprite.Sprite):
    def __init__(self,x,y,speed,type_spell,spell_dmg,movement="straight"):
        pygame.sprite.Sprite.__init__(self)

        self.speed = speed 
        self.x = x
        self.y = y
        self.time_update = pygame.time.get_ticks()
        self.type_spell = type_spell
        self.movement = movement
        self.spell_dmg = spell_dmg

        self.wave_limit=0
        self.wave_direction=1

        
        self.damage_sfx_2 = pygame.mixer.Sound(PATH + r"\\sfx\\player_meele.wav")
        self.animation_list = []
        self.frame_index = 0
        if(type_spell == "big"):
            self.animation_list = MetodoAuxiliar.getSurfaceFromSpriteSheet(
            PATH + r"\\spells\\spell_player.png",6,1,scale=0.60)
        if(type_spell == "small"):
            self.animation_list = MetodoAuxiliar.getSurfaceFromSpriteSheet(
            PATH + r"\\spells\\spell_enemy.png",6,1,scale=0.50)
            

        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        

        self.direction = 1
    
    def animation_update(self):
        #avanzar el frame en la animacion
        self.image = self.animation_list[self.frame_index]
        #verificar si el tiempo que paso desde la ultima update es maor a la cte ANIMATION_COOLDOWN
        if (pygame.time.get_ticks() - self.time_update > ANIMATION_COOLDOWN):
            self.time_update =  pygame.time.get_ticks()
            self.frame_index += 1
        #loopear la lista de frames
        if (self.frame_index >= len(self.animation_list)):
            self.frame_index = 0

    def draw(self,screen):
        if(DEBUG_MODE):
            pygame.draw.rect(screen,RED,self.rect,1)

        screen.blit(self.image,self.rect)

    def update(self,player,spell_group_player,spell_group_enemy,enemy_sprite_group):
        #animacion de los hechizos
        self.animation_update()
        #movimiento de los hechizos
        if(self.movement=="straight"):
            self.rect.x += self.speed
        elif(self.movement=="diag_up"):
            self.rect.y += self.speed//3
            self.rect.x += self.speed
        elif(self.movement=="diag_down"):
            self.rect.y -= self.speed//3
            self.rect.x += self.speed
        elif(self.movement=="wave_pattern"):
            self.rect.x += self.speed
            if(self.wave_direction==1):
                self.rect.y -= self.speed
            else:    
                self.rect.y += self.speed
            self.wave_limit+=1
            if(self.wave_limit>20):
                self.wave_direction *= -1
                self.wave_limit *= -1
        elif(self.movement=="flip_wave_pattern"):
            self.rect.x += self.speed
            if(self.wave_direction==-1):
                self.rect.y -= self.speed
            else:    
                self.rect.y += self.speed
            self.wave_limit+=1
            if(self.wave_limit>20):
                self.wave_direction *= -1
                self.wave_limit *= -1

        #verificar si los hechizos estan fuera de la pantalla
        if (self.rect.left > SCREEN_WIDTH or self.rect.right < 0):
            self.kill() #elimina sprite del grupo

        #verificar si los hechizos colisionan con enemigos/player
        for enemy in enemy_sprite_group:
            if (pygame.sprite.spritecollide(enemy,spell_group_player,False)): #hechizo jugador
                if (enemy.is_alive):
                    enemy.health -= self.spell_dmg
                    player.dmg_count += 1
                    player.score += player.dmg_count
                    
                    self.kill()
                        
        if (pygame.sprite.spritecollide(player,spell_group_enemy,False)): #hechizo enemigo
            if (player.is_alive):
                player.health -= self.spell_dmg
                self.damage_sfx_2.set_volume(0.2)
                self.damage_sfx_2.play()
                self.kill()
