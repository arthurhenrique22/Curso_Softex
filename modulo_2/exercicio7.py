x = 0
y = 0
z = 0
branco = 0

while True:
    print('Escolha sua opção de voto: ')
    print('1= Candidato_X'), print('2= Candidato_Y'), print('3= Candidato_X'), print('4-branco.')
    try:
        voto = int(input('Digite seu voto: '))
        if voto == 1:
            x += 1
        elif voto == 2:
            y += 1
        elif voto == 3:
            z += 1
        elif voto == 4:
            branco += 1
        else:
            print('Digite uma opção válida')
            continue

        sair = int(input('1) Fim da votação' ' 2) Continuar a votar:'))
        if sair == 1:
            print(f'Votos Candidato_X foi de: {x}')
            print(f'Votos Candidato_Y foi de: {y}')
            print(f'Votos Candidato_Z foi de: {z}')
            print(f'Votos em branco foi de: {branco}')
            if x > y and x > z:
                print('Candidato_X ganhou as eleições')
            elif y > x and y > z:
                print('Candidato_Y ganhou as eleições')
            elif z > x and z > y:
                print('Candidato_Z ganhou as eleições')
            elif branco > x and branco > y and branco > z:
                print('Branco conseguiu mais votos')
            break
        elif sair == 2:
            continue
    except Exception:
        print('ERROR')