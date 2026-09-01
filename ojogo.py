import pyxel
from parede import Mapa
from protagonista import Jogador

class Jogo:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load("mygame.pyxres")
        self.cenario = Mapa()
        self.jogador = Jogador(80, 60)
        pyxel.run(self.update, self.draw)
    def update(self):
        self.jogador.update()
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
    def draw(self):
        pyxel.cls(0)
        self.cenario.draw()
        self.jogador.desenha()

Jogo()