import heapq
from collections import defaultdict

class Solution(object):
    def minimumWeight(self, n, edges, src1, src2, dest):
        """
        :type n: int
        :type edges: List[List[int]]
        :type src1: int
        :type src2: int
        :type dest: int
        :rtype: int
        """

        # Função que implementa o algoritmo de Dijkstra para encontrar as distâncias mínimas
        def dijkstra(start, graph):
            dist = [float('inf')] * n  # Inicializa todas as distâncias como infinito
            dist[start] = 0
            heap = [(0, start)]  # Heap de prioridade com (distância, nó)
            while heap:
                curr_dist, u = heapq.heappop(heap)  # Nó com menor distância
                if curr_dist > dist[u]:  # Se já há um caminho melhor, ignora
                    continue
                for v, weight in graph[u]:  # Para cada vizinho v de u
                    if dist[v] > curr_dist + weight:
                        dist[v] = curr_dist + weight
                        heapq.heappush(heap, (dist[v], v))
            return dist  # Retorna as menores distâncias a partir de start

        # Cria dois grafos: o original (direcionado) e seu reverso
        graph = defaultdict(list)
        rev_graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))         # Grafo original: u → v com peso w
            rev_graph[v].append((u, w))     # Grafo reverso: v ← u com peso w

        # Calcula as distâncias mínimas de src1 e src2 até todos os nós
        dist1 = dijkstra(src1, graph)
        dist2 = dijkstra(src2, graph)

        # Calcula as distâncias mínimas de dest até todos os nós, no grafo reverso
        # Isso equivale a calcular as distâncias de todos os nós até dest no grafo original
        dist3 = dijkstra(dest, rev_graph)

        min_total = float('inf')

        # Para cada nó intermediário i, verifica se ele pode ser alcançado por src1 e src2,
        # e se pode alcançar dest. Se sim, calcula o custo total passando por i.
        for i in range(n):
            if dist1[i] < float('inf') and dist2[i] < float('inf') and dist3[i] < float('inf'):
                min_total = min(min_total, dist1[i] + dist2[i] + dist3[i])

        # Retorna o menor custo possível, ou -1 se não for possível alcançar dest a partir de ambos os fontes
        return -1 if min_total == float('inf') else min_total
