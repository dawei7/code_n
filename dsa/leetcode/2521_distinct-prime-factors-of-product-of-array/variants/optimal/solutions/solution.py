class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        factors = set()

        for number in nums:
            divisor = 2
            while divisor * divisor <= number:
                if number % divisor == 0:
                    factors.add(divisor)
                    while number % divisor == 0:
                        number //= divisor
                divisor += 1

            if number > 1:
                factors.add(number)

        return len(factors)
