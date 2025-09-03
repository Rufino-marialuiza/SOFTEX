idades=[]
alturas=[]

for i in range(10):
  idade=int(input('Idade:'))
  altura=float(input('Altura:'))
  idades.append(idade)
  alturas.append(altura)

print(idades[alturas.index(max(alturas))])