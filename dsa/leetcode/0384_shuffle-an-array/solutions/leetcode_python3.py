from random import randrange


class Solution:
    def __init__(self, nums: List[int]):
        self.original = nums.copy()

    def reset(self) -> List[int]:
        return self.original.copy()

    def shuffle(self) -> List[int]:
        shuffled = self.original.copy()
        for index in range(len(shuffled) - 1):
            swap_index = randrange(index, len(shuffled))
            shuffled[index], shuffled[swap_index] = shuffled[swap_index], shuffled[index]
        return shuffled
