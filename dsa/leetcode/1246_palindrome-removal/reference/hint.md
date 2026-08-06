## Hint

1. Use dynamic programming.
2. Define `dp[i][j]` as the solution for the subarray spanning indices $i$ through $j$.
3. The source writes that when `S[i] == S[j]`, one possible transition is `dp(i + 1, j + 1)`: on the last move, an existing palindrome can be extended from both sides. Derive the other transitions from the same interval idea.
