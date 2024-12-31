from generadorModelos import *
from generadorGrafos import *

#Numero de muestras que se graficaran por modelo
numNodos = [400]#30, 400]
#Matriz para el modelo malla
matriz = {30:[6, 5], 400: [20, 20]}

def generarMST(numNodos):
    """
    Genera el arbol de expansión mínima para los modelos
    de grafo generados
    """
    numNodos = str(numNodos)

    #Kruskal Inverso
    kruskalInverso = modelo.KruskalI()
    print("Kruskal Inverso: ", kruskalInverso)
    nombreArchivo = "kruskalInverso " + numNodos + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo, 'MST')
    modelo.limpiarMST()

    #Kruskal Directo
    kruskalDirecto = modelo.KruskalD()
    print("Kruskal Directo: ", kruskalDirecto)
    nombreArchivo = "kruskalDirecto " + numNodos + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo, 'MST')
    modelo.limpiarMST()

    #Prim
    prim = modelo.Prim()
    print("Prim: ", prim)
    nombreArchivo = "Prim " + numNodos + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo, 'MST')
    modelo.limpiarMST()

"""
Modelo Malla
"""
#i -> 30 y 400 nodos
for i in numNodos:   
    #Genera el modelo de grafo  
    modelo = modeloMalla(matriz[i][0], matriz[i][1])
    nombreArchivo = "Malla " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo, 'Grafo')
    generarMST(i)


"""
Modelo Erdos Renyi
"""
#i -> 30 y 400 nodos
for i in numNodos:
    #Genera el modelo de grafo
    modelo = modeloErdosRenyi(i, i*2)
    nombreArchivo = "Erdos Renyi " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo, 'Grafo')
    generarMST(i)


"""
Modelo Gilbert
"""
#i -> 30 y 400 nodos
p = 0.25 #Probabilidad de que exista una arista
for i in numNodos:
    #Genera el modelo de grafo
    modelo = modeloGilbert(p, i)
    nombreArchivo = "Gilbert " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo, 'Grafo')
    generarMST(i)


"""
Modelo Geografico Simple
"""
r = 0.15 #Distancia máxima entre nodos
#i -> 30 y 400 nodos
for i in numNodos:
    #Genera el modelo de grafo
    modelo = modeloGeograficoSimple(i, r)
    nombreArchivo = "Geografico Simple " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo, 'Grafo')
    generarMST(i)


"""
Modelo Barabasi Albert
"""
d = 3 #Número de aristas que se agregan en cada paso
#i -> 30 y 400 nodos    
for i in numNodos:
    #Genera el modelo de grafo
    modelo = modeloBarabasiAlbert(i, d)
    nombreArchivo = "Barabasi Albert " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo, 'Grafo')
    generarMST(i)


"""
Modelo Dorogovtsev Mendes
"""
#i -> 30 y 400 nodos
for i in numNodos:
    #Genera el modelo de grafo
    modelo = modeloDorogovtsevMendes(i)
    nombreArchivo = "Dorogovtsev Mendes " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo, 'Grafo')
    generarMST(i)