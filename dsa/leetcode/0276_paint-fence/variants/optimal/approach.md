## General

**The last two posts contain all needed history**

For two posts, `same = k`: choose one color and use it twice. The other `k * (k - 1)` assignments end
with different colors, so initialize `different` to that value.

For every later post, track valid colorings whose final two colors match and those whose final two colors differ. A
new same-color ending must extend a previously different ending by repeating its last color. A different ending may
extend either previous state with any of the $k - 1$ colors unlike the last post.

After each post, `same` and `different` partition every valid coloring according to its final two colors. Their sum is
therefore the complete valid count.

**State transitions enumerate every legal extension once**

A same-colored ending can arise only by extending a previously different ending with its final color. A different
ending can extend either prior state using any of the $k - 1$ other colors. These cases are disjoint and exhaustive,
while the forbidden third identical post appears in neither. Induction therefore preserves the exact count.

## Complexity detail

Initialization is constant work, and each remaining post performs one constant-size state transition. The total time
is $O(n)$. Only the two counts are retained, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Enumerate all color sequences:** takes exponential time.
- **Recompute every prefix DP:** repeats earlier recurrence steps and takes $O(n^2)$ time.
- **One post:** there are exactly `k` choices, handled before the two-post initialization.
- **Two posts:** all `k * k` assignments are legal and equal `same + different` after initialization.
- **One color:** one or two posts have one valid assignment, while every longer fence has zero.
- **Defensive empty fence:** the app-local contract accepts `n = 0` and returns zero, although the source contract starts
  at one post.
