# lorinda.anastasia.droner.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Jogo de direcionamento de drones.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Changelog
---------
.. versionadded::    21.03
        Classe Droner.

"""
from _spy.vitollino.main import Jogo, STYLE
from browser.timer import set_timeout
from collections import namedtuple
"""Usa o timer do navegador para dar um tempinho inicial"""
Rosa = namedtuple("Rosa", "norte leste sul oeste")
STYLE.update(width=1350, height="600px")
SF = {"transition": "left 3s, top 3s"}
J = Jogo()
"""Usa o recurso novo do Vitollino Jogo. Jogo.c é Cena, Jogo.a é Elemento, Jogo.n é Texto"""
SF = {"font-size":"30px", "transition": "left 1s, top 1s"}
"""Dá o tamanho da letra da legenda e faz a legenda se movimentar suavemente quando inicia e acerta"""
VAZIO = "https://i.imgur.com/npb9Oej.png"
KNOB  = "https://i.imgur.com/v8Lqqpt.png"
ROSA = Rosa((0, -1), (1, 0), (0, 1), (-1, 0))
CIS = {ROSA.norte: ROSA.leste, ROSA.leste: ROSA.norte, ROSA.sul: ROSA.oeste, ROSA.oeste: ROSA.sul}
TRS = {ROSA.norte: ROSA.oeste, ROSA.leste: ROSA.sul, ROSA.sul: ROSA.leste, ROSA.oeste: ROSA.norte}
SWP = {0: CIS, 90:TRS}
GAP = 60

class Droner:
    """ Jogo que direciona drones para atingir alvos
    """
    CENA ="https://i.imgur.com/AD1wScZ.jpg"
    CELULA = "https://i.imgur.com/tcCj6nw.png"
    DRONE = "https://i.imgur.com/XDuFNZw.png"
    KNOBS = 30
    def __init__(self, cena):

        class Anteparo(J.a):
            """ Um bloqueio que desvia o drone para esquerda ou direita

            As legendas aparecem inicialmente no local certo e depois de um intervalo vão para o canto esquerdo

            :param    x: a posição horizontal do anteparo
            :param    y: a posição vertical do anteparo
            :param jogo: o jogo que este anteparo aparece
            :param cena: a cena onde o anteparo aparece
            :param img: imagem de fundo do anteparo
            """
            def __init__(self, x, y, cena, jogo, img=KNOB):
                pw = ph = Droner.KNOBS*2
                self.jogo = jogo
                super().__init__(img, x=x, y=y, w=pw, h=ph, cena=cena)
                self.elt.onclick = self.rodar
                self.rotate = self.jogo.rotate

            def rodar(self, ev=None, nome=None):
                """Quando o jogador acerta, apaga as interrogações da lacuna e posiciona a legenda sobre a lacuna"""
                self.jogo.rotate = self.rotate = (self.rotate+90) % 180
                self.jogo.rodar(self.rotate)
                self.elt.style.transform = f"rotate({self.rotate}deg)"

            def roda(self, rodado=0):
                """Quando o jogador acerta, apaga as interrogações da lacuna e posiciona a legenda sobre a lacuna"""
                self.rotate = rodado
                self.elt.style.transform = f"rotate({self.rotate}deg)"
                
        class Borda(Anteparo):
            def __init__(self, x, y, cena, jogo):
                super().__init__(x=x, y=y, jogo=jogo, cena=cena, img=BORDA)
            def rodar(self, ev=None, nome=None):
                pass
            def roda(self, rodado=0):
                pass

        class Drone(J.a):
            """ Um drone que desvia para esquerda ou direita ao chocar com o anteparo

            As legendas aparecem inicialmente no local certo e depois de um intervalo vão para o canto esquerdo

            :param    x: a posição horizontal do anteparo
            :param    y: a posição vertical do anteparo
            :param jogo: o jogo que este anteparo aparece
            :param cena: a cena onde o anteparo aparece
            :param img: imagem de fundo do anteparo
            """
            def __init__(self, x, y, cena, jogo, img=self.DRONE):
                pw = ph = Droner.KNOBS
                self.jogo = jogo
                super().__init__(img, x=x, y=y, w=pw, h=ph, style=SF, cena=cena)
                # self.elt.style.transition = "left 1s top 1s"
                self.elt.ontransitionend = self.rodar
                self.rotate = 0
                self.azimuth = ROSA.oeste

            def rodar(self, ev=None, nome=None):
                """Quando o jogador acerta, apaga as interrogações da lacuna e posiciona a legenda sobre a lacuna"""
                dx, dy = self.azimuth = SWP[self.jogo.rotate][self.azimuth]
                print(" end", self.x, self.y, dx, dy, self.azimuth)
                self.x = self.x + dx*GAP*2
                self.y = self.y + dy*GAP*2

            def inicia(self, ev=None, nome=None):
                """Quando o jogador acerta, apaga as interrogações da lacuna e posiciona a legenda sobre a lacuna"""
                dx, dy = self.azimuth
                self.x = self.x + dx*GAP*2
                self.y = self.y + dy*GAP*2

    
        self.cena = cena
        self.rotate = 0
        # Anteparo(200, 75, cena, self)
        self.anteparos = [self.cria(index) for index in range(w*6)]
        self.drone = Drone(int(1.25*GAP), int(1.75*GAP), cena, self)
        set_timeout(self.inicia, "1000")
        
    def cria(self, index):
        w = 11
        x, y = GAP+2*GAP*(index%w), int(-0.5*GAP)+2*GAP*(index//w)
        good = 0 < x < 11 and 0 < y < 6
        return Anteparo(x, y, cena, self) if good else Borda(x, y, cena, self) 
        
    def inicia(self, _=0):
        self.drone.inicia()
        
    def rodar(self, rodado=0):
        """Quando o jogador acerta, apaga as interrogações da lacuna e posiciona a legenda sobre a lacuna"""
        self.rotate = rodado
        [anteparo.roda(rodado) for anteparo in self.anteparos]
        

def main():
    # Associa()
    cena = J.c(Droner.CENA)
    Droner(cena)
    cena.vai()
    
main()