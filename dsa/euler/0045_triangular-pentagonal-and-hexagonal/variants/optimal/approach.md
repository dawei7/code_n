# Triangular, Pentagonal, and Hexagonal - Optimal Approach

## Algorithm Explanation

Find the next number after $T_{285} = P_{165} = H_{143} = 40755$ that is simultaneously Triangular, Pentagonal, and Hexagonal.

### Mathematical Identity:
Every hexagonal number $H_m$ is automatically a triangle number $T_{2m-1}$:
$$T_{2m-1} = \frac{(2m-1)((2m-1)+1)}{2} = \frac{(2m-1)(2m)}{2} = m(2m-1) = H_m$$

Thus, we do not need to check for Triangular property! We only iterate Hexagonal numbers $H_m = m(2m-1)$ starting from $m = 144$ and test if $H_m$ is Pentagonal ($\sqrt{1 + 24 H_m} \equiv 5 \pmod 6$).

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ where $N \approx 27684$ iterations. Runs in $< 0.005\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
