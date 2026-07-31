from math import isqrt


class Solution:
    def largestPrime(self, n: int) -> int:
        is_prime = bytearray(b"\x01") * (n + 1)
        is_prime[:2] = b"\x00\x00"

        for prime in range(2, isqrt(n) + 1):
            if is_prime[prime]:
                start = prime * prime
                count = (n - start) // prime + 1
                is_prime[start : n + 1 : prime] = b"\x00" * count

        prefix_sum = 0
        answer = 0
        for prime in range(2, n + 1):
            if not is_prime[prime]:
                continue
            prefix_sum += prime
            if prefix_sum > n:
                break
            if is_prime[prefix_sum]:
                answer = prefix_sum

        return answer
