# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 01:38:53 2024

@author: vlope
"""

from Clases import Grafo, Nodo, Edge, Undirected_graph
import random


def graphGilbert(n,p,nodo_s=0):
    """Genera un grafo con el modelo de Gilbert.
    Crea n nodos y crea una arista entre cada par con probabilidad p.
    También se generan los grafos de BFS y DFS (recursivo e iterativo).
    
    Args:
        n (int): Indica la cantidad de nodos en el grafo.
        p (float): Probabilidad de crear una arista.
        nodo_s (int): Nodo raíz desde donde se inician las búsquedas.
        
    Returns:
        _DOT_: Archivo que contiene los nodos y aristas del grafo.
    """
    if n < 1 or p < 0 or p > 1:
        raise ValueError()
        
    if nodo_s > n:
        raise ValueError()
    
    enlaces = ((n*(n-1))/2)*(p)
    
    g = Grafo()
    
    nodos_list = []
    
    for i in range(n):
        g.add_nodo(Nodo(i))
        nodos_list.append(i)
        
    edge_list = []
    
    while len(edge_list) <= enlaces:
        node1 = random.choice(nodos_list)
        node2 = random.choice(nodos_list)
        if node1 != node2:
            arista = Edge(g.get_nodo(node1), g.get_nodo(node2))
            if arista not in edge_list:
               edge_list.append(arista)
               g.add_edge(arista)
    
    g.save_gephi('gilbert' + str(n) + '_' + str(p))
    g.bfs(g.get_nodo(nodo_s), 'gilbert_bfs' + str(n) + '_' + str(p))
    g.dfs_recursivo(g.get_nodo(nodo_s), 'gilbert_dfsrec' + str(n) + '_' + str(p))
    g.dfs_iterativo(g.get_nodo(nodo_s), 'gilbert_dfsit' + str(n) + '_' + str(p))
    g.dijkstra(nodo_s)
    g.prim(nodo_s)  
    g.kruskal(n) 
    g.kruskalInv()
    g.dibujoSpring()
    g.dibujoForce_D()


   
