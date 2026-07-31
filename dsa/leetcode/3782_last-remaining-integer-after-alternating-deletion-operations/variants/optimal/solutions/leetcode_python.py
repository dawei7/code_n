class Solution:
    def lastInteger(self, n: int) -> int:
        def survivor(length: int, from_left: bool) -> int:
            if length == 1:
                return 1

            reduced_index = survivor((length + 1) // 2, not from_left)
            if from_left or length % 2 == 1:
                return 2 * reduced_index - 1
            return 2 * reduced_index

        return survivor(n, True)
