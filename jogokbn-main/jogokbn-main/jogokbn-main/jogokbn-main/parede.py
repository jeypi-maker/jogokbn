import pyxel

class Mapa:
    def __init__(self):
        self.height = 16
        self.width = 16
        self.mapa_atual = 0
        self.baus = {
            2: {"pos": (10, 7), "tile_aberto": (5, 1), "aberto": False},
            6: {"pos": (13, 8), "tile_aberto": (5, 1), "aberto": False},
        }

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
        elif self.mapa_atual == 6:
            if grid_x == 13 and grid_y == 8:
                return True
        return False
      

    def colide(self, x, y, tamanho=8):
        return (
            self.tem_parede(x, y)
            or self.tem_parede(x + tamanho - 1, y)
            or self.tem_parede(x, y + tamanho - 1)
            or self.tem_parede(x + tamanho - 1, y + tamanho - 1)
        )

    def bau(self, x, y, tamanho=8):
        bau = self.baus.get(self.mapa_atual)
        if bau is None or bau["aberto"]:
            return False

        tx, ty = bau["pos"]
        bx, by = tx * 8, ty * 8
        margem = 2
        if (x + tamanho >= bx - margem and x <= bx + 8 + margem - 1
            and y + tamanho >= by - margem and y <= by + 8 + margem - 1):
                bau["aberto"] = True
                pyxel.tilemaps[self.mapa_atual].pset(tx, ty, bau["tile_aberto"])
                return True
        return False

    def draw(self):
        pyxel.bltm(0, 0, self.mapa_atual, 0, 0, 160, 120)

