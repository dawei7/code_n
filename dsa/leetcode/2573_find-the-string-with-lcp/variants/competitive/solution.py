class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        letters = [""] * n
        next_letter = ord("a")

        for i in range(n):
            if letters[i]:
                continue
            if next_letter > ord("z"):
                return ""
            letter = chr(next_letter)
            next_letter += 1
            for j in range(i, n):
                if lcp[i][j] > 0:
                    letters[j] = letter

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                expected = 0
                if letters[i] == letters[j]:
                    expected = 1
                    if i + 1 < n and j + 1 < n:
                        expected += lcp[i + 1][j + 1]
                if lcp[i][j] != expected:
                    return ""

        return "".join(letters)
