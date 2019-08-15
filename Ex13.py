sexo=(input("Informe o sexo: "))
maiorHomem = 0
maiorMulher = 0
menorHomem = 500
menorMulher = 555
if sexo == "masculino":
    idadeHomem1 = int(input("Informe a 1ª idade:" ))
    idadeHomem2 = int(input("Informe a 2ª idade: "))
    while idadeHomem1 == idadeHomem2:
      print("Idades iguai inválidaa!")
      break
    if idadeHomem1 > maiorHomem:
      maiorHomem = idadeHomem1
    elif idadeHomem2 > maiorHomem:
      maiorHomem = idadeHomem2
    if idadeHomem1 < menorHomem:
      menorHomem = idadeHomem1
    elif idadeHomem2 < menorHomem:
      menorHomem = idadeHomem2

if sexo == "feminino":
  idadeMulher1 = int(input("Informe a 1ª idade:"))
  idadeMulher2 = int(input("Informe a 2ª idade: "))
  while idadeMulher1 == idadeMulher2:
    print("Idades iguai inválidaa!")
    break
  if idadeMulher1 > maiorMulher:
    maiorMulher = idadeMulher1
  elif idadeMulher2 > maiorMulher:
    maiorMulher = idadeMulher2
  if idadeMulher1 < menorMulher:
    menorMulher = idadeMulher1
  elif idadeMulher2 < menorMulher:
    menorMulher = idadeMulher2

print("Maior idade Homem: " ,maiorHomem)
print("Maior idade Mulher: " ,maiorMulher)
print("Menor idade Masculino: " ,menorHomem)
print("Menor idade Mulher: " ,menorMulher)
print("A soma das idades do Homem mais velho com a mulher mais nova é: ", maiorHomem+menorMulher)
