from grafo import Grafo, Vertice

g = Grafo()

for i in range(4):
    g.add_vertice(Vertice(i))


g.add_aresta(0,1)
g.add_aresta(0,2)
g.add_aresta(1,2)
g.add_aresta(1,3)
g.add_aresta(2,3)

print(g.get_vertices())

g.print_grafo()
g.get_matriz_adjacencia()
