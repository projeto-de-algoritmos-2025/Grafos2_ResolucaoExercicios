import heapq

class Solution(object):
    def shortestPath(self, grid, k):
        m, n = len(grid), len(grid[0])

        # Fila de prioridade (min-heap): (distância, x, y, obstáculos restantes)
        pq = [(0, 0, 0, k)]  # Começamos no (0, 0) com 0 passos e k obstáculos restantes
        # Distâncias: dist[x][y][obstacles_left] -> menor número de passos para chegar a (x, y) com obstacles_left restantes
        dist = [[[float('inf')] * (k + 1) for _ in range(n)] for _ in range(m)]
        dist[0][0][k] = 0  # Inicializa a célula inicial

        # Direções de movimento (cima, baixo, esquerda, direita)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while pq:
            steps, x, y, remaining_obstacles = heapq.heappop(pq)

            # Se chegamos ao destino
            if x == m - 1 and y == n - 1:
                return steps

            # Tentar todas as direções possíveis
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Verificar se está dentro dos limites
                if 0 <= nx < m and 0 <= ny < n:
                    # Se não há obstáculo
                    if grid[nx][ny] == 0 and steps + 1 < dist[nx][ny][remaining_obstacles]:
                        dist[nx][ny][remaining_obstacles] = steps + 1
                        heapq.heappush(pq, (steps + 1, nx, ny, remaining_obstacles))
                    
                    # Se há obstáculo, e ainda podemos eliminar um
                    if grid[nx][ny] == 1 and remaining_obstacles > 0 and steps + 1 < dist[nx][ny][remaining_obstacles - 1]:
                        dist[nx][ny][remaining_obstacles - 1] = steps + 1
                        heapq.heappush(pq, (steps + 1, nx, ny, remaining_obstacles - 1))

        # Se não for possível alcançar o destino
        return -1