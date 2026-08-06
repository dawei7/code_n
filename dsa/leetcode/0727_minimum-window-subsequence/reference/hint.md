## Hint

For a target prefix `T[:j]` and a right endpoint `e`, let `dp[j][e] = s` store the greatest starting index `s` such that `S[s:e+1]` contains that target prefix in the required subsequence order. Maximizing the start for a fixed endpoint gives the shortest corresponding window.
