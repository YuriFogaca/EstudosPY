#Este programa irá calcula os juros compostos baseado em uma % de x parcelas de qualquer valor
class Calculadora:
    def __init__(self, valor1=0.0, valor2=0.0):
        self.valor1= valor1
        self.valor2= valor2

    def calcular(self, quantidadeParcelas):
        valorParcela= (self.valor2)/quantidadeParcelas
        juros= self.valor1
        valorTotal= 0.0
        juros= juros/12 #porcentagem dos juros mensais
        while quantidadeParcelas>0:
            valorTotal= valorTotal + valorParcela
            valorParcela= valorParcela*(1+(juros/100))
            quantidadeParcelas= quantidadeParcelas-1

        return valorTotal


print("Juros: ")
j= float(input())
print("Qual a quantidade de parcelas: ")
q= int(input())
print("Valor do emprestimo: ")
vTotal= float(input())

calculo= Calculadora(j,vTotal) #pensando em valor1 como juros e valor2 como valor total
vTotal= calculo.calcular(q)
print("Valor total à pagar será: ", vTotal)
print("Valor das pacelas em igual: ", vTotal/6)