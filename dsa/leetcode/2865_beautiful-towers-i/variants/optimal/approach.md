## General

**Turn each position into a candidate peak**

Fix an index `i` as the peak. On its left, the largest legal mountain is determined greedily: starting from `heights[i]` and moving left, each tower is capped by both its own limit and the tower immediately to its right. The right side is symmetric. Repeating those scans independently for every peak would be correct, but it would revisit the same constrained ranges and take $O(n^2)$ time.

**Reuse the sum beyond the nearest lower boundary**

Let `left[i]` be the maximum sum on indices `0` through `i` when `i` is the rightmost peak and has height `heights[i]`. Maintain a stack of indices whose heights are non-decreasing. Before processing `i`, remove every taller stack entry. The new top, if it exists, is the nearest index `previous` to the left with `heights[previous] \le \texttt{heights[i]}`.

Every position from `previous + 1` through `i` must then have height `heights[i]`: all intervening original limits were larger, while non-decreasing order ending at `heights[i]` forbids a larger chosen height. The best earlier prefix is already summarized by `left[previous]`, so

$$
\texttt{left[i]} = \texttt{left[previous]} + (i - \texttt{previous})\,\texttt{heights[i]}.
$$

If no such previous index exists, `heights[i]` caps the whole prefix and `left[i] = (i + 1) * heights[i]`.

**Combine the two directions**

Apply the same reasoning from right to left to obtain `right[i]`, the best sum on indices `i` through `n - 1` when `i` is the leftmost peak. For a fixed peak, `left[i] + right[i]` counts the peak twice, so its complete mountain sum is

$$
\texttt{left[i]} + \texttt{right[i]} - \texttt{heights[i]}.
$$

Taking the maximum over all `i` examines every possible peak position. Each directional value is the largest legal side for that peak, so the greatest combined value is exactly the requested optimum. Equal heights remain on the stack; this naturally supports a peak plateau.

## Complexity detail

Let $n$ be the number of towers. An index is pushed once and popped at most once in each directional pass, so the total time is $O(n)$. The two sum arrays and the monotonic stack use $O(n)$ space.

The benchmark uses $n$ as `size` and provides legal strictly increasing arrays from length 16 through 256. The stack method scales linearly. A correct method that builds both sides separately for every candidate peak completes all tiers but exhibits quadratic scaling.

## Alternatives and edge cases

- **Enumerate every peak:** Greedily scan left and right for each possible peak. This is simple and correct, but it takes $O(n^2)$ time.
- **Quadratic dynamic construction:** Materializing the full mountain for every peak repeats the same capped ranges and also requires quadratic work, with no benefit to the final maximum.
- **Endpoint peak:** A completely increasing or decreasing input is already a mountain whose peak may be at the last or first tower.
- **Peak plateau:** Equal adjacent maximum heights may all belong to the peak; keeping equal stack entries preserves the correct prefix and suffix sums.
- **Deep valley:** A small limit can constrain many taller towers on either side, which is why only examining local neighbors is insufficient.
- **Large total:** Individual heights may reach $10^9$, so the sum must use a wide integer type in languages with fixed-width integers.
- **Single tower:** Its original height is the only possible optimum.
