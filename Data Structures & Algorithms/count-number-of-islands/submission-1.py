class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        visited = set()

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            visited.add((r,c))

            while queue:
                row, col = queue.popleft()
                for rowChange, colChange in directions:
                    newRow = row + rowChange
                    newCol = col + colChange
                    if newRow >= 0 and newRow < rows and newCol >= 0 and newCol < cols and (newRow, newCol) not in visited and grid[newRow][newCol] == "1":
                        visited.add((newRow, newCol))
                        queue.append((newRow, newCol))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    islands += 1
                    bfs(i, j)

        return islands