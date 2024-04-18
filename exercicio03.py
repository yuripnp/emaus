# outros tipos de variaveis: bool, list, dict, tuplas, sets, 

# boolean - digas seus medos
sim = True
nao = False
sentenca_01 = 3 > 2
sentenca_02 = 100 >= 100
sentenca_03 = 10 < 9.99999
sentenca_04 = 23 == 23

print(sentenca_01)
print(sentenca_02)
print(sentenca_03)

#---------------------------------------------------------------
# é verdadeiro ou falso ?

expressao = ((3 * 2) + (6 - 2)) == ((2 + 2 + 1) * 2)

nome = "Fulano"
outro_nome = "Ciclano"
texto = nome

print(expressao)
print(id(nome) == id(outro_nome))
print(type(nome) == type(outro_nome))
print(id(nome) == id(texto))
#----------------------------------------------------------------

# listas - coloque em uma lista tudo que tem em um sanduiche e imprima
ingredientes = ["carne", "salada", "bacon", "queijo"]

print("Os ingredientes para o seu sanduiche é ")
print(ingredientes)

#------------------------------------------------
# liste todos os ingredientes separadamente
print(ingredientes[0])
print(ingredientes[3])
# ------------------------------------------------
# tire um ingrediente

print(" desculpe, pode tirar a " + ingredientes[1])

#------------------------------------------------
# dicionário alunos na sala
alunos = {1: "fulano", 2: "ciclano", 3: "beltrano", 4: "alfrano"}
print(alunos)
print(alunos[1])
print(alunos.get("fulano"))
