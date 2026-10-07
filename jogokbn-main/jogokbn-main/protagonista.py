import pyxel


class Jogador:
    def __init__(self, x, y, mapa):
        self.x = x
        self.y = y
        self.mapa = mapa
        self.andando = False
        self.sprite1 = 0
        self.direita = True
        self.direcao = 8

    def update(self):
        self.andando = False
        self.sprite1 = 0
        if pyxel.btn(pyxel.KEY_W) is True:
            self.y = self.y - 2
            self.andando = True
        if pyxel.btn(pyxel.KEY_S) is True:
            self.y = self.y + 2
            self.andando = True
        if pyxel.btn(pyxel.KEY_A) is True:
            self.x = self.x - 2
            self.andando = True
            self.direita = False
        if pyxel.btn(pyxel.KEY_D) is True:
            self.x = self.x + 2
            self.andando = True
            self.direita = True

        self.x = max(8, min(144, self.x))
        self.y = max(8, min(104, self.y))

        if self.direita is False:
            self.direcao = -8
        else:
            self.direcao = 8
        if self.andando is True:
            self.sprite1 = pyxel.frame_count % 2 * 8
        if self.andando is True:
            self.sprite1 = pyxel.frame_count % 2 * 8

        self.saida()

    def saida(self):
        if self.x == 144 and self.mapa.mapa_atual == 0:
            self.mapa.mapa_atual = 1
            self.x = 9
        if self.x == 8 and self.y == 56 and self.mapa.mapa_atual == 1:
            self.mapa.mapa_atual = 0
            self.x = 143
        if self.x == 144 and self.y == 88 and self.mapa.mapa_atual == 1:
            self.mapa.mapa_atual = 2
            self.x = 9
            self.y = 88
        if self.x == 8 and self.y == 88 and self.mapa.mapa_atual == 2:
            self.mapa.mapa_atual = 1
            self.x = 143
            self.y = 88
        if self.x == 127 and self.y == 104 and self.mapa.mapa_atual == 1:
            self.mapa.mapa_atual = 3
            self.x = 24
            self.y = 9
        if self.x == 24 and self.y == 8 and self.mapa.mapa_atual == 3:
            self.mapa.mapa_atual = 1
            self.x = 127
            self.y = 103

    def desenha(self):
        pyxel.blt(self.x, self.y, 1, self.sprite1, 0, self.direcao, 8, 0)
