# Lychrel Numbers - Optimal Approach

## Algorithm Explanation

A number is considered a **Lychrel number** if it does not produce a palindrome after $49$ iterations of the reverse-and-add process ($n \leftarrow n + \text{reverse}(n)$).

1. For each integer $n \in [1, 9999]$:
2. Initialize `curr = n`.
3. Perform up to $49$ iterations:
   - `curr += int(str(curr)[::-1])`.
   - Test if `str(curr)` is palindromic (`s == s[::-1]`).
   - If a palindrome is formed, $n$ is not Lychrel.
4. If no palindrome is formed within $49$ iterations, $n$ is Lychrel.
5. Return the count of Lychrel numbers under $10000$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot K)$ where $N = 10000$ and $K = 50$ iterations. Runs in $< 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary string memory.
