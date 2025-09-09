maior='0'

for i in range(5):
  num=int(input('Número:'))

  if maior=='0':
    maior=num
  if num>maior:
    maior=num

print(maior)