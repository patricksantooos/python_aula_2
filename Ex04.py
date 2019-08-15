valor = float(input("Informe o valor pago:"))
preco = float(input("Informe o preço do produto:"))
desconto = preco*0.10
precoatual = preco - desconto
print("Com desconto de 10% fica:", precoatual)
troco = valor - precoatual
print("Seu troco é: ", troco)

