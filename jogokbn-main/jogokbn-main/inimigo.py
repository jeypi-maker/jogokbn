import pyxel


class Inimigo:
    def __init__(self, x, y, mapa):
        self.x = x
        self.y = y
        self.mapa = mapa
        self.velocidade = 1
        self.direcao = 1
        self.tamanho = 6

    def pode_mover(self, novo_x, novo_y):
        metade = self.tamanho // 2

        pontos = [
            (novo_x - metade, novo_y - metade),
            (novo_x + metade, novo_y - metade),
            (novo_x - metade, novo_y + metade),
            (novo_x + metade, novo_y + metade)
        ]

        for ponto_x, ponto_y in pontos:
            if self.mapa.tem_parede(ponto_x, ponto_y):
                return False

        return True

    def update(self):
        novo_x = self.x + (self.velocidade * self.direcao)

        if novo_x <= 8 or novo_x >= 144:
            self.direcao *= -1
            return

        if self.pode_mover(novo_x, self.y):
            self.x = novo_x
        else:
            self.direcao *= -1

    def desenha(self):
        pyxel.rect(
            self.x - 3,
            self.y - 3,
            self.tamanho,
            self.tamanho,
            8
        )