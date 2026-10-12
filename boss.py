import math
import pyxel


class Chefe:
    def __init__(self, mapa, sala=7):
        self.mapa = mapa
        self.sala = sala
        self.x = 72
        self.y = 30
        self.w = 16
        self.h = 16
        self.hp_max = 15
        self.hp = self.hp_max
        self.morto = False
        self.flash = 0
        self.dir_x = 1
        self.timer = 90
        self.projeteis = []

    def fase(self):
        return 1 if self.hp > self.hp_max / 2 else 2

    def ativo(self):
        return self.mapa.mapa_atual == self.sala and not self.morto

    def levar_dano(self, dano=1):
        self.hp -= dano
        self.flash = 6
        if self.hp <= 0:
            self.morto = True
            self.projeteis.clear()

    def checa_tiros(self, jogador):
        for tiro in jogador.tiros[:]:
            if (self.x <= tiro["x"] <= self.x + self.w and
                    self.y <= tiro["y"] <= self.y + self.h):
                jogador.tiros.remove(tiro)
                self.levar_dano(1)
                if self.morto:
                    return

    def movimento(self):
        velocidade = 0.5 if self.fase() == 1 else 1
        self.x += velocidade * self.dir_x
        if self.x < 24 or self.x > 120:
            self.dir_x *= -1

    def atira(self, jogador, angulo_extra=0):
        cx = self.x + self.w / 2
        cy = self.y + self.h / 2
        angulo = math.atan2(jogador.y + 4 - cy, jogador.x + 4 - cx) + angulo_extra
        self.projeteis.append({
            "x": cx,
            "y": cy,
            "dx": math.cos(angulo) * 1.5,
            "dy": math.sin(angulo) * 1.5,
        })

    def ataque(self, jogador):
        self.timer -= 1
        if self.timer > 0:
            return
        if self.fase() == 1:
            self.atira(jogador)
            self.timer = 30
        else:
            for desvio in (-0.4, 0, 0.4):
                self.atira(jogador, desvio)
            self.timer = 20

    def atualiza_projeteis(self, jogador):
        for p in self.projeteis[:]:
            p["x"] += p["dx"]
            p["y"] += p["dy"]
            if p["x"] < 8 or p["x"] > 152 or p["y"] < 8 or p["y"] > 112:
                self.projeteis.remove(p)
            elif (abs(p["x"] - (jogador.x + 4)) < 5 and
                  abs(p["y"] - (jogador.y + 4)) < 5):
                jogador.levar_dano()
                self.projeteis.remove(p)

    def update(self, jogador):
        if not self.ativo():
            self.projeteis.clear()
            return
        if self.flash > 0:
            self.flash -= 1
        self.checa_tiros(jogador)
        if self.morto:
            return
        self.movimento()
        self.ataque(jogador)
        self.atualiza_projeteis(jogador)

    def desenha(self):
        if not self.ativo():
            return

        if self.flash == 0 or pyxel.frame_count % 2 == 0:
            pyxel.blt(self.x, self.y, 1, 16, 0, self.w, self.h, 0)

        for p in self.projeteis:
            pyxel.circ(p["x"], p["y"], 2, 10)

        largura = 100 * self.hp / self.hp_max
        pyxel.rect(30, 12, 100, 4, 1)
        pyxel.rect(30, 12, largura, 4, 8)
        pyxel.text(30, 5, "BOSS", 7)