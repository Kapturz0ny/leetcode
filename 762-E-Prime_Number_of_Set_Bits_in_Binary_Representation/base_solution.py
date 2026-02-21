class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes_count = 0
        for num in range(left, right+1):
            bits_cnt = 0
            while num > 0:
                if num % 2 == 1:
                    bits_cnt += 1
                num //= 2

            if self.is_prime(bits_cnt):
                primes_count += 1

        return primes_count
    
    def is_prime(self, num: int) -> bool:
        if num <= 1:
            return False
        if num == 2:
            return True
        for i in range(2, num):
            if num % i == 0:
                return False
        return True