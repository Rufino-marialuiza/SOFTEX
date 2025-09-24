n=int(input('Digite n:'))
i=1
pares=[]

while i<=n:
    if i%2==0:
        pares.append(i)
    i+=1

print(pares)