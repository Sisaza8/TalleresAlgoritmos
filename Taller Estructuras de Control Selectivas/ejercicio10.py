sb=int(input("Ingrese el salario bruto del trabajador: $"))
c=1
if(sb>4300000 and sb<=5000000):
    x=c
    a=sb+(sb*0.1)
    print("El salario con su respectivo aumento es: $",a,"y es categoria",x)
elif(sb>3600000 and sb<=4300000):
    x=c+1
    a=sb+(sb*0.15)
    print("El salario con su respectivo aumento es: $",a,"y es categoria",x)
elif(sb>2000000 and sb<=3600000):
    x=c+2
    a=sb+(sb*0.2)
    print("El salario con su respectivo aumento es: $",a,"y es categoria",x)
elif(sb>900000 and sb<=2000000):
    x=c+3
    a=sb+(sb*0.4)
    print("El salario con su respectivo aumento es: $",a,"y es categoria",x)
elif(sb<=900000):
    x=c+4
    a=sb+(sb*0.6)
    print("El salario con su respectivo aumento es: $",a,"y es categoria",x)