class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        i = j = 0

        while i < n or j < n:
            while i < n and start[i] == "_":
                i += 1
            while j < n and target[j] == "_":
                j += 1

            if i == n or j == n:
                return i == n and j == n

            piece = start[i]
            if piece != target[j]:
                return False
            if piece == "L" and i < j:
                return False
            if piece == "R" and i > j:
                return False

            i += 1
            j += 1

        return True
