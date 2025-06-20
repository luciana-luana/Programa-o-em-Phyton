
#exercicio 4.1.
def conta_letras (txt):
    
    contador = 0
    for c in txt:
            contador += 1
             #txt='Olá Mundo'
    return contador
    
#exercicio 4.2.
def apenas_letras(txt): #true ou false
    return txt.isalpha()

#exercicio 4.3.
def filtra_letras(txt):
    letras=''
    for i in txt:
        if i.isalpha(): #verifica se o caracter é uma letra
            letras+=i
    return letras


#exercicio 4.4.  
def inversa(txt):
    return txt[::-1]
    
#exercicio 4.5.
def palindromo (txt):
    return inversa(txt).upper()==txt.upper() #retorna a função inversa

#exercicio 4.6.
def filtra_letras(txt):
    letras=''
    for i in txt:
        if i.isalpha(): #verifica se o caracter é uma letra
            letras+=i
    return letras

def palindromo_geral(txt):
    txt_filtrado=filtra_letras(txt).lower()
    return txt_filtrado == txt_filtrado[::-1]

#exercicio 4.7.
def rem_espacos(txt):
        txt = txt.replace('  ', ' ')  # substitui dois por um
    return txt

#exercicio 4.8.

#exercicio 4.9.

#exercicio 4.10.

def media (xs):
    return soma (xs)/len(xs)
    
    
def soma (sequencia):
    resultado=0
    for i in sequencia:
        resultado=resultado+i
    return resultado

def produto (xs):
    total=1
    for x in xs:
        total=total * x 
    return total 

def maximo (xs):
    maior=xs[0]
    for x in xs [1:]:
        maior=max(maior,x)
    return maior

def elimrep1(xs):
    ys=[]
    for x in xs:
        if not (x in ys):
            ys.append(x)
    return ys

def elimrep2(xs):
    i=0
    while i<len(xs):
        if xs[i] in xs[0:i]:
            del xs[i]
        else:
            i=i+1



