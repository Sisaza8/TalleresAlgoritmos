ci=int(input("Ingrese la cantidad de dinero invertido en el banco: $"))
ti=float(input("Ingrese la tasa de interes que maneja el banco: %"))
ti2 = ti/100
i = ci*ti2
if (i>100000):
    print("Los intereses alcanzados son: $",i,"y superan los $100.000")
elif (i<100000):
    print("Los intereses alcanzados son: $",i,"y no superan los $100.000")
ct = ci+i
print("El total de dinero en la cuenta de banco es: $",ct)