#programa feito no pycharm com a linguagem python

nome = str(input('Qual é o seu nome? '))
nota1 = float(input('Escreva sua primeira nota: '))
nota2 = float(input('Escreva sua segunda nota: '))
nota3 = float(input('Escreva sua terceira nota: '))
falta = int(input('Quantas vezes você faltou? '))

media: float = (nota1 + nota2 + nota3) / 3

print('Media: ', media)

if media < 7.0:
    print('Infelizmente', nome, 'você foi reprovado')
elif media < 11:
    print('Parabéns,', nome, 'você foi aprovado com sucesso !!!')
elif falta > 3:
    print('Você foi reprovado por falta, pois faltou', falta, 'vezes')
