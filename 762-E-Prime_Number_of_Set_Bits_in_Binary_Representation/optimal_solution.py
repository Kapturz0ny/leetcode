class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        primes_count = 0
        for num in range(left, right+1):
            bits_cnt = bin(num).count('1')
            if bits_cnt in primes:
                primes_count += 1
        return primes_count
