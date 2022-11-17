usuarios={
    "iperurena": {
        "nombre": "Iñaki",
        "apellido": "Perurena",
        "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
        "apellido": "Muguruza",
        "password": "654321"
    },
    "aolaizola": {
        "nombre": "Aimar",
        "apellido": "Olaizola",
        "password": "123456"
    }
}

for i in range(1,4):
    u=input("Escriba su usuario: ")
    c=input("Escriba su password: ")
    if u in usuarios and c == usuarios[u]['password']:
        print("Bienvenido", usuarios[u]['nombre'], usuarios[u]['apellido'])
    else:
        print("Usuario y/o clave no identificado, intente de nuevo")