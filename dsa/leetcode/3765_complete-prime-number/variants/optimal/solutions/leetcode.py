class Solution:
    def completePrime(self, num: int) -> bool:
        def is_prime(value: int) -> bool:
            if value < 2:
                return False
            if value % 2 == 0:
                return value == 2

            divisor = 3
            while divisor * divisor <= value:
                if value % divisor == 0:
                    return False
                divisor += 2
            return True

        prefix = num
        while prefix:
            if not is_prime(prefix):
                return False
            prefix //= 10

        suffix = 0
        place = 1
        remaining = num
        while remaining:
            suffix = (remaining % 10) * place + suffix
            if not is_prime(suffix):
                return False
            remaining //= 10
            place *= 10

        return True
