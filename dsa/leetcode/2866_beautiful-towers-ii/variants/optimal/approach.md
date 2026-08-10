## General

**What is fixed once a peak is chosen.** If index `i` is the peak, its best height is `maxHeights[i]`. Moving left, every tower must be no higher than both its own cap and the tower to its right. Moving right, every tower must be no higher than both its cap and the tower to its left. Thus the best mountain for a fixed peak can be found with running minima. Repeating that scan for every peak would cost $O(n^2)$, which is too slow for $n=10^5$.

The solution accelerates the repeated running-minimum sums. Array `f` stores the maximum total height of positions `0..i` when position `i` is the rightmost peak. Array `g` stores the symmetric maximum total over `i..n-1` when position `i` is the leftmost peak. Once these are known, peak `i` has total

`f[i] + g[i] - maxHeights[i]`,

where the subtraction removes the peak counted by both sides.

**Previous lower-or-equal cap for the left side.** The first monotonic-stack pass computes `left[i]`. Before pushing `i`, it pops indices whose caps are strictly greater than current cap `x`. The surviving stack top, if any, is the nearest earlier index with cap at most `x`.

Why is that boundary useful? If `maxHeights[i]` is below the immediately previous cap, then walking left from `i` forces a whole suffix of positions to height at most `x`. This flat block continues until reaching an earlier cap no greater than `x`. If that boundary is `j = left[i]`, positions `j+1..i` can all contribute `x`, and positions through `j` retain their already computed optimal sum `f[j]`.

The recurrence is

$$
f[i]=x(i-j)+f[j],
$$

with `f[j] = 0` when no boundary exists. The source has a convenient fast branch: if `x >= maxHeights[i-1]`, the preceding optimal profile can simply be extended by height `x`, giving `f[i] = f[i-1] + x`. Otherwise it uses the boundary recurrence.

**Next strictly lower cap for the right side.** The right-to-left stack computes `right[i]`. It pops caps greater than or equal to `x`, leaving the nearest later index with cap strictly smaller than `x`. The asymmetric equality rule assigns equal-height plateaus consistently and makes the suffix recurrence progress to a genuinely lower boundary.

If `x >= maxHeights[i+1]`, the optimal right profile extends directly: `g[i] = g[i+1] + x`. Otherwise, with `j = right[i]`, positions `i..j-1` are capped at `x` and the already solved suffix begins at `j`:

$$
g[i]=x(j-i)+g[j].
$$

When no lower boundary exists, `j=n` and the suffix beyond it contributes zero.

**Why each recurrence gives the maximum, not merely a valid sum.** On the left of peak `i`, any tower in the block after `j` cannot exceed `x` because reaching the peak must be non-decreasing and the peak itself is `x`. Assigning all those positions exactly `x` is legal until a smaller cap intervenes; the monotonic boundary definition guarantees none does within the block. Everything through `j` is independent of this flat suffix and `f[j]` is already optimal. Therefore the recurrence reaches the coordinate-wise greatest legal left profile. The right proof is symmetric.

**Why stack work stays linear.** An index is pushed once in each stack pass. Once popped, it never returns to that stack. Although one iteration may pop several entries, total pushes and pops across a full pass are $O(n)$. This amortized argument is what turns the repeated minimum-boundary search into linear work.

For `[5,3,4,1,1]`, the left and right sums encode the same running-minimum shapes that a direct simulation would build. At peak zero, the right profile becomes `[5,3,3,1,1]` with sum `13`. At every other peak, combining `f` and `g` evaluates its best possible mountain without rescanning all positions.

## Complexity detail

Each of the two boundary passes pushes and pops every index at most once, taking $O(n)$ time. Computing `f`, computing `g`, and taking the maximum each take another $O(n)$. Total time is $O(n)$.

Arrays `left`, `right`, `f`, and `g` each have length $n$, and the stack may also contain $n$ indices, so auxiliary space is $O(n)$. The result and intermediate sums may reach $10^{14}$, requiring 64-bit arithmetic in fixed-width languages; Python integers handle them automatically.

## Alternatives and edge cases

- **Try every peak directly:** Running minima outward from every index is easy to derive and works for Beautiful Towers I, but costs $O(n^2)$ and is too slow here.
- **Single-pass contribution variants:** It is possible to combine stack events more compactly, but separate `f` and `g` arrays make the two constrained sides easier to verify.
- **Equal caps:** Non-strict mountain slopes allow plateaus. The left and right stacks deliberately use different equality popping rules so equal boundaries are owned consistently.
- **Peak counted twice:** Always subtract `maxHeights[i]` when combining `f[i]` and `g[i]`.
- **Peak at an endpoint:** One side consists only of that peak; sentinel boundaries make the same formulas work.
- **Single tower:** Both side sums equal its cap, and subtracting one copy returns that cap.
- **Large values:** Use a wide sum type; the answer greatly exceeds 32-bit range even though indices do not.
- **Input preservation:** The algorithm reads `maxHeights` without changing it and stores all derived state separately.
