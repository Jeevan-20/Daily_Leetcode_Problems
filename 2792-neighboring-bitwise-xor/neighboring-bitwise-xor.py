class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        
        # First assumption: original[0] = 0
        original1 = [0] * n
        for i in range(1, n):
            original1[i] = original1[i - 1] ^ derived[i - 1]
        computed_derived1 = [original1[i] ^ original1[(i + 1) % n] for i in range(n)]
        if computed_derived1 == derived:
            return True
        original2 = [0]*n
        original2[0] = 1
        for i in range(1, n):
            original2[i] = original2[i - 1] ^ derived[i - 1]
        computed_derived2 = [original2[i] ^ original2[(i + 1) % n] for i in range(n)]
        if computed_derived2 == derived:
            return True
        return False
