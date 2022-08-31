const Sequelize = require("sequelize")

const sequelize = new Sequelize("arthur", "root", "123456", {
    host: 'localhost',
    dialect: 'mysql'
})

sequelize.authenticate()
    .then(function() {
        console.log("Conexão com o banco de dados realizado com sucesso!")
    }).catch(function() {
        console.log("Erro: conexão de dados não conseguiu ser feita com sucesso!")
    })


module.exports = sequelize