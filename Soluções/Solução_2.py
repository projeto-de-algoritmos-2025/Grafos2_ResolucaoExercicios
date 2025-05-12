import heapq

class Solution(object):
    def findAnswer(self, n, edges):
        # Criar o grafo
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def dijkstra(source):
            dist = [float('inf')] * n
            dist[source] = 0
            heap = [(0, source)]

            while heap:
                d, u = heapq.heappop(heap)
                if d > dist[u]:
                    continue
                for v, w in graph[u]:
                    if dist[v] > d + w:
                        dist[v] = d + w
                        heapq.heappush(heap, (dist[v], v))

            return dist

        # Dijkstra a partir dos dois lados
        dist_from_start = dijkstra(0)
        dist_from_end = dijkstra(n - 1)

        # Se não há caminho de 0 até n - 1
        if dist_from_start[n - 1] == float('inf'):
            return [False] * len(edges)

        min_total = dist_from_start[n - 1]

        # Verificar se a aresta está em algum caminho mínimo
        result = []
        for u, v, w in edges:
            is_on_path = (
                dist_from_start[u] + w + dist_from_end[v] == min_total or
                dist_from_start[v] + w + dist_from_end[u] == min_total
            )
            result.append(is_on_path)

        return result
