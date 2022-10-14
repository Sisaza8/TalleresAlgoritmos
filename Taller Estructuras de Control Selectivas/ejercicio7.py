k=float(input("Ingrese la cantidad de kilometros recorridos: "))
f=50000
if (k<=300):
    tp=f
elif (k>300 and k<=1000):
    tp=70000+((k-300)*30000)
elif (k>1000):
    tp=150000+((k-1000)*9000)
print("El total de kilometros es:",k,"y el pago total es: $",tp)