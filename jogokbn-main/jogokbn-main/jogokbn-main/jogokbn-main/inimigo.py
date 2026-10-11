import pyxel


class Inimigo:
    def __init__(self, x, y, mapa):
        self.mapa = mapa
        self.spawns = {
            1: (x, y),
            3: (100, 80),
            5: (60, 70),
        }
        self.x = x
        self.y = y
        self.mapa_vista = mapa.mapa_atual
        self.velocidade = 1/2

    def reseta(self):
        self.x, self.y = self.spawns[self.mapa.mapa_atual]

    def update(self, jogador):
        atual = self.mapa.mapa_atual

        if atual not in self.spawns:
            self.mapa_vista = atual
            return

        if atual != self.mapa_vista:
            self.mapa_vista = atual
            self.reseta()
            return

        dx = 0
        dy = 0
        if jogador.x > self.x:
            dx = self.velocidade
        elif jogador.x < self.x:
            dx = -self.velocidade
        if jogador.y > self.y:
            dy = self.velocidade
        elif jogador.y < self.y:
            dy = -self.velocidade

        if not self.mapa.colide(self.x + dx, self.y):
            self.x += dx
        if not self.mapa.colide(self.x, self.y + dy):
            self.y += dy

        if abs(jogador.x - self.x) < 6 and abs(jogador.y - self.y) < 6:
            if jogador.levar_dano():
                self.reseta()

    def desenha(self):
        if self.mapa.mapa_atual not in self.spawns:
            return
        frame = pyxel.frame_count // 6 % 2 * 8
        pyxel.blt(self.x, self.y, 1, frame, 8, 8, 8, 0)

