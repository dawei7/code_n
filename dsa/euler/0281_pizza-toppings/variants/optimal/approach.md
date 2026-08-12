# Pizza Toppings - Optimal Approach

## Algorithm Explanation

Find the sum of all $f(m, n) \le 10^{15}$, where $f(m, n)$ is the number of distinct circular arrangements of $m \ge 2$ toppings on $m \cdot n$ slices such that each topping appears on exactly $n \ge 1$ slices (ignoring rotations).

### Burnside's Lemma / Pólya Enumeration Theorem:
1. **Symmetry Group Action**:
   The rotational symmetry group of $m \cdot n$ slices is cyclic group $C_{m \cdot n}$ of order $m \cdot n$.
2. **Fixed Point Counting**:
   A rotation by $k$ positions ($0 \le k < m \cdot n$) decomposes into $g = \gcd(k, m \cdot n)$ cycles of length $m \cdot n / g$.
   For an arrangement to be invariant, elements in each cycle must receive the same topping.
   This requires $g = m \cdot d$ for some divisor $d \mid n$.
   The number of valid cycle colorings is $\frac{(m d)!}{(d!)^m}$.
3. **Burnside Closed Form**:
   $$f(m, n) = \frac{1}{m \cdot n} \sum_{d \mid n} \phi\left( \frac{n}{d} \right) \frac{(m d)!}{(d!)^m}$$
4. **Execution**:
   Summing all $f(m, n) \le 10^{15}$ over $m \ge 2, n \ge 1$ yields $1485776387445623$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(M_{\max} \cdot N_{\max} \log N_{\max})$ where $M_{\max}, N_{\max} \le 30$. Runs in $\approx 0.00\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
