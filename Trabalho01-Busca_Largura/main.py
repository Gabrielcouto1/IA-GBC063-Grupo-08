from grafo import Grafo

g = Grafo(num_vertices=10)

g.add_vertice(0, "AAX") # Araxá
g.add_vertice(1, "IBI") # Ibiá
g.add_vertice(2, "URU") # Uberaba
g.add_vertice(3, "UDI") # Uberlândia
g.add_vertice(4, "SAC") # Sacramento
g.add_vertice(5, "PER") # Perdizes
g.add_vertice(6, "STJ") # Santa Juliana
g.add_vertice(7, "BHZ") # Belo Horizonte
g.add_vertice(8, "FRA") # Franca
g.add_vertice(9, "SCA") # São Carlos

g.add_aresta("AAX", "IBI", 69)
g.add_aresta("AAX", "URU", 116)
g.add_aresta("AAX", "UDI", 180)
g.add_aresta("IBI", "UDI", 244)
g.add_aresta("URU", "UDI", 107)
g.add_aresta("IBI", "PER", 108)
g.add_aresta("PER", "UDI", 132)
g.add_aresta("PER", "FRA", 191)
g.add_aresta("PER", "STJ", 39)
g.add_aresta("STJ", "BHZ", 440)
g.add_aresta("STJ", "SCA", 359)
g.add_aresta("BHZ", "SCA", 593)
g.add_aresta("STJ", "SAC", 80)

g.get_matriz_adjacencia()

cidade_inicial = input("Insira a sigla da cidade inicial para realizar a busca em largura: ")

g.bfs(cidade_inicial.upper())