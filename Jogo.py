import pygame as pg

#JOGO

class Jogo():
    def __init__(self):
        pg.init()
        self.running, self.playing = True, False
        self.START_KEY = False
        self.font_name = pg.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
       # self.main_menu = MainMenu(self)
      #  self.start = iniciar(self)
        #self.curr_menu = self.main_menu

    def checar_Se_iniciou(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running, self.playing = False, False
            if event.type == pg.K_KP_ENTER:
                self.START_KEY = True
            pg.display.update()

    def Loop_do_jogo(self):
        while self.playing:
            self.checar_Se_iniciou()
            if self.START_KEY:
                self.playing = True
            self.display.fill(self.BLACK)
            
