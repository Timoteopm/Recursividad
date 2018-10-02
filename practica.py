_Author_ = 'timoteo'


class practica:
   
    def convDecABin(self, num, residuo, lista):
        if (num == 0):
            return lista
        else:
            residuo = num % 2
            nAc = (int(num / 2))
            lista.insert(0, residuo)
            return self.convDecABin(nAc, residuo, lista)