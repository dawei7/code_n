class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        shift = 0
        index = k - 1
        operation = 0

        while index:
            if index & 1:
                shift += operations[operation]
            operation += 1
            index >>= 1

        return chr(ord("a") + shift % 26)
