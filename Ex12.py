
maior = 0

valor1 = int(input("Digite 1º valor: "))
valor2 = int(input("Digite 2º valor: "))
if valor1 > maior:
  maior = valor1

if valor2 == valor1:
  print("Valor inválido!")

if valor2 > maior:
  maior = valor2

print("O maior é: ", maior)
