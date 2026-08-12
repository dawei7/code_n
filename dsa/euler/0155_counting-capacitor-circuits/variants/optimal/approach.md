# Counting Capacitor Circuits - Optimal Approach

## Algorithm Explanation

Find $D(18)$, the total number of distinct capacitance values achievable using up to $n = 18$ identical capacitors of capacitance $C$.

### Rational Fractions & Reciprocal Symmetry:
Represent any circuit capacitance as a reduced fraction $\frac{a}{b}$ ($\gcd(a, b) = 1$).

1. **Reciprocal Duality**:
   If a circuit produces capacitance $\frac{a}{b}$, its dual circuit (swapping all series $\leftrightarrow$ parallel connections) produces $\frac{b}{a}$.
   Therefore, we only need to track reduced fractions with $a \ge b$.
2. **Dynamic Programming Combination**:
   Let $S[k]$ be the set of normalized fractions $\frac{a}{b} \ge 1$ produced using **exactly** $k$ capacitors.
   - Base case: $S[1] = \left\{ \frac{1}{1} \right\}$.
   - For $k = 2 \dots 18$:
     Combine sub-circuits of size $i$ and $j = k - i$ ($1 \le i \le \lfloor k/2 \rfloor$):
     - Parallel sum: $\frac{n_1}{d_1} + \frac{n_2}{d_2} = \frac{n_1 d_2 + n_2 d_1}{d_1 d_2}$.
     - Evaluate combinations over orientation pairs $(n_1/d1, d1/n1)$ and $(n2/d2, d2/n2)$.
3. **Cumulative Count**:
   Expand reciprocal pairs $(a, b)$ and $(b, a)$ across all $\bigcup_{k=1}^{18} S[k]$ and count unique values.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}\left( \sum_{k=2}^n \sum_{i=1}^{\lfloor k/2 \rfloor} |S_i| \cdot |S_{k-i}| \right)$ where $n = 18$. Runs in $\approx 15.2\text{s}$.
- **Space Complexity:** $\mathcal{O}(D(n))$ - Set storing $3,857,447$ distinct integer pairs.
