class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        modulo = 1_000_000_007
        length = len(s)

        next_same = [length] * length
        latest = {}
        for index in range(length - 1, -1, -1):
            next_same[index] = latest.get(s[index], length)
            latest[s[index]] = index

        previous_same = [-1] * length
        latest.clear()
        for index, character in enumerate(s):
            previous_same[index] = latest.get(character, -1)
            latest[character] = index

        dp = [[0] * length for _ in range(length)]
        for index in range(length):
            dp[index][index] = 1

        for interval_length in range(2, length + 1):
            for left in range(length - interval_length + 1):
                right = left + interval_length - 1

                if s[left] != s[right]:
                    value = dp[left + 1][right] + dp[left][right - 1]
                    if interval_length > 2:
                        value -= dp[left + 1][right - 1]
                else:
                    inner = dp[left + 1][right - 1] if interval_length > 2 else 0
                    low = next_same[left]
                    high = previous_same[right]

                    if low > high:
                        value = 2 * inner + 2
                    elif low == high:
                        value = 2 * inner + 1
                    else:
                        duplicated = dp[low + 1][high - 1] if low + 1 <= high - 1 else 0
                        value = 2 * inner - duplicated

                dp[left][right] = value % modulo

        return dp[0][length - 1]
