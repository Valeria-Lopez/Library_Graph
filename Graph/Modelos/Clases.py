# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 11:50:47 2024

@author: vlope
"""
import sys, random, heapq

class Nodo:
    """ Permite representar un nodo dentro de un grafo."""
    
    def __init__(self, nodo):
        """Permite inicializar a cada nodo con un identificador.

        Args:
            nodo (int): El identificador del nodo.
        """
        self.id = nodo
    
    
    def get_name(self):
        """Obtener el identificador del nodo.

        Returns:
            _int_: El identificador del nodo.
        """
        return self.id
    
    
    def __str__(self):
        """Imprime el identificador del nodo.

        Returns:
            _str_: El identificador del nodo.
        """
        return str(self.id)
        

class Edge:
    """Representa una arista dentro de un grafo."""
    
    def __init__(self, origen, destino):
        """Permite inicializar a cada arista con el nodo origen y destino.

        Args:
            origen (int): El identificador del nodo origen.
            destino (int): El identificador del nodo destino.
        """
        self.origen = origen
        self.destino = destino
        
        
    def get_origen(self):
        """Se obtiene el identificador del nodo origen.

        Returns:
            _str_: El identificador del nodo origen.
        """
        return self.origen
    
    
    def get_destino(self):
        """Se obtiene el identificador del nodo destino.

        Returns:
            _str_: El identificador del nodo destino.
        """
        return self.destino


    def __str__(self):
        """Se imprime la arista con el nodo origen y destino.

        Returns:
            _str_: Arista formada.
        """
        return str(self.origen.get_name()) + " -> " + str(self.destino.get_name())
    
        
class Grafo:
    """Representa un grafo"""
    
    def __init__(self):
        """Inicializa los objetos con un diccionario vacío."""
        self.diccionario = dict()
        
        
    def add_nodo(self, nodo):
        """Agrega un nodo al grafo.

        Args:
            nodo (int): El identificador del nodo.
            
        Returns:
            _str_: Indica si el nodo ya está en el diccionario.
        """
        if nodo in self.diccionario:
            return "Nodo ya agregado"
        self.diccionario[nodo] = []
        
        
    def add_edge(self, arista):
        """Agrega una arista al grafo.

        Args:
            arista (Edge): Objeto de la clase Edge, donde se obtendrán los nodos origen y destino.
        """
        origen = arista.get_origen()
        destino = arista.get_destino()
        if origen not in self.diccionario:
            raise ValueError(f'Nodo{origen.get_name()} no está en grafo')
        if destino not in self.diccionario:
            raise ValueError(f'Nodo{destino.get_name()} no está en grafo')
        if destino not in self.diccionario[origen]:
            self.diccionario[origen].append(destino)
        
    
    def get_nodo(self, nodo_name):
        """Obtiene el nodo del diccionario, para saber si existe.
        
        Args:
            nodo_name (int): Identificador del nodo.
            
        Returns:
            _int_: El nodo en el diccionario.
            _str_: Si no existe el nodo.
        """
        for v in self.diccionario:
            if nodo_name == v.get_name():
                return v
        print(f'Nodo {nodo_name} no existe')
        
        
    def bfs(self, nodo_origen, nombre_archivo:str):
        """Desde un nodo raíz visita todos los nodos adyaentes a él
        antes de pasar al siguiente nivel, para al final obtener un grafo.
        
        Args:
            nodo_origen (int): Nodo desde donde el algoritmo inicia la búsqueda.
            nombre_archivo (str): Nombre que llevará el archivo .DOT
            
        Returns:
            _.dot_: Archivo .DOT que contiene el grafo.
        """
        file = open(nombre_archivo + '.dot', "w")
        h = " "
        nodos_descubiertos = []
        cola = []
        nodos_descubiertos.append(nodo_origen)
        cola.append(nodo_origen)
        while cola:
            m = cola.pop(0)
            
            for vecino in self.diccionario[m]:
                if vecino not in nodos_descubiertos:
                    nodos_descubiertos.append(vecino)
                    cola.append(vecino)
                    h += str(m.get_name()) + ' -> ' + str(vecino.get_name()) + ';' + '\n'
        file.write('digraph {' + h + '}')
        file.close()
    
    
    def dfs_recursivo(self, nodo, archivo_name):
        """Desde un nodo raíz visita todos los nodos a los que puede acceder
        desde él de manera recursiva siguiendo una rama, antes de retroceder 
        y explorar otra rama, al final se obtiene un grafo.
        
        Args:
            nodo (int): Nodo desde donde el algoritmo inicia la búsqueda.
            archivo_name (str): Nombre que llevará el archivo .DOT
                
        Returns:
            _.dot_: Archivo .DOT que contiene el grafo.
        """
        file = open(archivo_name + '.dot', "w")
        file.write('digraph {')
        nodo_anterior = nodo
        nodos_visitados = set()
        self.dfs_utilrec(nodo, nodos_visitados, nodo_anterior, file)
        file.write('}')
        file.close()
        
        
    def dfs_utilrec(self, nodo, nodos_visitados, nodo_anterior, file):
        """Realiza el proceso de recursión para el algoritmo de búsqueda DFS.
        
        Args:
            nodo (int): Nodo desde donde el algoritmo inicia la búsqueda.
            nodos_visitados (set): Lista de los nodo visitados.
            nodo_anterior (int): Guarda el nodo visitado anterior.
            file (.dot): Archivo .DOT donde se guarda el grafo.
        """
        h = ''
        if nodo_anterior != nodo:
            h = str(nodo_anterior.get_name()) + ' -> ' + str(nodo.get_name()) + ';' + '\n'
        nodo_anterior = nodo
        nodos_visitados.add(nodo)
        file.write(h)
        
        for vecino in self.diccionario[nodo]:
            if vecino not in nodos_visitados:
                self.dfs_utilrec(vecino, nodos_visitados, nodo_anterior, file)
        
    
    def dfs_iterativo(self, nodo, archivo_name):
        """Desde un nodo raíz visita todos los nodos a los que puede acceder
        desde él de manera iterativa siguiendo una rama, antes de retroceder 
        y explorar otra rama, al final se obtiene un grafo.
        
        Args:
            nodo (int): Nodo desde donde el algoritmo inicia la búsqueda.
            archivo_name (str): Nombre que llevará el archivo .DOT
                
        Returns:
            _.dot_: Archivo .DOT que contiene el grafo.
        """
        h = ''
        file = open(archivo_name + '.dot', "w")
        file.write('digraph {')
        visitados = []
        cola = []
        arista = []
        
        cola.append(nodo)
        visitados.append(nodo)
        
        while cola:
            s = cola.pop()
        
            for j in visitados[::-1]:
                if s in self.diccionario[j]:
                    if s not in visitados:
                        if [j,s] in arista:
                            break
                        if [j,s] not in arista:
                            h += str(j.get_name()) + ' -> ' + str(s.get_name()) + ';' + '\n'
                            arista.append([j,s])
                            break
                
            if s not in visitados:
                visitados.append(s)
            
            for i in self.diccionario[s][::-1]:
                if i not in visitados:
                    cola.append(i)
        file.write(h)
        file.write('}')
        file.close()


     def dijkstra(self, s):
        """Encuentra el camino más corto entre un nodo origen y todos los otros
        nodos a los que puede acceder. Usa los valores de las aristas para
        encontrar el camino que minimiza el valor total entre el nodo origen
        y los demás nodos del grafo.
        
        Args:
            s (int): Nodo origen desde donde el algoritmo empieza a encontrar
            el camino más corto a los demás nodos del grafo.
                
        Returns:
            _generado.dot_: Archivo .DOT que contiene el grafo.
            _dijkstra.dot_: Archivo .DOT que contiene los caminos más cortos
            del nodo origen a todos los demás nodos.

        """
        new_dic = {}
        for l in self.diccionario.keys():
            new_dic.setdefault(l.get_name(),{})
            for valor in self.diccionario[l]:
                new_dic[l.get_name()].setdefault(valor.get_name(),random.randint(1,30))
        
        inf = sys.maxsize
        nodo_data ={}
        for nodo in new_dic.keys():
            nodo_data.setdefault(nodo,{'cost':inf,'pred':[]})
        
        nodo_data[s]['cost'] = 0
        temp = s
        queue = [(nodo_data[s]['cost'],temp)]
        
        while queue:
            distancia, nodo = heapq.heappop(queue)
            if distancia > nodo_data[nodo]['cost']:
                continue
            for vecino, peso in new_dic[nodo].items():
                costo = distancia + peso
                if costo < nodo_data[vecino]['cost']:
                    nodo_data[vecino]['cost'] = costo
                    k = []
                    k.append(nodo)
                    nodo_data[vecino]['pred'] = nodo_data[nodo]['pred'] + k
                    heapq.heappush(queue, (nodo_data[vecino]['cost'],vecino))
                    
        file = open('dijkstra.dot', "w")
        file.write('digraph dijkstra {')
        for nodos in nodo_data.keys():
            if nodo_data[nodos]['cost'] == inf:
                file.write(str(nodos) + "[Label=" + str(nodos) + "(inf)" + "];" + "\n")
            else:
                file.write(str(nodos) + "[Label=" + str(nodos) + "(" + str(nodo_data[nodos]['cost']) + ")" + "];" + "\n")
            cont=0
            ant = nodo_data[nodos]['pred'][::-1]
            for cvecinos in nodo_data[nodos]['pred'][::-1]:
                cont += 1
                if cont == 1:
                    file.write(str(cvecinos) + " -> " + str(nodos) + "[Label=" + str(new_dic[cvecinos][nodos]) + "];" + "\n")
                    ant = cvecinos
                else:
                    file.write(str(cvecinos) + " -> " + str(ant) + "[Label=" + str(new_dic[cvecinos][ant]) + "];" + "\n")
                    ant = cvecinos
        file.write('}')
        file.close()
        
        file = open('generado.dot', "w")
        file.write('digraph arbol {')
        for nodos in nodo_data.keys():
             file.write(str(nodos) + "[Label=" + str(nodos) + "(inf)" + "];" + "\n")
        for origen in new_dic.keys():
            for destino in new_dic[origen]:
                file.write(str(origen) + " -> " + str(destino) + "[Label=" + str(new_dic[origen][destino]) + "];" + "\n")
        file.write('}')
        file.close()
        

     def prim(self,s):
        """Encuentra el árbol de expansión mínimo del grafo conectando nodos con
        aristas de peso mínimo sin formar ciclos.
        
        Args:
            s (int): Nodo origen desde donde el algoritmo empieza a formar el
                árbol de expansión mínimo.
                
        Returns:
            _generado.dot_: Archivo .DOT que contiene el grafo.
            _prim.dot: Archivo .DOT que contiene el árbol de expansión mínimo.
            _MST_ : Imprime el valor del árbol de expansión mínimo.

        """
        new_dic = {}
        for l in self.diccionario.keys():
            new_dic.setdefault(l.get_name(),{})
            for valor in self.diccionario[l]:
                new_dic[l.get_name()].setdefault(valor.get_name(),random.randint(1,10))
                
        aristas = []
        for nodos in new_dic[s]:
            aristas.append((new_dic[s][nodos],s,nodos))
        aristas.sort()
        visitados = set([s])
        mst = []
        MST = 0
        heapq.heapify(aristas)
        
        while aristas:
            cost, frm, to = heapq.heappop(aristas)
            if to not in visitados:
                visitados.add(to)
                mst.append((frm, to, cost))
                MST += cost
                if new_dic[to] != 0:
                    for next_nodos in new_dic[to]:
                        if next_nodos not in visitados:
                            heapq.heappush(aristas, (new_dic[to][next_nodos], to, next_nodos))
                continue
        
        print(" El costo del árbol de expansión mínimo es: ", MST)
        
        file = open('prim.dot', "w")
        file.write('digraph arbol {')
        while mst:
            frm, to, cost = heapq.heappop(mst)
            file.write(str(frm) + " -> " + str(to) + "[Label=" + str(cost) + "];" + "\n")
        file.write('}')
        file.close()
        
        file = open('generado.dot', "w")
        file.write('digraph {')
        for origen in new_dic.keys():
            if new_dic[origen] == 0:
                file.write(str(origen) + ";" + "\n")
            for destino in new_dic[origen]:
                file.write(str(origen) + " -> " + str(destino) + "[Label=" + str(new_dic[origen][destino]) + "];" + "\n")
        file.write('}')
        file.close()
        
        
    def kruskal(self, num_nodos):
        """Construye el árbol de expansión mínimo formado por las aristas
        sucesivamente seleccionadas por su peso mínimo.
        
        Args:
            num_nodos (int): Número de nodos que contiene el grafo.
                
        Returns:
            _generado.dot_: Archivo .DOT que contiene el grafo.
            _kruskal.dot_:  Archivo .DOT que contiene el árbol de expansión mínimo.
            _MST_ : Imprime el valor del árbol de expansión mínimo.

        """
        aristas = []
        for orig in self.diccionario.keys():
            for dest in self.diccionario[orig]:
                aristas.append((random.randint(1, 10),orig.get_name(),dest.get_name()))
        uf = UnionFind(num_nodos)
        aristas.sort()
        mst = []
        MST = 0
        heapq.heapify(aristas)
        
        for cost, frm, to in aristas:
            if uf.find(frm) != uf.find(to):
                uf.union(frm, to)
                mst.append((frm,to,cost))
                MST += cost
                if len(mst) == num_nodos-1:
                    break
        
        print(" El costo del árbol de expansión mínimo es: ", MST)
        
        file = open('kruskal.dot', "w")
        file.write('digraph arbol {')
        while mst:
            frm, to, cost = heapq.heappop(mst)
            file.write(str(frm) + " -> " + str(to) + "[Label=" + str(cost) + "];" + "\n")
        file.write('}')
        file.close()
        
        file = open('generado.dot', "w")
        file.write('digraph {')
        for cost, frm, to in aristas:
            file.write(str(frm) + " -> " + str(to) + "[Label=" + str(cost) + "];" + "\n")
        file.write('}')
        file.close()
        
        
    def kruskalInv(self):
        """Construye el árbol de expansión mínimo formado por las aristas
        sucesivamente seleccionadas por su peso máximo.
        
        Args:
                
        Returns:
            _generado.dot_: Archivo .DOT que contiene el grafo.
            _kruskalInv.dot_:  Archivo .DOT que contiene el árbol de expansión mínimo.
            _mst_wt_ : Imprime el valor del árbol de expansión mínimo.

        """
        aristas = []
        adj = [0] * (len(self.diccionario.keys()))
        for i in range((len(self.diccionario.keys()))):
            adj[i] = []
            
        for o in self.diccionario.keys():
            for d in self.diccionario[o]:
                adj[o.get_name()].append(d.get_name())
                adj[d.get_name()].append(o.get_name())
                aristas.append((random.randint(1,10), (o.get_name(), d.get_name())))
                
        file = open('generado.dot', "w")
        file.write('digraph {')
        for cost, (frm, to) in aristas:
            file.write(str(frm) + " -> " + str(to) + "[Label=" + str(cost) + "];" + "\n")
        file.write('}')
        file.close()

        aristas.sort(key = lambda a: a[0])
     
        mst_wt = 0
        
        file = open('kruskalInv.dot', "w")
        file.write('digraph arbol {')
        
        for i in range(len(aristas) - 1, -1, -1):
            u = aristas[i][1][0]
            v = aristas[i][1][1]

            adj[u].remove(v)
            adj[v].remove(u)

            if self.connected(adj) == False:
                adj[u].append(v)
                adj[v].append(u)

                file.write(str(u) + " -> " + str(v) + "[Label=" + str(aristas[i][0]) + "];" + "\n")
                mst_wt += aristas[i][0]
        print(" El costo del árbol de expansión mínimo es: ", mst_wt)
        
        file.write('}')
        file.close()
                
        
    def dfs(self, v, visited, adj):
        """"Desde un nodo raíz visita todos los nodos a los que puede acceder
        desde él de manera recursiva siguiendo una rama, antes de retroceder 
        y explorar otra rama.
        
        Args:
            v (int): Nodo desde donde el algoritmo inicia la búsqueda.
            visited (list): Contiene los nodos visitados.
            adj (list): Contiene los vecinos de un nodo.

        """
        visited[v] = True
        for i in adj[v]:
            if not visited[i]:
                self.dfs(i, visited, adj)
                
                
    def connected(self, adj):
        """Verifica si el grafo está desconectado después de eliminar una aristas.
        
        Args:
            adj (list): Contiene los vecinos de un nodo.
                
        Returns:
            _Booleano_: (True) si está conectado; (False) si está desconectado.

        """
        visited = [False] * (len(self.diccionario.keys()))
        
        self.dfs(0, visited, adj)
        
        for i in range(1, (len(self.diccionario.keys()))):
            if not visited[i]:
                return False
  
        return True


    def save_gephi(self, nombre_archivo:str):
        """Guarda el grafo generado en un archivo DOT.

        Args:
            nombre_archivo (str): Nombre con el que se guardará el archivo.
            
        Returns:
            _.dot_: Archivo .DOT que contiene el grafo.
        """
        file = open(nombre_archivo + '.dot', "w")
        all_aristas = ''
        for origen in self.diccionario:
            if self.diccionario[origen] == []:
                if origen not in self.diccionario.values():
                    all_aristas += str(origen.get_name()) + ';' + '\n'
            if self.diccionario[origen] != []:
                for destino in self.diccionario[origen]:
                    all_aristas += str(origen.get_name()) + ' -> ' + str(destino.get_name()) + ';' + '\n'      
        file.write('digraph {' + all_aristas + '}')
        file.close()

     
    def __str__(self):
        """Permite imprimir el grafo generado.
        
        Returns:
            _str_: Indica todas las conexiones existentes en el grafo.
        """
        all_aristas = ''
        for origen in self.diccionario:
            for destino in self.diccionario[origen]:
                all_aristas += 'nodo_' + str(origen.get_name()) + '->' + 'nodo_' + str(destino.get_name()) +';' + '\n'      
        return all_aristas
    
    
class Undirected_graph(Grafo):
    """Permite generar un grafo no dirigido"""
    
    def add_edge(self, arista):
        """Modifica el método de añadir arista de la clase Grafo.
        
        Args:
            arista (Edge): Objeto de la clase Edge, donde se obtendrán los nodos origen y destino.
        """
        Grafo.add_edge(self, arista)
        arista_back = Edge(arista.get_destino(), arista.get_origen())
        Grafo.add_edge(self, arista_back)


class UnionFind:
    def __init__(self,size):
        self.root = list(range(size))
        self.rank = [1]*size
        
        
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] +=1

