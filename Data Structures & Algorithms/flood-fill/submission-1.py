class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        originalColour = image[sr][sc]
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        if originalColour == color:
            return image

        q = deque()
        q.append((sr, sc))
        visited = set()
        visited.add((sr, sc))
        image[sr][sc] = color

        while q:
            row, col = q.popleft()

            for rowChange, colChange in directions:
                newRow = row + rowChange
                newCol = col + colChange
                if newRow >= 0 and newRow < rows and newCol >= 0 and newCol < cols and (newRow, newCol) not in visited and image[newRow][newCol] == originalColour:
                    image[newRow][newCol] = color
                    visited.add((newRow, newCol))
                    q.append((newRow, newCol))
                    
        return image