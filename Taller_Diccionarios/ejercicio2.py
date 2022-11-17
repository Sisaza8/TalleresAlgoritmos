diccionario= {'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 'Maite': 5} 
l=[]
l2=[]
for i in diccionario:
    l.append(diccionario[i])

for i in l:
    if i not in l2:
        l2.append(i)
print(l2)