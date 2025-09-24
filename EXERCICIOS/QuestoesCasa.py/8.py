A=[]
soma=0
for i in range(10):
  num=int(input('um número inteiro:'))
  A.append(num)

for i in range(len(A)):
  quadrado= A[i]**2
  soma+= quadrado

print(soma)