from typing import List


class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        def evaluate(first_parity: int) -> tuple[int, int]:
            operations = 0
            largest_lower_choice = -10**10
            smallest_upper_choice = 10**10

            for index, value in enumerate(nums):
                required_parity = first_parity ^ (index & 1)

                if (value & 1) == required_parity:
                    lower_choice = value
                    upper_choice = value
                else:
                    operations += 1
                    lower_choice = value - 1
                    upper_choice = value + 1

                largest_lower_choice = max(largest_lower_choice, lower_choice)
                smallest_upper_choice = min(smallest_upper_choice, upper_choice)

            if len(nums) == 1:
                minimum_range = 0
            else:
                minimum_range = max(
                    1, largest_lower_choice - smallest_upper_choice
                )

            return operations, minimum_range

        even_first = evaluate(0)
        odd_first = evaluate(1)
        minimum_operations = min(even_first[0], odd_first[0])
        minimum_range = min(
            range_value
            for operations, range_value in (even_first, odd_first)
            if operations == minimum_operations
        )

        return [minimum_operations, minimum_range]
