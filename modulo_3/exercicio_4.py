num1 = 5 + 5
num2 = complex(5, 5)
num3 = complex(5, 5)

s = (num1 + num2) + num3
sub = (num1 - num2) - num3
m = (num1 * num2) * num3
d = (num1 / num2) / num3

print('Soma:'), print('real:', s.real, '\nimaginário:', s.imag, '\n')
print('Subtração:'), print('real:', sub.real, '\nimaginário', sub.imag, '\n')
print('Multiplicação:'), print('real:', m.real, '\nimaginário', m.imag, '\n')
print('Divisão:'), print('real:', d.real, '\nimaginário:', d.imag)