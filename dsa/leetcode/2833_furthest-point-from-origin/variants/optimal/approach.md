## General

Ignore the flexible moves temporarily. If there are $r$ forced right moves and $l$ forced left moves, their net displacement is

$$
d=r-l.
$$

Let $u$ be the number of `_` characters. Resolving those characters contributes a sum $x$ of $u$ values, each equal to $-1$ or $1$. The final coordinate is $d+x$.

By the triangle inequality,

$$
\lvert d+x\rvert \le \lvert d\rvert+\lvert x\rvert \le \lvert d\rvert+u.
$$

This upper bound is attainable. If $d>0$, direct every flexible move right; if $d<0$, direct every one left. When $d=0$, either common direction works. In all cases the flexible contribution has magnitude $u$ and points in the same direction as the fixed displacement, producing distance $\lvert d\rvert+u$.

Scan `moves` once. Update `displacement` by $-1$ for `L` and $1$ for `R`, count every `_`, and return their formula. This depends only on the terminal coordinate, exactly as required.

## Complexity detail

Let $n$ be the length of `moves`. The scan examines every character once, so it takes $O(n)$ time. Two integer counters use $O(1)$ auxiliary space.

The benchmark uses the string length as `size`, stays within $n \le 50$, and consists entirely of flexible moves. A repeated-prefix simulation rescans all earlier characters for every prefix and performs quadratic total work.

## Alternatives and edge cases

- **Three built-in counts:** Count `L`, `R`, and `_` separately and evaluate the same formula. This is also $O(n)$ time and $O(1)$ auxiliary space, though it may traverse the string three times.
- **Try both uniform resolutions:** Compute the final coordinate when all flexible moves go left and when all go right, then take the larger absolute value. This is another linear-time formulation.
- **Repeated prefix simulation:** Recompute all move counts for every growing prefix and return the last result. It is correct but takes $O(n^2)$ time.
- **No flexible moves:** The answer is simply the absolute difference between the right- and left-move counts.
- **Balanced fixed moves:** If the forced displacement is zero, every flexible move can point either all left or all right to obtain distance $u$.
- **All flexible:** A string of $n$ underscores can finish at coordinate $n$ or $-n$.
- **Opposing forced moves:** The maximum final distance may be zero, as for `"LR"`.
- **Final-state semantics:** A larger distance reached earlier does not matter if later forced moves bring the endpoint closer to the origin.
