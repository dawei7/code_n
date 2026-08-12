# Largest Product in a Series - Optimal Approach

## Algorithm Explanation

We search for the contiguous substring of length $K = 13$ in a $1000$-digit string that maximizes the product of its constituent digits.

1. Store the $1000$-digit string.
2. Slide a window of width $K = 13$ from index $0$ to $1000 - K$.
3. If the window contains `'0'`, skip calculation immediately since the product is $0$.
4. Multiply the $13$ digits using `math.prod()`.
5. Maintain and return the global maximum product.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot K)$ where $N = 1000$ and $K = 13$.
- **Space Complexity:** $\mathcal{O}(N)$ - Memory to store the string digits.
