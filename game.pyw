from msilib.schema import Class
import pygame as pg 
import sys 
import utils.constants as constants
import utils.matrix_transformations as mt
import sprite_mananger.sprite_mananger as sm
import random

clock = pg.time.Clock()
display = pg.display.set_mode(constants.WINDOW_SIZE, 0, 32)

tile_sheet_image = pg.image.load('./resources/atlas/iso_tileset1.png')
tile_sheet = sm.SpriteManganger(tile_sheet_image)

block_black_floor = tile_sheet.get_image(0, constants.FLOOR_SIZE, constants.FLOOR_SIZE, 4, (0, 0, 0))

block_white_floor = tile_sheet.get_image(1, constants.FLOOR_SIZE, constants.FLOOR_SIZE, 4, (0, 0, 0))

def calcularDistanciaPontos(xA,xB,yA,yB):
    return (((xB-xA)**2)+((yB-yA)**2))**(1/2)

#CONTADORES DE TEMPO SPAWN ITENS
static_timer = None
last_item_time = None

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
        self.ammo = 1
        self.hitbox = (self.posicao_x, self.posicao_y, self.raio)

        self.cima = True
        self.direita = False
        self.esquerda = False
        self.baixo = False
        
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
    def Dano():
        Dano += 1

#projetil_temp
#PROJÉTIL 

class projetil(object):
    def __init__(self):
        self.color = (238,173,14)
        self.tamanho = 10
        self.posicao_projetil_x = 0
        self.posicao_projetil_y = 0
        self.range = 300
        self.destino = None
        self.hitbox = (self.posicao_projetil_x, self.posicao_projetil_y, self.tamanho)

#
#

cords_item_Verde = mt.mudanca_base(random.randint(1,8), random.randint(0,7), constants.FLOOR_SIZE*4, constants.MATRIZ_MUDA_BASE)

item_Verde = coletaveis((61,145,64), 10, cords_item_Verde[0], cords_item_Verde[1])

cords_item_roxo = mt.mudanca_base(random.randint(1,8), random.randint(0,7), constants.FLOOR_SIZE*4, constants.MATRIZ_MUDA_BASE)

item_Roxo = coletaveis((138,43,226), 10, cords_item_roxo[0], cords_item_roxo[1])

#

projetil = projetil()

item_Verde_coletado = False

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
    pg.draw.circle(display, item_Verde.color, (item_Verde.posicao_coletavel_x, item_Verde.posicao_coletavel_y), item_Verde.tamanho )
    pg.draw.circle(display, item_Roxo.color, (item_Roxo.posicao_coletavel_x, item_Roxo.posicao_coletavel_y), item_Roxo.tamanho )

    
#DESENHO DO PLAYER E MOVIMENTAÇÂO COM OOP
 
    pg.draw.circle(display, Dama.cor, (Dama.posicao_x,Dama.posicao_y), Dama.raio)
    keys = pg.key.get_pressed()
    
    if keys[pg.K_LEFT] and Dama.posicao_x >= 490:
        Dama.posicao_x -= Dama.velocidade
        
        Dama.esquerda = True
        Dama.cima = False
        Dama.direita = False
        Dama.baixo = False
        
    if keys[pg.K_RIGHT] and Dama.posicao_x <= 1440: 
        Dama.posicao_x += Dama.velocidade

        Dama.direita = True
        Dama.cima = False
        Dama.esquerda = False
        Dama.baixo = False
        
    if keys[pg.K_UP] and Dama.posicao_y >= 275:
        Dama.posicao_y -= Dama.velocidade

        Dama.cima = True
        Dama.direita = False
        Dama.esquerda = False
        Dama.baixo = False
        
    if keys[pg.K_DOWN] and Dama.posicao_y <= 735:
        Dama.posicao_y += Dama.velocidade

        Dama.baixo = True
        Dama.cima = False
        Dama.direita = False
        Dama.esquerda = False

    #projetil_temp

    if keys[pg.K_SPACE] and Dama.posicao_y <= 735:
        if Dama.ammo>0:
            if Dama.cima == True:
                projetil.destino = [Dama.posicao_x, Dama.posicao_y-projetil.range]
            if Dama.direita == True:
                projetil.destino = [Dama.posicao_x+projetil.range, Dama.posicao_y]
            if Dama.esquerda == True:
                projetil.destino = [Dama.posicao_x-projetil.range, Dama.posicao_y]
            if Dama.baixo == True:
                projetil.destino = [Dama.posicao_x, Dama.posicao_y+projetil.range]
    if keys[pg.K_z]:
        Dama.ammo = 1
        projetil.destino = None
        #
            

