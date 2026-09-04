import pyxel

class Jogador:
    def __init__(self, x, y, mapa):
        self.x = x
        self.y = y
        self.velocidade = 2
        self.mapa = mapa
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
        futurox = self.x + dx
        futuroy = self.y + dy
        if self.pode_andar(futurox, self.y):
            self.x = max(8, min(futurox, 136))
            
        if self.pode_andar(self.x, futuroy):
            self.y = max(8, min(futuroy, 96))
                
        if self.x == 136 and self.y >= 60 and self.y <= 72:
            self.entrar_porta()

    def pode_andar(self, x, y):
        if self.mapa.tem_parede(x, y): return False
        if self.mapa.tem_parede(x + 15, y): return False
        if self.mapa.tem_parede(x, y + 15): return False
        if self.mapa.tem_parede(x + 15, y + 15): return False
        return True

    def entrar_porta(self):
        self.x = 10
        self.mapa.mapa_atual = 1

    def desenha(self):
        pyxel.rect(self.x, self.y, 16, 16, 9)