# Sum of Digits - Experience #13 - Optimal Approach

## Algorithm Explanation

Find the last 9 digits of $\sum_{i=1}^{17} f(13^i) \bmod 10^9$, where $f(n)$ is the sum of all positive integers without zeros in their decimal representation having digital sum equal to $n$.

### Matrix Exponentiation of Digit Compositions & Values:
1. **Composition Count & Value Recurrences**:
   Let $c(n)$ be the number of non-zero digit compositions of $n$:
   $$c(n) = \sum_{d=1}^9 c(n-d)$$
   Let $f(n)$ be the sum of all numerical values formed by these compositions:
   $$f(n) = \sum_{d=1}^9 \left( 10 \cdot f(n-d) + d \cdot c(n-d) \right)$$
2. **$18 \times 18$ Simultaneous State Matrix**:
   Combining $[c(n), \dots, c(n-8), f(n), \dots, f(n-8)]^T$ into an $18$-element state vector, the transition $T$ is linear.
   For large $N = 13^i$ ($i = 1 \dots 17$), $T^N \bmod 10^9$ is evaluated in $\mathcal{O}(\log N)$ time via binary matrix exponentiation.
3. **Execution**:
   Summing $f(13^i) \bmod 10^9$ for $i = 1 \dots 17$ yields $732385720$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K \cdot \log(13^K))$ for $K = 17$. Runs in $\approx 0.005\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
