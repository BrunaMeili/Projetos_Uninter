print('-' * 5 + 'Seja bem vindo(a) à Loja de Marmitas! Sou Bruna Meili Linhares e abaixo seguem as opções do dia' + '-' * 5)
print('-' * 49 + 'Cardápio' + '-' * 48)
print('-' * 105)
print('-' * 22 + '|  Tamanho  |' + '  Bife acebolado (BA)  |' + '  Filé de frango (FF)  |' + '-' * 22)
print('-' * 22 + '|     P     |' + '        R$16,00        |' + '        R$15,00        |' + '-' * 22)
print('-' * 22 + '|     M     |' + '        R$18,00        |' + '        R$17,00        |' + '-' * 22)
print('-' * 22 + '|     G     |' + '        R$22,00        |' + '        R$21,00        |' + '-' * 22)
print('-' * 105)

valor_total = 0

while True:
    #Para não haver erros, foi colocado o código de uppercase, assim o usuário digita conforme está descrito.
    #A string com input é para que não haja erro no código, já que não será necessária a entrada de números.

    sabor = str(input('Digite o sabor, sendo BA para Bife Acebolado ou FF para Filé de Frango: '))
    sabor = sabor.upper()
    if sabor != "BA" and sabor != "FF":
        print('Sabor inválido, por favor, tente novamente.')
        continue

    tamanho = str(input('Digite o tamanho desejado (P, M ou G): '))
    tamanho = tamanho.upper()
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('Tamanho inválido, por favor, tente novamente.')
        continue

    #Aqui utiliza-se o elif, já que há mais de duas opções.

    if sabor == 'BA':
        if tamanho == 'P':
            print('Você selecionou Bife acebolado do tamanho pequeno no valor de R$16,00.')
            valor_total = valor_total + 16
        elif tamanho == 'M':
            print('Você selecionou Bife acebolado do tamanho médio no valor de R$18,00.')
            valor_total = valor_total + 18
        else:
            print('Você selecionou Bife acebolado do tamanho grande no valor de R$22,00.')
            valor_total = valor_total + 22

    if sabor == 'FF':
        if tamanho == 'P':
            print('Você selecionou Filé de frango do tamanho pequeno no valor de R$15,00.')
            valor_total = valor_total + 15
        elif tamanho == 'M':
            print('Você selecionou Filé de frango do tamanho médio no valor de R$17,00.')
            valor_total = valor_total + 17
        else:
            print('Você selecionou Filé de frango do tamanho grande no valor de R$21,00.')
            valor_total = valor_total + 21

    #Aqui é para caso o usuário deseje mais de um produto, assim ele pode prosseguir com o pedido na seleção de carnes.
    #Também foi adicionado o uppercase, para que o usuário digite as opções conforme o descrito, sem gerar erros.

    outro_pedido = str(input('Deseja mais alguma coisa? Digite S para sim ou N para encerrar o pedido: '))
    outro_pedido = outro_pedido.upper()
    if outro_pedido == 'N':

        break

print('O valor do pedido foi de: R$ {:.2f}'.format(valor_total))