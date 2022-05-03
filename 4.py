"""
4. Faça um programa em Python que solicite ao usuário 2 valores inteiros. Após
isso calcule a tangente da raiz quadrada do resto da divisão do primeiro valor
pelo segundo valor. Apresente além do resultado final, os arredondamentos,
para cima e para baixo, relativos ao mesmo. Utilize variáveis do tipo int para
entrada e float para saída. Veja o exemplo:

"""
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
import math
raiz = math.sqrt(n1%n2)
tangente = math.tan(raiz)
print("- O valor da tangente (da raiz(do resto da divisão(",n1, "por",n2,"=",round(tangente,2))
print("- Arredondamento para cima =", math.ceil(tangente))
print("- Arredondamento para baixo =", math.floor(tangente))



