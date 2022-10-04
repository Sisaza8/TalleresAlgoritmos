Algoritmo ejercicio15
	Definir n,centenas,residuo,decenas,unidades Como Entero
	Escribir "Ingrese un numero con 2 o más digitos";
	Leer n;
	c<-trunc(n/100)
	r<-n MOD 100
	d<-trunc(r/10)
	u<-r MOD 10
	Escribir "El número invertido es: " ,u,d,c;
FinAlgoritmo
