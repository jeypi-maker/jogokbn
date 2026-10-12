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
        self.tiros = []
        self.velocidade_tiro = 4
        self.vidas = 1
        self.bonus_pego = False
        self.invulneravel = 0
        self.morto = False
        self.cooldown_tiro = 0
        self.intervalo_tiro = 15

    def update(self):
        self.andando = False
        self.sprite1 = 0
        dx = 0
        dy = 0
        dxt = 0
        dyt = 0

        if pyxel.btn(pyxel.KEY_W):
            dy -= 2
        if pyxel.btn(pyxel.KEY_S):
            dy += 2
        if pyxel.btn(pyxel.KEY_A):
            dx -= 2
            self.direita = False
        if pyxel.btn(pyxel.KEY_D):
            dx += 2
            self.direita = True

        if dx != 0 or dy != 0:
            self.andando = True

        if not self.mapa.colide(self.x + dx, self.y):
            self.x += dx
        if not self.mapa.colide(self.x, self.y + dy):
            self.y += dy

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

        if pyxel.btnp(pyxel.KEY_UP):
            dyt = -1
        elif pyxel.btnp(pyxel.KEY_DOWN):
            dyt = 1
        elif pyxel.btnp(pyxel.KEY_LEFT):
            dxt = -1
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            dxt = 1

        if (dxt != 0 or dyt != 0) and self.cooldown_tiro == 0:
            self.tiros.append({
                "x": self.x + 4,
                "y": self.y + 4,
                "dx": dxt,
                "dy": dyt
            })
            self.cooldown_tiro = self.intervalo_tiro

        for tiro in self.tiros[:]:
            tiro["x"] += tiro["dx"] * self.velocidade_tiro
            tiro["y"] += tiro["dy"] * self.velocidade_tiro
            if (tiro["x"] < 9 or tiro["x"] > 151 or
                tiro["y"] < 9 or tiro["y"] > 111):
                self.tiros.remove(tiro)

        if self.cooldown_tiro > 0:
            self.cooldown_tiro -= 1

        if self.invulneravel > 0:
            self.invulneravel -= 1

        if self.mapa.bau(self.x, self.y):
            self.vidas += 1

        if self.mapa.mapa_atual == 4:
            self.x = max(64, min(80, self.x))

        self.direcao = 8 if self.direita else -8
        if self.andando:
            self.sprite1 = pyxel.frame_count % 2 * 8

        self.saida()

    def saida(self):
        if self.x == 144 and self.y == 56 and self.mapa.mapa_atual == 0:
            self.mapa.mapa_atual = 1
            self.x = 10
            self.tiros.clear()
        if self.x == 8 and self.y == 56 and self.mapa.mapa_atual == 1:
            self.mapa.mapa_atual = 0
            self.x = 142
            self.tiros.clear()
        if self.x == 144 and self.y == 88 and self.mapa.mapa_atual == 1:
            self.mapa.mapa_atual = 2
            self.x = 10
            self.y = 88
            self.tiros.clear()
        if self.x == 8 and self.y == 88 and self.mapa.mapa_atual == 2:
            self.mapa.mapa_atual = 1
            self.x = 142
            self.y = 88
            self.tiros.clear()
        if self.x == 128 and self.y == 104 and self.mapa.mapa_atual == 1:
            self.mapa.mapa_atual = 3
            self.x = 24
            self.y = 10
            self.tiros.clear()
        if self.x == 24 and self.y == 8 and self.mapa.mapa_atual == 3:
            self.mapa.mapa_atual = 1
            self.x = 128
            self.y = 102
            self.tiros.clear()
        if self.x == 72 and self.y == 104 and self.mapa.mapa_atual == 3:
            self.mapa.mapa_atual = 4
            self.x = 72
            self.y = 10
            self.tiros.clear()
        if self.x == 72 and self.y == 8 and self.mapa.mapa_atual == 4:
            self.mapa.mapa_atual = 3
            self.x = 72
            self.y = 102
            self.tiros.clear()
        if self.x == 72 and self.y == 104 and self.mapa.mapa_atual == 4:
            self.mapa.mapa_atual = 5
            self.x = 72
            self.y = 10
            self.tiros.clear()
        if self.x == 72 and self.y == 8 and self.mapa.mapa_atual == 5:
            self.mapa.mapa_atual = 4
            self.x = 72
            self.y = 102
            self.tiros.clear()
        if self.x == 144 and self.y == 16 and self.mapa.mapa_atual == 5:
            self.mapa.mapa_atual = 6
            self.x = 10
            self.y = 16
            self.tiros.clear()
        if self.x == 8 and self.y == 16 and self.mapa.mapa_atual == 6:
            self.mapa.mapa_atual = 5
            self.x = 142
            self.y = 16
            self.tiros.clear()
        if self.x == 8 and self.y == 72 and self.mapa.mapa_atual == 5:
            self.mapa.mapa_atual = 7
            self.x = 142
            self.y = 72
            self.tiros.clear()
        if self.x == 144 and self.y == 72 and self.mapa.mapa_atual == 7:
            self.mapa.mapa_atual = 5
            self.x = 10
            self.y = 72
            self.tiros.clear()

    def levar_dano(self):
        if self.invulneravel > 0 or self.morto:
            return False
        self.vidas -= 1
        if self.vidas <= 0:
            self.morto = True
            return False
        self.invulneravel = 60
        return True

    def desenha(self):
        for tiro in self.tiros:
            pyxel.circ(tiro["x"], tiro["y"], 2, 12)
        if self.invulneravel > 0 and pyxel.frame_count % 4 < 2:
            return
        pyxel.blt(self.x, self.y, 1, self.sprite1, 0, self.direcao, 8, 0)

