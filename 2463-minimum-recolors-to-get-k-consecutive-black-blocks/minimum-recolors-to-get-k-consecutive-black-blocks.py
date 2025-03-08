class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_changes = blocks[:k].count('W')
        current_changes = min_changes    
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                current_changes -= 1
            if blocks[i] == 'W':
                current_changes += 1        
            min_changes = min(min_changes, current_changes)
        
        return min_changes
