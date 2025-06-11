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
