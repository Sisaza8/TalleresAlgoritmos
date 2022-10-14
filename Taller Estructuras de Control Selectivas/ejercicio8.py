x="P"
y="Q"
t=x + " y " + y
p=float(input("Ingrese el valor de P: "))
q=float(input("Ingrese el valor de Q: "))
r=(p**3)+(q**4)-(2*(p**2))
if(r>680):
    print(t,"satisfacen la expresión")
elif(r<680):
    print(t,"no satisfacen la expresión")