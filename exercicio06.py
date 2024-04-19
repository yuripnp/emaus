# o que são listas em python
# --------------------------
# a primeira lista
nomes = ['fulano', 'ciclano', 'beltrano', 'ecrano', 'altrano', 'deltrino'] # 0, 1, 2
#print(nomes)

# acessando elementos de uma lista

# o primeiro
print(nomes[0])

# o ultimo e penultimo
print(nomes[-1], nomes[-2])

# de um até o outro
print(nomes[0:3])
print(nomes[1:4])
print(nomes[0:-1])

# adicionando elementos de uma lista
nomes.append('Yuri')
print(nomes)
# numero de elementos de uma lista
print(len(nomes))
# inserir elemento em uma lista em uma posição especifica
nomes.insert(1, 'Yan')
print(nomes)
# remover elementos de uma lista de uma determinado conteudo
nomes.remove('Yuri')
print(nomes)
# remove e retorna o ultimo elemento de uma lista
ultimo = nomes.pop()
print(ultimo)
print(nomes)
# retorna o indice do primeiro elemento com o valor especifico
print(nomes.index('fulano'))
# retorna o numero de vezes que aquele elemento aparece em uma lista
print(nomes.count('fulano'))
# ordena a lista
print(nomes.sort())
# nome completo e dividir para transformar em lista
nome = "Fulano da Silva Nunes"
lista = nome.split()
print(lista)
# uma frase inteira e transformar em lista
outro_nome = "Yuri"
print(list(outro_nome))


