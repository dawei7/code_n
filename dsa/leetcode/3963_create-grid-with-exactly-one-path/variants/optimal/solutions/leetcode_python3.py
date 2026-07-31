class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        return ["." * n] + ["#" * (n - 1) + "." for _ in range(m - 1)]
