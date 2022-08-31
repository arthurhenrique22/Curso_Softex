const express = require("express")
const rotas = express()

rotas.get("/", function(req, res) {
    res.send("Pagina home")

})
rotas.get("/contato", (req, res) => {
    res.send("Pagina de contato")
})
rotas.listen(8080, () => {
    console.log("Servidor iniciado na porta 8080: http://localhost:8080/")
})