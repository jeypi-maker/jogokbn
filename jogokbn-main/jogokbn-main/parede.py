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

    def draw(self):
        pyxel.bltm(0, 0, self.mapa_atual, 0, 0, 160, 120)

