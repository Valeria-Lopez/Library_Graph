# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:18:54 2024

@author: vlope
"""

from Clases import Grafo, Nodo, Edge, Undirected_graph


def graph_malla(m=0,n=0,nodo_s=0):
    """Genera un grafo con el modelo de malla, crea m*n nodos. También se
    generan los grafos de BFS y DFS (recursivo e iterativo).
    
    Args:
        m (int): Número de columnas.
        n (int): Número de filas.
        nodo_s (int): Nodo raíz desde donde se inician las búsquedas.
        
    Returns:
        _DOT_: Archivo que contiene los nodos y aristas del grafo.
    """
    g = Grafo()
    
    if nodo_s > (n*m):
        raise ValueError()
    
    for i in range(m):
        for j in range(n):
            g.add_nodo(Nodo((i * n)+j))
            
    
    for v in g.diccionario.keys():
        for i in range(m):
            for j in range(n):
                if j < n-1:
                    g.add_edge(Edge(g.get_nodo((i*n)+j), g.get_nodo((i*n)+j+1)))   
                if i < m-1:
                    g.add_edge(Edge(g.get_nodo((i*n)+j), g.get_nodo(((i+1)*n)+j)))
    
    g.save_gephi('malla' + str(m) + '_' + str(n))
    g.bfs(g.get_nodo(nodo_s), 'malla_bfs'+ str(m) + '_' + str(n))
    g.dfs_recursivo(g.get_nodo(nodo_s), 'malla_dfsrec'+ str(m) + '_' + str(n))
    g.dfs_iterativo(g.get_nodo(nodo_s), 'malla_dfsit'+ str(m) + '_' + str(n))
    g.dijkstra(nodo_s)

