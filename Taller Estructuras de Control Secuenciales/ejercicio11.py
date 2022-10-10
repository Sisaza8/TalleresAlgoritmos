n= input("Ingrese su nombre y apellido: ")
ht= int(input("Ingrese el numero de horas normales trabajadas: "))
ph= float(input("Ingrese el valor de cada hora trabajada: "))
he= int(input("Ingrese el numero de horas extras trabajadas: "))
nhi= int(input("Ingrese el numero de hijos que tiene: "))
s1= ht*ph
phe= (ph*0.25)+ph
hep= he*phe
d= ((s1*0.05)+(s1*0.02)+(s1*0.07))
a= 250000+(nhi*173000)+180000
sf= (s1+hep+a)-d
print("El total de las asignaciones es de: ",a)
print("El total de las deducciones es de: ",d)
print("El sueldo neto para el trabajador ",n," en el mes de Diciembre es de $",sf)