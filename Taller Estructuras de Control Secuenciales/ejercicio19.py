x=int (input("Ingrese la cantidad de naranjas que compró: "))
y=int (input("Ingrese el valor de la docena de naranjas: "))
k=int (input("Ingrese los ingresos por venta del lote: "))
cu = y/12
vl = x*cu
pg = (100*(k/vl))-100
print ("El porcentaje de ganancia es: ",pg,"%")