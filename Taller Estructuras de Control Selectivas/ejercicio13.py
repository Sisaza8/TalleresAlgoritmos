from re import M


d=int(input("Ingrese el día de su nacimiento "))
m=int(input("Ingrese el mes de su nacimiento "))
s=""
if(m==11 and (d>=22 and d<=30)) or (m==12 and (d>=1 and d<=21)):
    s="Sagitario"
    print (s)
elif(m==12 and (d>=22 and d<=31)) or (m==1 and (d>=1 and d<=20)):
    s="Capricornio"
    print (s)
elif(m==1 and (d>=21 and d<=31)) or (m==2 and (d>=1 and d<=19)):
    s="Acuario"
    print (s)
elif(m==2 and (d>=20 and d<=29)) or (m==3 and (d>=1 and d<=19)):
    s="Piscis"
    print (s)
elif(m==3 and (d>=21 and d<=31)) or (m==4 and (d>=1 and d<=20)):
    s="Aries"
    print (s)
elif(m==4 and (d>=21 and d<=30)) or (m==5 and (d>=1 and d<=21)):
    s="Tauro"
    print (s)
elif(m==5 and (d>=22 and d<=31)) or (m==6 and (d>=1 and d<=21)):
    s="Géminis"
    print (s)
elif(m==6 and (d>=22 and d<=30)) or (m==7 and (d>=1 and d<=22)):
    s="Cáncer"
    print (s)
elif(m==7 and (d>=23 and d<=31)) or (m==8 and (d>=1 and d<=23)):
    s="Leo"
    print (s)
elif(m==8 and (d>=24 and d<=31)) or (m==9 and (d>=1 and d<=22)):
    s="Virgo"
    print (s)
elif(m==9 and (d>=23 and d<=30)) or (m==10 and (d>=1 and d<=22)):
    s="Libra"
    print (s)
elif(m==10 and (d>=23 and d<=31)) or (m==11 and (d>=1 and d<=21)):
    s="Escorpión"
    print (s)