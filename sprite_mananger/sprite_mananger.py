import pygame as pg 

class SpriteManganger():
    def __init__(self, image: pg.surface.Surface) -> None:
        self.sheet = image

    def get_image(self, frame: int, width: int, height, scale: float, bg_color) -> pg.surface.Surface:
        
        image = pg.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0,0), ((frame * width), 0, width, height))
        image = pg.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(bg_color)

        return image
    
