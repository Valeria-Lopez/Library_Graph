# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:57:37 2024

@author: vlope
"""

from Clases import Grafo, Nodo, Edge, Undirected_graph
import random


def graphDorogov_Mendes(n):
    """Genera un grafo con el modelo de Dorogovtsev-Mendes.
    Crea 3 nodos y 3 aristas formando un triángulo, cada nodo adicional
    se une con los nodos que forman la arista selecionada al azar.
    
    Args:
        n (int): Indica la cantidad de nodos en el grafo.
        
    Returns:
        _DOT_: Archivo que contiene los nodos y aristas del grafo.
    """
    g = Grafo()
    
    nodos_list = []
    edge_dict = []
    
    for i in range(3):
        g.add_nodo(Nodo(i))
        nodos_list.append(i)
    
    
    g.add_edge(Edge(g.get_nodo(0), g.get_nodo(1)))
    g.add_edge(Edge(g.get_nodo(0), g.get_nodo(2)))
    g.add_edge(Edge(g.get_nodo(1), g.get_nodo(2)))
    edge_dict.append([0,1])
    edge_dict.append([0,2])
    edge_dict.append([1,2]) 
    
    for nodos in range(3, 3+n):
        g.add_nodo(Nodo(nodos))
        nodos_list.append(nodos)
        select_edge = random.randrange(len(edge_dict))
        for k in edge_dict[select_edge]:
            g.add_edge(Edge(g.get_nodo(nodos), g.get_nodo(k)))
            edge_dict.append([nodos,k])
            
    g.save_gephi('dorogovtsevMendes' + str(n))
    return print('ok')
