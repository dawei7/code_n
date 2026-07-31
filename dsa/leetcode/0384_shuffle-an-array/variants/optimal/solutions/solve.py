from random import randrange


class Solution:
    def __init__(self, nums: list[int]):
        self.original = nums.copy()

    def reset(self) -> list[int]:
        return self.original.copy()

    def shuffle(self) -> list[int]:
        shuffled = self.original.copy()
        for index in range(len(shuffled) - 1):
            swap_index = randrange(index, len(shuffled))
            shuffled[index], shuffled[swap_index] = (
                shuffled[swap_index],
                shuffled[index],
            )
        return shuffled


def solve(nums: list[int], operations: list[str]) -> list[list[int]]:
    solution = Solution(nums)
    return [getattr(solution, operation)() for operation in operations]
