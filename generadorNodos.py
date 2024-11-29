class Nodo:
    """
    Clase generadora de Nodos
    """
    def __init__(self, id):
        """
        Constructor
        """
        self.id = id      #Identificador del nodo
        self.grado = 0    #Conteo de grado de conexión
        self.attr = {
            """
            Diccionario en construcción
            """
        }

    def __str__(self):
        """
        Convertir nodo en string
        """
        return str(self.id)

    def getNodo(self):
        """
        Método para imprimir el identificador del nodo
        """
        print(self.id)