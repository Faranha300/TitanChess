from Jogo import Jogo
import pygame as pg 
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
orbe = tile_sheet.get_image(2, constants.FLOOR_SIZE, constants.FLOOR_SIZE, 1, (0, 0, 0))
torre_img = tile_sheet.get_image(3, constants.FLOOR_SIZE, constants.FLOOR_SIZE, 2, (0, 0, 0))

Game = Jogo()

#CORES USADAS:
AzulMarinho = (0,0,123) #Player
AzulClaroFosco = (153,153,255) #Imunidade
Ciano = (0,238,238)  #Velocidade

def calcularDistanciaPontos(xA,xB,yA,yB):
    return (((xB-xA)**2)+((yB-yA)**2))**(1/2)

#CONTADORES DE TEMPO SPAWN ITENS

static_timer = None
last_item_time = None

#CONTADORES DE TEMPO DE DANO AO PLAYER
static_timer_player = None
last_hit_time = None
tempo_imune = 3000 #milisegundos
hits = 0


class Player(object):
    def __init__(self, posicao_x, posicao_y) -> None:
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.velocidade = 3
        self.raio = 20
        self.cor = (0,0,123)
        self.hitbox = (self.posicao_x, self.posicao_y, self.raio)
        self.ammo = 1
        self.vida = 1
        self.imune = False

        self.cima = True
        self.direita = False
        self.esquerda = False
        self.baixo = False
        
    def desenhar(self):
        pg.draw.circle(display, self.cor, (self.posicao_x, self.posicao_y), self.raio)
        
    def andar(self):
        keys = pg.key.get_pressed()
    
        if keys[pg.K_LEFT]: #and self.posicao_x >= 490:
            self.posicao_x -= self.velocidade

            Dama.esquerda = True
            Dama.cima = False
            Dama.direita = False
            Dama.baixo = False

        if keys[pg.K_RIGHT]: #and self.posicao_x <= 1440: 
            self.posicao_x += self.velocidade

            Dama.direita = True
            Dama.cima = False
            Dama.esquerda = False
            Dama.baixo = False


        if keys[pg.K_UP]: #and self.posicao_y >= 275:
            self.posicao_y -= self.velocidade

            Dama.cima = True
            Dama.direita = False
            Dama.esquerda = False
            Dama.baixo = False

        if keys[pg.K_DOWN]: #and self.posicao_y <= 735:
            self.posicao_y += self.velocidade

            Dama.baixo = True
            Dama.cima = False
            Dama.direita = False
            Dama.esquerda = False
    
    def barra_de_vida(self):      
        
        coracao_sprite = pg.image.load('./resources/atlas/heart pixel art 48x48.png')

        if self.vida >= 1:           
            display.blit(coracao_sprite,(220,120))
        if self.vida >= 2:           
            display.blit(coracao_sprite,(275,120))  
        if self.vida >= 3:
            display.blit(coracao_sprite,(330,120))


#BOSS

class Boss(object):
    def __init__(self, bossX, bossY):
        self.bossX = bossX
        self.bossY = bossY
        self.velI = 32
        self.raio = 20
        self.cor = (255,0,0)
        self.walkCount = 2
        self.jump_count = 10
        self.is_jump = True
        self.largura = 0
        self.altura = 0
        self.vida = 400
        self.tamanho_da_barra_vida = 400

    def tomar_dano(self,dano_do_player):
        if self.vida > 0:
            self.vida -= dano_do_player       
        if self.vida <= 0:
            self.vida = 0

    def barra_De_vida(self):
        pg.draw.rect(display, (255, 0, 0), (1300, 110, self.vida, 15))
        pg.draw.rect(display, (0,255,0), (1300,110, self.vida, 15))
        pg.draw.rect(display, (0,0,0), (1300, 110, self.tamanho_da_barra_vida, 15),4)

            


#Clase específica, recebe os parâmetros do boss, mas prioriza o que for dado dentro dela

