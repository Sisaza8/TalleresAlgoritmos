l1=int (input("Ingrese el primer lado del triángulo: "))
l2=int (input("Ingrese el segundo lado del triángulo: "))
l3=int (input("Ingrese el tercer lado del triángulo: "))
s = (l1+l2+l3)/2
a = (s*(s-l1)*(s-l2)*(s-l3))**0.5
print ("El área del triángulo es: ",a,"u²")