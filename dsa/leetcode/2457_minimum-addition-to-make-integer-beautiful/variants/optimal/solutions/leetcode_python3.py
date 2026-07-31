class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        original = n
        digit_sum = sum(int(character) for character in str(n))
        place = 1

        while digit_sum > target:
            digit = (n // place) % 10
            if digit == 0:
                place *= 10
                continue

            prefix = n // (place * 10)
            trailing_nines = 0
            scan = prefix
            while scan % 10 == 9:
                trailing_nines += 1
                scan //= 10

            digit_sum = digit_sum - digit + 1 - 9 * trailing_nines
            n += (10 - digit) * place
            place *= 10

        return n - original
