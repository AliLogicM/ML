import random
import string
import math
import copy

def GenerarI(individuo):                #genera individuos a 4 posiciones
    for i in range(4):
        a= random.randint(0,1)
        individuo.append(a)
    return individuo

def fitness(x,f):               #genera fitness 
    a=x-5
    b=2+(math.sin(x))
    f=abs(a/b)
    return f

def pSel(f1,t,psel):        #genea probabilidad de seleccion
    psel= f1/t
    return psel

def selPadre(pAcum):
    valor=[]
    V1= random.random()
    print("el valor random es: ",V1)
    for i in range(5):
        if pAcum[i] >= V1:
            valor.append(i)
    return valor[0]

def cruza(i1,i2):
    aux= random.randint(0,3)
    print("el punto de cruce al azar es: ",aux)
    i1[aux], i2[aux] =i2[aux], i1[aux]
    h1=i1
    h2=i2
    return h1,h2

def mutar(hijos,pm):
    aux=[]
    for i in range(4):
        a= random.random()
        aux.append(a)
    print("el arreglo generado al azar para la mutacion es: ",aux)
    for i in range(4):
        if aux[i] <= pm:
            print("La poscicion",i,"del arreglo es menor que Pm = 0.1, por lo que se mutará el hijo")
            if hijos[i]==0:
                hijos[i]=1
            else:
                hijos[i]=0          
    return hijos
    
def seleccion(fh0,fh1,fp0,fp1):
    lista=[fh0,fh1,fp0,fp1]
    lista.sort(reverse=True)  # Ordenarla de forma inversa
    top_dos = lista[:2]  # Y capturar los 10 primeros elementos
    return top_dos

#declaracion de variables
individuo0= []              #inicializacion de individuos vacios
individuo1= []
individuo2= []
individuo3= []
individuo4= []
individuos=[]
pc= 0.85
pm= 0.1
f0= 0
f1= 0 
f2= 0
f3= 0 
f4= 0
fg=[]
t= 0
psel0= 0
psel1= 0
psel2= 0
psel3= 0
psel4= 0
pAcum=[]
vp1= 0
vp2= 0
hijos=[]
np=[]

#realiza la funcion para gener los 5 individuos
print("====poblacion inicial====")
GenerarI(individuo0)    
GenerarI(individuo1)
GenerarI(individuo2)
GenerarI(individuo3)
GenerarI(individuo4)
print("El individuo 0 es: ",individuo0 )    
print("El individuo 1 es: ",individuo1 )    
print("El individuo 2 es: ",individuo2 )
print("El individuo 3 es: ",individuo3 )
print("El individuo 4 es: ",individuo4 )
individuos.append(individuo0)
individuos.append(individuo1)
individuos.append(individuo2)
individuos.append(individuo3)
individuos.append(individuo4)
individuosC=copy.copy(individuos)
individuosD=copy.copy(individuos)

#convierte de arreglo a string, para posteriormente convertir a decimal
num0=(str(individuo0[0])+str(individuo0[1])+str(individuo0[2])+str(individuo0[3]))   
num1=(str(individuo1[0])+str(individuo1[1])+str(individuo1[2])+str(individuo1[3]))
num2=(str(individuo2[0])+str(individuo2[1])+str(individuo2[2])+str(individuo2[3]))
num3=(str(individuo3[0])+str(individuo3[1])+str(individuo3[2])+str(individuo3[3]))
num4=(str(individuo4[0])+str(individuo4[1])+str(individuo4[2])+str(individuo4[3]))

#genera la conversion de binario a decimal   ||  Genotipo 
n0=int(str(num0), 2)            
n1=int(str(num1), 2)
n2=int(str(num2), 2)
n3=int(str(num3), 2)
n4=int(str(num4), 2)
print("El numero 0 es: ",n0)
print("El numero 1 es: ",n1)
print("El numero 2 es: ",n2)
print("El numero 3 es: ",n3)
print("El numero 4 es: ",n4)

