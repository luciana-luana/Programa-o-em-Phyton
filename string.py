
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