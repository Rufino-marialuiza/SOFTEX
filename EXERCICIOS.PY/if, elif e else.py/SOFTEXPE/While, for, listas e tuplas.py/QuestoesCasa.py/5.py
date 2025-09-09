somaNotas=0
lista=[]
mediaAlta=0

for i in range(10):
  media=0
  for j in range(4):
    nota=float(input('Digite sua nota:'))
    somaNotas+=nota

  media=somaNotas/4
  lista.append(media)
  if media>=7:
    mediaAlta+=1
  else:
    somaNotas=0

print(lista)
print(mediaAlta)