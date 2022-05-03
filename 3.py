"""
3. Faça um programa em Python que solicite ao usuário 4 valores inteiros. Após
isso efetue o seguinte cálculo: logaritmo na base 10 da raiz quadrada do
primeiro valor somado ao quarto elevado a potência do segundo valor somado
ao terceiro. Utilize variáveis do tipo float. Veja o exemplo:
"""

n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
n3 = float(input("Digite o terceiro valor: "))
n4 = float(input("Digite o terceiro valor: "))
import math
raiz = math.sqrt(n1+n4)
potencia = math.pow(raiz,n2+n3)
resultadoLog = math.log(10,potencia)
print(round(resultadoLog,2))
