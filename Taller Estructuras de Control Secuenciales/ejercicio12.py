#matemáticas
e1=float (input("Ingrese la nota del examen de matemáticas: "))
ne1 = e1*0.9
t1=float (input("Ingrese la nota de la primera tarea de matemáticas: "))
t2=float (input("Ingrese la nota de la segunda tarea de matemáticas: "))
t3=float (input("Ingrese la nota de la tercera tarea de matemáticas: "))
nt = ((t1+t2+t3)/3)*0.1
nfm = ne1+nt

#física
e2=float (input("Ingrese la nota del examen de física: "))
ne2 = e2*0.8
t4=float (input("Ingrese la nota de la primera tarea de física: "))
t5=float (input("Ingrese la nota de la segunda tarea de física: "))
nt2 = ((t4+t5)/2)*0.2
nff =ne2+nt2

#química
e3=float (input("Ingrese la nota del examen de química: "))
ne3 = e3*0.85
t6=float (input("Ingrese la nota de la primera tarea de química: "))
t7=float (input("Ingrese la nota de la segunda tarea de química: "))
t8=float (input("Ingrese la nota de la tercera tarea de química: "))
nt3 = ((t6+t7+t8)/3)*0.15
nfq = ne3+nt3

print ("La nota final de matemáticas es: ",nfm)
print ("La nota final de física es: ",nff)
print ("La nota final de química es: ",nfq)

#promedio materias
pm = (nfm+nff+nfq)/3
print ("El promedio de la tres materias es: ",pm)