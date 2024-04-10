# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 11:50:47 2024

@author: vlope
"""


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
            
            
    def save_gephi(self, nombre_archivo:str):
        """Guarda el grafo generado en un archivo DOT.

        Args:
            nombre_archivo (str): Nombre con el que se guardará el archivo.
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


