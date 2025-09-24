listaTotal=[]
listaPar=[]
listaImpar=[]

for i in range(20):
  num=int(input('Digite um número inteiro:'))
  listaTotal.append(num)
  if num%2==0:
    listaPar.append(num)
  else:
    listaImpar.append(num)

print(listaTotal,listaPar,listaImpar)