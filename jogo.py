import random

def adivinha():
    print("Escolhe um número")
    chave=random.randint(0,99)
    i=int(input())
    while i!=chave:
        if i<chave:
            print("Escolhe um número maior")
        else:
            print("Escolhe um número menor")
        i=int(input())
    print("Acertou!!!")


adivinha()