import pyxel
from parede import Mapa
from protagonista import Jogador
from inimigo import Inimigo
from boss import Chefe
from trilha import carregar_trilha


class Jogo:
    def __init__(self):
        pyxel.init(160, 120)
        self.iniciar = "menu"
        self.trilha_atual = None
        self.inicia()
        pyxel.run(self.update, self.draw)

    def inicia(self):
        pyxel.load("mygame.pyxres")
        carregar_trilha() 
        self.cenario = Mapa()
        self.jogador = Jogador(80, 60, self.cenario)
        self.inimigo = Inimigo(100, 50, self.cenario)
        self.boss = Chefe(self.cenario, sala=7)
        self.trilha_atual = None
        self.tocar_trilha(0 if self.iniciar == "menu" else 1)

    def tocar_trilha(self, faixa):
        if self.trilha_atual == faixa:
            return 
        self.trilha_atual = faixa
        if faixa is None:
            pyxel.stop()
        else:
            pyxel.playm(faixa, loop=True)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.iniciar == "menu":
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.iniciar = "jogo"
                self.tocar_trilha(1)
            return

        if self.jogador.morto:
            self.tocar_trilha(None)
            if pyxel.btnp(pyxel.KEY_R):
                self.inicia()
            return

        if self.boss.morto:
            self.tocar_trilha(None)
            return

        self.jogador.update()
        self.inimigo.update(self.jogador)
        self.boss.update(self.jogador)

        if self.jogador.morto or self.boss.morto:
            self.tocar_trilha(None)
        elif self.cenario.mapa_atual == 7:
            self.tocar_trilha(2)
        else:
            self.tocar_trilha(1)

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

