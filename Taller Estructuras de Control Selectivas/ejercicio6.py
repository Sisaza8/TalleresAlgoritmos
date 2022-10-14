a=int(input("Ingrese el primer digito del numero: "))
b=int(input("Ingrese el segundo digito del numero: "))
c=int(input("Ingrese el tercer digito del numero: "))
d=int(input("Ingrese el cuarto digito digito del numero: "))
n=(a*1000)+(b*100)+(c*10)+(d)
s=100-((c*10)+(d))
r=(c*10)+(d)
if (c>=5):
    x=n+s
elif (c<5):
    x=n-r
print("El numero",n,"se aproxima a:",x)