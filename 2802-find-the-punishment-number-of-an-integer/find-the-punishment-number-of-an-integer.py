class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(s, target, index=0, current_sum=0):
            if index == len(s):
                return current_sum == target
            
            num = 0
            for i in range(index, len(s)):
                num = num * 10 + int(s[i])
                if can_partition(s, target, i + 1, current_sum + num):
                    return True
            
            return False

        total = 0
        for i in range(1, n + 1):
            square_str = str(i * i)
            if can_partition(square_str, i):
                total += i * i

        return total

