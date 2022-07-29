# Para executar o programa, atribuia valor as variaveis

rodas = 4

pesobruto = 6001

pessoas = 4

if 1 < rodas <= 3:
    print('Veículos com duas ou três rodas, tem a habilitação do tipo A')

elif rodas == 4 and pesobruto <= 3500 and pessoas <= 8:
    print('Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg,tem a habilitação do tipo B')

elif rodas >= 4 and 3500 <= pesobruto <= 6000:
    print('Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg, tem a habilitação do tipo C')

elif rodas >= 4 and pessoas > 8:
    print('Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas, tem a habilitação do tipo D')

elif rodas >= 4 and pesobruto > 6000:
    print('Veículos com quatro rodas ou mais e com mais de 6000 kg, tem a habilitação do tipo E')
