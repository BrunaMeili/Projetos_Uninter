print('Seja bem vindo à nossa loja de camisetas! Sou Bruna Meili Linhares e estou aqui para ajudá-lo(a):')
#Inicio com a definição dos modelos de camisetas.
def escolha_modelo():
    while True:
        modelo = input('Nossas opções de modelo disponíveis são: \n Camiseta Manga Curta Simples (MCS) \n Camiseta Manga Longa Simples (MLS) \n Camiseta Manga Curta Com Estampa (MCE) \n Camiseta Manga Longa Com Estampa (MLE) \n Digite o código do modelo (MCS/MLS/MCE/MLE): ')
        if modelo == 'MCS':
            valor = 1.80
            return valor
        elif modelo == 'MLS':
            valor = 2.10
            return valor
        elif modelo == 'MCE':
            valor = 2.90
            return valor
        elif modelo == 'MLE':
            valor = 3.20
            return valor
        else:
            print('Opção Inválida! Digte MCS, MLS, MCE ou MLE de acordo com a tabela de opções: ')
modelo_valor = escolha_modelo()
#Definição do número de camisetas, utilizando o "int" para que não haja erros na digitação
#Também foi inserido o valor de desconto para determinadas quantidades de camiseta. Menos de 20 peças, não há desconto
#Entre 20 a 200: desconto de 5%; 200 a 2000: desconto de 7%; 2000 a 20000: desconto de 12%
def num_camisetas():
    while True:
        try:
            qtd_camisetas = int(input('Quantas camisetas deseja comprar? '))
            if qtd_camisetas > 20000:
                print('Quantidade inválida! O número de camisetas precisa ser de 1 a 20000 unidades.')
                continue
            elif qtd_camisetas < 20:
                return qtd_camisetas
            elif 20 <= qtd_camisetas < 200:
                return qtd_camisetas * (5 / 100)
            elif 200 <= qtd_camisetas < 2000:
                return qtd_camisetas * (7 / 100)
            elif 2000 <= qtd_camisetas < 20000:
                return qtd_camisetas * (12 / 100)
        except:
            print("Quantidade inválida! Por favor, digite um número inteiro.")
desconto = num_camisetas()
#Definição do valor do frete, onde foi utilizado o "int" para que não haja erro de digitação do cliente.
def frete():
    while True:
        try:
            frete = int(input('As formas de envio são: \n 0 - Retirar no local = Grátis \n 1 - Envio por transportadora = R$ 100,00 \n 2 - Envio por Sedex = R$ 200,00 \n Selecione uma dessas opções: '))
            if frete == 0:
                total_frete = 0
            elif frete == 1:
                total_frete = 100
            elif frete == 2:
                total_frete = 200

            return total_frete
        except:
            print('Opção inválida! Por favor, digite uma das opções disponíveis (0, 1 ou 2): ')
frete = frete()
total_pagar = (modelo_valor * desconto) + frete
print('Este é o valor total de sua compra: R$ {:.2f}'.format(total_pagar))
