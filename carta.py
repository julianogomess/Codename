import pygame

LARANJA = (255, 165, 0)
ROXO = (138, 43, 226)
VERDE = (127,255,212)
VERDENEON = (57, 255, 20)
class Carta(object):
    def __init__(self,palavra , cor ):
        self.palavra = palavra
        self.cor = cor
        self.estado = 'fechado'
        self.marcado = False
        self.x = 0
        self.y = 0
        self.width = 175
        self.height = 100

    def getP(self):
        return self.palavra
    def getCor(self):
        if self.cor == 'preto':
            return (0,0,0)
        if self.cor == 'branco':
            return (211, 211, 211)
        if self.cor == 'laranja':
            return LARANJA
        if self.cor == 'roxo':
            return ROXO
        if self.cor == 'verde':
            return VERDENEON

    def draw(self, win):
        font = pygame.font.SysFont("Arial", 25)
        if self.estado == 'fechado':
            text = font.render(self.palavra, False, (0, 0, 0))
            pygame.draw.rect(win, VERDE , (self.x, self.y, self.width, self.height))
        elif self.estado == 'aberto':
            if self.cor == 'preto':
                text = font.render(self.palavra, False , (255,255,255))
            else:
                text = font.render(self.palavra, False, (0, 0, 0))
            pygame.draw.rect(win, self.getCor(), (self.x, self.y, self.width, self.height))

        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))


    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False