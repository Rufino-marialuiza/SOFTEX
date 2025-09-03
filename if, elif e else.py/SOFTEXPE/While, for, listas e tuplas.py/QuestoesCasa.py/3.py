SomaNotas=0
Lista=[]

for i in range(40):
  nota=float(input('Digite uma nota:'))
  SomaNotas +=nota
  Lista.append(nota)

Media=SomaNotas/40
print(Lista,Media)