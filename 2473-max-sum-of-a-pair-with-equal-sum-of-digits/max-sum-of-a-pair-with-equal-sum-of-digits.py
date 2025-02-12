from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(n: int) -> int:
            return sum(int(d) for d in str(n))

        digit_sum_map = {}
        max_sum = -1

        for num in nums:
            d_sum = digit_sum(num)
            if d_sum in digit_sum_map:
                max_sum = max(max_sum, num + digit_sum_map[d_sum])
                digit_sum_map[d_sum] = max(num, digit_sum_map[d_sum])
            else:
                digit_sum_map[d_sum] = num

        return max_sum
