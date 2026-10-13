"""Trilha autoral chiptune 8-bit para Scooby Dungeon.

Faixas: pyxel.playm(0) menu, (1) exploracao, (2) boss.
Usa sons 40-63 para preservar os primeiros 40 slots do jogo.
Importar e chamar carregar_trilha() sempre DEPOIS de pyxel.load().
"""
import pyxel


def carregar_trilha():
    """Registra 3 temas no banco de som atual do Pyxel."""
    # menu: lead, parte 1
    pyxel.sounds[40].set('d3 r a2 r f3 e3 d3 r d3 r f3 r a3 f3 d3 r g3 r d3 r a2 c3 d3 r e3 r c#3 r e3 g3 a3 r', 'p', '65546454655464546554645465546454', "n", 36)
    # menu: lead, parte 2
    pyxel.sounds[41].set('a3 r f3 e3 d3 r a2 r d3 r f3 a3 g3 f3 e3 r g3 r f3 d3 c3 d3 e3 r c#3 r e3 r a2 r d3 r', 'p', '65546454655464546554645465546454', "n", 36)
    # menu: chords, parte 1
    pyxel.sounds[42].set('f2 a2 d3 a2 f2 a2 d3 a2 f2 a2 d3 a2 f2 a2 d3 a2 d2 g2 b-2 g2 d2 g2 b-2 g2 e2 a2 c#3 a2 e2 a2 c#3 a2', 't', '32323232323232323232323232323232', "n", 36)
    # menu: chords, parte 2
    pyxel.sounds[43].set('f2 a2 d3 a2 f2 a2 d3 a2 f2 b-2 d3 b-2 f2 b-2 d3 b-2 d2 g2 b-2 g2 d2 g2 b-2 g2 e2 a2 c#3 a2 e2 a2 c#3 a2', 't', '32323232323232323232323232323232', "n", 36)
    # menu: bass, parte 1
    pyxel.sounds[44].set('d1 r d1 a1 d1 r a1 r b-0 r b-0 f1 b-0 r f1 r g0 r g0 d1 g0 r d1 r a0 r a0 e1 a0 r e1 r', 's', '54455445544554455445544554455445', "n", 36)
    # menu: bass, parte 2
    pyxel.sounds[45].set('d1 r d1 a1 d1 r a1 r b-0 r b-0 f1 b-0 r f1 r g0 r g0 d1 g0 r d1 r a0 r a0 e1 a0 r e1 r', 's', '54455445544554455445544554455445', "n", 36)
    # menu: drums, parte 1
    pyxel.sounds[46].set('c1 r r r g1 r r a1 c1 r r r g1 r r a1 c1 r r r g1 r r a1 c1 r r r g1 r r a1', 'n', '40002002400020024000200240002002', "n", 36)
    # menu: drums, parte 2
    pyxel.sounds[47].set('c1 r r r g1 r r a1 c1 r r r g1 r r a1 c1 r r r g1 r r a1 c1 r r r g1 r r a1', 'n', '40002002400020024000200240002002', "n", 36)
    # dungeon: lead, parte 1
    pyxel.sounds[48].set('d3 f3 a3 d3 c3 a2 f3 e3 d3 f3 a3 c4 a3 f3 d3 r a2 c3 f3 a3 g3 f3 c3 r g3 e3 c3 e3 g3 a3 g3 e3', 'p', '65546454655464546554645465546454', "n", 28)
    # dungeon: lead, parte 2
    pyxel.sounds[49].set('d3 f3 a3 c4 a3 f3 e3 d3 f3 a3 d3 f3 g3 f3 d3 r g3 b-3 a3 g3 d3 f3 g3 r e3 g3 a3 c#4 a3 g3 e3 r', 'p', '65546454655464546554645465546454', "n", 28)
    # dungeon: chords, parte 1
    pyxel.sounds[50].set('d2 a2 f2 a2 d2 a2 f2 a2 b-1 f2 d2 f2 b-1 f2 d2 f2 f2 c3 a2 c3 f2 c3 a2 c3 c2 g2 e2 g2 c2 g2 e2 g2', 't', '32323232323232323232323232323232', "n", 28)
    # dungeon: chords, parte 2
    pyxel.sounds[51].set('d2 a2 f2 a2 d2 a2 f2 a2 b-1 f2 d2 f2 b-1 f2 d2 f2 g1 d2 b-1 d2 g1 d2 b-1 d2 a1 e2 c#2 e2 a1 e2 g2 e2', 't', '32323232323232323232323232323232', "n", 28)
    # dungeon: bass, parte 1
    pyxel.sounds[52].set('d1 r d1 a1 d1 r a1 r b-0 r b-0 f1 b-0 r f1 r f1 r f1 c2 f1 r c2 r c1 r c1 g1 c1 r g1 r', 's', '54455445544554455445544554455445', "n", 28)
    # dungeon: bass, parte 2
    pyxel.sounds[53].set('d1 r d1 a1 d1 r a1 r b-0 r b-0 f1 b-0 r f1 r g0 r g0 d1 g0 r d1 r a0 r a0 e1 a0 r e1 r', 's', '54455445544554455445544554455445', "n", 28)
    # dungeon: drums, parte 1
    pyxel.sounds[54].set('c1 a2 g1 a2 c1 a2 g1 a2 c1 a2 g1 a2 c1 a2 g1 a2 c1 a2 g1 a2 c1 a2 g1 a2 c1 a2 g1 a2 c1 a2 g1 a2', 'n', '54525352545253525452535254525352', "n", 28)
    # dungeon: drums, parte 2
    pyxel.sounds[55].set('c1 a2 g1 a2 c1 a2 g1 a2 c1 a2 g1 a2 c1 a2 g1 a2 c1 a2 g1 a2 c1 a2 g1 a2 c1 a2 g1 a2 c1 a2 g1 a2', 'n', '54525352545253525452535254525352', "n", 28)
    # boss: lead, parte 1
    pyxel.sounds[56].set('d3 d3 a3 d3 f3 e3 d3 a2 f3 f3 a3 f3 e3 d3 c3 r d3 f3 a3 d3 c4 a3 f3 e3 c#3 c#3 e3 g3 a3 g3 e3 c#3', 'p', '65546454655464546554645465546454', "n", 22)
    # boss: lead, parte 2
    pyxel.sounds[57].set('d3 a3 d4 a3 c4 a3 f3 e3 f3 a3 b-3 a3 f3 e3 d3 r g3 g3 b-3 g3 a3 g3 f3 e3 c#3 e3 a3 c#4 d4 c#4 a3 r', 'p', '65546454655464546554645465546454', "n", 22)
    # boss: chords, parte 1
    pyxel.sounds[58].set('d2 f2 a2 f2 d2 f2 a2 f2 b-1 d2 f2 d2 b-1 d2 f2 d2 d2 f2 a2 f2 d2 f2 a2 f2 a1 c#2 e2 c#2 a1 c#2 e2 g2', 't', '32323232323232323232323232323232', "n", 22)
    # boss: chords, parte 2
    pyxel.sounds[59].set('d2 a2 f2 a2 d2 a2 f2 a2 b-1 f2 d2 f2 b-1 f2 d2 f2 g1 d2 b-1 d2 g1 d2 b-1 d2 a1 e2 c#2 e2 a1 e2 g2 e2', 't', '32323232323232323232323232323232', "n", 22)
    # boss: bass, parte 1
    pyxel.sounds[60].set('d1 r d1 a1 d1 r a1 r b-0 r b-0 f1 b-0 r f1 r d1 r d1 a1 d1 r a1 r a0 r a0 e1 a0 r e1 r', 's', '54455445544554455445544554455445', "n", 22)
    # boss: bass, parte 2
    pyxel.sounds[61].set('d1 r d1 a1 d1 r a1 r b-0 r b-0 f1 b-0 r f1 r g0 r g0 d1 g0 r d1 r a0 r a0 e1 a0 r e1 r', 's', '54455445544554455445544554455445', "n", 22)
    # boss: drums, parte 1
    pyxel.sounds[62].set('c1 a2 g1 a2 c1 c1 g1 a2 c1 a2 g1 a2 c1 c1 g1 a2 c1 a2 g1 a2 c1 c1 g1 a2 c1 a2 g1 a2 c1 c1 g1 a2', 'n', '64646465646464656464646564646465', "n", 22)
    # boss: drums, parte 2
    pyxel.sounds[63].set('c1 a2 g1 a2 c1 c1 g1 a2 c1 a2 g1 a2 c1 c1 g1 a2 c1 a2 g1 a2 c1 c1 g1 a2 c1 a2 g1 a2 c1 c1 g1 a2', 'n', '64646465646464656464646564646465', "n", 22)

    pyxel.musics[0].set([40, 41], [42, 43], [44, 45], [46, 47])
    pyxel.musics[1].set([48, 49], [50, 51], [52, 53], [54, 55])
    pyxel.musics[2].set([56, 57], [58, 59], [60, 61], [62, 63])
