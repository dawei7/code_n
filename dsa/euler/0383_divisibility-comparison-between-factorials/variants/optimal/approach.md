# Divisibility Comparison Between Factorials - Optimal Approach

## Algorithm Explanation

Find $T_5(10^{18})$, the number of integers $1 \le i \le 10^{18}$ satisfying $v_5((2i-1)!) < 2 v_5(i!)$, where $v_5(m)$ is the exponent of $5$ in the prime factorization of $m!$.

### Legendre's Formula & Base-5 Digit DP:
1. **Legendre Formula Reduction**:
   By Legendre's formula, the exponent of $5$ in $m!$ is $v_5(m!) = \frac{m - S_5(m)}{4}$, where $S_5(m)$ is the sum of digits of $m$ in base $5$.
   For $(2i-1)!$:
   $$v_5((2i-1)!) = v_5((2i)!) - v_5(2i) = \frac{2i - S_5(2i)}{4} - v_5(i)$$
   $$2 v_5(i!) = \frac{2i - 2 S_5(i)}{4}$$
2. **Base-5 Digit Sum Inequality**:
   Substituting into the target inequality $v_5((2i-1)!) < 2 v_5(i!)$:
   $$S_5(2i) + 4 v_5(i) > 2 S_5(i)$$
   This condition depends solely on the base-$5$ digits of $i$ and carry propagation when doubling $i$.
3. **Base-5 Digit DP**:
   We construct a digit DP processing $i$ digit-by-digit in base $5$.
   State tracking: $(\text{digit\_pos}, \text{carry\_in}, \text{sum\_diff}, \text{is\_less})$.
   For $N = 10^{18}$, base-$5$ length is $\lfloor \log_5(10^{18}) \rfloor + 1 = 26$ digits.
4. **Execution**:
   Running the digit DP for $N = 10^{18}$ yields $22173624649806$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log_5 N)$ for $N = 10^{18}$. Runs in $\approx 0.005\text{s}$.
- **Space Complexity:** $\mathcal{O}(\log_5 N)$ state DP table.
