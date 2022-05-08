import pygame as pg

class Player():
    def __init__ (self, position: tuple, size: tuple, velocidade: int, vida: int, ammo: int,  img: pg.surface.Surface):
        self.rect = pg.Rect(position[0], position[1], position[0] + size[0], position[1] + size[1])
        self.size = size
        self.velocidade = velocidade
        self.vida = vida
        self.ammo = ammo
        self.vida = vida
        self.imune = False
        self.img = img
        self.direcao = {
                'cima': False,
                'baixo': False,
                'esquerda': False,
                'direita': False
                }

    def draw(self, dest_surface: pg.surface.Surface):
        dest_surface.blit(self.img, (self.rect[0] - self.size[0]//2, self.rect[1] - self.size[1]//2, self.rect[2] + self.size[0]//2, self.rect[3] + self.size[1]//2))

    def move(self):
        keys = pg.key.get_pressed()

        up = keys[pg.K_UP] or keys[pg.K_w]
        down = keys[pg.K_DOWN] or keys[pg.K_s]
        left = keys[pg.K_LEFT] or keys[pg.K_a]
        right = keys[pg.K_RIGHT] or keys[pg.K_d]

        self.direcao['cima'] = up
        self.direcao['baixo'] = down
        self.direcao['esquerda'] = left
        self.direcao['direita'] = right

        movement = pg.math.Vector2(right - left, down - up)

        if movement.length_squared() > 0:
            movement.scale_to_length(self.velocidade)
            self.rect.move_ip(round(movement.x), round(movement.y))

    def barra_de_vida(self, display):
        
        if self.vida >= 1:           
            pg.draw.circle(display, (254,0,123), (220,120), 10) 

        if self.vida >= 2:           
            pg.draw.circle(display, (254,0,123), (245,120), 10) 
        
        if self.vida >= 3:
            pg.draw.circle(display, (254,0,123), (270,120), 10)



