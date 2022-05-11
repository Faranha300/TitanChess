import pygame as pg 

class SpriteManganger():
    def __init__(self, image: pg.surface.Surface) -> None:
        self.sheet = image

    def get_image(self, frame: int, row: int,  width: int, height: int, scale: int, bg_color: tuple) -> pg.surface.Surface:
        
        image = pg.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0,0), ((frame * width), (row * height), width, height))
        image = pg.transform.scale(image, (width*scale, height*scale)) 
        image.set_colorkey(bg_color)

        return image
    
