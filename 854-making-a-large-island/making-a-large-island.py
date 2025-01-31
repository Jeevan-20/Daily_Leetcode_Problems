class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_size = {}  
        index = 2  

        def dfs(r, c, idx):
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
                return 0
            grid[r][c] = idx  
            size = 1  
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]: 
                size += dfs(r + dr, c + dc, idx)
            return size
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:  
                    island_size[index] = dfs(r, c, index)
                    index += 1  
        max_island = max(island_size.values(), default=0)  
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:  
                    seen = set()
                    new_size = 1  
                    for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            seen.add(grid[nr][nc]) 
                    new_size += sum(island_size[idx] for idx in seen)
                    max_island = max(max_island, new_size)
        return max_island
