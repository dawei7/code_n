## General

Sort the hen positions and grain positions. For a proposed time limit $T$, process hens from left to right while keeping an index at the leftmost uneaten grain. A hen should cover a consecutive prefix of the remaining grains: assigning a farther grain while leaving a nearer one for a later hen can only make the later assignment harder.

**Farthest reachable grain after covering the leftmost one**

Suppose the next grain is at $g$ and the current hen starts at $h$.

If $g \geq h$, the hen never needs to move left. It can eat every remaining grain through position $h+T$.

If $g<h$, let $d=h-g$. The hen must first ensure that the grain at $g$ is covered. When $d>T$, this hen cannot reach it, and no later hen can reach it either. Otherwise, a route that also extends right can use either order:

- go left first and then right, allowing a right reach of $h+T-2d$;
- go right first and return left to $g$, allowing a right reach of $h+\lfloor(T-d)/2\rfloor$.

The larger of these two reaches is optimal. Advance the grain index across every position at or before that reach, then continue with the next hen. This feasibility test is monotone: if time $T$ works, every larger time also works.

Binary-search the smallest feasible $T$. A bound of $2\cdot10^9$ is always sufficient because all positions lie between $0$ and $10^9$, even when one hen must cover grains on both sides.

## Complexity detail

Let $n=\lvert\texttt{hens}\rvert$, $m=\lvert\texttt{grains}\rvert$, and let $C=2\cdot10^9+1$ denote the binary-search range size. Sorting costs $O(n\log n+m\log m)$. Each feasibility test advances monotonically through both arrays in $O(n+m)$ time, and binary search performs $O(\log C)$ tests. The total time is $O(n\log n+m\log m+(n+m)\log C)$.

The app-local implementation stores sorted copies of both inputs, using $O(n+m)$ auxiliary space.

## Alternatives and edge cases

- **Dynamic programming over assignments:** Contiguous grain groups can be assigned to hens with DP, but direct transitions are substantially slower than the monotone feasibility scan.
- **Deleting eaten grains from the front:** This preserves the greedy logic but shifts a list repeatedly and can make each feasibility probe quadratic.
- **Grains on both sides:** Both possible turn orders must be considered; always visiting the left side first can underestimate the achievable right reach.
- **Duplicate positions:** Multiple grains at one coordinate are consumed together, and the pointer naturally advances across all of them.
- **Zero time:** The binary search includes $T=0$, which succeeds exactly when stationary hens already cover all grain positions.
- **Large coordinates:** The answer and intermediate reaches fit in 64-bit signed arithmetic in fixed-width languages.
