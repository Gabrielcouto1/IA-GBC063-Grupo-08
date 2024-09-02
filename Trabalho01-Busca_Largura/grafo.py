from collections import deque

class Grafo:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz_adjacencia = [[0] * num_vertices for i in range(num_vertices)]
        self.vertices = {}

    def add_vertice(self, id, nome):
        
        if nome in self.vertices.values():
            print(f"Erro: O vértice com nome '{nome}' já existe!")
            return False
        
        if id not in self.vertices:
            self.vertices[id] = nome
            return True
        return False

    def add_aresta(self, v1_nome, v2_nome, peso):
        v1_index = v2_index = None

        for id, nome in self.vertices.items():
            if nome == v1_nome:
                v1_index = id
            if nome == v2_nome:
                v2_index = id
        
        if v1_index is None or v2_index is None or peso <= 0:
            return False

        self.matriz_adjacencia[v1_index][v2_index] = peso
        self.matriz_adjacencia[v2_index][v1_index] = peso
        return True
    
    def get_matriz_adjacencia(self):
        ids = list(self.vertices.keys())
        ids.sort()

        print("\t" + "\t".join(self.vertices[i] for i in ids))

        for i in ids:
            linha = [self.vertices[i]]
            for j in ids:
                linha.append(str(self.matriz_adjacencia[i][j]))
            print("\t".join(linha))
            
        print()
        

    def bfs(self, start_nome):
        start_index = None
    
        for id, nome in self.vertices.items():
            if nome == start_nome:
                start_index = id
                break

        if start_index is None:
            print("Vértice inicial não encontrado!")
            return

        visitados = [False] * self.num_vertices
        fila = deque([start_index])
        visitados[start_index] = True

        ordem_visita = []

        while fila:
            vertice_atual = fila.popleft()
            ordem_visita.append(self.vertices[vertice_atual])

            for i in range(self.num_vertices):
                if self.matriz_adjacencia[vertice_atual][i] > 0 and not visitados[i]:
                    fila.append(i)
                    visitados[i] = True

        print("Ordem de visita BFS:", " -> ".join(ordem_visita))