
# O tipo Lista pode sofrer alterações
lista = [1,2,3,4,5,6]
print(type(lista))

# Imprime os valores da lista * 4
for l in lista:
    print(l*4)

lista.append('Casa')

for l in lista:
    print(l)


# Criando objetos do tipo tupla    
tup = (1,2,3,4)
print(type(tup))
# Imprime os valores da Tupla. OBS a tupla é imutavél
for t in tup:
    print(t)


