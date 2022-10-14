a=int(input("Ingrese la cantidad de piezas a comprar: "))
b=int(input("Ingrese el costo de una pieza: "))
t = a*b
if (t>5000000):
    i=t*0.55
    b=t*0.3
    c=t*0.15
elif (t<=5000000):
    i=t*0.7
    b=0
    c=t*0.3
z=c*0.2
print("El total es de: $",t)
print("La inversión es de: $",i)
print("El prestamo del banco es de: $",b)
print("El credito a pagar es: $",c)
print("El interes por el credito es: $",z)