A=[]
B=[]

for i in range(10):
  num=int(input('um número inteiro:'))
  num2=int(input('um outro número inteiro:'))
  A.append(num)
  B.append(num2)

C=[]

C=A.copy()
for i in range(len(B)):
  C.insert(i+i+1,B[i])

print(C)