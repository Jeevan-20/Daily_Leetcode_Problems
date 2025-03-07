class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if right < 2:
            return [-1, -1]  
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False  
        for num in range(2, int(right**0.5) + 1):
            if is_prime[num]:  
                for multiple in range(num * num, right + 1, num):
                    is_prime[multiple] = False  
        primes = [i for i in range(left, right + 1) if is_prime[i]]
        if len(primes) < 2:
            return [-1, -1]  
        min_diff = float('inf')
        closest_pair = [-1, -1]
        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                closest_pair = [primes[i], primes[i + 1]]
        return closest_pair
