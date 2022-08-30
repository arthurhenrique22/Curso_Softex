var cliente = {
    tipodeconta: "Conta corrente",
    conta: "58843",
    agencia: "90504-0",
    saldo: 50

}

var saldoatual = function(valor) {
    console.log("Saldo atual: " + cliente.saldo)
}


var deposito = function(valor) {
    cliente.saldo = cliente.saldo + valor
}
var printdeposito = function(valor) {
    console.log("Saldo após depósito: " + cliente.saldo)
}

var saque = function(valor) {
    cliente.saldo = cliente.saldo - valor
}
var printsaque = function(valor) {
    console.log("Saldo após saque: " + cliente.saldo)
}

var consultar_conta = function() {
    console.log("Tipo de conta: " + cliente.tipodeconta)
    console.log("Agência: " + cliente.agencia)
    console.log("Conta: " + cliente.conta)
    console.log("Saldo disponivel: " + cliente.saldo)
}

consultar_conta()
    //Deposito:
deposito(100)
printdeposito()
saldoatual()
    //Saque:
saque(50.50)
printsaque()
saldoatual()