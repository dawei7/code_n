# Constants


def solve():
    BIG_MOD = 998244353  # Large prime number
    MOD = 1000000007      # Modulus value for calculations
    MAXN = int(1e3 + 1)   # Maximum size of the input string

    class Solution:
        def count_ways(self, s: str) -> int:
            n = len(s)
            s = " " + s  # Add leading space for 1-based indexing

            # List of lists to hold ranges for each position
            d = [[] for _ in range(n + 1)]
            d[1] = [(1, 1)]  # Initialize first element

            # Fill the ranges for each character
            for i in range(2, n + 1):
                d[i] = [(i, i)]
                if s[i] == s[i - 1]:
                    d[i].append((i - 1, i))
                for j in d[i - 1]:
                    if s[j[0] - 1] == s[i]:
                        d[i].append((j[0] - 1, i))

            # DP array to count ways
            f = [0] * (n + 1)
            f[0] = 1  # Base case

            for i in range(1, n + 1):
                for j in d[i]:
                    f[i] += f[j[0] - 1]
                    f[i] %= MOD

            return f[n]


if __name__ == "__main__":
    solve()
