import random, math
from generadorGrafos import Grafo

def condicionesIniciales(nodos = 1, aristas =  1, v =0 , e = 0):
    """
    Evalua si los datos ingresados al modelo de Grafo son los básicos
    necesarios para generarse:
    nodos: núm de nodos con los que se desea generar el modelo
    aristas: núm de aristas con los que se desea generar el modelo
    n: nodos minimos de trabajo
    m: aristas minimas necesarias
    """
    if nodos > v and aristas > e:
        return True
    else:
        print("\n\n¡ Datos de inicio de modelo incorrectos !") 
        return False 

def modeloMalla(m, n, dirigido = False):
    """
    Crea n*m nodos y une en aristas con el nodo n(i+1,j) y n(i, j+1)
    """
    G = Grafo(dirigido)
    #Condición de inicio
    columnas = 1    #>1
    filas = 1       #>1
    inicio = condicionesIniciales(m, n, columnas, filas)
    if inicio != True:
        #Se interrumpe la ejecución del método si no se cumplen las
        #condiciones de inicio
        return

    #Creamos los nodos
    for i in range(n*m):
        G.agregarNodo(i)    
    #Creamos la malla
    for i in range(m*n):
        #Conectamos nodos de la misma fila
        if (i % n) != 0:
            G.agregarArista(i-1, i, ' -> ')
        #Conectamos nodos de la misma columna
        if i > 0 and (i + n) < m*n+1:
            G.agregarArista(i-1, (i-1)+n, ' -> ')
    
    return G


def modeloErdosRenyi(n, m, dirigido = False):
    """
    Crea n vertices y elige al azar m pares de
    vertices para formar las aristas
    """
    G = Grafo(dirigido)
    #Condiciones iniciales
    nodos = 1   #>1
    aristas = n   #>=n-1
    inicio = condicionesIniciales(n, m, nodos, aristas)
    if inicio != True:
        #Se interrumpe la ejecución del método si no se cumplen las
        #condiciones de inicio
        return

    #Creamos los nodos
    for i in range(n):
        G.agregarNodo(i)
    #Creamos las aristas
    for i in range(m):
        #Nodo aleatorio 1
        v1 = random.randint(0, n-1)
        #Nodo aleatorio 2
        v2 = random.randint(0, n-1)
        #Si v1 != v2 creamos una arista
        if v1 != v2:
            G.agregarArista(v1, v2,' -> ')
    return G

def modeloGilbert(p, n, dirigido = False):
    """
    Crea m aristas y n vértices, coloca una
    arista entra cada par independiente y de
    forma uniforme con probabilidad p
    """
    G = Grafo(dirigido)
    #Condiciones iniciales
    nodos = 1   #>0
    probabilidad = 0    #[0, 1]
    inicio = condicionesIniciales(n, p, nodos, probabilidad)
    if inicio != True or p > 1:
        print("\n\n¡ Datos de inicio de modelo incorrectos !")
        #Se interrumpe la ejecución del método si no se cumplen las
        #condiciones de inicio
        return
    #Creamos los nodos
    for i in range(n):
        G.agregarNodo(i)
    #Creamos las aristas
    for i in range(n):
        for j in range(n):
            #La arista se crea si es menor a p
            if random.random() < p:
                #No se crea aristas hacia el mismo nodo
                if(j != i):
                    G.agregarArista(i, j,' -> ')
    return G

def distanciaNodos(n1, n2):
    """
    Método que calcula la distancia entre dos puntos
    representados por nodos
    """
    #Coordenadas 'X' n_[0]
    #Coordenadas 'Y' n_[1]
    n1 = list(n1)
    n2 = list(n2)
    d = math.sqrt((n2[0] - n1[0])**2 + (n2[1] - n1[1])**2)
    return d

