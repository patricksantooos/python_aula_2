
lista = []
maior = 0
menor = 500000000
soma=0
for i  in range(10):
  numero = int(input("Digite o {}º  numero : ".format(i+1)))
  lista.append(numero)
  if (numero > maior):
    maior = numero
  if (numero < menor):
    menor = numero
  soma = soma+numero
media = sum(lista)/10
print("Maior: ", maior)
print("Menor: ", menor)
print("Soma: ", soma)
print("Média: ", media)
