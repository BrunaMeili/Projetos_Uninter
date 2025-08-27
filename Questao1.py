print('Seja bem vindo(a) à Loja da Bruna! Sou Bruna Meili Linhares e estou à sua disposição.')

valorPedido = float(input('Digite o valor do pedido: '))
quantidadeParcelas = float(input('Digite a quantidade de parcelas que deseja fazer: '))

#Para parcelamentos menores que 3 vezes. os juros são de 0%;
if(quantidadeParcelas < 4):
    juros = (0 / 100)
    valordaParcela = (valorPedido * (1 + juros) / quantidadeParcelas)
    valorTotalParcelado = valordaParcela * quantidadeParcelas
    print(f'Valor da parcela: R$ {valordaParcela}')
    print(f'Valor total parcelado: R$ {valorTotalParcelado}')

#Parcelamentos iguais ou maiores a 4 vezes, porém menores a 6, o acréscimo é de 4%
elif(quantidadeParcelas >= 4 and quantidadeParcelas < 6):
    juros = (4 / 100)
    valordaParcela = (valorPedido * (1 + juros) / quantidadeParcelas)
    valorTotalParcelado = valordaParcela * quantidadeParcelas
    print(f'Valor da parcela: R$ {valordaParcela}')
    print(f'Valor total parcelado: R$ {valorTotalParcelado}')

#Em caso de parcelamento igual ou maior que 6, mas menor que 9 vezes, os juros são de 8%
elif(quantidadeParcelas >= 6 and quantidadeParcelas < 9):
    juros = (8 / 100)
    valordaParcela = (valorPedido * (1 + juros) / quantidadeParcelas)
    valorTotalParcelado = valordaParcela * quantidadeParcelas
    print(f'Valor da parcela: R$ {valordaParcela}')
    print(f'Valor total parcelado: R$ {valorTotalParcelado}')

#Para parcelamentos iguais ou superiores a 9, porém menores que 13 vezes, os juros acrescentados são de 16%
elif(quantidadeParcelas >= 9 and quantidadeParcelas < 13):
    juros = (16 / 100)
    valordaParcela = (valorPedido * (1 + juros) / quantidadeParcelas)
    valorTotalParcelado = valordaParcela * quantidadeParcelas
    print(f'Valor da parcela: R$ {valordaParcela}')
    print(f'Valor total parcelado: R$ {valorTotalParcelado}')

#Por fim, parcelamentos acima de 13 vezes, têm os juros acrescentados em 32%
else:
    if(quantidadeParcelas >= 13):
        juros = (32 / 100)
        valordaParcela = (valorPedido * (1 + juros) / quantidadeParcelas)
        valorTotalParcelado = valordaParcela * quantidadeParcelas
        print(f'Valor da parcela: R$ {valordaParcela}')
        print(f'Valor total parcelado: R$ {valorTotalParcelado}')
