import pygame

class MetodoAuxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet(path:str,columns:int,rows:int,flip:bool = False, step:int = 1,scale:int = 1)->list:
        '''
        It loads a sprite sheet image and creates surfaces with the diferent parts of the image
        Arguments: path to a sprite sheet (string), number of columns (int), rows (int), scale (int), step (int)  and if its fliped or not (bool)
        Returns: a list containing the differet frames of the animation (list)
        '''
        list = []
        surface_image = pygame.image.load(path)
        frame_width = int(surface_image.get_width()/columns)
        frame_height = int(surface_image.get_height()/rows)
        frame_width_scaled = int(frame_width*scale)
        frame_height_scaled = int(frame_height*scale)
        x = 0
        
        for row in range(rows):
            for column in range(0,columns,step):
                x = column * frame_width
                y = row * frame_height
                surface_frame = surface_image.subsurface(x,y,frame_width,frame_height)
                if(scale != 1):                    
                    surface_frame = pygame.transform.scale(surface_frame,(frame_width_scaled, frame_height_scaled)).convert_alpha()
                if(flip):
                    surface_frame = pygame.transform.flip(surface_frame,True,False)
                list.append(surface_frame)
        return list
