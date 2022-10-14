d=int(input("Ingrese la cantidad de dinero que quiere desglosar: $"))
if(d>=100000):
    q=d//100000
    print ("Existen " + str (q) + " billetes de $100000")
    d=d%100000
if(d>=50000):
    q=d//50000
    print ("Existen " + str (q) + " billetes de $50000")
    d=d%50000
if(d>=20000):
    q=d//20000
    print ("Existen " + str (q) + " billetes de $20000")
    d=d%20000
if(d>=10000):
    q=d//10000
    print ("Existen " + str (q) + " billetes de $10000")
    d=d%10000
if(d>=5000):
    q=d//5000
    print ("Existen " + str (q) + " billetes de $5000")
    d=d%5000
if(d>=2000):
    q=d//2000
    print ("Existen " + str (q) + " billetes de $2000")
    d=d%2000
if(d>=1000):
    q=d//1000
    print ("Existen " + str (q) + " billetes de $1000")
    d=d%1000
if(d>=500):
    q=d//500
    print ("Existen " + str (q) + " monedas de $500")
    d=d%500
if(d>=200):
    q=d//200
    print ("Existen " + str (q) + " monedas de $200")
    d=d%200
if(d>=100):
    q=d//100
    print ("Existen " + str (q) + " monedas de $100")
    d=d%100
if(d>=50):
    q=d//50
    print ("Existen " + str (q) + " monedas de $50")
    d=d%50