#MUDANÇA DE LUGAR DO ITEM / IDENTIFICAÇÃO SE ITEM FOI COLETADO
    if item_Verde_coletado == True:
        if last_item_time>3000:
            cords_item_Verde = mt.mudanca_base(random.randint(1,8), random.randint(0,7), constants.FLOOR_SIZE*4, constants.MATRIZ_MUDA_BASE)
            item_Verde = coletaveis((61,145,64), 10, cords_item_Verde[0], cords_item_Verde[1])
            item_Verde_coletado = False

            
#IDENTIFICAÇÃO DE COLISÃO COM O ITEM
        
    distanciaPlayerObjeto=calcularDistanciaPontos(Dama.posicao_x, item_Verde.posicao_coletavel_x, Dama.posicao_y, item_Verde.posicao_coletavel_y)
    if distanciaPlayerObjeto<=20:
        if Dama.velocidade<12:
            Dama.velocidade+=3

        item_Verde.posicao_coletavel_x = 0
        item_Verde.posicao_coletavel_y = 0
        item_Verde.color = (146, 244, 255)
        item_Verde.tamanho = 0
        static_timer = pg.time.get_ticks()

        item_Verde_coletado = True

        
#COOLDOWN DE SPAWN DE ITENS
    if static_timer:
        last_item_time = pg.time.get_ticks() - static_timer
    #projetil_temp
    if Dama.ammo>0:
        if Dama.cima:
            projetil.posicao_projetil_x = Dama.posicao_x
            projetil.posicao_projetil_y = Dama.posicao_y-20
            
        elif Dama.direita:
            projetil.posicao_projetil_x = Dama.posicao_x+20
            projetil.posicao_projetil_y = Dama.posicao_y
            
        elif Dama.esquerda:
            projetil.posicao_projetil_x = Dama.posicao_x-20
            projetil.posicao_projetil_y = Dama.posicao_y
            
        elif Dama.baixo:
            projetil.posicao_projetil_x = Dama.posicao_x
            projetil.posicao_projetil_y = Dama.posicao_y+20
            
    if projetil.destino != None:
        if not projetil.destino==(projetil.posicao_projetil_x, projetil.posicao_projetil_y):
            Dama.ammo = 0
            #
            if projetil.destino[0]>projetil.posicao_projetil_x:
                if (projetil.destino[0] - projetil.posicao_projetil_x)<5:
                    
                    projetil.posicao_projetil_x = projetil.destino[0]
                else:
                    projetil.posicao_projetil_x += 5
                    
            if projetil.destino[0]<projetil.posicao_projetil_x:
                if (projetil.posicao_projetil_x - projetil.destino[0])<5:
                    
                    projetil.posicao_projetil_x = projetil.destino[0]
                else:
                    projetil.posicao_projetil_x -= 5
            #
            if projetil.destino[1]>projetil.posicao_projetil_y:
                if (projetil.destino[1] - projetil.posicao_projetil_y)<5:
                    
                    projetil.posicao_projetil_y = projetil.destino[1]
                else:
                    projetil.posicao_projetil_y += 5
                    
            if projetil.destino[1]<projetil.posicao_projetil_y:
                if (projetil.posicao_projetil_y - projetil.destino[1])<5:
                    
                    projetil.posicao_projetil_y = projetil.destino[1]
                else:
                    projetil.posicao_projetil_y -= 5

    


        
    
    pg.draw.circle(display, projetil.color, (projetil.posicao_projetil_x, projetil.posicao_projetil_y), projetil.tamanho)
    #
    pg.display.update()
    clock.tick(60)


        

