from random import random, randrange

print("**********************************")
print("Bem vindo ao Jogo de adivinhação!")
print("**********************************")

numer_secreto = randrange(0, 101)
tentativa_total = 0
pontos = 1000

print("Qual nivél de dificuldade ?")
print("(1) Fácil (2) Médio (3) Dificil")

nivel = int(input("Defina o nivél: "))

if nivel == 1:
    tentativa_total = 20
elif nivel == 2:
    tentativa_total = 10
else:
    tentativa_total = 4

print(numer_secreto)

for rodada in range(1, tentativa_total + 1):
    print("Tentativa:  {} de {}".format(rodada, tentativa_total))
    chute_str = input("Digite um numero entre 1 e 100: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)
    if chute < 1 or chute > 100:
        print("Você deve digitar um numero entre 1 e 100!")
        continue

    acertou = numer_secreto == chute
    maior = numer_secreto < chute
    menor = numer_secreto > chute

    if acertou:
        print("Você acetou !")
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if maior:
            print("Seu chute foi maior do que o numero secreto.")
        elif menor:
            print("Seu chute foi menor do que o numero secreto.")
        pontos_perdidos = abs(numer_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim do Jogo")
