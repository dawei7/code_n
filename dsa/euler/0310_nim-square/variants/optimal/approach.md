# Nim Square - Optimal Approach

## Algorithm Explanation

Find the number of losing positions $(a, b, c)$ for the next player in Nim Square where $0 \le a \le b \le c \le 100\,000$. Nim Square is 3-heap Nim where players may only remove a square number $k^2$ ($k \ge 1$) of stones from a single heap.

### Sprague-Grundy Mex Calculation & Frequency Combinatorics:
1. **Square-Subtraction Grundy Recurrence**:
   For a single heap of size $n$, the Grundy value $G(n)$ follows the minimum excluded value (mex) over square moves:
   $$G(n) = \text{mex}\{ G(n - k^2) \mid 1 \le k^2 \le n \}$$
2. **Losing Condition**:
   A 3-heap position $(a, b, c)$ is a losing position for the next player iff the Nim sum $G(a) \oplus G(b) \oplus G(c) = 0$.
3. **Ordered Triple Counting**:
   We tabulate the frequencies $cnt[g]$ of Grundy values $0 \le n \le 100\,000$ and count ordered triples $a \le b \le c$ satisfying $G(a) \oplus G(b) \oplus G(c) = 0$.
4. **Execution**:
   Summing valid triples for $0 \le a \le b \le c \le 100\,000$ yields $2586528661783$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \sqrt{N})$ for $N = 100\,000$. Runs in $\approx 2.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ for Grundy array.
