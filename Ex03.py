class Calculadora:

  def soma(self, n1, n2):
    return  n1+n2

  def subtracao(self, n1, n2):
    return n1-n2

  def multiplicaco(self, n1, n2):
    return n1*n2

  def divisao(self, n1, n2):
    return n1/n2

calc=Calculadora()
result= calc.soma(10,2)
print(result)
result= calc.subtracao(10,2)
print(result)
result= calc.multiplicaco(10,2)
print(result)
result= calc.divisao(10,2)
print(result)
