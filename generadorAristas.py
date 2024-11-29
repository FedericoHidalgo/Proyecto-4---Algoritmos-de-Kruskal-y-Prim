class Arista:
    """
    Clase generadora de Aristas
    """
    def __init__(self,nodo0, nodo1, id, dirigido = False):
        """
        Constructor
        """
        self.nodo0 = nodo0  #Nodo de origen
        self.nodo1 = nodo1  #Nodo de destino  
        self.arista =  str(nodo0) + str(id) + str(nodo1)    #Identificador de la arista
        self.dirigido = dirigido #Arista dirigida o no
        self.attr = {
            """
            Diccionario en construcción
            """
        }

    def __str__(self):
        """
        Convertir nodo en string
        """
        return str(self.arista)

    def getArista(self):
        """
        Método para imprimir los valores de la Arista
        """     
        print(self.arista)
