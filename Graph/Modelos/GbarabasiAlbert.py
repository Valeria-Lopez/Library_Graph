# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:50:20 2024

@author: vlope
"""

from Clases import Grafo, Nodo, Edge, Undirected_graph


def barabasiAlbertGraph(n, d, nodo_s=0):
    """Genera un grafo con el modelo de Barabási-Albert.
    Se coloca nodo por nodo y se asigna una cantidad de d aristas para que
    cada nuevo nodo se enlace.
    También se generan los grafos de BFS y DFS (recursivo e iterativo).
    
    Args:
        n (int): Indica la cantidad de nodos en el grafo.
        d (int): Grado máximo esperado para cada uno de los nodos nuevos.
        nodo_s (int): Nodo raíz desde donde se inician las búsquedas.
        
    Returns:
        _DOT_: Archivo que contiene los nodos y aristas del grafo.
    """
    g = Grafo()
    
    if nodo_s > n:
        raise ValueError()
     
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
    g.bfs(g.get_nodo(nodo_s), 'barabasiAlbert_bfs' + str(n) + '_' + str(d))
    g.dfs_recursivo(g.get_nodo(nodo_s), 'barabasiAlbert_dfsrec' + str(n) + '_' + str(d))
    g.dfs_iterativo(g.get_nodo(nodo_s), 'barabasiAlbert_dfsit' + str(n) + '_' + str(d))
         
