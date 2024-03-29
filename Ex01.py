# idade = input("Digite a idade: ")

class Ex01():

    def testarIdade(self):
        idade = input("Digite a idade: ")
        print(self.maior_idade(idade))

    def maior_idade(self, idade):
      if int(idade) > 18:
        return "Maior de 18 anos"
      elif int(idade) < 18:
        return "Menor de 18"
      else:
        return "Igual a 18"


def calculaMedia():
    lista = []
    for i in range(5):
        aluno = input("Digite o nome do aluno: ")
        for i in range(3):
            nota = float(input("Digite  nota {}: ".format(i + 1)))
            lista.append(nota)

        media = sum(lista) / 3

        if float(media) >= 7:
            print("{} está Aprovado!".format(aluno))
        else:
            print("{} está Reprovado!".format(aluno))


# calculaMedia()


# teste unitario, feito por Bruno #

import unittest


class ex01Test(unittest.TestCase):

    def test_idade_maior(self):
        calc = Ex01()

        resultado = calc.maior_idade(19)

        self.assertEqual(resultado, "Maior de 18 anos")

    def test_idade_menor(self):
      calc = Ex01()

      resultado = calc.maior_idade(9)

      self.assertEqual(resultado, "Menor de 18")

    def test_idade_igual(self):
      calc = Ex01()

      resultado = calc.maior_idade(18)

      self.assertEqual(resultado, "Igual a 18")
