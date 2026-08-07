class Solution:
    def countHousePlacements(self, n: int) -> int:
        modulus = 1_000_000_007
        ending_empty = 1
        ending_house = 1

        for _ in range(2, n + 1):
            ending_empty, ending_house = (
                ending_empty + ending_house,
                ending_empty,
            )

        one_side = (ending_empty + ending_house) % modulus
        return one_side * one_side % modulus
