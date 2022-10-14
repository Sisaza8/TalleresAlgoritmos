from math import sqrt


a=float(input("Ingrese el valor de A: "))
b=float(input("Ingrese el valor de B: "))
c=float(input("Ingrese el valor de C: "))
d=(b**2)-(4*a*c)
if(d==0):
    x=(b)/(2*a)
    print ("El resultado para x es:",x)
elif(d>0):
    x1=((-b)+((b**2)-(4*a*c))**0.5)/(2*a)
    x2=((-b)-((b**2)-(4*a*c))**0.5)/(2*a)
    print ("El resultado para x1 es:",x1,"y para x2 es:",x2)
elif(d<0):
    print("No tiene solución para los reales")