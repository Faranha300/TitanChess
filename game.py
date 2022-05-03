import pygame as pg 
import sys 
import utils.constants as constants
import utils.matrix_transformations as mt
import sprite_mananger.sprite_mananger as sm

clock = pg.time.Clock()
display = pg.display.set_mode(constants.WINDOW_SIZE, 0, 32)
#display = pg.Surface((300, 200))

tile_sheet_image = pg.image.load('./resources/atlas/iso_tileset1.png')
tile_sheet = sm.SpriteManganger(tile_sheet_image)

block_black_floor = tile_sheet.get_image(0, constants.FLOOR_SIZE, constants.FLOOR_SIZE, 4, (0, 0, 0))

block_white_floor = tile_sheet.get_image(1, constants.FLOOR_SIZE, constants.FLOOR_SIZE, 4, (0, 0, 0))

def app():
    run = True
    while run:
        display.fill((146, 244, 255))

        for event in pg.event.get():
            if event == pg.QUIT:
                pg.display.quit()
                pg.quit()
                sys.exit()
                run = False
            

        for row in range(8):
            for col in range(8):
                block_coords = mt.mudanca_base(row, col, constants.FLOOR_SIZE*4, constants.MATRIZ_MUDA_BASE)
                if (row % 2 == 0 and col % 2 == 0) or (row % 2 == 1 and col % 2 == 1):
                    display.blit(block_white_floor, block_coords)
                else:
                    display.blit(block_black_floor, block_coords)

        pg.display.update()
        clock.tick(60)

app()
        

