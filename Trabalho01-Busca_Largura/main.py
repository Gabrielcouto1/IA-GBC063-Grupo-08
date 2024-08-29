from grafo import Grafo, Vertice

g = Grafo()

g.add_vertice(Vertice(0, "AAX"))
g.add_vertice(Vertice(1, "IBI"))
g.add_vertice(Vertice(2, "URU"))
g.add_vertice(Vertice(3, "UDI"))


g.add_aresta("AAX","IBI",69)
g.add_aresta("AAX","URU",116)
g.add_aresta("AAX","UDI",180)
g.add_aresta("IBI","UDI",244)
g.add_aresta("URU","UDI",107)

g.print_grafo()

g.get_matriz_adjacencia()