# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 01:01:19 2024

@author: vlope
"""

from Clases import Grafo, Nodo, Edge, Undirected_graph
import math
import random
import numpy as np


def geoGraph(n, r):
    """Genera un grafo con el modelo geográfico simple.
    Crea n nodos y crea una arista entre otros nodos que esten a una distancia
    r o menor.
    Args:
        n (int): Indica la cantidad de nodos en el grafo.
        r (float): Distancia máxima para crear una arista.
        
    Returns:
        _DOT_: Archivo que contiene los nodos y aristas del grafo.
    """
    g = Grafo()
    
    if n < 1 or r < 0:
        raise ValueError()
        
    nodos_list = []
    coordenada = []
     
    for i in range(n):
         g.add_nodo(Nodo(i))
         nodos_list.append(i)
         
    for i in np.arange(0, 1, 0.1):
        coordenada.append(i)
   
    for i in range(n):
        for j in range(i+1, n):
            x1 = random.choice(coordenada)
            y1 = random.choice(coordenada)
            x2 = random.choice(coordenada)
            y2 = random.choice(coordenada)
            distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            if distancia <= r:
                g.add_edge(Edge(g.get_nodo(nodos_list[i]), g.get_nodo(nodos_list[j])))
           
    g.save_gephi('geografico' + str(n) + '_' + str(r))            
    return print('ok')


H = geoGraph(50, 2)