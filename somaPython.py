operacao = int(input(' selecione o tipo de operação (SOMA = 1, SUB = 2, MULT = 3, DIV = 4)'))
print('Entre com os valores')
valorA = int(input('digite o valor da 1 parcela: '))
valorB = int(input('Digite o valor da 2 parcela: '))
resultado = 0

if operacao == 1:
    resultado  = valorA + valorB
elif operacao == 2:
    resultado = valorA - valorB
elif operacao == 3:
    resultado =  valorA * valorB
else:
    resultado =  valorA / valorB

print('O resultado da operação {:.0f} é:'.format(resultado))
