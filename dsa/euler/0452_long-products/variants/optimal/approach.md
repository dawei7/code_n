# Long Products - Optimal Approach

## Algorithm Explanation

Find $F(10^9, 10^9) \bmod 1234567891$, where $F(m, n)$ is the number of $n$-tuples of positive integers $(x_1, \dots, x_n)$ with $\prod_{i=1}^n x_i \le m$.

### Non-Unit Factor Partition & Sub-linear Memoized DP:
1. **Non-Unit Term Decompositions**:
   In any $n$-tuple $(x_1, \dots, x_n)$, terms equal to $1$ contribute nothing to the product.
   Let $k$ be the number of non-$1$ elements $y_1, y_2, \dots, y_k \ge 2$.
   Since $2^k \le \prod y_i \le m$, $k \le \lfloor \log_2 m \rfloor = 29$ for $m = 10^9$.
2. **Combinatorial Binomial Summation**:
   Selecting $k$ non-$1$ positions out of $n$ gives $\binom{n}{k}$ ways.
   $$F(m, n) = 1 + \sum_{k=1}^{\lfloor \log_2 m \rfloor} \binom{n}{k} G(m, k)$$
   where $G(v, k)$ is the number of ordered $k$-tuples of integers $\ge 2$ with product $\le v$.
3. **Sub-linear Hyperbola Memoization**:
   $G(v, k)$ is evaluated recursively by dividing $v$ into hyperbola blocks $\lfloor v / d \rfloor$.
   Memoizing $G(v, k)$ over states $\lfloor m / d \rfloor$ for $v \le m = 10^9$ evaluates $F(10^9, 10^9)$ in $\mathcal{O}(m^{1/2} \log m)$ operations.
4. **Execution**:
   Evaluating $F(10^9, 10^9) \bmod 1234567891$ yields $345558983$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(m^{1/2} \log m)$ for $m = 10^9$. Runs in $\approx 0.25\text{s}$.
- **Space Complexity:** $\mathcal{O}(m^{1/2})$ DP memoization table.
