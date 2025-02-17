from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)  
        def backtrack():
            total = 0
            for letter in count:
                if count[letter] > 0:
                    total += 1  
                    count[letter] -= 1  
                    total += backtrack()  
                    count[letter] += 1  
            return total
        return backtrack()
