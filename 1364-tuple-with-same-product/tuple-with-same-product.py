class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_map = defaultdict(int)
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_map[product] += 1        
        for freq in product_map.values():
            if freq > 1:
                count += (freq * (freq - 1)) * 4          
        return count

