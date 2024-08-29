class Vertice:

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.vizinhos = []

    def add_vizinho(self, vizinho, peso):
        if vizinho not in self.vizinhos:
            self.vizinhos.append((vizinho, peso))


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
    
    def add_aresta(self, v1, v2, peso):
        for vertice in self:
            if vertice.nome == v1:
                v1_index = vertice.id
            if vertice.nome == v2:
                v2_index = vertice.id
        
        if v1_index not in self.vertices or v2_index not in self.vertices and peso <= 0:
            return False
        
        self.vertices[v1_index].add_vizinho(v2_index, peso)
        self.vertices[v2_index].add_vizinho(v1_index, peso)
        return True
    
    def print_grafo(self):
        for vertice in self:
            vizinhos = ', '.join(str(v) for v in vertice.vizinhos)
            print(f"Vertice {vertice.id}: Vizinhos -> {vizinhos}")

    def get_matriz_adjacencia(self):
        ids = list(self.vertices.keys())
        ids.sort()  

        print("\t" + "\t".join(self.vertices[i].nome for i in ids))

        for i in ids:
            linha = [self.vertices[i].nome]  
            for j in ids:
                peso = 0
                for vizinho, p in self.vertices[i].vizinhos:
                    if vizinho == j:
                        peso = p
                        break
                linha.append(str(peso))
            print("\t".join(linha))
