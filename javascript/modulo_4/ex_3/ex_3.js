const pessoa = {
    nome: "Arthur",
    idade: 18,
    nacionalidade: "Brasileiro"
}
const array = [1, 2, 3]

var printpessoa = function() {
    console.log("Nome: " + pessoa.nome)
    console.log("Idade: " + pessoa.idade)
    console.log("Nacionalidade: " + pessoa.nacionalidade)
}
var printarray = function() {
    console.log("Número:", array[0])
    console.log("Número:", array[1])
    console.log("Número:", array[2])
}
printpessoa()
printarray()