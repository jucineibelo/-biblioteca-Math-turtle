"""
2. Faça um programa em Python que solicite ao usuário três valores inteiros. Após
isso calcule o seno do primeiro valor elevado a potência do segundo valor
somado com a raiz quadrada do terceiro valor. Utilize variáveis do tipo float. Veja
o exemplo:
"""
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
n3 = float(input("Digite o terceiro valor: "))
import math
potencia = math.pow(n1,n2)
raiz = math.sqrt(n3)
seno = math.sin(potencia+raiz)
print(round(seno,2))
