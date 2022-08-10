class Carro:
    def __init__(self, marca, vm):
        self.marca = marca
        self.vm = vm

    def exibir1(self):
        print(self.marca, self.vm)


class Carro2:
    def __init__(self, marca, vm):
        self.marca = marca
        self.vm = vm

    def exibir(self):
        print(self.marca, self.vm)


carro = Carro('Marca: BMW', '\nVelocidade Maxima: 300KM')
carro.exibir1()

carro2 = Carro2('Marca: MERCEDES-BENZ', '\nVelocidade Maxima: 350KM')
carro2.exibir()