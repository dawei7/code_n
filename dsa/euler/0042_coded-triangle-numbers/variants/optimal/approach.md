# Coded Triangle Numbers - Optimal Approach

## Algorithm Explanation

A word is a **triangle word** if its alphabetical character sum $V = \sum (\text{ord}(c) - 64)$ is a triangle number $V = \frac{n(n+1)}{2}$.

### Mathematical Test
Solving $n^2 + n - 2V = 0$ for $n$:
$$n = \frac{-1 + \sqrt{1 + 8V}}{2}$$
Thus, $V$ is a triangle number if and only if $8V + 1$ is a **perfect square**.

### Strategy:
1. Parse the list of English words from `words.txt`.
2. For each word, sum $V = \sum (\text{ord}(c) - 64)$.
3. Check if $\lfloor \sqrt{8V + 1} \rfloor^2 == 8V + 1$.
4. Count and return matching triangle words.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot L)$ where $N = 1786$ words and $L \approx 6$ average length. Runs in $< 0.1\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory.
