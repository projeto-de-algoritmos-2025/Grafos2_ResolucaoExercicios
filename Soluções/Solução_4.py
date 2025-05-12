import heapq

class Solution(object):
    def minimumObstacles(self, grid):
        m, n = len(grid), len(grid[0])
        
        # Definir as direções de movimento (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Min-heap para o algoritmo de Prim (baseado em heap)
        heap = [(0, 0, 0)]  # (obstáculos removidos, x, y)
        
        # Matriz para armazenar o número mínimo de obstáculos removidos para cada célula
        obstacles = [[float('inf')] * n for _ in range(m)]
        obstacles[0][0] = 0
        
        while heap:
            removed, x, y = heapq.heappop(heap)
            
            # Se chegamos ao canto inferior direito, retornamos o número de obstáculos removidos
            if x == m - 1 and y == n - 1:
                return removed
            
            # Explorar os vizinhos
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Verificar se as novas coordenadas estão dentro do grid
                if 0 <= nx < m and 0 <= ny < n:
                    new_removed = removed + grid[nx][ny]  # Se for obstáculo, aumenta 1
                    
                    # Se encontramos um caminho com menos obstáculos removidos, atualizamos
                    if new_removed < obstacles[nx][ny]:
                        obstacles[nx][ny] = new_removed
                        heapq.heappush(heap, (new_removed, nx, ny))
        
        # Caso não consiga encontrar caminho (o que não é esperado pela definição do problema)
        return -1
