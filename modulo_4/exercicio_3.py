class getset:
    def __int__(self):
        self._id = 0

    @property
    def id(self):
        print("Sua idade: ")
        return self._id

    @id.setter
    def id(self, i):
        if  (i < 18):
            raise ValueError('Você ainda não é maior de idade')
        print('Você é maior de idade')
        self._id = i


pt = getset()

pt.id = 19

print(pt.id)