#se obtiene f(x) para cada individuo
f0= fitness(n0,f0)
f1= fitness(n1,f1)
f2= fitness(n2,f2)
f3= fitness(n3,f3)
f4= fitness(n4,f4)
fg.append(f0)
fg.append(f1)
fg.append(f2)
fg.append(f3)
fg.append(f4)
fg2=copy.copy(fg)
print("el fitness de num 0 es: ", f0)
print("el fitness de num 1 es: ", f1)
print("el fitness de num 2 es: ", f2)
print("el fitness de num 3 es: ", f3)
print("el fitness de num 4 es: ", f4)
t= f0+f1+f2+f3+f4

#generamos probabilidad de selecccion 
psel0=pSel(f0,t, psel0)
psel1=pSel(f1,t, psel1)
psel2=pSel(f2,t, psel2)
psel3=pSel(f3,t, psel3)
psel4=pSel(f4,t, psel4)
print("la probabilidad de Seleccion del individuo 0 es: ",psel0)
print("la probabilidad de Seleccion del individuo 1 es: ",psel1)
print("la probabilidad de Seleccion del individuo 2 es: ",psel2)
print("la probabilidad de Seleccion del individuo 3 es: ",psel3)
print("la probabilidad de Seleccion del individuo 4 es: ",psel4)

#generamos probabilidad acumulada
pAcum0= psel0
pAcum1= pAcum0+psel1
pAcum2= pAcum1+psel2
pAcum3= pAcum2+psel3
pAcum4= pAcum3+psel4
pAcum.append(pAcum0)
pAcum.append(pAcum1)
pAcum.append(pAcum2)
pAcum.append(pAcum3)
pAcum.append(pAcum4)
print("la probabilidad de Seleccion Acumulada del individuo 0 es: ",pAcum0)
print("la probabilidad de Seleccion Acumulada del individuo 1 es: ",pAcum1)
print("la probabilidad de Seleccion Acumulada del individuo 2 es: ",pAcum2)
print("la probabilidad de Seleccion Acumulada del individuo 3 es: ",pAcum3)
print("la probabilidad de Seleccion Acumulada del individuo 4 es: ",pAcum4)

## Seleccion de padres
print("")
print("GENERACION 1----------------------------------------------------------------------")
vp1=selPadre(pAcum)
print("El padre 1 es el individuo numero ",vp1,"con valor: ", individuos[vp1])
vp2=selPadre(pAcum)
while vp2==vp1:             # mientras valor padre 2 es igual a vp1 seguira iterando otro resultado
    vp2=selPadre(pAcum)
print("El padre 2 es el individuo numero ",vp2,"con valor: ", individuos[vp2])
p1=copy.copy(individuos[vp1])
p2=copy.copy(individuos[vp2])

#cruza
print("")
pac=random.random()
print("el numero aleatorio de cruza es: ",pac)
if pac <= pc:
    print("El numero aleatorio cruza es menor que la probabilidad de cruza (",pc,"), por lo que se genera la cruza: ")
    hijos=cruza(individuos[vp1],individuos[vp2])
    print("el hijo 1 es: ", hijos[0]) 
    print("el hijo 2 es: ", hijos[1])
else:
    print("El numero aleatorio cruza es menor que la probabilidad de cruza, por lo que NO se genera la cruza ")
    hijos=individuos[vp1],individuos[vp2]
    print("Los padres pasan a la siguiente generacion (",hijos,")")
 
#Mutacion
print("")
print("para",hijos[0],": ")
mutar(hijos[0],pm)
print("para",hijos[1],": ")
mutar(hijos[1],pm)
print("los hijos resultantes son: ",hijos)

