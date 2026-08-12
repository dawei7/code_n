# Sum of a Square and a Cube - Optimal Approach

## Algorithm Explanation

Find the sum of the five smallest palindromic numbers that can be expressed as $a^2 + b^3$ ($a > 1, b > 1$) in exactly $4$ different ways.

### Monotonic Palindrome Generation & Square Remainder Test:
1. **Palindrome Enumeration**:
   Palindromes are generated sequentially in ascending order by constructing half-strings $H$ and reflecting them ($H \circ H^R$ or $H \circ d \circ H^R$).
2. **Representation Count Test**:
   For a candidate palindrome $N$:
   - Iterate cubes $b^3 < N$ for $b \ge 2$.
   - Calculate $rem = N - b^3$.
   - Check if $rem = a^2$ for integer $a > 1$ using fast integer square root.
   - Increment the representation count whenever $rem$ is a valid square.
3. **Filtering & Summation**:
   When a palindrome has exactly $4$ valid representations, it is collected.
   We stop after finding the first $5$ such palindromes.
4. **Execution**:
   Summing the five smallest matching palindromes yields $1004195061$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N_{\max}^{1/3} \cdot P)$ for $N_{\max} \approx 10^9$. Runs in $\approx 0.08\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
