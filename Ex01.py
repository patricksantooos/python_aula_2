#idade = input("Digite a idade: ")

class Ex01():

  def testarIdade(self):
    idade = input("Digite a idade: ")
    if int(idade) > 18:
      print("Maior de 18 anos")
    elif int(idade) < 18:
      print("Menor de 18")
    else:
      print("Igual a 18")

  testarIdade()

def calculaMedia():
  lista = []
  for i in range(5):
    aluno = input("Digite o nome do aluno: ")
    for i  in range(3):
      nota = float(input("Digite  nota {}: ".format(i+1)))
      lista.append(nota)

    media = sum(lista)/3

    if float(media) >= 7:
      print("{} está Aprovado!".format(aluno))
    else:
      print("{} está Reprovado!".format(aluno))

#calculaMedia()
