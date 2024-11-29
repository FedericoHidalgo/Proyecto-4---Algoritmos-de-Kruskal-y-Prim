from generadorNodos import Nodo
from generadorAristas import Arista
import random

class Grafo:
    """
    Clase generadora de Grafos
    """
    def __init__(self, dirigido = False):
        """
        Constructor                                                   
        """
        self.nodos = {}         #Conjunto, para evitar duplicados
        self.aristas = {}
        self.costos = {}
        self.dirigido = dirigido    #Grafo no dirigido como valor de inicio
        self.attr = {}

    def agregarNodo(self, id):
        """
        Agrega un nuevo nodo al grafo
        """
        nodo = self.nodos.get(id)   #Verifica si el nodo existe
        #Si no existe se crea uno nuevo        
        if nodo == None:
            nodo = Nodo(id)
            self.nodos[id] = str(nodo)  #Agrega un nodo  
        return nodo
    
    def agregarArista(self, n1, n2, id, le = None):
        """
        Agrega una arista al grafo
        """
        arista = Arista(n1, n2, id)
        arista = self.aristas.get(str(arista))   #Verifica si la arista existe
        #Si no existe se crea uno nuevo        
        if arista == None:
            V0 = self.agregarNodo(n1)   #Agrega nodo base
            V1 = self.agregarNodo(n2)   #Agrega nodo adyacente 
            arista = str(Arista(V0, V1, id))        
            self.aristas[arista] = arista   #Agrega arista
            #Agrega el costo de recorrer una arista
            if le == None:
                self.costos[arista] = random.randint(0, 100)  #Si no hay un valor definido de arista
            else:
                self.costos[arista] = le    #Si ya existe un valor definido para esa arista
        return arista
       
    def __str__(self):
        """
        Convertir grafo en string
        """
        graf = "Nodos: "
        for i in self.nodos:
            graf += str(i) + ','

        graf += "\nAristas: "
        for i in self.aristas:
            graf += str(i) + '(' + str(self.costos.get(i)) + ')' + ','

        return str(graf)
    
    def crearCadena(self, id):
        """
        Crea la cadena de aristas y nodos que es
        reconocida por Gephi
        """
        cadena = ''
        #Formato DOT
        cadena += 'digraph ' + id + '{\n'
        #Imprimir los nodos
        for nodo in self.nodos:
            if self.attr.get(nodo) == str(0):
                cadena += str(nodo) + '[label="N' + str(nodo) + ' (' + str(self.attr.get(nodo)) + '), ", color="red"];\n'
            else:
                cadena += str(nodo) + '[label="N' + str(nodo) + ' (' + str(self.attr.get(nodo)) + ')"];\n'
        #Imprimir las aristas
        for arista in self.aristas:
            cadena += str(arista) + '[label="' + str(self.costos.get(arista)) + '"];\n'
        #Final del formato
        cadena += '}\n'
        return cadena
    
    def crearArchivo(self, id, cadena):
        """
        Genera el archivo .gv y lo exporta
        """
        nombreArchivo = id + '.gv'
        #Escribimos el archivo de salida
        archivo = open(nombreArchivo, 'w+')
        archivo.write(cadena)
        archivo.close()
        return nombreArchivo     

    def graphViz(self, id):
        """
        Genera un archivo con formato GraphViz
        """
        cadena = self.crearCadena(id)
        archivo = self.crearArchivo(id, cadena)
        print('Archivo GraphViz generado: ' + archivo + '\n')        
        
    def getDiccionarios(self):
        """
        Visualizar en consola el diccionario creado
        """
        print("Nodos: ")
        print(self.nodos.items())
        print("Aristas: ")
        print(self.aristas.items())

    def setAtributo(self, id, distNB='inf'):
        """
        Asigna al nodo el costo de llegar desde el nodo base
        """
        self.attr[id] = str(distNB)     #Distancia del Nodo Base al nodo actual
        return True
    
    def nodosDeArista(self, nodo):
        """
        Método que obtiene los nodos adyacentes a un nodo de interes
        Asignar un método de generación de grafo
        nodo -> nodo de interes
        """
        #Obtenemos las aristas generadas en el modelo
        aristaGrafo = self.aristas.values()
        #Generar una lista de nodos conectados por la arista
        n1 = []
        #Generar una lista de los pesos de recorrer cada camino
        #camino = []
        #Convertimos al nodo de busqueda en cadena
        nodo = str(nodo)
        #Obtenemos el segundo nodo unido a la arista
        for i in aristaGrafo:
            #Obtenemos los nodos (u, v)        
            n2 = i.split(' -> ', 1)
            if str(n2[0]) == nodo:       #Obtenemos el segundo nodo
                n1.append(int(n2[1]))
                #Agregamos nuestra lista de caminos
                #camino.append(self.costos.get(i))
            elif str(int(n2[1])) == nodo:     #Obtenemos el segundo nodo
                n1.append(int(n2[0]))
                #Agregamos nuestra lista de caminos
                #camino.append(self.costos.get(i))
        #Retornamos la lista de nodos adyacentes y distancia de cada camino
        return n1#, camino
    
    def nodoVecino(self, arista):
        """
        Método que obtiene los nodos conectados a una arista
        n0 -- n1
        """
        #Obtenemos los nodos (u, v)        
        n = arista.split(' -> ', 1)
        return n
    
    def combinarConjuntos(self, lista, indices):
        """
        Une dos sublistas en una sola dentro de una lista principal,
        elimina las sublistas previas
        lista -> lista a ordenar
        indices -> Posición en la lista de sublistas a ordenar 
        """
        # Obtener las sublistas a combinar
        conjunto = [lista[i] for i in indices]
        
        # Crear la nueva sublista combinada
        nvaSublista = sum(conjunto, [])
        
        # Eliminar las sublistas originales y agregar la nueva
        for i in sorted(indices, reverse=True):  # Eliminar en orden inverso
            del lista[i]
        lista.append(nvaSublista)        
        return lista
    
    def KruskalD(self):
        """
        Genera el MST conectando las aristas de menor valor al cumplirse 
        que se encuentren entre nodos de distintos conjuntos.
        """
        #Ordena las aristas ascendentemente de acuerdo a su costo
        aristasOrd = sorted(self.costos.items(), key = lambda x: x[1])
        #Conjuntos de cada nodo
        V = []
        for n in self.nodos:
            V.append([n])            
        #Generamos el arbol de minima expansión
        T = []
        for i in aristasOrd:
            #Obtenemos la arista conectada entre u y v
            ei = str(i[0])
            u, v = self.nodoVecino(ei)
            #Variable auxiliar para combinar los conjunto
            indices = []
            #Obtenemos los conjuntos donde se encuentran u y v
            for numConjunto, conjunto in enumerate(V):
                if int(u) in conjunto or int(v) in conjunto:
                    indices.append(numConjunto)
            #Combinan los conjuntos conectados que contienen u y v
            for numConjunto, conjunto in enumerate(V):         
                #Si u y v estan en distintos conjuntos       
                if (int(u) in conjunto and int(v) not in conjunto) or\
                      (int(u) not in conjunto and int(v) in conjunto):
                    #Añadimos la arista al arbol
                    T.append(i)
                    #Obtenemos el nuevo conjunto de nodos conectados
                    V = self.combinarConjuntos(V, indices)
                    break
        #Retornamos en MST
        return T
