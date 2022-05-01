import pygame as pg 
import sys 
import utils.constants as constants
import sprite_mananger.sprite_mananger as sm
clock = pg.time.clock
pg.display.set_mode(constants.WINDOW_SIZE, 0, 32)
display = pg.Surface((300, 200))

tile_sheet_image = pg.image.load('.resources/atlas/iso_tileset1.png')
tile_sheet = sm.SpriteManganger(tile_sheet_image)

block_black_floor = tile_sheet.get_image(0, constants.FLOOR_SIZE, constants.FLOOR_SIZE, 1, (0, 0, 0))

block_white_floor = tile_sheet.get_image(0, constants.FLOOR_SIZE, constants.FLOOR_SIZE, 1, (0, 0, 0))

def app():
    run = True
    while run:
        display.fill((146, 244, 255))

        for event in pg.event.get():
            if event == pg.QUIT:
                pg.quit()
                sys.exit()

        

