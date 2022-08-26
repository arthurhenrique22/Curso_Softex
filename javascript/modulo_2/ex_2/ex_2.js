var input = require("prompt-sync")()

function calculadora(num1, num2, num) {
    switch (num) {
        case 1:
            return num1 + num2;
            break;
        case 2:
            return num1 - num2;
            break;
        case 3:
            return num1 * num2;
            break;
        case 4:
            sobra = num1 % num2
            if (num2 == 0) {
                console.log("Não é possivel dividir por 0")
                break;
            } else {
                console.log("Sobra da operação", sobra)
            }
            return num1 / num2;
            break;
        default:
            return 0;
    }
}
console.log("1:Adição\n2:Subtração\n3:Multiplicação\n4:Divisão");

var num = input()
num = parseFloat(num)

console.log("Digite um número: ")

var num1 = input()
num1 = parseFloat(num1)

console.log("Digite outro número: ")

var num2 = input()
num2 = parseFloat(num2)

var resultado = calculadora(num1, num2, num)
console.log("Resultado da operação:", resultado)