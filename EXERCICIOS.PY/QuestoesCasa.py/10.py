A=[]
B=[]
C=[]

for i in range(10):
  num=int(input('um número inteiro:'))
  num2=int(input('um outro número inteiro:'))
  num3=int(input('um outro número inteiro diferente dos acima:'))
  A.append(num)
  B.append(num2)
  C.append(num3)

D=[]

D=A.copy()
for i in range(len(B)):
  D.insert(i+i+1,B[i])

for i in range(len(A)):
  D.insert(i+i+i+2,C[i])

print(D)