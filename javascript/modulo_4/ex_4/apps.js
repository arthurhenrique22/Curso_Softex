const express = require("express")
const app = express()

const conexao = require('./models/conexao')

app.get("/", async(req, res) => {
    res.send("Pagina inicial")
})
app.listen(8080, () => {
    console.log("Servidor iniciado na porta 8080: http://localhost:8080/")
})