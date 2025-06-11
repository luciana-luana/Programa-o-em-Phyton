
def conta_letras (txt):
    
    contador = 0
    for c in txt:
            contador += 1
             #txt='Olá Mundo'
    return contador
    

def apenas_letras(txt): #true ou false
    return txt.isalpha()

    
def inversa(txt):
    return txt[::-1]
    

def palindromo (txt):
    return inversa(txt).upper()==txt.upper()

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



