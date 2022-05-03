"""
1. Faça um programa em Python que solicite ao usuário três valores inteiros. Após
isso calcule a raiz quadrada do primeiro valor elevado a potência do segundo
valor, elevado a potência do terceiro valor. Utilize variáveis do tipo float. Veja o
exemplo: ((2
"""

n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
n3 = float(input("Digite o terceiro valor: "))

import math
potencia = math.pow(n1,n2)
potencia = math.pow(potencia,n3)
resultado = math.sqrt(potencia)
print(resultado)

