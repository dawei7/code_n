from typing import List


class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        components = []
        place_value = 1

        while n:
            digit = n % 10
            if digit:
                components.append(digit * place_value)
            n //= 10
            place_value *= 10

        components.reverse()
        return components
