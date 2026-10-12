import pyxel
from parede import Mapa
from protagonista import Jogador
from inimigo import Inimigo
from boss import Chefe

class Jogo:
    def __init__(self):
        pyxel.init(160, 120)
        self.inicia()
        self.iniciar = "menu"
        pyxel.run(self.update, self.draw)

    def inicia(self):
        pyxel.load("mygame.pyxres")  
        self.cenario = Mapa()
        self.jogador = Jogador(80, 60, self.cenario)
        self.inimigo = Inimigo(100, 50, self.cenario)
        self.boss = Chefe(self.cenario, sala=7)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.iniciar == "menu":
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.iniciar = "jogo"
            return

        if self.jogador.morto:
            if pyxel.btnp(pyxel.KEY_R):
                self.inicia()
            return

        self.jogador.update()
        self.inimigo.update(self.jogador)
        self.boss.update(self.jogador)

    def draw(self):
        pyxel.cls(0)
        if self.iniciar == "menu":
            pyxel.text(60, 56, "SCOOBY DUNGEON", 10)
            pyxel.text(48, 66, "ENTER para iniciar", 7)
            return
        self.cenario.draw()
        self.jogador.desenha()
        self.inimigo.desenha()
        self.boss.desenha()
        pyxel.text(2, 2, f"VIDAS: {self.jogador.vidas}", 7)

        if self.jogador.morto:
            pyxel.text(60, 56, "GAME OVER", 8)
            pyxel.text(48, 66, "R para reiniciar", 7)

        if self.boss.morto:
            pyxel.text(56, 56, "VOCE VENCEU!", 11)
Jogo()