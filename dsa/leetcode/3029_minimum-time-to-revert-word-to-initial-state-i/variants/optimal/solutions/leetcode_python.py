class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)

        for removed in range(k, n, k):
            if word[removed:] == word[: n - removed]:
                return removed // k

        return (n + k - 1) // k
