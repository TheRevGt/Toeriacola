import math
def unservidor():
    resultado=[]
    print("SISTEMA DE COLAS UN SERVIDOR")
    l=int(input("Ingrese el valor de Lamda: "))
    m=int(input("Ingrese el valor de Miu: "))
    ls=l/(m-l)
    ws=(1/(m-l))
    lq=l**2/(m*(m-l))
    wq=l/(m*(m-l))
    p=l/m
    po=1-(l/m)
    resultado=({"Longitud del sistema:": ls,"Logitud de la cola:": lq,"Tiempo de espera del sistema:": ws,"Tiempo de espera cola:":wq,"Probabilidad de uso:":p,"Probabilidad de no uso:":po})
    print(resultado)
    for _ in range(int(lq)):
        print('☺')
    print("Personas en fila")
    for _ in range(int(ls)):
        print('☺')
    
def spos(s,lm):
    r=0
    for i in range (0,s):
        r+=lm**i/math.factorial(i)
    return r

def vservidores():
    resultado=[]
    print("SISTEMA DE COLAS VARIOS SERVIDOR")
    l=int(input("Ingrese el valor de Lamda: "))
    m=int(input("Ingrese el valor de Miu: "))
    s=int(input("Ingrese el valor de S: "))
    lm=l/m
    po1=spos(s+1,lm)
    po2=1/(1-(l/(s*m)))
    po=1/(po1*po2)
    lq=po*((lm**(s+1))/(math.factorial(s-1)*(s-lm)**2))
    ls=lq+lm
    wq=lq/l
    ws=ls/l
    resultado=({"Longitud del sistema:": ls,"Logitud de la cola:": lq,"Tiempo de espera en sistema:": ws,"Tiempo de espera en cola:":wq,"Probabilidad de no uso:":po})
    print(resultado)
    print("Personas en cola")
    for _ in range(int(lq)):
        print('☺')
    print("Personas en fila")
    for _ in range(int(ls)):
        print('☺')
        

print("TEORIAS DE COLAS")
entrada=input("De un solo servidor (y/n)")
if entrada=="y":
    print(unservidor())
elif entrada=="n":
    print(vservidores())
elif entrada!="y" and entrada!="n":
    print("Ingrese un valor valido")
