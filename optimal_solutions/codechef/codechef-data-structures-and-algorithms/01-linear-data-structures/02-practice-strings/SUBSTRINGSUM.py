


def solve():
    def beauty_sum(s):
        n = len(s)
        total = 0

        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1
                nonzero = [f for f in freq if f > 0]
                total += max(nonzero) - min(nonzero)
        return total


if __name__ == "__main__":
    solve()
