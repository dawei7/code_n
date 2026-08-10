## General

**Fix a peak and make every other tower as tall as legality permits.** A mountain can rise non-decreasingly toward a chosen peak index `i` and fall non-increasingly after it. Towers may be shortened but never raised above `maxHeights[j]`. Once peak `i` is fixed at its maximum allowed height `x = maxHeights[i]`, the best height at every other position is forced greedily.

Moving left from the peak, each tower must be no taller than the tower immediately to its right; otherwise the sequence would decrease while approaching the peak. It must also be no taller than its own cap. If `y` is the height chosen for the position to the right, the greatest legal current height is

`min(y, maxHeights[j])`.

Moving right is symmetric: each tower must be no taller than the previously chosen tower on its left and no taller than its cap, so the same minimum rule applies.

**Following one candidate peak.** For each pair `(i, x)` from `enumerate(maxHeights)`, the solution sets `y = t = x`. Variable `t` is the candidate mountain's total height, initially containing the peak. Variable `y` remembers the last chosen height while expanding.

The first inner loop visits `j = i-1, i-2, ..., 0`. At each position, `y = min(y, maxHeights[j])` chooses the tallest value that respects both the local cap and the already fixed right neighbor. Adding `y` to `t` includes that tower.

Before scanning right, the code resets `y = x` because the right slope starts again from the peak rather than from the far-left height. The second inner loop visits `i+1` through `n-1` and applies the same running minimum. Finally, `ans = max(ans, t)` retains the best peak candidate.

**Why lowering the peak is unnecessary.** For a fixed peak index, starting below `maxHeights[i]` cannot help. Raising the peak toward its cap cannot force either side lower: adjacent side heights are bounded above by the peak, so a larger peak only relaxes that bound. The caps farther away are unchanged. Therefore some optimum using peak index `i` always sets its peak to the full cap.

**Why the running minimum gives the best side.** Consider a position $j<i$ on the left. Its height cannot exceed any cap encountered from $j$ through $i$, because the heights must not decrease on the walk from $j$ toward the peak. Hence

$$
\texttt{height[j]}
\le
\min_{p=j}^{i}\texttt{maxHeights[p]}.
$$

The running-minimum loop assigns exactly this upper bound at every position. It is feasible because those minima are non-decreasing as positions approach the peak. Thus no other legal left side can be taller at any coordinate. The same argument with suffix minima proves optimality of the constructed right side.

**Why testing every peak finds the global answer.** Every beautiful mountain has at least one index that can serve as a peak; a flat maximum plateau may offer several choices. When the outer loop reaches any peak index of an optimal mountain, its greedy construction produces the maximum possible mountain for that fixed index, whose sum is at least the chosen optimum's sum. Since every constructed candidate is itself legal, taking the maximum yields exactly the global optimum.

For `[5,3,4,1,1]` with peak index `0`, the right-running minima are `3,3,1,1`, producing `[5,3,3,1,1]` with sum `13`. The cap `4` at index two is shortened to `3` because allowing it to rise above its left neighbor would violate the non-increasing right side.

**The exact source is quadratic.** The package manifest says this solution combines prefix and suffix sums with monotonic stacks in $O(n)$ time. That description belongs to the advanced Beautiful Towers II technique, not to this checked-in implementation. This source explicitly expands left and right for every peak. The quadratic algorithm is still acceptable here because this version limits $n$ to `1000`.

## Complexity detail

For peak `i`, the two inner loops together visit exactly `i + (n-1-i) = n-1` non-peak positions. Repeating for all $n$ peaks performs $n(n-1)$ position updates, so time is $\Theta(n^2)$, not $O(n)$.

The algorithm stores only scalar variables `ans`, `n`, `i`, `x`, `y`, `t`, and `j`. It does not construct the candidate height arrays, so auxiliary space is $O(1)$. Python integers safely hold the maximum sum, which can reach $10^{12}$ for this problem. The input array is not modified.

The manifest's stated $O(n)$ time and $O(n)$ space do not match the protected source. A monotonic-stack implementation can attain those bounds, but it is a different algorithm.

## Alternatives and edge cases

- **Monotonic-stack prefix and suffix sums:** Compute the best constrained sum ending at every index from the left and from the right, then combine them. This gives $O(n)$ time and $O(n)$ space and is the true optimal asymptotic method.
- **Materializing each mountain:** Building a full temporary array per peak is conceptually similar but adds unnecessary $O(n)$ working space; the source accumulates its sum directly.
- **Peak at an endpoint:** One side loop is empty, and the other side's running minima correctly form a one-sided mountain.
- **Flat peak plateau:** Equal adjacent maximum heights are allowed because mountain inequalities are non-strict. Testing every index safely covers any plateau.
- **Single tower:** Both inner loops are empty, so the only cap is used and returned.
- **Very low cap away from the peak:** Once the running minimum drops, all farther towers on that side can be no higher until an even lower cap appears.
- **Large sums:** Fixed-width implementations need 64-bit accumulation even though individual heights fit 32 bits.
- **Manifest mismatch:** Complexity documentation must follow the loops that execute; calling this exact source a monotonic-stack solution would be misleading.
