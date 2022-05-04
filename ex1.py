'''
1. Construa um programa que receba como entrada a altura e o sexo de uma
pessoa (letra F para Feminino e letra M para Masculino) Em seguida
calcule e escreva o peso ideal dessa pessoa, utilizando as seguintes
fórmulas
 para homens:(72.7 * altura) - 58;
 para mulheres:(62.1 * altura) - 44.7;
'''

sexo = input("Insira letra F para Feminino e letra M para Masculino: ")
altura = float(input("Digite a altura? "))

if sexo == "F":
    print("Seu peso ideal é: ",(62.1 * altura) - 44.7,2)
elif sexo == "M":
    print("Seu peso ideal é: ",(72.7 * altura) - 58)



