'''
Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
  C = (5 * (F-32) / 9).
'''

F = float(input("Digite a temperatura em graus Farenheit: "))

C = (5 * (F-32) / 9)

print(f'{F:.2f} graus Farenheit é {C:.2f} graus Celsius')
