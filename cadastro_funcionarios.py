
#Aqui eu crio a função onde iremos cadastrar os funcionários. O copy serve para evitar referências diretas
def cadastrar_funcionario(id):
    global lista_funcionarios
    print(f'ID do funcionario: {id}')
    nome = input('Digite o nome do funcionário: ').upper().strip()
    setor = input('Digite o nome do setor onde o funcionário trabalha: ').upper().strip()
    salario = float(input('Digite o salário recebido pelo funcionário: '))
    dados = {'id': id, 'nome': nome, 'setor': setor, 'salario': salario,}
    lista_funcionarios.append(dados.copy())
#Aqui é a função para consultar o funcionário, apresentando 3 opções de consulta e a opção de retorno para o menu principal
def consultar_funcionario():
    while True:
        print("-----CONSULTAR FUNCIONÁRIO-----\n 1 - Consultar todos\n 2 - Consultar por ID\n 3 - Consultar por Setor\n 4- Voltar ao menu principal")
        opcao = int(input('\n Digite a opção desejada: '))
    # As opções de consulta são "Consultar todos", onde aparecem todos os funcionários
        if opcao == 1:
            print()
            for dicionario in lista_funcionarios:
                for chave in dicionario:
                    print(f'{chave.upper()}: {dicionario[chave]}')
                print()
        # Consulta por ID, onde aparece apenas o funcionário que utiliza o ID pesquisado
        elif opcao == 2:
            id_consulta = int(input('Digite o ID do funcionário: '))
            for funcionario in lista_funcionarios:
                if (funcionario['id'] == id_consulta):
                    for chave in funcionario:
                        print(f'{chave.upper()}: {funcionario[chave]}')
                    print()
                else:
                    break
        # Consulta por setor, onde aparecem todos os funcionários de determinado setor
        elif opcao == 3:
            consultar_funcionario = input('Digite o nome do setor do funcionário: ').upper().strip()
            print()
            for dicionario in lista_funcionarios:
                if (consultar_funcionario == dicionario['setor']):
                    for chave in dicionario:
                        print(f'{chave.upper()}: {dicionario[chave]}')
                    print()
        elif opcao == 4:
            return
        else:
            print('Opção inválida! Digite uma das opções válidas (1, 2, 3 ou 4): ')
#Aqui faço a função para remover um funcionário do catálogo
def remover_funcionario():
    while True:
        id_procurado = int(input('Qual o ID do funcionário que deseja remover?: '))
        encontrou = False
        for funcionario in lista_funcionarios:
            if funcionario['id'] == id_procurado:
                lista_funcionarios.remove(funcionario)
                encontrou = True
                print('Funcionário removido com sucesso!')
        if not encontrou:
            print('Id inválido')
            continue
        else:
            break
#Esta é a função do menu principal
print('Seja bem vindo(a) à empresa de Bruna Meili Linhares!')
#Lista criada utilizando como variável o meu RU
lista_funcionarios = []
id_global = 5289844
while True:
    menu_principal = int(input('-----MENU PRINCIPAL-----\n 1 - Cadastrar funcionário\n 2 - Consultar funcionário\n 3 - Remover funcionário\n 4 - Sair\n -------------------------\n Digite a opção desejada: '))
    if menu_principal == 1:
        cadastrar_funcionario(id_global)
        id_global += 1
        print()
    elif menu_principal == 2:
        consultar_funcionario()
        print()
    elif menu_principal == 3:
        remover_funcionario()
        print()
    elif menu_principal == 4:
        break
    else:
        print('Opção inválida! Por favor digite uma das opções (1, 2, 3 ou 4): ')
