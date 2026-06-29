


def solve():
    def longestHappyPrefix(s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        lps = [0] * n
        length = 0
        i = 1

        # Build the lps array
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        happyPrefixLength = lps[n - 1]
        return s[:happyPrefixLength]


if __name__ == "__main__":
    solve()
