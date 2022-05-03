'''
6. Faça um programa em Python utilizando a biblioteca fractions, para determinar o
resultado da multiplicação entre as frações: 1/2 x 3/2 x 6/7 x 9/3 = ?
'''

import fractions

a = fractions.Fraction(1, 2)
b = fractions.Fraction(3, 2)
c = fractions.Fraction(6, 7)
d = fractions.Fraction(9, 3)

resultado = a * b * c * d

print(resultado)
