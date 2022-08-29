var input = require("prompt-sync")()

nota1 = 10
nota2 = 4
nota3 = 4

console.log("qual é o seu nome? ")
var nome = input()


media = (nota1 + nota2 + nota3) / 3

if (media >= 7)
    console.log(nome, "foi aprovado!!")
else
    console.log(nome, "foi reprovado")