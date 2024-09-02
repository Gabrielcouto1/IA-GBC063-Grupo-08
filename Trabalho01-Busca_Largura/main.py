from grafo import Grafo

g = Grafo(num_vertices=4)

g.add_vertice(0, "AAX")
g.add_vertice(1, "IBI")
g.add_vertice(2, "URU")
g.add_vertice(3, "UDI")

g.add_aresta("AAX", "IBI", 69)
g.add_aresta("AAX", "URU", 116)
g.add_aresta("AAX", "UDI", 180)
g.add_aresta("IBI", "UDI", 244)
g.add_aresta("URU", "UDI", 107)

g.print_grafo()

g.get_matriz_adjacencia()

g.bfs("AAX")