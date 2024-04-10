# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:43:17 2024

@author: vlope
"""

from Clases import Grafo, Nodo, Edge
import random


def graphErdosRenyi(n,m):
    """Genera un grafo con el modelo de Erdos y Rényi.
    Crea n nodos y al azar se generan m cantidad de aristas.
    Args:
        n (int): Indica la cantidad de nodos en el grafo.
        m (int): Número de aristas en el grafo.
        
    Returns:
        _DOT_: Archivo que contiene los nodos y aristas del grafo.
    """
    g = Grafo()
    
    nodos_list = []
    
    for i in range(n):
        g.add_nodo(Nodo(i))
        nodos_list.append(i)
        
    edge_list = []
    
    while len(edge_list) < m:
        node1 = random.choice(nodos_list)
        node2 = random.choice(nodos_list)
        if node1 != node2:
            arista = Edge(g.get_nodo(node1), g.get_nodo(node2))
            if arista not in edge_list:
               edge_list.append(arista)
               g.add_edge(arista)
               
    g.save_gephi('ErdosRenyi_' + str(n) + '_' + str(m))
    return print('ok')
              

H = graphErdosRenyi(500,997)

