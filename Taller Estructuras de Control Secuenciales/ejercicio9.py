sb=int (input("Ingrese el sueldo base del trabajador: "))
ph=int (input("Ingrese el precio de una hora trabajada: "))
ch=int (input("Ingrese la cantidad de horas trabajadas: "))
sbd = sb-(sb*0.2)
sh = ph*ch
sn = sbd+sh
print ("El salario neto del trabajador es: $",sn)