#seleccion || reemplazo
print("")
fh0=0
fh1=0
numh0=(str(hijos[0][0])+str(hijos[0][1])+str(hijos[0][2])+str(hijos[0][3]))
nh0=int(str(numh0), 2) 
numh1=(str(hijos[1][0])+str(hijos[1][1])+str(hijos[1][2])+str(hijos[1][3]))
nh1=int(str(numh1), 2) 
fh0=fitness(nh0,fh0)      #fitness de hijo 0
fh1=fitness(nh1,fh1)      #fitness de hijo 1
print("el fitnes de los padres son: ",fg[vp1],fg[vp2])
print("el fitnes de los hijos son: ",fh0,fh1)
aux=seleccion(fh0,fh1,fg[vp1],fg[vp2])
np.append(aux[0])
np.append(aux[1])

provi=[]
print("los individuos que pasan a la siguiente generacion son: ",np)
for i in range(len(np)):
    if np[i]==fh0:
        provi.append(hijos[0])
        print("el fitness de hijo 0 pasa!!!! ",hijos[0])
    elif np[i]==fh1:
        provi.append(hijos[1])
        print("el fitness de hijo 1 pasa!!!! ",hijos[1])
    elif np[i]==fg[vp1]:
        provi.append(p1)
        print("el fitness de padre 1 pasa!!!! ",p1)
    elif np[i]==fg[vp2]:
        provi.append(p2)
        print("el fitness de padre 2 pasa!!!! ",p2)
print("la poblacion actual es:",provi)
print("")

#generacion 2----------------------------------------------------------------------
## Seleccion de padres
print("GENERACION 2 ------------------------------------------------------------------")
vp3=selPadre(pAcum)
print("El padre 1 es el individuo numero ",vp3,"con valor: ", individuosC[vp3])
vp4=selPadre(pAcum)
while vp3==vp4:             # mientras valor padre 2 es igual a vp1 seguira iterando otro resultado
    vp4=selPadre(pAcum)
print("El padre 2 es el individuo numero ",vp4,"con valor: ", individuosC[vp4])
p3=copy.copy(individuosC[vp3])
p4=copy.copy(individuosC[vp4])

#cruza
print("")
pac2=random.random()
print("el numero aleatorio de cruza es: ",pac2)
if pac2 <= pc:
    print("El numero aleatorio cruza es menor que la probabilidad de cruza (",pc,"), por lo que se genera la cruza: ")
    hijos2=cruza(individuosC[vp3],individuosC[vp4])
    print("el hijo 1 es: ", hijos2[0]) 
    print("el hijo 2 es: ", hijos2[1])
else:
    print("El numero aleatorio cruza es menor que la probabilidad de cruza, por lo que NO se genera la cruza ")
    hijos2=individuosC[vp3],individuosC[vp4]
    print("Los padres pasan a la siguiente generacion (",hijos2,")")
 
#Mutacion
print("")
print("para",hijos2[0],": ")
mutar(hijos2[0],pm)
print("para",hijos2[1],": ")
mutar(hijos2[1],pm)
print("los hijos resultantes son: ",hijos2)

#seleccion || reemplazo
print("")
fh3=0
fh4=0
numh3=(str(hijos2[0][0])+str(hijos2[0][1])+str(hijos2[0][2])+str(hijos2[0][3]))
nh3=int(str(numh3), 2) 
numh4=(str(hijos2[1][0])+str(hijos2[1][1])+str(hijos2[1][2])+str(hijos2[1][3]))
nh4=int(str(numh4), 2) 
fh3=fitness(nh3,fh3)      #fitness de hijo 0
fh4=fitness(nh4,fh4)      #fitness de hijo 1
print("el fitnes de los padres son: ",fg2[vp3],fg2[vp4])
print("el fitnes de los hijos son: ",fh3,fh4)
aux2=seleccion(fh3,fh4,fg2[vp3],fg2[vp4])
np2=[]
np2.append(aux2[0])
np2.append(aux2[1])
provi2=[]
print("los individuos que pasan a la siguiente generacion son: ",np2)
for i in range(len(np2)):
    if np2[i]==fh3:
        provi2.append(hijos2[0])
        print("el fitness de hijo 0 pasa!!!! ",hijos2[0])
    elif np2[i]==fh4:
        provi2.append(hijos2[1])
        print("el fitness de hijo 1 pasa!!!! ",hijos2[1])
    elif np2[i]==fg2[vp3]:
        provi2.append(p3)
        print("el fitness de padre 1 pasa!!!! ",p3)
    elif np2[i]==fg2[vp4]:
        provi2.append(p4)
        print("el fitness de padre 2 pasa!!!! ",p4)
