sb=int (input("ingrese el sueldo base del vendedor: "))
v1=int (input("ingrese el valor de la primera venta: "))
v2=int (input("ingrese el valor de la segunda venta: "))
v3=int (input("ingrese el valor de la tercera venta: "))
com = (v1+v2+v3)*0.1
st = com+sb
print ("El sueldo base del vendedor es: $",sb)
print ("El valor de la comisión es: $",com)
print ("El sueldo total del vendedor es: $",st)