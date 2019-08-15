lista=[]
for i in range(3):
  nota =float (input("Informe a {}ª nota: " .format(i+1)))
  lista.append(nota)

media = sum(lista)/3

if (media >= 7):
  print("Aprovado!")
else:
  print("Reprovado!")
