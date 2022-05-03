'''
Faça um programa em Python que solicite ao usuário o valor dos catetos oposto
(CO) e adjacente (CA) para um dado triangulo retângulo. Após o armazenamento
destes dois valores, calcule e apresente o valor da hipotenusa deste triangulo.
Apresente, também, o valor da hipotenusa arredondado para cima e para baixo.
Veja o exemplo:
'''
import math
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
hipotenusa = math.hypot(n1, n2)
print("Hipotenusa Calculada: ",round(hipotenusa,2))
print("Arredondado para Cima",math.ceil(hipotenusa))
print("Arredondado para Baixo",math.floor(hipotenusa))




