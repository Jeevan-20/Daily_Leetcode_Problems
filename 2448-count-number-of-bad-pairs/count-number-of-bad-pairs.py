from typing import List
from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        good_pairs = 0
        n = len(nums)
        
        for i in range(n):
            key = nums[i] - i
            good_pairs += freq[key]  
            freq[key] += 1  
        
        total_pairs = n * (n - 1) // 2  
        return total_pairs - good_pairs  