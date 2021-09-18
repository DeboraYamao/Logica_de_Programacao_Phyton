'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
'''

valor = float(input("Digite o valor da sua hora: "))
horas = float(input("Digite as horas trabalhadas no mês: "))

print(f'O salário a receber no mês: {(valor*horas):.2f}')
