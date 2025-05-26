arroz=1
agua=1
sal=1
cebola=1
alho=1
azeite=1
list_de_ing=[arroz,agua,sal,cebola,alho,azeite]

def fazerArroz():
    panela(list_de_ing)
    fogao()
    servir()
    #return ("arroz pronto a comer")

def panela (x):
    for ing in x:
        print ("coloquei ingrediente na panela")
    print("está pronta para colocar no fogao")
    
def fogao ():
    print ("coloquei a panela no fogão")
    
def servir ():
    print("o arroz está pronto")
    print("bom apetite!!")