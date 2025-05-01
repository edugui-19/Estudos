# Proposta para o mini-projeto: Criar um programa que possibilite ao usuário a escolha de seu nome
## deve apresentar diálogos pré-montados e aleatórios contendo o nome fornecido
## utiliza os conceitos aprendidos de: Estruturas de repetição, manipulação do git, estruturas condicionais e funções
import random

#--FUNÇÃO DE VALIDAÇÃO DO USUÁRIO
def validacao(nickname):
    return nickname.replace(" ", "").isalpha()


#--FUNÇÃO RANDOMIZADORA DE DIÁLOGO
def dialogoRandomizador(nickname):
    nickname = nickname.title()
    return [
        f"Você sabia, {nickname}? Este pequeno código foi feito por Eduarda Guilherme... "
        "Ela apenas estava curiosa sobre como poderia utilzar algumas coisinhas que aprendeu no seu primeiro mês "
        "estudando python.",                                                                 #FRASE 1

        f"{nickname}, você sabe falar inglês? Se não, posso te ensinar uma coisa ou duas.",  #FRASE 2

        f"Espero que {nickname} tenha tomado um bom café da manhã hoje.",                    #FRASE 3

        nickname.upper() + "!"                                                               #FRASE 4
    ]
    

#--DEFINIÇÃO DO USUÁRIO
nickname = input("Bem-Vindo ao Nickname Dialogues!\nPara prosseguir, defina um nome de usuário: ")

while not validacao(nickname):
    nickname = input("\nDesculpe, mas seu nome pode conter apenas letras.\nTente novamente: ")
nickname = nickname.title()


#--INÍCIO DA DINÂMICA
dialogoLib = dialogoRandomizador(nickname)
print("\nPerfeito! Já podemos começar a conversar.\nVou te mostrar as opções disponíveis:\n")

opcao = -1
while opcao != 0:
    try:
        opcao = int(input("[1] Continuar falando\n[2] Trocar nome\n[0] Encerrar\n"))

        if opcao == 1:
            print(random.choice(dialogoLib))

        elif opcao == 2:
            nickname = input("Ok, podemos mudar seu nome! Qual a sua nova escolha? ")
            while not validacao(nickname):
                nickname = input("\nDesculpe, mas seu nome pode conter apenas letras.\nTente novamente: ")
            nickname = nickname.title()
            print(f"{nickname} é um belo nome!")
            dialogoLib = dialogoRandomizador(nickname)

        elif opcao == 0:
            print(f"Até mais, {nickname}!")

    except ValueError: print("\nPor favor, insira uma opção válida.")
