import pyxel

class Jogador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = 2
    def update(self):
        dx = 0
        dy = 0
        if pyxel.btn(pyxel.KEY_A):
            dx = -1 * self.velocidade
        elif pyxel.btn(pyxel.KEY_D):
            dx = self.velocidade
        if pyxel.btn(pyxel.KEY_W):
            dy = -1 * self.velocidade
        elif pyxel.btn(pyxel.KEY_S):
            dy = self.velocidade
        self.x = self.x + dx
        self.y = self.y + dy

       
        self.x = max(8, min(self.x, 147))
        self.y = max(8, min(self.y, 107))

        if self.x == 147 and self.y >= 60 and self.y <= 72:
            self.entrar_porta()

        def entrar_porta(self):
            pass

    def desenha(self):
        pyxel.rect(self.x, self.y, 5, 5, 9)