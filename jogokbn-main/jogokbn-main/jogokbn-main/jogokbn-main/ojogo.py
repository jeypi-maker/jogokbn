import pyxel
from parede import Mapa
from protagonista import Jogador
from inimigo import Inimigo

class Jogo:
    def __init__(self):
        pyxel.init(160, 120)
        self.inicia()
        pyxel.run(self.update, self.draw)

    def inicia(self):
        pyxel.load("mygame.pyxres")  
        self.cenario = Mapa()
        self.jogador = Jogador(80, 60, self.cenario)
        self.inimigo = Inimigo(40, 40, self.cenario)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.jogador.morto:
            if pyxel.btnp(pyxel.KEY_R):
                self.inicia()
            return

        self.jogador.update()
        self.inimigo.update(self.jogador)

    def draw(self):
        pyxel.cls(0)
        self.cenario.draw()
        self.jogador.desenha()
        self.inimigo.desenha()
        pyxel.text(2, 2, f"VIDAS: {self.jogador.vidas}", 7)

        if self.jogador.morto:
            pyxel.text(60, 56, "GAME OVER", 8)
            pyxel.text(48, 66, "R para reiniciar", 7)
Jogo()