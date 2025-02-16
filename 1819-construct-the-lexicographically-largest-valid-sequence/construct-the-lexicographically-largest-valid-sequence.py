from typing import List
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        sequence = [0] * (2 * n - 1)  
        used = set()  
        def backtrack(index):
            if index == len(sequence):  
                return True
            if sequence[index] != 0:  
                return backtrack(index + 1)
            for num in range(n, 0, -1): 
                if num in used:
                    continue
                if num == 1:
                    sequence[index] = 1
                    used.add(1)
                    if backtrack(index + 1):
                        return True
                    sequence[index] = 0
                    used.remove(1)
                else:
                    second_index = index + num
                    if second_index < len(sequence) and sequence[second_index] == 0:
                        sequence[index] = sequence[second_index] = num
                        used.add(num)
                        if backtrack(index + 1):
                            return True
                        sequence[index] = sequence[second_index] = 0
                        used.remove(num)
            return False
        backtrack(0)
        return sequence

