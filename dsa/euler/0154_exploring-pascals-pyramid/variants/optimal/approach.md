# Exploring Pascal's Pyramid - Optimal Approach

## Algorithm Explanation

Find the total number of trinomial coefficients $\binom{N}{i, j, k} = \frac{N!}{i! j! k!}$ in the expansion of $(x + y + z)^{200,000}$ ($i + j + k = N = 200,000$) that are divisible by $10^{12} = 2^{12} \times 5^{12}$.

### Prime Valuation & Divisibility Criteria:
Using Legendre's formula for factorial prime powers $v_p(n!)$:
$$v_p\left(\binom{N}{i, j, k}\right) = v_p(N!) - v_p(i!) - v_p(j!) - v_p(k!)$$

A trinomial coefficient is divisible by $10^{12}$ if and only if both conditions hold:
1. $v_5\left(\binom{N}{i, j, k}\right) \ge 12$
2. $v_2\left(\binom{N}{i, j, k}\right) \ge 12$

### Sliced Numpy Array Vectorization:
1. **Precompute Exponent Arrays**:
   Pre-fill Numpy integer arrays `f2[n]` $= v_2(n!)$ and `f5[n]` $= v_5(n!)$ for $n \in [0, N]$ in $\mathcal{O}(N)$ time.
2. **Ordered Search Triples & Vector Slicing**:
   Restrict outer loop $i \in [0, N/3]$.
   For each $i$, slice $j \in [i, (N-i)/2]$ and $k = N - i - j \in [N-2i, N-i-\lfloor(N-i)/2\rfloor]$ in reverse.
3. **Vectorized Masking**:
   Apply zero-copy SIMD array boolean masks `mask5` and `mask2` across array slices.
4. **Multinomial Permutation Sum**:
   Count vector permutations ($1$ for $i=j=k$, $3$ for $2$ equal, $6$ for $3$ distinct).

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^2 / \text{SIMD})$ where $N = 200,000$. Runs in $\approx 8.7\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Exponent array lookup.
