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
        self.hp_max = 3
        self.hp = self.hp_max
        self.mortos = set()
        self.flash = 0

    def reseta(self):
        self.x, self.y = self.spawns[self.mapa.mapa_atual]

    def ativo(self):
        atual = self.mapa.mapa_atual
        return atual in self.spawns and atual not in self.mortos

    def levar_dano(self, dano=1):
        self.hp -= dano
        self.flash = 6
        if self.hp <= 0:
            self.mortos.add(self.mapa.mapa_atual)

    def checa_tiros(self, jogador):
        for tiro in jogador.tiros[:]:
            if (self.x <= tiro["x"] <= self.x + 8 and
                    self.y <= tiro["y"] <= self.y + 8):
                jogador.tiros.remove(tiro)
                self.levar_dano(1)
                if not self.ativo():
                    return

    def update(self, jogador):
        atual = self.mapa.mapa_atual

        if atual not in self.spawns or atual in self.mortos:
            self.mapa_vista = atual
            return

        if atual != self.mapa_vista:
            self.mapa_vista = atual
            self.hp = self.hp_max
            self.reseta()
            return

        if self.flash > 0:
            self.flash -= 1

        self.checa_tiros(jogador)
        if not self.ativo():
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
        if not self.ativo():
            return

        if self.flash == 0 or pyxel.frame_count % 2 == 0:
            frame = pyxel.frame_count // 6 % 2 * 8
            pyxel.blt(self.x, self.y, 1, frame, 8, 8, 8, 0)

        largura = 8 * self.hp / self.hp_max
        pyxel.rect(self.x, self.y - 3, 8, 2, 1)
        pyxel.rect(self.x, self.y - 3, largura, 2, 8)