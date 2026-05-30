"""Dynamic Programming challenges."""

import random
from typing import Any, Optional

from code_n.challenge import Challenge, ChallengeInfo
from code_n.counter import ComplexityClass, get_counter
from code_n.grid import Grid, CellType
from code_n.tracked import TrackedList, TrackedGrid


class FibonacciChallenge(Challenge):
    """Compute the n-th Fibonacci number efficiently."""

    def __init__(self):
        super().__init__()
        self._n_val: int = 0
        self._expected: int = 0

    @property
    def info(self) -> ChallengeInfo:
        return ChallengeInfo(
            id="dp_01",
            name="Fibonacci",
            description=(
                "Compute the n-th Fibonacci number.\n"
                "fib(0)=0, fib(1)=1, fib(n) = fib(n-1) + fib(n-2)\n"
                "Requirement: O(n) - naive recursion (O(2ⁿ)) will FAIL!\n"
                "Use memoization or bottom-up DP."
            ),
            category="dynamic",
            difficulty=3,
            required_complexity=ComplexityClass.O_N,
            hint="Store previously computed values in an array. Build up from fib(0) to fib(n).",
        )

    def setup(self, n: int, seed: Optional[int] = None) -> dict[str, Any]:
        self._n_val = min(n, 40)  # Cap to avoid huge numbers
        self._expected = self._fib(self._n_val)

        # Visualize the DP table
        width = self._n_val + 1
        self.grid = Grid(min(width, 20), 3)
        for i in range(min(width, 20)):
            self.grid.set(i, 0, CellType.EMPTY, "?")
        self.grid.set(0, 0, CellType.SORTED, "0")
        if width > 1:
            self.grid.set(1, 0, CellType.SORTED, "1")

        return {"n": self._n_val}

    def _fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def verify(self, result: Any) -> bool:
        return result == self._expected


class ClimbingStairsChallenge(Challenge):
    """Count ways to climb n stairs (1 or 2 steps at a time)."""

    def __init__(self):
        super().__init__()
        self._n_val: int = 0
        self._expected: int = 0

    @property
    def info(self) -> ChallengeInfo:
        return ChallengeInfo(
            id="dp_02",
            name="Climbing Stairs",
            description=(
                "You are climbing a staircase with n steps.\n"
                "Each time you can climb 1 or 2 steps.\n"
                "How many distinct ways can you reach the top?\n"
                "Requirement: O(n)"
            ),
            category="dynamic",
            difficulty=3,
            required_complexity=ComplexityClass.O_N,
            hint="ways(n) = ways(n-1) + ways(n-2). Same as Fibonacci!",
        )

    def setup(self, n: int, seed: Optional[int] = None) -> dict[str, Any]:
        self._n_val = min(n, 35)
        self._expected = self._climb(self._n_val)

        self.grid = Grid(min(self._n_val + 1, 20), 3)
        for i in range(min(self._n_val + 1, 20)):
            self.grid.set(i, 1, CellType.VALUE, i)
            self.grid.set(i, 0, CellType.EMPTY, "?")

        return {"n": self._n_val}

    def _climb(self, n: int) -> int:
        if n <= 2:
            return max(n, 1)
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

    def verify(self, result: Any) -> bool:
        return result == self._expected


class KnapsackChallenge(Challenge):
    """0/1 Knapsack problem."""

    def __init__(self):
        super().__init__()
        self._weights: list[int] = []
        self._values: list[int] = []
        self._capacity: int = 0
        self._expected: int = 0

    @property
    def info(self) -> ChallengeInfo:
        return ChallengeInfo(
            id="dp_03",
            name="Knapsack",
            description=(
                "0/1 Knapsack: Given items with weights and values, and a capacity,\n"
                "find the maximum total value that fits in the knapsack.\n"
                "Each item can be used at most once.\n"
                "Requirement: O(n * capacity) using DP."
            ),
            category="dynamic",
            difficulty=6,
            required_complexity=ComplexityClass.O_N2,
            hint="Build a 2D table dp[i][w] = max value using first i items with capacity w.",
        )

    def setup(self, n: int, seed: Optional[int] = None) -> dict[str, Any]:
        rng = random.Random(seed)
        num_items = min(n, 15)
        self._capacity = num_items * 3

        self._weights = [rng.randint(1, self._capacity // 2) for _ in range(num_items)]
        self._values = [rng.randint(1, 50) for _ in range(num_items)]
        self._expected = self._solve_knapsack()

        # Visualize items as grid
        self.grid = Grid(num_items, 4)
        self.grid.fill_row(0, list(range(num_items)), CellType.VALUE)
        self.grid.fill_row(1, self._weights, CellType.MARKER)
        self.grid.fill_row(2, self._values, CellType.PATH)

        return {
            "weights": TrackedList(self._weights),
            "values": TrackedList(self._values),
            "capacity": self._capacity,
            "n": num_items,
        }

    def _solve_knapsack(self) -> int:
        n = len(self._weights)
        cap = self._capacity
        dp = [[0] * (cap + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for w in range(cap + 1):
                dp[i][w] = dp[i - 1][w]
                if self._weights[i - 1] <= w:
                    dp[i][w] = max(dp[i][w], dp[i - 1][w - self._weights[i - 1]] + self._values[i - 1])
        return dp[n][cap]

    def verify(self, result: Any) -> bool:
        return result == self._expected


class LCSChallenge(Challenge):
    """Longest Common Subsequence."""

    def __init__(self):
        super().__init__()
        self._seq_a: str = ""
        self._seq_b: str = ""
        self._expected: int = 0

    @property
    def info(self) -> ChallengeInfo:
        return ChallengeInfo(
            id="dp_04",
            name="Longest Common Subsequence",
            description=(
                "Find the length of the longest common subsequence of two strings.\n"
                "A subsequence is a sequence that appears in the same order but not necessarily contiguous.\n"
                "Requirement: O(n * m) where n, m are string lengths."
            ),
            category="dynamic",
            difficulty=6,
            required_complexity=ComplexityClass.O_N2,
            hint="Build dp[i][j] = LCS length of first i chars of A and first j chars of B.",
        )

    def setup(self, n: int, seed: Optional[int] = None) -> dict[str, Any]:
        rng = random.Random(seed)
        length = min(n, 15)
        chars = "ABCDEFGH"
        self._seq_a = "".join(rng.choice(chars) for _ in range(length))
        self._seq_b = "".join(rng.choice(chars) for _ in range(length))
        self._expected = self._solve_lcs()

        # Visualize
        self.grid = Grid(length + 1, length + 1)
        for i, c in enumerate(self._seq_a):
            self.grid.set(i + 1, 0, CellType.VALUE, c)
        for j, c in enumerate(self._seq_b):
            self.grid.set(0, j + 1, CellType.VALUE, c)

        return {"seq_a": self._seq_a, "seq_b": self._seq_b}

    def _solve_lcs(self) -> int:
        m, n = len(self._seq_a), len(self._seq_b)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if self._seq_a[i - 1] == self._seq_b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]

    def verify(self, result: Any) -> bool:
        return result == self._expected
