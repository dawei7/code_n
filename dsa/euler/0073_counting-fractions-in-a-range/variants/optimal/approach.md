# Counting Fractions in a Range - Optimal Approach

## Algorithm Explanation

Count how many reduced proper fractions $\frac{n}{d}$ lie strictly between $\frac{1}{3}$ and $\frac{1}{2}$ for $d \le 12000$.

### Bound Analysis
For a given denominator $d$:
- Lower numerator bound: $\frac{n}{d} > \frac{1}{3} \implies n_{\min} = \lfloor \frac{d}{3} \rfloor + 1$.
- Upper numerator bound: $\frac{n}{d} < \frac{1}{2} \implies n_{\max} = \lfloor \frac{d-1}{2} \rfloor$.

### Search Strategy:
1. Iterate $d \in [4, 12000]$.
2. Iterate $n \in [n_{\min}, n_{\max}]$.
3. Test $\text{GCD}(n, d) == 1$.
4. Accumulate and return total count.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(D^2)$ where $D = 12000$. Evaluates $\approx 1.2 \times 10^7$ pairs in $< 0.4\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
