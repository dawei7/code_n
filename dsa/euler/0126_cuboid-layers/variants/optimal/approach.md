# Cuboid Layers - Optimal Approach

## Algorithm Explanation

Find the least integer $n$ for which $C(n) = 1000$, where $C(n)$ represents the number of cuboids (with integer side lengths $x \ge y \ge z \ge 1$) that require exactly $n$ cubes to construct one of their outer layers $k \ge 1$.

### Algebraic Layer Cube Counting Formula:
For a cuboid of dimensions $x \times y \times z$, the $k^{\text{th}}$ outer layer requires:
$$C(x, y, z, k) = 2(xy + yz + zx) + 4(x + y + z + k - 2)(k - 1)$$

### Bounded Frequency Sieve:
1. Set upper search bound $N_{\max} = 20000$.
2. Loop over integer dimensions $1 \le z \le y \le x$:
   - For each tuple $(x, y, z)$, increment layer count $k = 1, 2 \dots$ until $C(x, y, z, k) > N_{\max}$.
   - Increment global frequency counter `counts[C(x, y, z, k)] += 1`.
3. Scan frequency table `counts` sequentially and return the first $n$ where `counts[n] == 1000`.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N_{\max} \cdot \text{Layers})$ over bounded dimension loops. Runs in $< 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(N_{\max})$ - Frequency lookup table.
