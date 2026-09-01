import pyxel

class Mapa:
    def __init__(self):
        self.height = 16
        self.width = 16

    def tem_parede(self, x, y):
        grid_x = x // 8
        grid_y = y // 8
        
        if grid_x < 0 or grid_x >= 20 or grid_y < 0 or grid_y >= 15:
            return True

        bloco = pyxel.tilemaps[0].pget(grid_x, grid_y)
        
        if bloco == (0, 0):
            return True  
        
        return False     

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, 160, 120)
