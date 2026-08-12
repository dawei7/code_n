# Smallest Multiple - Optimal Approach

## Algorithm Explanation

The smallest positive integer divisible by all numbers $1, 2, \dots, N$ is the **Least Common Multiple (LCM)** of that set:
$$\text{LCM}(1, 2, \dots, N)$$

Using the binary LCM recurrence:
$$\text{LCM}(a, b) = \frac{a \times b}{\text{GCD}(a, b)}$$

We compute the accumulated LCM across the range $1 \le k \le 20$ sequentially using Python's built-in `math.lcm(*range(1, 21))`.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log N)$ - Executing Euclidean GCD for each integer $1 \le k \le N$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary space is constant.
