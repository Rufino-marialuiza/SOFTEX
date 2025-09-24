valorporHora=int(input('Valor recebido por hora: '))
horasMes=int(input('Quantidade de horas trabalhada no mês:'))

salarioBruto=valorporHora*horasMes
IR=11/100 * salarioBruto
INSS=8/100*salarioBruto
sindicato=5/100*salarioBruto
salarioLiquido=salarioBruto-IR-INSS-sindicato

print('-'*20)
print(f'Salário Bruto: R$ {salarioBruto:.2f}')
print(f'IR (11%): R$ {IR:.2f}')
print(f'INSS(8%): R$ {INSS:.2f}')
print(f'Sindicato(5%): R$ {sindicato:.2f}')
print(f'= Salário Líquido: R$ {salarioLiquido:.2f}')
print('-'*20)