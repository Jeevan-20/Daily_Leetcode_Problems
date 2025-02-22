class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class UnionFind:
            def __init__(self, n):
                self.parent = list(range(n + 1))  # Parent array
                self.rank = [0] * (n + 1)  # Rank array for union by rank

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])  # Path compression
                return self.parent[x]

            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)

                if rootX == rootY:
                    return False  # Cycle detected

                if self.rank[rootX] > self.rank[rootY]:
                    self.parent[rootY] = rootX
                elif self.rank[rootX] < self.rank[rootY]:
                    self.parent[rootX] = rootY
                else:
                    self.parent[rootY] = rootX
                    self.rank[rootX] += 1

                return True

        n = len(edges)
        uf = UnionFind(n)

        for u, v in edges:
            if not uf.union(u, v):  # If union fails, a cycle is found
                return [u, v]

