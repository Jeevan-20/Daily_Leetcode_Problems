from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        left = 0
        total = 0
        max_fruits = 0

        for right in range(n):
            total += fruits[right][1]

            # Shrink window if the segment is too far
            while left <= right:
                l_pos = fruits[left][0]
                r_pos = fruits[right][0]

                # Distance to cover
                dist_left_first = 2 * max(0, startPos - l_pos) + max(0, r_pos - startPos)
                dist_right_first = 2 * max(0, r_pos - startPos) + max(0, startPos - l_pos)

                if min(dist_left_first, dist_right_first) <= k:
                    break  # valid window
                else:
                    total -= fruits[left][1]
                    left += 1  # shrink window

            max_fruits = max(max_fruits, total)

        return max_fruits