def modeloGeograficoSimple(n, r, dirigido = False):
    """
    Coloca n vértices en un rectangulo unitario
    con coordenadas normales y coloca una arista
    entre cada par que queda a distancia r o menor
    """
    G = Grafo(dirigido)
    #Condiciones iniciales
    nodos = 1   #>0
    distancia = 0   #[0,1]
    inicio = condicionesIniciales(n, r, nodos, distancia)
    if inicio != True or r > 1:
        print("\n\n¡ Datos de inicio de modelo incorrectos !")
        #Se interrumpe la ejecución del método si no se cumplen las
        #condiciones de inicio
        return
    #Diccionario de coordenadas para cada nodo
    posicion = {}
    #Creamos los nodos
    for i in range(n):
        G.agregarNodo(i)
        #A cada nodo i le corresponde una coordenada {x,y} 
        #de valor (0,0) hasta (1,1) generada con random
        x = random.random()
        y = random.random()
        posicion[i] = {x, y}
    #Se crea una arista entre cada par de nodos con distancia
    #menor a r
    for i in range(n):
        n1 = posicion.get(i)    #Coordenadas del nodo "i"        
        for j in range(n):
            n2 = posicion.get(j)    #Coordenadas del nodo "j"
            #No se crea aristas hacia el mismo nodo
            if i != j:
                #Obtenemos distancia r
                d = distanciaNodos(n1, n2)
                if d <= r:
                     G.agregarArista(i, j,' -> ')
    return G

def listaAleatoria(inicio, fin):
    """
    Método que genera una lista de números aleatorios
    """
    lista = random.sample(range(inicio, fin), fin-inicio)
    return lista

def modeloBarabasiAlbert(n, d=0, dirigido = False):
    """
    Colocar n nodos uno por uno, asignando a cada uno d aristas 
    a vértices distintos de tal manera que la probabilidad de que 
    el vértice nuevo se conecte a un vértice existente v es 
    proporcional a la cantidad de aristas que v tiene actualmente.
    """
    G = Grafo(dirigido)  
    #Condiciones iniciales
    nodos = 1   #>1
    aristas = 1   #>1
    inicio = condicionesIniciales(n, d, nodos, aristas)
    if inicio != True:
        #Se interrumpe la ejecución del método si no se cumplen las
        #condiciones de inicio
        return
    #Diccionario de grados de conexión para cada nodo
    grado = {}  
    #Creamos los nodos
    for i in range(n):
        G.agregarNodo(i)
        #A cada nodo le corresponde un grado cero al ser creado
        grado[i] = 0 
    #Comienza evaluando uno a uno los nodos del modelo
    for i in range(1, n):
        #Creamos una lista de nodos aleatorios, con los cuales nuestro nodo
        #origen intentará conectarse
        lista = listaAleatoria(0, i)
        #Intentamos conectar el nodo origen con los nodos aleatorios
        for j in range(i):
            #Obtenemos el grado de conexión del nodo aleatorio
            gradoRandom = grado.get(lista[j])
            #Calculamos la probabilidad de conexión que presenta
            p = 1 - (gradoRandom / d)
            #Generamos el número random de comparación
            r = random.random()
            #¿r < p?
            if r < p:
                #Nos aseguramos que el nodo no se conecte consigo mismo
                if lista[j] != i:
                    #Agregamos arista entre el nodo origen y el nodo random
                    G.agregarArista(i, lista[j], ' -> ')
                    #Aumentamos el grado del nodo random
                    grado[lista[j]] += 1 
                    #Aumentamos el grado del nodo origen
                    grado[i] += 1                    
    return G

def modeloDorogovtsevMendes(n, dirigido = False):
    """
    Crea 3 nodos y 3 aristas formando un triángulo. Para cada nodo adicional, 
    se selecciona una arista al azar y se crean aristas entre el nodo nuevo y 
    los extremos de la arista seleccionada.
    """
    #Condiciones iniciales
    nodos = 2   #>=3
    inicio = condicionesIniciales(n, v=nodos)
    if inicio != True:
        #Se interrumpe la ejecución del método si no se cumplen las
        #condiciones de inicio
        return
    G = Grafo(dirigido)
    #Diccionario para almacenar las aristas del triangulo
    triangulo = {}
    #Creamos los nodos
    for i in range(n):
        G.agregarNodo(i)
    #Crear las aristas del triangulo inicial
    #Nodos 0 y 1
    for i in [0, 1]:
        #Nodos 1 y 2
        for j in [1, 2]:
            #Evitamos conexiones al mismo nodo
            if i != j:
                G.agregarArista(i, j, ' -> ')
                #Guardamos los nodos donde se conectan las aristas
                #1, 2 y 3 respectivamente
                triangulo[i+j] = i, j
    #Creamos las aristas restantes
    for i in range(4, n):
        #Seleccionamos de forma aleatoria la arista de conexión
        aristaTriangulo = random.randint(1, 3)
        #Creamos dos aristas entre el nodo creado y los dos extremos 
        #de la arista obtenida de forma random
        for j in [0, 1]:
            G.agregarArista(i, triangulo[aristaTriangulo][j], ' -> ')
    return G