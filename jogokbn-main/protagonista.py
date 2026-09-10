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
        if pyxel.btn(pyxel.KEY_W) == True:
            self.y = self.y - 2
            self.andando = True
        if pyxel.btn(pyxel.KEY_S) == True:
            self.y = self.y + 2
            self.andando = True
        if pyxel.btn(pyxel.KEY_A) == True:
            self.x = self.x - 2
            self.andando = True
            self.direita = False
        if pyxel.btn(pyxel.KEY_D) == True:
            self.x = self.x + 2
            self.andando = True
            self.direita = True

        self.x = max(8, min(144, self.x))
        self.y = max(8, min(104, self.y))

        if self.direita == False:
            self.direcao = -8
        else:
            self.direcao = 8
        if self.andando == True:
            self.sprite1 = pyxel.frame_count % 2 * 8

    def desenha(self):
        pyxel.blt(self.x, self.y, 1, self.sprite1, 0, self.direcao, 8, 0)
