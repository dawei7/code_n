## General
**Complete corner pyramids have tetrahedral capacity**

Walls can supply two of the required neighboring sides, so an optimal stack grows from a room corner. A complete stack of height $h$ has layers containing the first $h$ triangular numbers. Its total capacity and floor footprint are

$$
T_h=\frac{h(h+1)(h+2)}{6}
\qquad\text{and}\qquad
F_h=\frac{h(h+1)}{2}.
$$

Find the greatest $h$ for which $T_h \le n$. Those $T_h$ boxes form the largest complete corner pyramid that fits, and its $F_h$ floor boxes support all of it.

**The unfinished layer grows as a staircase**

Let $r=n-T_h$ be the number of boxes still unplaced. Extend the floor along the edge of the next layer. The first new floor box supports one additional box in this unfinished corner construction, the second raises its available capacity to $1+2$, and after $k$ new floor boxes the extra capacity is

$$
\frac{k(k+1)}{2}.
$$

Therefore the fewest extra floor boxes is the smallest $k$ whose triangular number is at least $r$. The answer is $F_h+k$. This is sufficient because the staircase realizes that capacity, and necessary because fewer than $k$ new support positions can hold only the preceding, smaller triangular number.

**Binary-search both monotone boundaries**

Both formulas increase with their nonnegative integer argument. Binary-search the largest feasible complete height $h$, then binary-search the smallest sufficient staircase length $k$. Integer arithmetic avoids rounding errors near $10^9$.

## Complexity detail
Each binary search examines $O(\log n)$ integer candidates and uses constant-time arithmetic. Only interval endpoints and a few formula values are stored, so the algorithm takes $O(\log n)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Incremental layer construction:** Repeatedly adding complete layers and then staircase boxes is intuitive, but takes $O(\sqrt[3]{n})$ iterations before handling the remainder.
- **Closed-form roots:** Cube-root and square-root estimates can locate both boundaries, but floating-point rounding must be corrected carefully at exact tetrahedral or triangular numbers.
- **One box:** The largest complete height is one and the answer is one floor box.
- **Exact tetrahedral total:** When $n=T_h$, the remainder is zero, so no staircase boxes are added.
- **Just beyond a complete stack:** A remainder of one requires exactly one additional floor box.
- **Large input:** All products must be evaluated with integer arithmetic wide enough for the intermediate cubic expression.
