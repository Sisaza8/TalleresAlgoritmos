e1=float (input("Ingrese la primera nota parcial: "))
e2=float (input("Ingrese la segunda nota parcial: "))
e3=float (input("Ingrese la tercera nota parcial: "))
np1 = ((e1+e2+e3)/3)*0.55
ef=float (input("Ingrese la nota del examen final: "))
np2 = ef*0.3
tf=float (input("Ingrese la nota del trabajo final: "))
np3 = tf*0.15
nf = np1+np2+np3
print ("La nota final en la materia de computación es: ",nf)