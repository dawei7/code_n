## General

**Translate two chosen lines into an area formula**

For indices `l < r`, the container width is the horizontal distance

$$
r-l.
$$

Water must remain level, and the container may not be slanted. The shorter vertical line determines the highest water level before water spills over that side. Therefore the area is

$$
A(l,r) = (r-l)\min(\texttt{height[l]},\texttt{height[r]}).
$$

The taller line contributes no extra height above the shorter one. This “minimum height times distance” fact is what makes it possible to eliminate pairs without trying all of them.

**Start with the greatest possible width**

The method places

```python
l = 0
r = len(height) - 1
```

at the two outermost lines. No pair has a larger width. The widest pair is not necessarily optimal—a shorter inner width may be compensated by much taller lines—but it gives a useful comparison point and leaves every other pair inside the interval.

At each iteration, the code evaluates the current pair before moving a pointer:

```python
t = min(height[l], height[r]) * (r - l)
ans = max(ans, t)
```

Recording the current area first is essential because the elimination argument uses that already-measured pair as an upper bound for many unmeasured pairs.

**Why moving the taller side cannot help while the shorter side stays**

Assume `height[l] < height[r]`. The current area is

$$
(r-l)\texttt{height[l]}.
$$

Consider pairing the same left line with any inner right index `k`, where $l < k < r$. Its width is smaller:

$$
k-l < r-l.
$$

Its usable height is at most the fixed left height:

$$
\min(\texttt{height[l]},\texttt{height[k]}) \le \texttt{height[l]}.
$$

Combining the two inequalities gives

$$
A(l,k) \le (k-l)\texttt{height[l]} < (r-l)\texttt{height[l]} = A(l,r).
$$

Every remaining pair that keeps `l` is strictly worse than the current pair, which has already been considered. The left line can never participate in a better unseen answer, so discarding it with `l += 1` is safe.

Moving `r` instead would reduce the width while keeping `height[l]` as the limiting height. Even an infinitely tall new right line could not recover the lost width. The only possibility for improvement is to replace the shorter line and hope for a higher limiting height.

**The symmetric case and equal heights**

If `height[l] > height[r]`, the same reasoning applies in the other direction. Any inner pair that retains `r` has smaller width and usable height at most `height[r]`, so `r` can be discarded.

The implementation is

```python
if height[l] < height[r]:
    l += 1
else:
    r -= 1
```

When the heights are equal, the `else` branch moves `r`. Either side is safe to discard. If both endpoints have height `h`, every pair keeping one endpoint and moving the other inward has width below `r - l` and limiting height at most `h`; it cannot beat the area just recorded. Some presentations move both pointers on a tie, but moving one preserves the linear bound and remains correct.

**A focused trace of the maximum example**

For `height = [1,8,6,2,5,4,8,3,7]`:

| `l` | `r` | Heights | Width | Area | `ans` | Safe move |
|---:|---:|---|---:|---:|---:|---|
| `0` | `8` | `1`, `7` | `8` | `8` | `8` | discard left height `1` |
| `1` | `8` | `8`, `7` | `7` | `49` | `49` | discard right height `7` |
| `1` | `7` | `8`, `3` | `6` | `18` | `49` | discard right height `3` |
| `1` | `6` | `8`, `8` | `5` | `40` | `49` | equal; discard right endpoint |

Later pairs have smaller width and do not exceed `49`. The optimal container uses indices `1` and `8`: its width is `7`, its limiting height is `7`, and its area is `49`.

The trace also shows why choosing the two tallest lines alone is not a valid strategy. The two height-`8` lines at indices `1` and `6` produce only `40`; the slightly shorter line at index `8` gains enough width to produce a larger area.

**Why the elimination process cannot skip the optimum**

Before each pointer move, the current pair is evaluated. The shorter endpoint is then removed only after proving that every still-unseen pair containing that endpoint has area no greater than the current evaluated area. Thus each removal discards no candidate capable of improving `ans`.

The interval shrinks by one endpoint per iteration. Eventually the pointers meet, by which time every pair has either been evaluated directly or dominated by an evaluated pair during a safe elimination. Since `ans` is the maximum of all directly evaluated areas, it equals the global maximum.

## Complexity detail

Let $n$ be the number of lines.

- **Time complexity: $O(n)$.** Each iteration increments `l` or decrements `r`. Neither pointer reverses direction, and their total number of moves before meeting is at most `n - 1`. Area calculation and comparison are constant work.
- **Space complexity: $O(1)$.** The algorithm stores two indices, the current area, and the best area. It creates no pair list, stack, or input-sized auxiliary structure.

The numerical area can be as large as `(n - 1) * 10**4` under the stated constraints, which fits comfortably in Python's integer type.

## Alternatives and edge cases

- **Brute-force all pairs:** Evaluate the exact area for every $l < r$. This uses constant auxiliary space but $O(n^2)$ time, which is too slow for up to $10^5$ lines.
- **Sort lines by height:** Height alone is insufficient because width is equally important. Sorting also destroys direct positional relationships unless indices are carried and does not simplify the maximum-product tradeoff as cleanly as two pointers.
- **Move the taller pointer:** With the shorter height unchanged and width reduced, no immediate or future pair retaining the shorter endpoint can improve. This move lacks the safe-elimination proof.
- **Move both pointers on unequal heights:** This can skip a tall line that should pair with the retained taller endpoint. Only the known limiting side is safe to discard.
- **Equal endpoint heights:** Either pointer may move after recording the area; the implementation moves `r`.
- **Exactly two lines:** The loop evaluates the only possible pair once and returns its area.
- **Zero-height lines:** They create area zero. When one endpoint is zero, discarding that limiting endpoint is safe; if both are zero, the tie branch removes the right one.
- **All heights equal:** The widest outer pair is optimal. Later widths shrink with the same limiting height, so `ans` never changes.
- **Strictly increasing heights:** The left endpoint is repeatedly discarded until width/height tradeoffs have all been represented by evaluated pairs.
- **Strictly decreasing heights:** The right endpoint is symmetrically discarded.
- **No slanting:** The formula intentionally uses the shorter vertical height; averaging heights or using the taller height would describe a different, invalid geometry.
- **Input preservation:** Only indices move. The height array is never sorted or modified.
