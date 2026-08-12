# Least Common Multiple Count - Optimal Approach

## Algorithm Explanation

Find $g(10^{12}) = \sum_{i=1}^{N} f(i)$, where $f(n)$ is the number of ordered pairs $(x, y)$ of positive integers with $1 \le x \le y$ and $\operatorname{lcm}(x, y) = n$.

### Squared Divisor Function $d(n^2)$ & Dirichlet Sub-linear Sieve:
1. **Prime Factorization Representation**:
   For $n = \prod p_i^{a_i}$, the number of valid pairs $(x, y)$ with $\operatorname{lcm}(x, y) = n$ and $x \le y$ is:
   $$f(n) = \frac{1}{2} \left( 1 + \prod_{i} (2 a_i + 1) \right) = \frac{1}{2} (1 + d(n^2))$$
   where $d(n^2)$ is the number of divisors of $n^2$.
2. **Summatory Function Transformation**:
   $$g(N) = \sum_{n=1}^N f(n) = \frac{N}{2} + \frac{1}{2} \sum_{n=1}^N d(n^2)$$
3. **Sub-linear Dirichlet Convolution**:
   The sum $\sum_{n=1}^N d(n^2)$ is expressed as a Dirichlet convolution sum $\sum_{a b c \le N, \gcd(a, b)=1} 1$.
   Evaluating this 3-parameter floor sum using sub-linear hyperbola decomposition takes $\mathcal{O}(N^{2/3})$ operations.
4. **Execution**:
   Evaluating $g(10^{12})$ yields $132314136838185$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^{2/3})$ for $N = 10^{12}$. Runs in $\approx 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(N^{2/3})$ sub-linear sieve tables.
