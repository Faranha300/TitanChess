import pygame
import sys

clock = pygame.time.Clock()
pygame.display.set_caption('Pygame Window')
pygame.init()

WINDOW_SIZE = (1280, 720)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
display = pygame.Surface((300, 200))

tile_image = pygame.image.load('./resources/atlas/iso_tileset1.png').convert_alpha()
block_size = 32
floor_image_1 = pygame.Surface((block_size, block_size))
floor_image_2 = pygame.Surface((block_size, block_size))
floor_image_1.set_colorkey((0, 0, 0))
floor_image_2.set_colorkey((0, 0, 0))
floor_image_1.blit(tile_image, (0, 0), (0, 0, block_size, block_size))
floor_image_2.blit(tile_image, (0, 0), (block_size, 0, block_size, block_size))
#tile_image.set_colorkey((0, 0, 0))
#tile_image = pygame.transform.scale2x(tile_image)
#floor_block = pygame.Surface((12, 12))

run = True
while run:
    display.fill((146, 244, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    for row in range(8):
        for col in range(8):
            if row%2 == 0 and col%2 == 0:
                display.blit(floor_image_1, ((row*0.5*block_size - col*0.5*block_size + 3.5*block_size+1, row*block_size*0.25 + col*0.25*block_size + 10)))
            elif (row%2 == 1 and col%2==1):   
                display.blit(floor_image_1, ((row*0.5*block_size - col*0.5*block_size + 3.5*block_size+1, row*block_size*0.25 + col*0.25*block_size + 10)))
            else:
                display.blit(floor_image_2, ((row*0.5*block_size - col*0.5*block_size + 3.5*block_size+1, row*block_size*0.25 + col*0.25*block_size + 10)))
            #display.blit(floor_image, ((row*20, col*18)))
    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    pygame.display.update()
    clock.tick(60)