print("la poblacion actual es:",provi2)
print("")

#generacion 3----------------------------------------------------------------------
## Seleccion de padres
print("GENERACION 3 ------------------------------------------------------------------")
vp5=selPadre(pAcum)
print("El padre 1 es el individuo numero ",vp5,"con valor: ", individuosD[vp5])
vp6=selPadre(pAcum)
while vp5==vp6:             # mientras valor padre 2 es igual a vp1 seguira iterando otro resultado
    vp6=selPadre(pAcum)
print("El padre 2 es el individuo numero ",vp6,"con valor: ", individuosD[vp6])
p5=copy.copy(individuosD[vp5])
p6=copy.copy(individuosD[vp6])
print(individuosD)

#cruza
print("")
pac3=random.random()
print("el numero aleatorio de cruza es: ",pac3)
if pac3 <= pc:
    print("El numero aleatorio cruza es menor que la probabilidad de cruza (",pc,"), por lo que se genera la cruza: ")
    hijos3=cruza(individuosD[vp5],individuosD[vp6])
    print("el hijo 1 es: ", hijos3[0]) 
    print("el hijo 2 es: ", hijos3[1])
else:
    print("El numero aleatorio cruza es menor que la probabilidad de cruza, por lo que NO se genera la cruza ")
    hijos3=individuosD[vp5],individuosD[vp6]
    print("Los padres pasan a la siguiente generacion (",hijos3,")")

#Mutacion
print("")
print("para",hijos3[0],": ")
mutar(hijos3[0],pm)
print("para",hijos3[1],": ")
mutar(hijos3[1],pm)
print("los hijos resultantes son: ",hijos3)

#seleccion || reemplazo
print("")
fh5=0
fh6=0
numh5=(str(hijos3[0][0])+str(hijos3[0][1])+str(hijos3[0][2])+str(hijos3[0][3]))
nh5=int(str(numh5), 2) 
numh6=(str(hijos3[1][0])+str(hijos3[1][1])+str(hijos3[1][2])+str(hijos3[1][3]))
nh6=int(str(numh6), 2) 
fh5=fitness(nh5,fh5)      #fitness de hijo 0
fh6=fitness(nh6,fh6)      #fitness de hijo 1
print("el fitnes de los padres son: ",fg2[vp5],fg2[vp6])
print("el fitnes de los hijos son: ",fh5,fh6)
aux3=seleccion(fh5,fh6,fg2[vp5],fg2[vp6])
np3=[]
np3.append(aux3[0])
np3.append(aux3[1])
provi3=[]
print("los individuos que pasan a la siguiente generacion son: ",np3)
for i in range(len(np3)):
    if np3[i]==fh5:
        provi3.append(hijos3[0])
        print("el fitness de hijo 0 pasa!!!! ",hijos3[0])
    elif np3[i]==fh6:
        provi3.append(hijos3[1])
        print("el fitness de hijo 1 pasa!!!! ",hijos3[1])
    elif np3[i]==fg2[vp5]:
        provi3.append(p5)
        print("el fitness de padre 1 pasa!!!! ",p3)
    elif np3[i]==fg2[vp6]:
        provi3.append(p6)
        print("el fitness de padre 2 pasa!!!! ",p4)
print("la poblacion actual es:",provi3)
print("")

print("===== POBLACION FINAL: =====")
finalP=[]
finalP.append(provi[0])
finalP.append(provi[1])
finalP.append(provi2[0])
finalP.append(provi2[1])
finalP.append(provi3[0])
print(finalP[0])
print(finalP[1])
print(finalP[2])
print(finalP[3])
print(finalP[4])
