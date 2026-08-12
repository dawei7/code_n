# Cuboid Route - Optimal Approach

## Algorithm Explanation

Find the least maximum side length $M$ such that the number of cuboids with integer shortest surface route exceeds $1,000,000$.

### Surface Geodesic Unfolding
For a cuboid with dimensions $a \ge b \ge c \ge 1$:
Unfolding the 3D surfaces onto a 2D plane reveals that the shortest surface path length is $\sqrt{a^2 + (b + c)^2}$.

Let $S = b + c$ where $2 \le S \le 2a$.
For an integer path, $a^2 + S^2$ must be a perfect square.

For a valid pair $(b, c)$ satisfying $a \ge b \ge c \ge 1$:
- If $S \le a$: Number of valid pairs is $\lfloor S / 2 \rfloor$.
- If $S > a$: Number of valid pairs is $a - \lfloor (S - 1) / 2 \rfloor$.

### Strategy:
Increment $a = 1, 2 \dots$, test all $S \in [2, 2a]$ for perfect square $a^2 + S^2$, accumulate valid $(b, c)$ counts, and return $a$ when total count exceeds $1,000,000$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(M^2)$ where $M \approx 1818$. Runs in $< 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Memory overhead is constant.
