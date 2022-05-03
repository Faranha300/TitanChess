from msilib.schema import Class
import pygame as pg 
import sys 
import utils.constants as constants
import utils.matrix_transformations as mt
import sprite_mananger.sprite_mananger as sm
import random

clock = pg.time.Clock()
display = pg.display.set_mode(constants.WINDOW_SIZE, 0, 32)
#display = pg.Surface((300, 200))


tile_sheet_image = pg.image.load('./resources/atlas/iso_tileset1.png')
tile_sheet = sm.SpriteManganger(tile_sheet_image)

block_black_floor = tile_sheet.get_image(0, constants.FLOOR_SIZE, constants.FLOOR_SIZE, 4, (0, 0, 0))

block_white_floor = tile_sheet.get_image(1, constants.FLOOR_SIZE, constants.FLOOR_SIZE, 4, (0, 0, 0))

def calcularDistanciaPontos(xA,xB,yA,yB):
    return (((xB-xA)**2)+((yB-yA)**2))**(1/2)
    
#PLAYER

velocidade = 5
vida = 1
class player(object):
    def __init__(self, posicao_x, posicao_y) -> None:
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.velocidade = 5
        self.raio = 20
        self.cor = (0,0,123)
        self.hitbox = (self.posicao_x, self.posicao_y, self.raio)
        
        pg.draw.circle(display, self.cor, (self.posicao_x,self.posicao_y), self.raio)
        pg.display.update()
        

Dama = player(950,500)
              

#coletáveis
class coletaveis(object):
    def __init__(self, color, tamanho, posicao_coletavel_x, posicao_coletavel_y) -> None:
        self.color = color
        self.tamanho = tamanho
        self.posicao_coletavel_x = posicao_coletavel_x
        self.posicao_coletavel_y = posicao_coletavel_y
        self.hitbox = (self.posicao_coletavel_x, self.posicao_coletavel_y, self.tamanho)
    
    def mais_velocidade():
        velocidade += 3
    def vida():
        vida += 1

item_vermelho = coletaveis((200,0,0), 10, random.randrange(750,1300), random.randint(500,700))

#MAIN LOOP

run = True
while run:
    display.fill((146, 244, 255))

#SAIR DO JOGO        
    for event in pg.event.get():
        if event.type == pg.QUIT:            
            run = False

            
#CONSTRUÇÂO DO TABULEIRO           

    for row in range(8):
        for col in range(8):
            block_coords = mt.mudanca_base(row, col, constants.FLOOR_SIZE*4, constants.MATRIZ_MUDA_BASE)
            if (row % 2 == 0 and col % 2 == 0) or (row % 2 == 1 and col % 2 == 1):
                display.blit(block_white_floor, block_coords)
            else:
                display.blit(block_black_floor, block_coords)

#DESENHO DO COLETÁVEL MAIS ATRIBUTO
    pg.draw.circle(display, item_vermelho.color, (item_vermelho.posicao_coletavel_x, item_vermelho.posicao_coletavel_y), item_vermelho.tamanho )
    
#DESENHO DO PLAYER E MOVIMENTAÇÂO COM OOP
 
    pg.draw.circle(display, Dama.cor, (Dama.posicao_x,Dama.posicao_y), Dama.raio)
    keys = pg.key.get_pressed()
    
    if keys[pg.K_LEFT] and Dama.posicao_x >= 490:
        Dama.posicao_x -= Dama.velocidade
    if keys[pg.K_RIGHT] and Dama.posicao_x <= 1440:
        Dama.posicao_x += Dama.velocidade
    if keys[pg.K_UP] and Dama.posicao_y >= 275:
        Dama.posicao_y -= Dama.velocidade
    if keys[pg.K_DOWN] and Dama.posicao_y <= 735:
        Dama.posicao_y += Dama.velocidade

    #print(Dama.posicao_x, Dama.posicao_y)
    distanciaPlayerObjeto=calcularDistanciaPontos(Dama.posicao_x, item_vermelho.posicao_coletavel_x, Dama.posicao_y, item_vermelho.posicao_coletavel_y)
    if distanciaPlayerObjeto<=30:
        item_vermelho.color=(255,255,255)
        Dama.velocidade=10
    #print(calcularDistanciaPontos(0,0,3,4))

    

    pg.display.update()
    clock.tick(60)


        

