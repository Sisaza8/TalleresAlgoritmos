sb=int(input("Ingrese el sueldo del trabajador: $"))
if (sb<900000):
    a = (sb*0.15)
elif (sb>900000):
    a = (sb*0.12)
st = a+sb
print("El salario total del trabajador es: $",st)