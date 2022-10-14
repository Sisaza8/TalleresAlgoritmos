m=float(input("Ingrese el monto de la compra que desea realizar: $"))
if(m<50000):
    tp=m
elif(m>=50000 and m<=100000):
    tp=m-(m*0.05)
elif(m>100000 and m<=700000):
    tp=m-(m*0.11)
elif(m>700000 and m<=1500000):
    tp=m-(m*0.18)
elif(m>1500000):
    tp=m-(m*0.25)
print ("El valor a pagar será: ",tp)