class Torre(Boss):
    def andar(self):
        if self.walkCount <= 0: # o Boss anda "2" vezes antes de parar
                if distanciaX > 2 or distanciaX < -1: # Para o boss n ficar travando numa posição especifica (passível de mudança)
                    if self.bossX < Dama.posicao_x and distanciaX > 0: # Direita
                        self.bossX += (torre.velI + 32)
                        sombra.posicao_X += (torre.velI + 32)
                        self.is_jump = True
                        
                    elif self.bossX > Dama.posicao_x and distanciaX < 0: # Esquerda
                        self.bossX -= (torre.velI + 32)
                        sombra.posicao_X -= (torre.velI + 32)
                        self.is_jump = True
                    
                if distanciaY > 2 or distanciaY < -1:
                    if self.bossY < Dama.posicao_y and distanciaY > 0: # Baixo
                        self.bossY += self.velI
                        sombra.posicao_Y += self.velI
                        self.is_jump = True
                    
                    elif self.bossY > Dama.posicao_y and distanciaY < 0: # Cima
                        self.bossY -= self.velI
                        sombra.posicao_Y -= self.velI
                        self.is_jump = True

    def pular(self):
        self.is_jump = True
        if self.jump_count >= -10:
            self.bossY -= (self.jump_count ** 3) / 25
            self.jump_count -= 1

        else:
            self.is_jump = False
            self.jump_count = 10


