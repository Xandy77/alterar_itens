# lista de nomes
nomes = ['Fulano', 'Cicrano', 'Beltrano', 'João', 'Maria', 'José']

# exibir a lista e seus respectivos índices
for i in range(len(nomes)):
    print(f'Índice {i}: {nomes[i]}.')

# quebra de linha
print('\n')

try:
    # usuário informa o índice
    indice = int(input('Informe o número do índice: '))

    # faz a alteração
    nomes[indice] = input('Informe o novo nome: ').capitalize()
except:
    print('Não foi possível fazer a alteração.')

# exibe a nova lista
for i in range(len(nomes)):
    print(f'índice {i}: {nomes[i]}.')