num1=int(input('Digite um numero:'))
num2=int(input('Digite outro numero:'))
print('+ = soma \n- = subtração \n* = multiplicação \n/ = divisão')
operacao=input('Digite a operação:')

if operacao =='+':
  print(num1+num2)

elif operacao=='-':
  print(num1-num2)

elif operacao=='*':
  print(num1*num2)

else:
  print(num1/num2)