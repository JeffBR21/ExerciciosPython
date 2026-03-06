
n1 = int(input(print('Qual o primeiro numero: ')))
opm = str(input(print('Qual o operador matematico(+)(-)(*)(/): ')))
n2 = int(input(print('Qual o segundo numero: ')))

if(opm == '+'):
    print(f'O resultado da operação de {n1} + {n2} é',n1 + n2)
elif(opm == '-'):
    print(f'O resultado da operação de {n1} - {n2} é',n1 - n2)
elif(opm == '*'):
    print(f'O resultado da operação de {n1} * {n2} é',n1 * n2)
elif(opm == '/'):
    print(f'O resultado da operação de {n1} / {n2} é',n1 / n2)
else:
    print('Operação invalida!!!')