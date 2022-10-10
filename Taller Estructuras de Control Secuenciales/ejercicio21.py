pc=int (input("Ingrese el precio de compra al contado de computadores: "))
vp=int (input("Ingrese el precio de compra de un computador: "))
cc=int (input("Ingrese la cantidad de cuotas: "))
vc=int (input("Ingrese el valor de la cuota: "))
pc2 = (100/cc)
vcp = (vc*cc)+vp
vcps = (pc*pc2)+pc
print ("El porcentaje de cada cuota es: ",pc2)
print ("El valor de compra de un computador a cuotas es: ",vcp)
print ("El precio de compra de varios computadores a cuotas es: ",vcps)