class Vertice:

    def __init__(self, id):
        self.id = id
        self.vizinhos = []

    def add_vizinho(self, vizinho):
        if vizinho not in self.vizinhos:
            self.vizinhos.append(vizinho)


class Grafo:

    def __init__(self):
        self.vertices = {}

    def __iter__(self):
        return iter(self.vertices.values())
    
    def add_vertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.id not in self.vertices:
            self.vertices[vertice.id] = vertice
            return True
        return False
    
    def add_aresta(self, v1, v2):
        if v1 not in self.vertices or v2 not in self.vertices:
            return False
        
        self.vertices[v1].add_vizinho(v2)
        self.vertices[v2].add_vizinho(v1)
        return True
    
    def get_vertices(self):
        return self.vertices.keys()
    
    def print_grafo(self):
        for vertice in self:
            vizinhos = ', '.join(str(v) for v in vertice.vizinhos)
            print(f"Vertice {vertice.id}: Vizinhos -> {vizinhos}")

    def get_matriz_adjacencia(self):
        for i in range(len(self.vertices)): # printa o cabecalho 
            print(f"\t{i}", end="")
        print("\n") 

        for vertice in self: 
            print(vertice.id, end="") # printa o id do vertice na esquerda
            
            for j in range(len(self.vertices)): # printa se tem adjacencia ou nao
                if j in vertice.vizinhos:
                    print("\t1", end="")
                else:
                    print("\t0", end="")
            print()
        