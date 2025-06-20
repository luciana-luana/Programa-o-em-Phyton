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
    
#exercicio 5.10
def pascal(n):
    linha = [1] #começa a lista contendo apenas um número 
    for k in range(1, n + 1):
        coef = linha[-1] * (n + 1-k) // k
        linha.append(coef)#adiciona o coeficiente recém-calculado à lista
    return linha

#exercicio 5.11
def anagramas (txt1,tx2):
        if st(txt1) == len(tx2):
            return True
        else:
            return False

def anagramas(txt1, txt2):
    # Remove espaços, sinais e torna tudo minúsculo
    txt1 = ''.join(c.lower() for c in txt1 if c.isalpha())
    txt2 = ''.join(c.lower() for c in txt2 if c.isalpha())

    # Compara se as letras e suas quantidades são iguais
    if sorted(txt1) == sorted(txt2):
        return True
    else:
        return False
