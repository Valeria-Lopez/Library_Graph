# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:50:20 2024

@author: vlope
"""

from Clases import Grafo, Nodo, Edge, Undirected_graph


def barabasiAlbertGraph(n, d):
    """Genera un grafo con el modelo de Barabási-Albert.
    Se coloca nodo por nodo y se asigna una cantidad de d aristas para que
    cada nuevo nodo se enlace.
    
    Args:
        n (int): Indica la cantidad de nodos en el grafo.
        d (int): Grado máximo esperado para cada uno de los nodos nuevos.
        
    Returns:
        _DOT_: Archivo que contiene los nodos y aristas del grafo.
    """
    g = Grafo()
     
    nodos_list = []
    degree = {}
     
    for i in range(2):
        g.add_nodo(Nodo(i))
        nodos_list.append(i)
     
    g.add_edge(Edge(g.get_nodo(0), g.get_nodo(1)))
    degree.setdefault(0, 1)
    degree.setdefault(1, 1)
       
     
    for nodos in range(n):
        if nodos not in nodos_list:
            g.add_nodo(Nodo(nodos))
            nodos_list.append(nodos)
            degree.setdefault(nodos, 0)
            for k in nodos_list:
                if k != nodos:
                    g.add_edge(Edge(g.get_nodo(nodos), g.get_nodo(k)))
                    degree[k] += 1
                    degree[nodos] += 1
                    if degree[nodos] == d:
                        break
                    continue
    g.save_gephi('barabasiAlbert' + str(n) + '_' + str(d))
    return print('ok')
         

     
K = barabasiAlbertGraph(500, 5)