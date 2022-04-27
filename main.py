import pygame
import sys

clock = pygame.time.Clock()
pygame.display.set_caption('Pygame Window')
pygame.init()

WINDOW_SIZE = (600, 400)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
display = pygame.Surface((150, 100))

tile_image = pygame.image.load('./resources/atlas/iso_tileset.png').convert_alpha()
floor_image = pygame.Surface((18, 17))
floor_image.set_colorkey((0, 0, 0))
floor_image.blit(tile_image, (0, 0), (0, 3, 18, 20))
#tile_image.set_colorkey((0, 0, 0))
#tile_image = pygame.transform.scale2x(tile_image)
#floor_block = pygame.Surface((12, 12))

run = True
while run:
    display.fill((146, 244, 255))
    display.blit(floor_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    pygame.display.update()
    clock.tick(60)
