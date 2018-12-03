# ESTUDOS EM PYTHON SOBRE STRING

frase = input()

print(type(frase))

# Tamanho da Frase
print(len(frase))

# Lower Case
print(frase.lower())

# Quebrar String criando uma Lista
vec = frase.split()

print(vec)

nome = 'Caiua'
sobrenome = 'França'

# Concatenar String
print ("{} {} seja bem vindo ao Sistema!".format(nome, sobrenome))

test = 'lib, lib, lin'

# REPLACE STRING LIB POR LAB
teste2 = test.replace('lib','lab')

print(teste2)