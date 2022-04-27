import pygame
import sys

clock = pygame.time.Clock()
pygame.display.set_caption('Pygame Window')
pygame.init()

WINDOW_SIZE = (1280, 720)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
display = pygame.Surface((300, 200))

tile_image = pygame.image.load('./resources/atlas/iso_tileset.png').convert_alpha()
floor_image_1 = pygame.Surface((18, 17))
floor_image_2 = pygame.Surface((18, 17))
floor_image_1.set_colorkey((0, 0, 0))
floor_image_2.set_colorkey((0, 0, 0))
floor_image_1.blit(tile_image, (0, 0), (0, 3, 18, 20))
floor_image_2.blit(tile_image, (0, 0), (0, 23, 18, 40))
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
                display.blit(floor_image_1, ((row*0.5*18 - col*0.5*18 + 3.25*20+1, row*20*0.25 + col*0.25*20 + 10)))
            elif (row%2 == 1 and col%2==1):   
                display.blit(floor_image_1, ((row*0.5*18 - col*0.5*18 + 3.25*20+1, row*20*0.25 + col*0.25*20 + 10)))
            else:
                display.blit(floor_image_2, ((row*0.5*18 - col*0.5*18 + 3.25*20+1, row*20*0.25 + col*0.25*20 + 10)))
            #display.blit(floor_image, ((row*20, col*18)))
    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    pygame.display.update()
    clock.tick(60)
