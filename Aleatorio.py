'''
    fibonacci
'''
import random
class Aleatorio:
    varA = 10
    varB = 100
    __b =+ 8
    __a = __b

    # Lista
    global numeros
    numeros = []


    # constructor
    def __init__(self):
        self.__miVarA = None
        self.__miVarB = None


    # getter & setter
    def __geta(self):
        return self.__miVarA

    def __seta(self,valorParaA):
        self.__miVarA = valorParaA

    def numeroAleatorio(self, mn, mx):
        self.min = mn
        self.max = mx
        return (random.randint(self.min, self.max))

    def generaNumeroAleatorio(self, numIteracciones, min, max):
        self.min = min
        self.max = max
        self.numIteracciones = numIteracciones
        x = range(self.numIteracciones)
        y = None

        #print(f"Len:{len(numeros)}")
        # primera iteraccion agregar en la lista
        numeros.append(self.numeroAleatorio(self.min,self.max))
        #print(f"El valos cero es:{numeros[0]}")

        for n in x:
            #print(f"inetraccion: {n}")
            while True:
                y = self.numeroAleatorio(self.min,self.max)
                #print(f"y:{y}")
                if(numeros.count(y)<1):
                    numeros.append(y)
                    #False
                    break
            #print(f"inetraccion: {n}")
            #print(f"Len:{len(numeros)}")
        print(numeros)
        numeros.clear()


'''
def __init__():
    #constructor
    return

def __init__(self, varA, varB):
    # __ private
    #a = b = c = 10
    self.__a = varA
    self.__b = varB

def __init__(self):
    pass
'''
