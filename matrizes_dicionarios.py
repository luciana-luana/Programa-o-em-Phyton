#exercicio 6.1.
def is_contained(a,b): 
    for i in a:
        if a.count(i)>b.count(i):
            return False
    return True
  
#exercicio 6.2.

def remadj(xs):
    if not xs:
        return []
    
    ys = [xs[0]]  
    for i in range(1, len(xs)):
        if xs[i] != xs[i - 1]:
            ys.append(xs[i])
    return ys

#exercicio 6.3.