class Sombra(object): 
    def __init__(self):
        self.raio = torre.raio
        self.posicao_X = torre.bossX - (self.raio // 2) + (torre.raio // 2)
        self.posicao_Y = torre.bossY - (self.raio // 2) + (torre.raio // 2)

    def desenhar(self):
        if torre.is_jump:
            pg.draw.circle(display, (54,54,54), (self.posicao_X, self.posicao_Y,), self.raio)

Dama = Player(1200,500)
torre = Torre(constants.WINDOW_SIZE[0] // 2, constants.WINDOW_SIZE[1] // 2) 
sombra = Sombra()          

#PROJÉTIL
#imgs dos projéteis


class projetil(object):
    def __init__(self):
        self.color = (238,173,14)
        self.tamanho = 10
        self.dano = 50
        self.posicao_projetil_x = 0
        self.posicao_projetil_y = 0
        self.range = 300
        self.destino = None
        self.movimentando = False
        self.hitbox = (self.posicao_projetil_x, self.posicao_projetil_y, self.tamanho)
    

Espada = projetil()

#COLETÁVEIS

class coletaveis(object):
    def __init__(self, color, tamanho, posicao_coletavel_x, posicao_coletavel_y) -> None:
        self.color = color
        self.tamanho = tamanho
        self.posicao_coletavel_x = posicao_coletavel_x
        self.posicao_coletavel_y = posicao_coletavel_y
        self.hitbox = (self.posicao_coletavel_x, self.posicao_coletavel_y, self.tamanho)

cords_item_Verde = mt.mudanca_base(random.randint(1,8), random.randint(0,7), constants.FLOOR_SIZE*4, constants.MATRIZ_MUDA_BASE)
item_Verde = coletaveis((61,145,64), 10, cords_item_Verde[0], cords_item_Verde[1])

cords_item_vida_drop = mt.mudanca_base(random.randint(1,8), random.randint(0,7), constants.FLOOR_SIZE*4, constants.MATRIZ_MUDA_BASE)
Vida_item = coletaveis((255,0,226), 10, cords_item_vida_drop[0], cords_item_vida_drop[1])

posicao_da_bala_chao = [0,0]
arma_no_chao = coletaveis((238,173,14), 10, posicao_da_bala_chao[0], posicao_da_bala_chao[1])


item_Verde_coletado = False

item_vida_coletada = False

#ARRUMAR ESSA PARTE

game_over_img = pg.image.load('game_over.jpg')
bck_gr = pg.image.load('Game_background.png')
display.blit(bck_gr,(0,0))


#MAIN LOOP

while Game.running:   

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
    item_vida_sprite = pg.image.load('./resources/atlas/heart_full_32x32.png')
    item_velocidade_Sprite = pg.image.load('./resources/atlas/Emerald.png')
    
    display.blit(item_vida_sprite, (Vida_item.posicao_coletavel_x - 10, Vida_item.posicao_coletavel_y - 20))
    display.blit(item_velocidade_Sprite, (item_Verde.posicao_coletavel_x-20, item_Verde.posicao_coletavel_y-30))
   
    torre.barra_De_vida()

    
#DESENHO DO PLAYER E MOVIMENTAÇÂO COM OOP
 
    Dama.desenhar()
    Dama.andar()
    Dama.barra_de_vida()

#BALA

    keys = pg.key.get_pressed()

    if keys[pg.K_SPACE] and Dama.posicao_y <= 735:
        if Dama.ammo > 0:
            if Dama.cima == True:
                Espada.destino = (Dama.posicao_x, Dama.posicao_y-Espada.range)
                posicao_da_bala_chao = Espada.destino
                
            if Dama.direita == True:
                Espada.destino = (Dama.posicao_x+Espada.range, Dama.posicao_y)
                posicao_da_bala_chao = Espada.destino

            if Dama.esquerda == True:
                Espada.destino = (Dama.posicao_x-Espada.range, Dama.posicao_y)
                posicao_da_bala_chao = Espada.destino

            if Dama.baixo == True:
                Espada.destino = (Dama.posicao_x, Dama.posicao_y+Espada.range)
                posicao_da_bala_chao = Espada.destino
        
#BLOCO DE VERIFICAÇÃO SE O TEMPO DA IMUNIDADE DO PLAYER JÁ PASSOU
    if hits > 0:
        last_hit_time = pg.time.get_ticks() - static_timer_player
        if last_hit_time > tempo_imune:
            Dama.imune = False
            if Dama.cor == AzulClaroFosco: #VERIFICA SE O PLAYER ESTÁ COM A COR FOSCA DA IMUNIDADE
                Dama.cor = (0,0,123)
            
#DESENHO DO BOOS E MOVIMENTAÇÃO COM OOP
    if torre.vida > 0: # Se a vida da torre for < 0, a torre morre
        display.blit(torre_img, (torre.bossX-30, torre.bossY-50))
    
        distanciaX = Dama.posicao_x - torre.bossX # Distancia entre o player e o boss na posição X
        distanciaY = Dama.posicao_y - torre.bossY # Distancia entre o player e o boss na posição Y

        if not torre.is_jump: #Caso não esteja pulando, anda
            torre.andar()

        else: #Pula e desenha a sombra
            torre.pular()
            sombra.desenhar()

        torre.walkCount += 1
        if torre.walkCount >= 40: #Velocidade do boss
            torre.walkCount = 0

        if not torre.is_jump: #Para ele não bater no player em cima no meio do pulo
            if calcularDistanciaPontos(Dama.posicao_x, torre.bossX, Dama.posicao_y, torre.bossY) <= 40:
                if Dama.imune == False: # Verifica se o player está imune aos hits ainda (Variável)
                    Dama.vida -= 0
                    Dama.imune = True
                    static_timer_player = pg.time.get_ticks()
                    hits+=1
                if Dama.imune == True: # Caso o player não esteja mais imune
                    Dama.cor = (153,153,255)
            if calcularDistanciaPontos(Espada.posicao_projetil_x, torre.bossX, Espada.posicao_projetil_y, torre.bossY) <= 30 and Espada.movimentando:
                torre.tomar_dano(Espada.dano)
                Espada.destino = (Espada.posicao_projetil_x, Espada.posicao_projetil_y)              
                Espada.dano = 0      
                posicao_da_bala_chao = Espada.destino   
                        
    #VERIFICANDO SE PLAYER PERDEU (GAME OVER)
    if Dama.vida == 0:
        while True:
            display.blit(game_over_img,(0,0))
            pg.display.update()    
            pg.time.delay(1500)
            pg.quit()
                    

#MUDANÇA DE LUGAR DO ITEM / IDENTIFICAÇÃO SE ITEM FOI COLETADO
    
    if item_Verde_coletado:
        
        if last_item_time > 3000:          
            cords_item_Verde = mt.mudanca_base(random.randint(1,8), random.randint(0,7), constants.FLOOR_SIZE*4, constants.MATRIZ_MUDA_BASE)
            item_Verde = coletaveis((61,145,64), 10, cords_item_Verde[0], cords_item_Verde[1])
            item_Verde_coletado = False
            Dama.velocidade -= 2
            Dama.cor  = (0,0,255)
    
    if item_vida_coletada:

        if last_item_time > 30000:

            cords_item_vida_drop = mt.mudanca_base(random.randint(1,8), random.randint(0,7), constants.FLOOR_SIZE*4, constants.MATRIZ_MUDA_BASE)
            Vida_item = coletaveis((255,0,226), 10, cords_item_vida_drop[0], cords_item_vida_drop[1])
            item_vida_coletada = False
            

            
#IDENTIFICAÇÃO DE COLISÃO COM O ITEM e CD para SPAWN
        
    distanciaPlayerObjeto = calcularDistanciaPontos(Dama.posicao_x, item_Verde.posicao_coletavel_x, Dama.posicao_y, item_Verde.posicao_coletavel_y)
    
    if distanciaPlayerObjeto <= 20:       
       
        Dama.velocidade += 2
        Dama.cor = (0,238,238)           
        item_Verde.posicao_coletavel_x = 0
        item_Verde.posicao_coletavel_y = 0
        item_Verde.color = (146, 244, 255)
        item_Verde.tamanho = 0
        static_timer = pg.time.get_ticks()
    
        item_Verde_coletado = True

    distanciaPlayerObjeto_2 = calcularDistanciaPontos(Dama.posicao_x, Vida_item.posicao_coletavel_x, Dama.posicao_y, Vida_item.posicao_coletavel_y)

    if distanciaPlayerObjeto_2 <= 20:
        if Dama.vida <= 3:
            Dama.vida += 1

        Vida_item.posicao_coletavel_x = 0
        Vida_item.posicao_coletavel_y = 0
        Vida_item.tamanho = 0
        static_timer = pg.time.get_ticks()
    
        item_vida_coletada = True
    
    distacia_da_bala_chao = calcularDistanciaPontos(Dama.posicao_x, posicao_da_bala_chao[0], Dama.posicao_y, posicao_da_bala_chao[1])

    if distacia_da_bala_chao <= 20:
        Dama.ammo = 1
        Espada.destino = None
        Espada.dano = 30


    if static_timer:
        last_item_time = pg.time.get_ticks() - static_timer

#MOVIMENTAÇÃO DO PROJÉTIL
    if Dama.ammo > 0:
        if Dama.cima:
            Espada.posicao_projetil_x = Dama.posicao_x
            Espada.posicao_projetil_y = Dama.posicao_y-20
            
        elif Dama.direita:
            Espada.posicao_projetil_x = Dama.posicao_x+20
            Espada.posicao_projetil_y = Dama.posicao_y
            
        elif Dama.esquerda:
            Espada.posicao_projetil_x = Dama.posicao_x-20
            Espada.posicao_projetil_y = Dama.posicao_y
            
        elif Dama.baixo:
            Espada.posicao_projetil_x = Dama.posicao_x
            Espada.posicao_projetil_y = Dama.posicao_y+20

#
            
    if Espada.destino != None:
        if not Espada.destino == (Espada.posicao_projetil_x, Espada.posicao_projetil_y):
            Espada.movimentando = True
            Dama.ammo = 0
            #
            if Espada.destino[0]>Espada.posicao_projetil_x:
                if (Espada.destino[0] - Espada.posicao_projetil_x)<5:
                    
                    Espada.posicao_projetil_x = Espada.destino[0]
                    
                else:
                    Espada.posicao_projetil_x += 8
                    
            if Espada.destino[0]<Espada.posicao_projetil_x:
                if (Espada.posicao_projetil_x - Espada.destino[0])<5:
                    
                    Espada.posicao_projetil_x = Espada.destino[0]
                    
                else:
                    Espada.posicao_projetil_x -= 8
            #
            if Espada.destino[1]>Espada.posicao_projetil_y:
                if (Espada.destino[1] - Espada.posicao_projetil_y)<5:
                    
                    Espada.posicao_projetil_y = Espada.destino[1]
                    
                else:
                    Espada.posicao_projetil_y += 8
                    
            if Espada.destino[1]<Espada.posicao_projetil_y:
                if (Espada.posicao_projetil_y - Espada.destino[1])<5:
                    
                    Espada.posicao_projetil_y = Espada.destino[1]
                    
                else:
                    Espada.posicao_projetil_y -= 8
                    
        else:
            Espada.destino = None #Caso tenha chegado no destino, volta a ser destino = None
    else:
        Espada.movimentando = False #Já que o destino virou None no tick passado, ele deixa de estar em movimento

    if Dama.ammo > 0:   

        if Dama.esquerda:
            display.blit(orbe, (Espada.posicao_projetil_x-30, Espada.posicao_projetil_y-20))
            chao = orbe
        if Dama.direita:
            display.blit(orbe, (Espada.posicao_projetil_x-10, Espada.posicao_projetil_y-20))
            chao = orbe
        if Dama.cima:
            display.blit(orbe, (Espada.posicao_projetil_x-20, Espada.posicao_projetil_y-30))
            chao = orbe
        if Dama.baixo:
            display.blit(orbe, (Espada.posicao_projetil_x-20, Espada.posicao_projetil_y-20))
            chao = orbe

    else:
        display.blit(chao, (Espada.posicao_projetil_x-20, Espada.posicao_projetil_y-20))

    pg.display.update()
    clock.tick(60)
    