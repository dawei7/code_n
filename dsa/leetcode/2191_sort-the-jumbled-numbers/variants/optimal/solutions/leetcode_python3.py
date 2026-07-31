from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapped_value(number: int) -> int:
            if number == 0:
                return mapping[0]

            place = 1
            result = 0
            while number:
                number, digit = divmod(number, 10)
                result += mapping[digit] * place
                place *= 10
            return result

        return sorted(nums, key=mapped_value)
