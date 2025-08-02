from collections import Counter
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        total = count1 + count2

        for fruit in total:
            if total[fruit] % 2 != 0:
                return -1  

        extra1, extra2 = [], []
        for fruit in total:
            half = total[fruit] // 2
            if count1[fruit] > half:
                extra1.extend([fruit] * (count1[fruit] - half))
            elif count2[fruit] > half:
                extra2.extend([fruit] * (count2[fruit] - half))

        if len(extra1) != len(extra2):
            return -1

        extra1.sort()
        extra2.sort(reverse=True)

        min_val = min(min(basket1), min(basket2))
        total_cost = 0

        for a, b in zip(extra1, extra2):
            total_cost += min(min(a, b), 2 * min_val)

        return total_cost
