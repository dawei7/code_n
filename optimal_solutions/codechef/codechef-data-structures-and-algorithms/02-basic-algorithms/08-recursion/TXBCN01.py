


def solve():
    class Solution:
        def canSegmentString(self, inputString, dictionaryWords):
            word_set = set(dictionaryWords)
            n = len(inputString)

            dp = [False] * (n + 1)
            dp[0] = True  # empty string is valid

            for i in range(1, n + 1):
                for j in range(i):
                    if dp[j] and inputString[j:i] in word_set:
                        dp[i] = True
                        break

            return dp[n]


if __name__ == "__main__":
    solve()
