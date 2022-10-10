ck=int (input("Ingrese el costo por kilovatio: "))
lp=int (input("Ingrese la lectura anterior: "))
la=int (input("Ingrese la lectura actual: "))
tk = ((lp-la)**2)**0.5
tp = ck*tk
print ("El total a pagar de energía durante el mes es: $",tp)