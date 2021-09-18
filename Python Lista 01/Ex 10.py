'''
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
'''

C = float(input("Digite a temperatura em graus Celsius: "))

F = (C * ( 9 / 5 )) + 32

print(f'{C:.2f} graus Celsius é {F:.2f} graus Farenheit')
