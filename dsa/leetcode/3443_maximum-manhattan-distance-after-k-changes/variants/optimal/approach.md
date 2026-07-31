## General

After a prefix of length $t$, let its unchanged endpoint be $(x,y)$ and its Manhattan distance be $d=\lvert x\rvert+\lvert y\rvert$. Every move changes the parity of the distance, so $t-d$ is even. More specifically, $(t-d)/2$ moves are canceled by opposing movement along the two axes.

Changing one canceling move into a direction that points away from the origin removes one unit of cancellation and increases the prefix distance by two. Up to `k` such changes can therefore raise the distance to $d+2k$. No length-$t$ path can be farther than $t$, because each unit move increases Manhattan distance by at most one. The best possible distance for this prefix is consequently

$$
\min(t, d+2k).
$$

This bound is achievable: change as many canceling moves as allowed until either `k` is exhausted or every move contributes outward. Scan the original path once, maintain its current coordinates, evaluate this expression for every prefix, and retain the largest value. Changes may be chosen specifically for the prefix that realizes the global maximum; later unused moves do not constrain that choice.

## Complexity detail

Let $n$ be the number of moves. Each direction is processed once, so the time complexity is $O(n)$. Only the two coordinates and the running answer are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Try four target quadrants:** Tracking favorable and unfavorable moves for northeast, northwest, southeast, and southwest is also linear but duplicates the same cancellation calculation.
- **Recompute every prefix:** Summing its coordinates from the beginning for each endpoint costs $O(n^2)$ time.
- **No changes:** With `k = 0`, the formula reduces to the largest Manhattan distance of the original path.
- **Enough changes:** Once $d+2k\ge t$, every move in that prefix can contribute one unit and the distance reaches $t$.
- **Maximum before the end:** Later opposing moves may reduce distance, so every prefix—not only the complete path—must be evaluated.
- **Single move:** Its distance is always one, regardless of whether a change is used.
