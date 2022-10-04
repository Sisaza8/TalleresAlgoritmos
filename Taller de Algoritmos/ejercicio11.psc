Algoritmo ejercicio11
	Escribir "Escriba la nota del primer parcial";
	Leer p1;
	Escribir "Escriba la nota del segundo parcial";
	Leer p2;
	Escribir "Escriba la nota del tercer parcial";
	Leer p3;
	Escribir "Escriba la nota del parcial final";
	Leer pf;
	Escribir "Escriba la nota del trabajo final";
	Leer tf;
	pn<-((p1+p2+p3)/3)*0.55
	pfn<-pf*0.3
	tfn<-tf*0.15
	nf<-pn+pfn+tfn
	Escribir "La nota final de algoritmos es: " ,nf;
FinAlgoritmo
