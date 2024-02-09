#calculadora para converter a idade de cachorro em idade humana.
#fórmula: Idade de cachorro = (logaritmo natural * 16) + 31
#fonte: www.biorxiv.org/content/10.1101/829192v1.full

idadecao = int(input('Por favor, digite a idade de seu cachorro: '))

ln1, ln2, ln3, ln4, ln5, ln6, ln7, ln8, ln9, ln10, ln11, ln12, ln13, ln14, ln15, ln16, ln17 = \
0.0, 0.69, 1.09, 1.38, 1.60, 1.79, 1.94, 2.07, 2.19, 2.30, 2.39, 2.48, 2.56, 2.63, 2.70, 2.77, 2.83

if idadecao == 1:
    print(f'A idade de seu cachorro em relação aos humanos é: {(ln1 * 16) + 31:.0f} anos.')
elif idadecao == 2:
    print(f'A idade de seu cachorro em relação aos humanos é: {(ln2 * 16) + 31:.0f} anos.')
elif idadecao == 3:
    print(f'A idade de seu cachorro em relação aos humanos é: {(ln3 * 16) + 31:.0f} anos.')
elif idadecao == 4:
    print(f'A idade de seu cachorro em relação aos humanos é: {(ln4 * 16) + 31:.0f} anos.')
elif idadecao == 5:
    print(f'A idade de seu cachorro em relação aos humanos é: {(ln5 * 16) + 31:.0f} anos.')
elif idadecao == 6:
    print(f'A idade de seu cachorro em relação aos humanos é: {(ln6 * 16) + 31:.0f} anos.')
elif idadecao == 7:
    print(f'A idade de seu cachorro em relação aos humanos é: {(ln7 * 16) + 31:.0f} anos.')
elif idadecao == 8:
    print(f'A idade de seu cachorro em relação aos humanos é: {(ln8 * 16) + 31:.0f} anos.')
elif idadecao == 9:
    print(f'A idade de seu cachorro em relação aos humanos é: {(ln9 * 16) + 31:.0f} anos.')
elif idadecao == 10:
    print(f'A idade de seu cachorro em relação aos humanos é: {(ln10 * 16) + 31:.0f} anos.')
elif idadecao == 11:
    print(f'A idade de seu cachorro em relação aos humanos é: {(ln11 * 16) + 31:.0f} anos.')
elif idadecao == 12:
    print(f'A idade de seu cachorro em relação aos humanos é: {(ln12 * 16) + 31:.0f} anos.')
elif idadecao == 13:
    print(f'A idade de seu cachorro em relação aos humanos é: {(ln13 * 16) + 31:.0f} anos.')
elif idadecao == 14:
    print(f'A idade de seu cachorro em relação aos humanos é: {(ln14 * 16) + 31:.0f} anos.')
elif idadecao == 15:
    print(f'A idade de seu cachorro em relação aos humanos é: {(ln15 * 16) + 31:.0f} anos.')
elif idadecao == 16:
    print(f'A idade de seu cachorro em relação aos humanos é: {(ln16 * 16) + 31:.0f} anos.')
elif idadecao == 17:
    print(f'A idade de seu cachorro em relação aos humanos é: {(ln17 * 16) + 31:.0f} anos.')
else:
    print('Por favor, digite uma idade entre 1 e 17 anos.')


#modo simplificado
"""ln1 = 0.0
ln2 = 0.69
ln3 = 1.09
ln4 = 1.38
ln5 = 1.60
ln6 = 1.79
ln7 = 1.94
ln8 = 2.07
ln9 = 2.19
ln10 = 2.30
ln11 = 2.39
ln12 = 2.48
ln13 = 2.56
ln14 = 2.63
ln15 = 2.70
ln16 = 2.77
ln17 = 2.83

valores_ln = [0.0, 0.69, 1.09, 1.38, 1.60, 1.79, 1.94, 2.07, 2.19, 2.30, 2.39, 2.48, 2.56, 2.63, 2.70, 2.77, 2.83]

# Obter a idade do cachorro do usuário
idadecao = int(input('Digite a idade do seu cachorro: '))

# Verificar se a idade está no intervalo válido
if 1 <= idadecao <= len(valores_ln):
    print(f'A idade canina é {(valores_ln[idadecao-1] * 16) + 31:.0f}')
else:
    print('Por favor, digite uma idade entre 1 e 17.')"""
