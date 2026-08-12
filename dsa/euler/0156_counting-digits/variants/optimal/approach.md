# Counting Digits - Optimal Approach

## Algorithm Explanation

Find the sum of all positive integers $n$ for which the total number of occurrences of digit $d$ in the decimal representations of numbers $0 \dots n$ equals $n$ ($f(n, d) = n$), summed across all digits $1 \le d \le 9$.

### Digit Frequency Function $f(n, d)$:
For any integer $n$, digit $d$ occurrences can be counted in $\mathcal{O}(\log_{10} n)$ time by iterating over digit positions $i$:
$$f(n, d) = \sum_{i=0}^{L-1} \left( \text{prefix} \times 10^{L-1-i} + \text{suffix contribution} \right)$$

### Divide-and-Conquer Range Pruning:
Since $f(n, d)$ is monotonically non-decreasing, for any range $[a, b]$, $f(n, d) \in [f(a, d), f(b, d)]$.
1. **Pruning Criterion**:
   A range $[a, b]$ contains no solutions if $f(a, d) > b$ or $f(b, d) < a$.
2. **Recursive Search**:
   If the range passes the pruning test, split into $[a, m]$ and $[m+1, b]$ ($m = \lfloor \frac{a+b}{2} \rfloor$).
3. **Upper Bound**:
   All solutions satisfy $n \le 10^{11}$ since $f(10^{11}, d) = 1.1 \times 10^{11} > n$ for all $n > 10^{11}$.

Sum $s(d)$ over $d \in \{1, 2, \dots, 9\}$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log_{10} N \cdot \text{ActiveBranches})$ per digit $d$ where $N = 10^{11}$. Total execution time $< 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(\log_2 N)$ - Recursion depth.
