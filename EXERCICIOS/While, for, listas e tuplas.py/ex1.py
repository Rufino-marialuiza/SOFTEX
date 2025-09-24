cont=0
soma=0

while cont==0:
  num=int(input('Número:'))
  soma+=num

  if num==0:
    cont=1

print(soma)