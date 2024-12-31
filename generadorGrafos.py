from generadorNodos import Nodo
from generadorAristas import Arista
#Importamos el módulo queue que permite trabajar con colas de prioridad
from queue import PriorityQueue
import random, copy

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
        #Para el MST
        self.nodosT = {}
        self.aristasT = {}
        self.costosT = {}
        self.attrT = {}
        self.dirigidoT = dirigido    #Grafo no dirigido como valor de inicio

    def limpiarMST(self):
        """
        Limpia los diccionarios del MST
        """
        self.nodosT = {}
        self.aristasT = {}
        self.costosT = {}
        self.attrT = {}
        return True

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

    def agregarNodoT(self, id):
        """
        Agrega un nuevo nodo al MST
        """
        nodo = self.nodosT.get(id)   #Verifica si el nodo existe
        #Si no existe se crea uno nuevo
        if nodo == None:
            nodo = Nodo(id)
            self.nodosT[id] = str(nodo)  #Agrega un nodo
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
                self.costos[arista] = random.randint(0, 1000)  #Si no hay un valor definido de arista
            else:
                self.costos[arista] = le    #Si ya existe un valor definido para esa arista
        return arista

    def agregarAristaT(self, n1, n2, id, le = None):
        """
        Agrega una arista al MST
        """
        V0 = self.agregarNodoT(n1)   #Agrega nodo base
        V1 = self.agregarNodoT(n2)  #Agrega nodo adyacente
        arista = str(Arista(V0, V1, id))
        self.aristasT[arista] = arista   #Agrega arista 
        #Agrega el costo de recorrer una arista
        if le == None:
            self.costosT[arista] = random.randint(0, 1000)
        else:             
            self.costosT[arista] = le
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
                cadena += str(nodo) + '[label="N' + str(nodo) + ', color="red"];\n'
            else:
                cadena += str(nodo) + '[label="N' + str(nodo) + '"];\n'
        #Imprimir las aristas
        for arista in self.aristas:
            cadena += str(arista) + '[label="' + str(self.costos.get(arista)) + '"];\n'
        #Final del formato
        cadena += '}\n'
        return cadena
    
    def crearCadenaT(self, id):
        """
        Crea la cadena de aristas y nodos que es
        reconocida por Gephi
        """
        cadena = ''
        #Formato DOT
        cadena += 'digraph ' + id + '{\n'
        #Imprimir los nodos
        for nodo in self.nodosT:
            if self.attrT.get(nodo) == str(0):
                cadena += str(nodo) + '[label="N' + str(nodo) + ', color="red"];\n'
            else:
                cadena += str(nodo) + '[label="N' + str(nodo) + '"];\n'
        #Imprimir las aristas
        for arista in self.aristasT:
            cadena += str(arista) + '[label="' + str(self.costosT.get(arista)) + '"];\n'
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

    def graphViz(self, id, tipo):
        """
        Genera un archivo con formato GraphViz
        """
        if tipo == 'Grafo':
            cadena = self.crearCadena(id)
        elif tipo == 'MST':
            cadena = self.crearCadenaT(id)
        else:
            print("Tipo de grafo no reconocido")
            return False
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
    
    def nodosDeArista(self, nodo, aristas):
        """
        Método que obtiene los nodos adyacentes a un nodo de interes
        Asignar un método de generación de grafo
        nodo -> nodo de interes
        """
        #Obtenemos las aristas generadas en el modelo
        aristaGrafo = aristas
        #Generar una lista de nodos conectados por la arista
        n1 = []
        #Generar una lista de los pesos de recorrer cada camino
        camino = []
        #Convertimos al nodo de busqueda en cadena
        nodo = str(nodo)
        #Obtenemos el segundo nodo unido a la arista
        for i in aristaGrafo:
            #Obtenemos los nodos (u, v)        
            n2 = i.split(' -> ', 1)
            if str(n2[0]) == nodo:       #Obtenemos el segundo nodo
                n1.append(int(n2[1]))
                #Agregamos nuestra lista de caminos
                camino.append(self.costos.get(i))
            elif str(int(n2[1])) == nodo:     #Obtenemos el segundo nodo
                n1.append(int(n2[0]))
                #Agregamos nuestra lista de caminos
                camino.append(self.costos.get(i))
        #Retornamos la lista de nodos adyacentes y distancia de cada camino
        return n1, camino
    
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
    
    def DFS(self, s, listaExplorados, e):
        """
        Busqueda en Profundidad
        s - nodo ancestro
        e - aristas a evaluar
        """
        s = self.nodos.get(int(s))  #Nodo ancestro
        #si el nodo ancestro no existe termina el proceso
        if s == None:
            print("El nodo no pertenece al modelo")
            return False
        descubierto = listaExplorados
        #Marcar s como explorado
        descubierto[s] = True
        #Obtenemos los vecinos de u
        nodosIncidentes = self.nodosDeArista(s, e)
        #Recorremos los nodos en busqueda de los no explorados
        for v in nodosIncidentes[0]:
            #Si v esta marcado como no explorado
            if descubierto.get(str(v)) == False:
                #Invocar recursivamente DFS
                self.DFS(v, listaExplorados, e)
    
    def getDFS(self, s, e):
        """
        Método de apoyo para generar un arbol por busqueda a lo largo
        DFS Recursiva
        s - nodo fuente
        e - aristas a evaluar
        """
        descubierto = {}                    #Diccionario para indicar si el nodo ya fue descubierto
        #Para cada nodo v que pertenece al Grafo con v != nodoFuente
        for u in self.nodos.values():
            descubierto[u] = False
        self.DFS(s, descubierto, e)
        nodosConectados = sum(descubierto.values())
        return nodosConectados

    
    def KruskalD(self):
        """
        Genera el MST conectando las aristas de menor valor al cumplirse 
        que se encuentren entre nodos de distintos conjuntos.
        """
        #Ordena las aristas ascendentemente de acuerdo a su costo
        aristasOrd = sorted(self.costos.items(), key = lambda x: x[1])
        #print("Aristas ascendentes: ", aristasOrd)
        #Conjuntos de cada nodo
        V = []
        for n in self.nodos:
            V.append([n])            
        #Generamos el arbol de minima expansión
        T = {}
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
                    T[i[0]] = i[1]
                    self.agregarAristaT(int(u), int(v), ' -- ', i[1])
                    #Obtenemos el nuevo conjunto de nodos conectados
                    V = self.combinarConjuntos(V, indices)
                    break
        #Retornamos el valor de recorrer dicho MST
        return sum(T.values())

    def KruskalI(self):
        """
        Comienza con T=E
        Ordenar las aristas descendentemente por su costo
        Borrar la arista e de T q menos que se desconecte T
        """
        #Ordena las aristas descendentemente de acuerdo a su costo
        aristasOrd = sorted(self.costos.items(), key = lambda x: x[1], reverse=True)
        #print("Aristas descendentes", aristasOrd)
        #Generamos el arbol de minima expansión y le asignamos las aristas del grafo
        T = {} #self.aristas
        T = copy.deepcopy(self.aristas)
        #print("T: ", T)
        nodosConectados = self.getDFS(0, self.aristas)
        #El ciclo for recorre las aristas desconectando una a una
        for i in aristasOrd:
            print("Arista: ", i)
            #Quitar e_i no desconecta T
            x = T.pop(str(i[0]), None)
            #Obtenemos la arista conectada entre u y v
            ei = str(i[0])
            u, v = self.nodoVecino(ei)
            nodosSinX = self.getDFS(0, T)
            #T <- (T - {e_i})
            if nodosConectados > nodosSinX:
                #T = copy.deepcopy(T)
            #else:
                T[i[0]] = i[1]
                self.agregarAristaT(int(u), int(v), ' -- ', i[1])
        return sum(T.values())

    def Prim(self):
        """
        Comenzar con algún nodo s como raíz.
        Crecer el árbol vorazmente a partir de s, agregando la aristal
        que tenga menor costo T.
        """
        #Para cada vértice v \in V se asigna un peso inicial a{v} = \infty
        v = {}; a = {}
        v = copy.deepcopy(self.nodos)
        #Aristas
        e = {}
        e = copy.deepcopy(self.costos)
        aristas = e.keys()
        #Q: Una cola de prioridad que almacenará los vértices a procesar.
        Q = PriorityQueue()
        #S: Conjunto de vértices que ya forman parte del árbol MST.        
        S = []
        #Todos los vértices v \in V se insertan en Q.
        for i in v:
            if i == 0:
                Q.put((0, i))
                a[i] = 0
            else:
                a[i] = float('inf')
        #Mientras Q no esté vacío
        while not Q.empty():
            #u <- Siguiente(Q)
            u = Q.get()[1]
            #S <- S \cup {u}
            S.append(u)
            #Obtenemos la arista conectada entre u y v1
            v1 = self.nodosDeArista(u, aristas)
            #v1[0][x] = nodos adyacentes, v1[1][x] = costos de recorrer cada arista
            for i in range(len(v1[0])):
                j = v1[0][i]    #Nodo adyacente
                k = v1[1][i]    #Costo de recorrer la arista
                #Si v \in Q y a[v] > w(u, v)
                if j not in S and k < a.get(j):                    
                    a[j] = k 
                    Q.put((k, j))
        #Añadimos las aristas al MST
        for i in a:
            if a.get(i) in e.values():
                for j in e:
                    if e.get(j) == a.get(i):
                        #Obtenemos la arista conectada entre u y v
                        u, v = self.nodoVecino(j)
                        if int(i) == int(u) or int(i) == int(v):
                            self.agregarAristaT(int(u), int(v), ' -- ', a.get(i))
                            break
            else:
                a[i] = 0
        #Retornamos el valor de recorrer dicho MST                      
        return sum(a.values())
