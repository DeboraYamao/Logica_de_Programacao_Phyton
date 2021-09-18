caractere = '\u2588'
espaco = " "
n = 0
print()
base = 40
altura = 10
print(caractere * base, end="")
print('\r')
while n < (altura - 2):
	print(caractere, (base -4)* espaco, caractere)
	n = n + 1
print(caractere * base)
