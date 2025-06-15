def elimrep2(xs):
    i=0
    while i<len(xs):
        if xs[i] in xs[0:i]:
            del xs[i]
        else:
            i=i+1

#Matriz-lista dentro de uma lista
for i in [0,1,2]:
    for j in [0,1,2]:
        print(i,j)
    print()


def listas_iguais(xs: list, ys: list) -> int:
  for i in range(len(xs)):
    if xs[i] != ys[i]:
        return i
  return -1

def soma_parcial(lista:list,n:int)-> int:
    soma = 0
    for i in range(0, n+1):
        soma += lista[i]
    return soma

#exercicio 5.4

def intervalo (xs,a,b):
    contagem=0
    for x in xs:
        if a<=x <=b:
            contagem=contagem + 1
    return contagem

#exercício 5.5
def segundoMaior(l) -> int:
    ordem = list(set(l))         
    ordem.sort(reverse=True)      
    if len(ordem) < 2:
        return None               
    return ordem[1]

#exercicio 5.6
def ocorrencias (txt,c):
    ys=[]
    for i in range(len(txt)):
        if txt[i] ==c:
            ys.append(i)
    return ys

#exercicio 5.8
def repetidos (lista):
    ys=[]
    for i in lista:
        if i in ys:
            return True
        ys.append(i)
    return False

#exercicio 5.9
def palavras(txt):
    ys=[]
    lista = ''
    for i in txt:
        if i.isalpha():
            lista += i
        else:
            if lista != '':
                ys.append(lista)
                lista=''
    if lista != '':
        ys.append(lista)
    return ys
