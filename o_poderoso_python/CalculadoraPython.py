operacao = int(input(' selecione o tipo de operação (SOMA = 1, SUB = 2, MULT = 3, DIV = 4)'))
print('Entre com os valores')
valorA = int(input('digite o valor da 1 parcela: '))
valorB = int(input('Digite o valor da 2 parcela: '))

if operacao == 1:
    resultado  = valorA + valorB
elif operacao == 2:
    resultado = valorA - valorB
elif operacao == 3:
    resultado =  valorA * valorB
else:
    if(valorA != 0):
        resultado =  valorA / valorB
    else:
        resultado = 'Não é possivel dividir o numero 0'

print (resultado)
