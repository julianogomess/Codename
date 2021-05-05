
import sys
import pygame
import pygame.font
from pygame.locals import *
import random
#from bot import enviarPalavra
from gerar import gerar
from carta import Carta




#Criação para spymaster


#ordem das palavras
def gerarordem(cpreta,cbrancas,claranja,croxo):
    ordem = []
    contp , contb , contl ,contr = 1,8,8,8
    while contp!=0 or contb!=0 or contl!=0 or contr!=0:
        a = random.randint(0,4)
        if a==0 and contp != 0:
            c = Carta(cpreta,'preto')
            ordem.append(c)
            contp = contp - 1
        elif a==1 and contb != 0:
            c = Carta(cbrancas[contb-1],'verde')
            ordem.append(c)
            contb -= 1
        elif a == 2 and contl != 0:
            c = Carta(claranja[contl - 1], 'laranja')
            ordem.append(c)
            contl -= 1
        elif a == 3 and contr != 0:
            c = Carta(croxo[contr - 1], 'roxo')
            ordem.append(c)
            contr -= 1
    return ordem



def fraseBot(lista):
    msg = ''
    msgl = 'As laranjas são: '
    msgr = 'As roxas são: '
    msgp = 'A preta é: '
    msgb = 'As verdes são é: '
    for x in range(5):
        for y in range(5):
            if(lista[y][x].estado == 'fechado'):
                msg1 = lista[y][x].palavra
                if(lista[y][x].cor=='preto'):
                    msgp += msg1
                elif(lista[y][x].cor=='verde'):
                    msgb += msg1 + ' , '
                elif(lista[y][x].cor=='laranja'):
                    msgl +=  msg1 + ' , '
                elif(lista[y][x].cor=='roxo'):
                    msgr += msg1 + ' , '
    msg = msgp + '\n\n' + msgb + '\n\n' + msgl +'\n\n'+ msgr + '\n\n'
    arquivo = open('spy.txt', 'w+')
    arquivo.write(msg)
    arquivo.close()


    return msg


