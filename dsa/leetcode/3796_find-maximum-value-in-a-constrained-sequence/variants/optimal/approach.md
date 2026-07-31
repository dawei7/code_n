## General

Treat `a[0] = 0` as an upper bound at index `0` and every `[idx, maxVal]` pair as another upper bound. If position `i - 1` cannot exceed `bounds[i - 1]`, then the adjacent rule implies `a[i] <= bounds[i - 1] + diff[i - 1]`. A left-to-right pass propagates every bound in that direction. Symmetrically, a right-to-left pass applies `a[i] <= bounds[i + 1] + diff[i]` and propagates every restriction toward smaller indices.

After both passes, `bounds[i]` is the minimum value allowed by all cones of the form “anchor bound plus cumulative edge distance.” Consequently, no valid sequence can exceed `bounds[i]` at position `i`: doing so would violate either an explicit anchor or some adjacent-difference limit along the path from that anchor.

The complete `bounds` array is itself a valid sequence. Its first value is zero, every entry is non-negative, explicit restrictions were included before propagation, and each pass ensures neighboring values differ by no more than the corresponding `diff`. Thus every pointwise upper bound is simultaneously attainable. The greatest entry of this envelope is exactly the largest value possible in an optimal sequence.

## Complexity detail

Let $N=\texttt{n}$ and $R=\lvert\texttt{restrictions}\rvert$. Initializing the bounds and performing the two directional passes take $O(N)$ time; installing the explicit restrictions takes $O(R)$ time. The total is $O(N+R)$, which is $O(N)$ because $R<N$. The bounds array uses $O(N)$ auxiliary space.

## Alternatives and edge cases

- **Evaluate every anchor at every position:** Prefix edge distances make this direct formula possible, but it takes $O(NR)$ time when restrictions are dense.
- **One directional pass:** Left propagation alone misses restrictions to the right of a position; both directions are necessary.
- **Treat restrictions as exact values:** Each `maxVal` is only an upper bound. Forcing equality can make a feasible instance appear impossible or overstate the answer.
- **Position zero:** The fixed value `a[0] = 0` is an implicit anchor even though restrictions only use positive indices.
- **Loose explicit bounds:** A restriction larger than the value propagated from another anchor has no effect and must be combined with `min`.
- **Unsorted restrictions:** Directly installing bounds by index avoids any dependence on their input order.
