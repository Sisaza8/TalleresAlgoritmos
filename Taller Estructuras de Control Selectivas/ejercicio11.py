t=float(input("Ingrese la temperatura en Fahrenheit: "))
d=""
if (t>85):
    d="Natación"
elif (t>70 and t<=85):
    d="Tenis"
elif (t>=33 and t<=70):
    d="Golf"
elif (t>10 and t<33):
    d="Esquí"
elif (t<10):
    d="Marcha"
print(d)