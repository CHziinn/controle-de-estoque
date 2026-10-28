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

def seletor():
    while True:
        escolha = input('Selecione dentre as opções 1/2/3/4: ')

        if escolha == '1':
            cadastrar_produto()

        elif escolha == '2':
            excluir_produto()

        elif escolha == '3':
            visualizacao()

        elif escolha == '4':
            modificar_estoque()

        if escolha == '0':
            print('Fechando..')
            break


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
    return menu

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

def modificar_estoque():
   while True:
    busca = int(input('Digite o Id do produto registrado para modifica-lo: '))
    id_encontrado = False

    for produto in produtos:
        if produto['id'] == busca:
            id_encontrado = True 
            
            print(f"Produto encontrado: {produto['nome']}")
            print('1 - Id')
            print('2 - Nome')
            print('3 - Categoria')
            print('4 - Preço')
            print('5 - Quantidade')

            mod = input('Selecione a opção desejada para modificar: ')

            if mod == '1':
                new_id = int(input('Digite o novo Id: '))
                produto['id'] = new_id

            elif mod == '2':
                new_nome = input('Digite o novo nome: ')
                produto['nome'] = new_nome

            elif mod == '3':
                new_categoria = input('Digite a nova categoria: ')
                produto['categoria'] = new_categoria

            elif mod == '4':
                new_price = float(input('Digite o novo preço: '))
                produto['preco'] = new_price

            elif mod == '5':
                new_quant = int(input('Digite a nova quantia: '))
                produto['quantidade'] = new_quant   

            salvar_produtos()
            print("Produto atualizado com sucesso!")
            
            escolha = input('Deseja modificar outro produto (Y/N)? ')
            if escolha.lower() == 'y':
                break
            else:
                return seletor()
                
    if not id_encontrado:
        print('Produto não encontrado.\n')


while True:
    print ('0 - Fechar')
    print ('1 - Cadastrar produto')
    print ('2 - Remover produto')
    print ('3 - Visualizar estoque')
    print ('4 - Modificar produtos')

    menu = seletor()