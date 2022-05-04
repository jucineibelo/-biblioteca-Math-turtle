'''
2. Faça um programa que pergunte a idade de uma pessoa, se a idade for
menor do que 16 o programa dirá que ela não pode votar e nem dirigir, se
for maior ou igual a 16 e menor que 18 o programa dirá que ela pode votar
mas não dirigir, e se for maior ou igual a 18 o programa dirá que ela pode
votar e dirigir.
'''

nome = input("Insira seu nome? ")
idade = int(input("Qual sua idade? "))

if idade < 16:
    print(nome,"Infelizmente você ainda não pode votar e dirigir!")
elif (idade >= 16) and (idade < 18):
    print(nome,"Você já pode votar, entretanto ainda não pode dirigir! ")
elif (idade >= 18) and (idade <60):
    print(nome,"Você já pode votar e dirigir!")
elif idade >= 60:
    print(nome,"Voce está na terceira idade e o voto para você é opcional.")

