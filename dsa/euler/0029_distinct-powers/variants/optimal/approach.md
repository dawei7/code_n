# Distinct Powers - Optimal Approach

## Algorithm Explanation

Count the number of distinct values of $a^b$ for $2 \le a \le 100$ and $2 \le b \le 100$.

Using a Python set comprehension:
1. Compute $a^b$ for all $99 \times 99 = 9801$ parameter pairs.
2. Store values in a set to eliminate duplicate terms automatically.
3. Return `len(set)`.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^2)$ where $N = 100$. Evaluates in $< 0.005\text{s}$.
- **Space Complexity:** $\mathcal{O}(N^2)$ - Storage for unique set elements.
