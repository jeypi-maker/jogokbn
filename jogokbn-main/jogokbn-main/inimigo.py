import pyxel


class Inimigo:
    def __init__(self, x, y, mapa):
        self.x = x
        self.y = y
        self.mapa = mapa
        self.velocidade = 1
        self.direcao = 1

    def update(self):
        proximo_x = self.x + (self.velocidade * self.direcao)

        # Verifica se existe uma parede na frente
        if self.mapa.tem_parede(proximo_x, self.y):
            self.direcao *= -1
        else:
            self.x = proximo_x

        # Impede o inimigo de sair da tela
        self.x = max(8, min(144, self.x))

    def desenha(self):
        pyxel.rect(self.x - 3, self.y - 3, 6, 6, 8)