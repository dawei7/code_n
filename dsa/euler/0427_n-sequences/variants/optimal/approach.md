# n-sequences - Optimal Approach

## Algorithm Explanation

Find $f(7\,500\,000) \bmod 1000000009$, where $f(n) = \sum_S L(S)$ over all $n^n$ sequences $S \in \{1, \dots, n\}^n$ and $L(S)$ is the length of the longest contiguous run of equal elements in $S$.

### Generating Functions & Complementary Run-Length Bound Summation:
1. **Tail Expectation Identity**:
   The sum of maximum run lengths equals:
   $$f(n) = \sum_{k=1}^n \Big( n^n - A(n, k) \Big)$$
   where $A(n, k)$ is the number of $n$-sequences in $\{1, \dots, n\}^n$ with no contiguous run of length $\ge k$.
2. **Generating Function for Bounded Runs**:
   The ordinary generating function for sequences with all run lengths $< k$ is:
   $$G_k(x) = \frac{1 + x + \dots + x^{k-1}}{1 - (n-1)(x + x^2 + \dots + x^{k-1})}$$
   $A(n, k)$ equals $n \cdot [x^n] G_k(x)$.
3. **Linear Binomial Coefficient Extraction**:
   $[x^n] G_k(x)$ is extracted as a linear combination of binomial coefficients $\binom{n - j k}{j}$ for $j \ge 0$.
   Evaluating the total sum across all $k = 1 \dots n$ modulo $1000000009$ takes $\mathcal{O}(n)$ time.
4. **Execution**:
   Evaluating $f(7\,500\,000) \bmod 1000000009$ yields $97138867$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ for $N = 7\,500\,000$. Runs in $\approx 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ precomputed factorials.
