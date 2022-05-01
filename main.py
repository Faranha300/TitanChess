import pygame as pg 
import sys

import utils.constants as constants

clock = pg.time.Clock()
pg.display.set_caption('Pygame Window')
pg.init()


screen = pg.display.set_mode(constants.WINDOW_SIZE, 0, 32)
display = pg.Surface((300, 200))

tile_image = pg.image.load('./resources/atlas/iso_tileset1.png').convert_alpha()

floor_image_1 = pg.Surface((constants.FLOOR_SPRITE_SIZE, constants.FLOOR_SPRITE_SIZE))
floor_image_2 = pg.Surface((constants.FLOOR_SPRITE_SIZE, constants.FLOOR_SPRITE_SIZE))
floor_image_1.set_colorkey((0, 0, 0))
floor_image_2.set_colorkey((0, 0, 0))
floor_image_1.blit(tile_image, (0, 0), (0, 0, constants.FLOOR_SPRITE_SIZE, constants.FLOOR_SPRITE_SIZE))
floor_image_2.blit(tile_image, (0, 0), (constants.FLOOR_SPRITE_SIZE, 0, constants.FLOOR_SPRITE_SIZE, constants.FLOOR_SPRITE_SIZE))
#tile_image.set_colorkey((0, 0, 0))
#tile_image = pg.transform.scale2x(tile_image)
#floor_block = pg.Surface((12, 12))

run = True
while run:
    display.fill((146, 244, 255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


    for row in range(8):
        for col in range(8):
            if row%2 == 0 and col%2 == 0:
                display.blit(floor_image_1, ((row*0.5*constants.FLOOR_SPRITE_SIZE - col*0.5*constants.FLOOR_SPRITE_SIZE + 3.5*constants.FLOOR_SPRITE_SIZE+1, row*constants.FLOOR_SPRITE_SIZE*0.25 + col*0.25*constants.FLOOR_SPRITE_SIZE + 10)))
            elif (row%2 == 1 and col%2==1):   
                display.blit(floor_image_1, ((row*0.5*constants.FLOOR_SPRITE_SIZE - col*0.5*constants.FLOOR_SPRITE_SIZE + 3.5*constants.FLOOR_SPRITE_SIZE+1, row*constants.FLOOR_SPRITE_SIZE*0.25 + col*0.25*constants.FLOOR_SPRITE_SIZE + 10)))
            else:
                display.blit(floor_image_2, ((row*0.5*constants.FLOOR_SPRITE_SIZE - col*0.5*constants.FLOOR_SPRITE_SIZE + 3.5*constants.FLOOR_SPRITE_SIZE+1, row*constants.FLOOR_SPRITE_SIZE*0.25 + col*0.25*constants.FLOOR_SPRITE_SIZE + 10)))
            #display.blit(floor_image, ((row*20, col*18)))
    surf = pg.transform.scale(display, constants.WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    pg.display.update()
    clock.tick(60)
