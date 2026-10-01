import pyxel

class Mapa:
    def __init__(self):
        self.height = 16
        self.width = 16
        self.mapa_atual = 0

    def tem_parede(self, x, y):
        grid_x = x // 8
        grid_y = y // 8
        if self.mapa_atual == 1:
            if (grid_x == 6 and grid_y == 7) or (grid_x == 11 and grid_y == 10):
                return True
        return False
      

    def colide(self, x, y, tamanho=8):

        return (
            self.tem_parede(x, y)
            or self.tem_parede(x + tamanho - 1, y)
            or self.tem_parede(x, y + tamanho - 1)
            or self.tem_parede(x + tamanho - 1, y + tamanho - 1)
        )

    def draw(self):
        pyxel.bltm(0, 0, self.mapa_atual, 0, 0, 160, 120)

