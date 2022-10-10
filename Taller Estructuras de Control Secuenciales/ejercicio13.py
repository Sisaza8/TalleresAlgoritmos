#50.000
n1=int (input("Ingrese la cantidad de billetes de 50.000 que hay en el banco: "))
n1d = n1*50000

#20.000
n2=int (input("Ingrese la cantidad de billetes de 20.000 que hay en el banco: "))
n2d = n2*20000

#10.000
n3=int (input("Ingrese la cantidad de billetes de 10.000 que hay en el banco: "))
n3d = n3*10000

#5.000
n4=int (input("Ingrese la cantidad de billetes de 5.000 que hay en el banco: "))
n4d = n4*5000

#2.000
n5=int (input("Ingrese la cantidad de billetes de 2.000 que hay en el banco: "))
n5d = n5*2000

#1.000
n6=int (input("Ingrese la cantidad de billetes de 1.000 que hay en el banco: "))
n6d = n6*1000

#500
n7=int (input("Ingrese la cantidad de billetes de 500 que hay en el banco: "))
n7d = n7*500

#100
n8=int (input("Ingrese la cantidad de billetes de 100 que hay en el banco: "))
n8d = n8*100

dt = n1d+n2d+n3d+n4d+n5d+n6d+n7d+n8d
print ("El dinero total que hay en el banco es: $",dt)