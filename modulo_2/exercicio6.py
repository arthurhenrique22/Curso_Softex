def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        anoatual = str(input(msg))
        if anoatual.isnumeric():
            valor = int(anoatual)
            ok = True
        else:
            print('ERRO! Digite um número válido entre 1922 a 2022.')
        if ok:
            break
    return valor

def leiaInt2(msg):
    ok = False
    valor = 0
    while True:
        anonasc = str(input(msg))
        if anonasc.isnumeric():
            valor = int(anonasc)
            ok = True
        else:
            print('ERRO! Digite um número válido entre 1922 a 2022.')
        if ok:
            break
    return valor


nome = input('Digite seu nome completo: ')
anoatual = leiaInt('Digite o ano atual: ')
while anoatual < 1922 or anoatual > 2022:
    anoatual = int(input('Invalido, digite um numero entre 1922 a 2022: '))


anonasc = leiaInt2('Digite o ano que você nasceu: ')
while anonasc < 1922 or anoatual > 2022:
    anonasc = int(input('Invalido, digite um numero entre 1922 a 2022: '))

print(f'{nome}, idade: ', anoatual - anonasc)
