from math import gcd


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        common = gcd(a, b)
        answer = 0
        divisor = 1

        while divisor * divisor <= common:
            if common % divisor == 0:
                answer += 1
                if divisor * divisor != common:
                    answer += 1
            divisor += 1

        return answer
