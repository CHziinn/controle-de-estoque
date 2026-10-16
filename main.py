import json

def carregar_produtos():
    arquivo = open('produtos.json', 'r', encoding='utf-8')
    produtos = json.load(arquivo)
    arquivo.close()
    return produtos

def salvar_produtos(produtos):
    arquivo = open('produtos.json', 'w', encoding= 'utf-8')
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()

produtos = carregar_produtos()

def cadastrar_produto():

    new_id = int(input('Digite a Id: '))
    nome = input('Digite o nome do novo produto: ')
    categoria = input('Digite a nova categoria: ')
    preco = float(input('Digite o preco: '))
    quantia = int(input('DIgite a quantia em estoque: '))

    produtos.append ({
        'id': new_id,
        'nome': nome,
        'categoria': categoria,
        'preco': preco,
        'quantia': quantia
    })

    salvar_produtos(produtos)

def excluir_produto():
    print (produtos)

    old_id = int(input('Digite a Id: '))
    for produto in produtos:
        if produto ['id'] == old_id:
            produtos.remove(produto)
    
    salvar_produtos(produtos)

def visualizacao():
    print ('1 - Estoque Abaixo de 15')
    print ('2 - Estoque Abaixo de 50')
    print ('3 - Estoque Abaixo de 100')

    print('4 - Pesquisa por categoria')

    escolha = input('Escolha dentre 0/1/2/3/4: ')
    if escolha == '1':
        for produto in produtos:
            if produto ['estoque'] <= 15:
                print (produto)
                return visualizacao()

    elif escolha == '2':
        for produto in produtos:
            if produto ['estoque'] <= 50:
                print (produto)
                return visualizacao()



while True:
    print ('0 - Fechar')
    print ('1 - Cadastrar produto')
    print ('2 - Remover produto')
    print ('3 - Visualizar estoque')

    escolha = input('Selecione dentre as opções 1/2/3: ')

    if escolha == '0':
        print('Fechando..')
        break

    elif escolha == '1':
        cadastrar_produto()

    elif escolha == '2':
        excluir_produto()

    elif escolha == '3':
        visualizacao()