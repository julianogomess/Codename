#a=int(input())
i=0
# coding: utf-8


#while i < l.__len__():
#   b=input()
#  l.append(b)
# i = i+1
#print(l)

def colocaMaisculo(l):
    for x in range(l.__len__()):
        l[x] = l[x].upper()
    return l


def remove_repetidos(l):
    lista = l
    i = 0
    while i < len(lista):
        j = i + 1
        while j < len(lista):
            if lista[j] == lista[i]:
                del(lista[j])
            else:
                j = j + 1
        i = i + 1
    return sorted(lista)



def gerar():
    l = []
    arquivo = open('palavras.txt', 'r')
    l = arquivo.readlines()
    for x in range(len(l)):
        l[x] = l[x].rstrip("\n")
    arquivo.close()
    l = colocaMaisculo(l)
    l = remove_repetidos(l)
    return l

x = gerar()

def ler():
    l = gerar()
    arquivo = open('palavras.txt','w')
    for x in l:
        msg = x + '\n'
        arquivo.write(msg)
    arquivo.close()

ler()
