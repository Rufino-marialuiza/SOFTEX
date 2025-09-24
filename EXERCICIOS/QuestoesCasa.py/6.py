lista=[]
somaNum=0
multipNum=1

for i in range(50):
  num=int(input('Digite um número:'))
  lista.append(num)
  somaNum+=num
  multipNum*=num

print(lista)
print(somaNum,multipNum)