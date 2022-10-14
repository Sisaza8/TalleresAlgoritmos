a=int(input("Ingrese el valor de A: "))
b=int(input("Ingrese el valor de B: "))
c=int(input("Ingrese el valor de C: "))
d=int(input("Ingrese el valor de D: "))
if (d==0):
    s=(a-c)**2
elif (d>0):
    s=((a-b)**3)/d
print("El resultado final es:",s)