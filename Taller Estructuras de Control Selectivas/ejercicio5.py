sv= int(input("Ingrese el salario del vendedor: "))
vt= int(input("Ingrese el numero de ventas totales realizadas por la empresa: "))
d1= int(input("Ingrese el numero de ventas realizadas por el departamento 1: "))
d2= int(input("Ingrese el numero de ventas realizadas por el departamento 2: "))
d3= int(input("Ingrese el numero de ventas realizadas por el departamento 3: "))
b= sv*0.2
f= vt*0.33
if(d1>f and d1<vt):
    sd1=sv+b
elif(d1<f):
    sd1=sv
else:
    print("Ha digitado un numero menor a 0 o un dato incorrecto")
if(d2>f and d2<vt):
    sd2=sv+b
elif(d2<f):
    sd2=sv
else:
    print("Ha digitado un numero menor a 0 o un dato incorrecto")
if(d3>f and d3<vt):
    sd3=sv+b
elif(d3<f):
    sd3=sv
else:
    print("Ha digitado un numero menor a 0 o un dato incorrecto")
ss=sd1+sd2+sd3
print("El salario del vendedor del departamento 1 es igual a:", sd1)
print("El salario del vendedor del departamento 2 es igual a:", sd2)
print("El salario del vendedor del departamento 3 es igual a:", sd3)
print("La suma de los salarios es es igual a:",ss)