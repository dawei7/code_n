## General
**The last two posts contain all needed history**

Track valid colorings whose last two posts have the same color and those whose last two differ. A new same-color ending must extend a previously different ending; a different ending may extend either state with any of $k - 1$ new colors.

After each post, `same` and `different` partition every valid coloring according to whether its final two colors match. Their sum is the complete valid count.

**State transitions enumerate every legal extension once**

A same-colored ending can arise only by extending a previously different ending with its final color. A different ending can extend either prior state using any of the $k - 1$ colors unlike the previous post. These cases are disjoint and exhaustive, while the forbidden third identical post appears in neither. Induction therefore preserves the exact count.

## Complexity detail
Each additional post performs constant arithmetic, giving $O(n)$ time and $O(1)$ space.

## Alternatives and edge cases
- **Enumerate all color sequences:** takes exponential time.
- **Recompute every prefix DP:** is correct but can take $O(n^2)$.
- One post has `k` choices; with one color, at most two posts can be painted validly.
