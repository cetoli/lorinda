# lorinda.anastasia.main.py
from _spy.vitollino.main import Jogo, STYLE
from browser.timer import set_timeout
STYLE.update(width=1350, height="600px")
J = Jogo()
SF = {"font-size":"30px", "transition": "left 2s, top 4s"}

class Associa:
    CENA ="https://i.imgur.com/AD1wScZ.jpg"
    CELULA = "https://i.imgur.com/tcCj6nw.png"
    VAZIO = "https://i.imgur.com/2moCwSz.png"
    VAZIO = "https://i.imgur.com/npb9Oej.png"
    class Nome:
        def __init__(self,nome, tit, x, y, cena):
            self.nome, self.tit, self.x, self.y = nome, tit, x, y
            drop = {nome: self.acertou}
            self.lacuna = J.a(Associa.VAZIO, x=x, y=y, w=160, h=40, style=SF, cena=cena, drop=drop)
            self.o_nome = J.a(Associa.VAZIO, tit=f"n_{tit}", x=x, y=y, w=160, h=40, style=SF, cena=cena, drag=True)
            self.o_nome.elt.html = f"{nome}"
            set_timeout(self.inicia, 3000+10*tit)
            
        def acertou(self, ev=None):
            self.lacuna.elt.html = ""
            self.o_nome.x = self.x
            self.o_nome.y = self.y
            
        def inicia(self, ev=None):
            self.lacuna.elt.html = "??????????"
            self.o_nome.x = 100
            self.o_nome.y = 50+100*self.tit
        

    
    def __init__(self):
        self.cena = J.c(self.CENA)
        self.celula = J.a(self.CELULA, x=300, y=50, w=600, h=500, cena=self.cena)
        self.mito = self.Nome(nome="mitocôndria", tit=0, x=650, y=150, cena=self.cena)
        self.nucle = self.Nome(nome="núcleo",  tit=1, x=550, y=220, cena=self.cena)
        self.cena.vai()

def main():
    Associa()
    
main()