# Ordered Fractions - Optimal Approach

## Algorithm Explanation

Find the numerator of the reduced proper fraction $\frac{n}{d}$ immediately to the left of $\frac{3}{7}$ for $d \le 1000000$.

### Farey Sequence Property:
For a fixed denominator $d$, the largest numerator $n$ satisfying $\frac{n}{d} < \frac{3}{7}$ is:
$$n = \left\lfloor \frac{3d - 1}{7} \right\rfloor$$

The closest fraction across all denominators $d \le 1000000$ occurs at a denominator within $7$ steps of the upper limit $1000000$.
Iterating $d \in [1000000-6, 1000000]$ and maximizing $\frac{n}{d}$ identifies the exact numerator in $\mathcal{O}(1)$ time.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ - Checks $7$ constant bounds. Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
