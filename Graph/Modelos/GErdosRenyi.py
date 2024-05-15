# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:43:17 2024

@author: vlope
"""

from Clases import Grafo, Nodo, Edge
import random


def graphErdosRenyi(n,m,nodo_s=0):
    """Genera un grafo con el modelo de Erdos y Rényi.
    Crea n nodos y al azar se generan m cantidad de aristas.
    También se generan los grafos de BFS y DFS (recursivo e iterativo).
    Args:
        n (int): Indica la cantidad de nodos en el grafo.
        m (int): Número de aristas en el grafo.
        nodo_s (int): Nodo raíz desde donde se inician las búsquedas.
        
    Returns:
        _DOT_: Archivo que contiene los nodos y aristas del grafo.
    """
    g = Grafo()
    
    if nodo_s > n:
        raise ValueError()
    
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
    g.bfs(g.get_nodo(nodo_s), 'ErdosRenyi_bfs'+ str(n) + '_' + str(m))
    g.dfs_recursivo(g.get_nodo(nodo_s), 'ErdosRenyi_dfsrec'+ str(n) + '_' + str(m))
    g.dfs_iterativo(g.get_nodo(nodo_s), 'ErdosRenyi_dfsit'+ str(n) + '_' + str(m))
    g.dijkstra(nodo_s)
              
