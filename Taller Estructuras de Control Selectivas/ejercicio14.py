i=int(input("Ingrese la lectura del mes pasado de energía: "))
f=int(input("Ingrese la lectura del mes actual de energía: "))
x=abs(i-f)
if(x<=100):
    pf=x*4600
elif(x>=101 and x<=300):
    pf=x*80000
elif(x>=301 and x<=500):
    pf=x*100000
elif(x>501):
    pf=x*120000
print ("El total a pagar de energía en el mes será: $",pf)