class Button:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.width = 60
        self.height = 60
        self.text = ''

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("Arial", 30)
        text = font.render(self.text, 1, (255, 255, 255))
        win.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2),
                        self.y + round(self.height / 2) - round(text.get_height() / 2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False
pygame.init()
janelaw , janelah = 1250, 620
size = (janelaw,janelah)
screen = pygame.display.set_mode(size)

def main_doistimes():
    LARANJA = (255, 165, 0)
    ROXO = (138, 43, 226)


    #banco de palavras
    palavras = gerar()
    #sorteio das palavras
    msgcel = ''
    totalp = palavras.__len__() - 1
    cbrancas = []
    croxo = []
    claranja = []
    sorteio = random.randint(0 , totalp)
    cpreta = palavras[sorteio]

    del(palavras[sorteio])
    totalp -= 1
    for x in range(8):
        sorteio = random.randint(0, totalp)
        cbrancas.append(palavras[sorteio])
        del (palavras[sorteio])
        totalp -= 1
    for x in range(8):
        sorteio = random.randint(0, totalp)
        claranja.append(palavras[sorteio])
        del (palavras[sorteio])
        totalp -= 1

    for x in range(8):
        sorteio = random.randint(0, totalp)
        croxo.append(palavras[sorteio])
        del (palavras[sorteio])
        totalp -= 1

    ordem = gerarordem(cpreta,cbrancas,claranja,croxo)

    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    lista5 = []
    lista = []
    for x in range (5):
        lista1.append(ordem[x])
        lista2.append(ordem[x+5])
        lista3.append(ordem[x+10])
        lista4.append(ordem[x+15])
        lista5.append(ordem[x+20])

    lista=[lista1 , lista2 , lista3 , lista4 , lista5]
    for i in range(5):
        for j in range(5):
            lista[j][i].x = 20 + (j * (lista[j][i].width + 20))
            lista[j][i].y = 20 + (i * (lista[j][i].height + 20))

    msg = fraseBot(lista)
    BEGE = 71,74,81

    #uso o cronometro
    clock = pygame.time.Clock()
    CLOCKTICK = pygame.USEREVENT + 1
    pygame.time.set_timer(CLOCKTICK, 1000)
    VEZ = 120
    temporizador = VEZ

    pygame.font.init()
    font = pygame.font.SysFont('Arial', 20)
    fontgrande = pygame.font.SysFont('Arial',75)
    VERDENEON = (57, 255, 20)
    screen.fill(BEGE)

    contador = 0

    pygame.display.update()
    proxo = 8
    plaranja = 8
    pverde = 8
    msg = 'CODE NOMES'
    pygame.display.set_caption(msg)
    tamW , tamH = 175,100
    jogo = False
    vez = 0
    placar1 = fontgrande.render(str(plaranja) , False, LARANJA)
    placarx = fontgrande.render('X' , False, (255, 255, 255))
    placar2 = fontgrande.render(str(proxo) , False, ROXO)
    placar3 = fontgrande.render(str(pverde) , False, VERDENEON)
    pygame.draw.rect(screen,BEGE,(janelaw-260,30,250,100))
    screen.blit(placar1, (janelaw - 260, 30))
    screen.blit(placarx, (janelaw - 210, 30))
    screen.blit(placar2, (janelaw - 160, 30))
    screen.blit(placarx, (janelaw - 110, 30))
    screen.blit(placar3, (janelaw - 60, 30))
    botaoLaranja= Button(janelaw - 240, 150, LARANJA)
    botaoRoxo= Button(janelaw - 160, 150, ROXO)
    botaoVerde = Button(janelaw - 80, 150, VERDENEON)
    botaoFim = Button(janelaw - 250,500,(0,0,0))

    botaoFim.text = 'Jogar novamente!'
    botaoFim.width=230
    botaoFim.height=90
    for x in range(5):
        for y in range(5):
            lista[y][x].draw(screen)
    run = True
    while run:
        botaoLaranja.draw(screen)
        botaoRoxo.draw(screen)
        botaoFim.draw(screen)
        botaoVerde.draw(screen)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                run = False
            if event.type == CLOCKTICK:
                if(jogo):
                    temporizador = temporizador - 1

            if pygame.mouse.get_pressed()[0]:
                a, b = pygame.mouse.get_pos()
                jogo = True
                if botaoLaranja.click((a,b)):
                    vez = 0
                    temporizador = VEZ
                    jogo = True
                if botaoRoxo.click((a,b)):
                    vez = 1
                    temporizador = VEZ
                    jogo = True
                if botaoVerde.click((a,b)):
                    vez = 2
                    temporizador = VEZ
                    jogo = True

                if botaoFim.click((a,b)):
                    run = False
                for x in range(5):
                    for y in range(5):
                        if lista[y][x].click((a,b)):
                            if(lista[y][x].cor=='laranja' and lista[y][x].estado == 'fechado') :
                                plaranja -= 1
                                lista[y][x].estado = 'aberto'
                                if vez==1:
                                    vez = 2
                                    temporizador = VEZ
                                elif vez==2:
                                    vez = 0
                                    temporizador = VEZ
                            elif (lista[y][x].cor=='roxo' and lista[y][x].estado == 'fechado'):
                                proxo -= 1
                                if vez==2:
                                    vez = 0
                                    temporizador = VEZ
                                elif vez==0:
                                    vez = 1
                                    temporizador = VEZ
                                lista[y][x].estado = 'aberto'
                            elif (lista[y][x].cor=='verde' and lista[y][x].estado=='fechado'):
                                pverde -=1
                                lista[y][x].estado = 'aberto'
                                if vez==0:
                                    vez = 1
                                    temporizador = VEZ
                                elif vez==1:
                                    vez = 2
                                    temporizador = VEZ
                            if(lista[y][x].getCor()==(0,0,0) or proxo == 0 or plaranja == 0 or pverde==0):
                                jogo = False


                        lista[y][x].draw(screen)
                if jogo == False:
                    for x in range(5):
                        for y in range(5):
                            lista[y][x].estado = 'aberto'
                            lista[y][x].draw(screen)


                msg = fraseBot(lista)

                placar1 = fontgrande.render(str(plaranja), False, LARANJA)
                placarx = fontgrande.render('X', False, (255, 255, 255))
                placar2 = fontgrande.render(str(proxo), False, ROXO)
                placar3 = fontgrande.render(str(pverde), False, VERDENEON)
                pygame.draw.rect(screen, BEGE, (janelaw - 260, 30, 280, 100))
                screen.blit(placar1, (janelaw - 260, 30))
                screen.blit(placarx, (janelaw - 210, 30))
                screen.blit(placar2, (janelaw - 160, 30))
                screen.blit(placarx, (janelaw - 110, 30))
                screen.blit(placar3, (janelaw - 60, 30))
            if temporizador == 0:
                vez+=1
                if vez==3:
                    vez=0
                temporizador = VEZ
            if vez==0:
                timer1 = fontgrande.render(str(temporizador), True, LARANJA)
            elif vez==1:
                timer1 = fontgrande.render(str(temporizador), True, ROXO)
            else:
                timer1 = fontgrande.render(str(temporizador), True, VERDENEON)
            pygame.draw.rect(screen, BEGE, (janelaw - 220, 250, 250, 100))
            screen.blit(timer1, (janelaw - 220, 250))
            clock.tick(60)
            pygame.display.update()



def menu_screen():
    run = True
    clock = pygame.time.Clock()
    BEGE = 71, 74, 81
    while run:
        clock.tick(60)
        screen.fill(BEGE)
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Clique para jogar!!!", 1, (255,0,0))
        screen.blit(text, (janelaw/2 - text.get_width()/2, janelah/2 - text.get_height()/2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main_doistimes()

while True:
    menu_screen()
