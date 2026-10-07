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
        elif self.mapa_atual == 2:
            if (grid_x == 10 and grid_y == 7):
                return True
        elif self.mapa_atual == 3:
            if (grid_x == 8 and grid_y == 9) or (grid_x == 9 and grid_y == 9) or (grid_x == 15 and grid_y == 5):
                return True
        elif self.mapa_atual == 5:
            if (grid_x == 3 and grid_y == 2) or (grid_x == 4 and grid_y == 8) or (grid_x == 9 and grid_y == 7) or (grid_x == 12 and grid_y == 11) or (grid_x == 17 and grid_y == 9):
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

