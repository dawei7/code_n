## General

**Remove the distracting signs**

The original conditions contain both `|a - b|` and `|a + b|`, so checking them directly for every pair would be cumbersome and quadratic. The first simplification is to describe both quantities using only

`x = |a|` and `y = |b|`.

Assume without loss of generality that `x <= y`. If `a` and `b` have the same sign, then the smaller of `|a - b|` and `|a + b|` is `y - x`, while the larger is `y + x`. If the signs are opposite, subtraction and addition exchange those roles, but the unordered pair of results is still

`{y - x, y + x}`.

Therefore, regardless of signs,

`min(|a - b|, |a + b|) = y - x`

and

`max(|a - b|, |a + b|) = y + x`.

This identity proves that whether a pair is perfect depends only on the two magnitudes. Replacing every input value by its absolute value cannot change the answer.

**Reduce both inequalities to one ratio condition**

Under `x <= y`, the smaller input magnitude is `x` and the larger is `y`. Substitute the identities into the two required inequalities.

The first becomes

`y - x <= x`,

which rearranges to

`y <= 2x`.

The second becomes

`y + x >= y`.

Because `x` is non-negative, that second inequality is always true. It imposes no additional restriction.

Thus two values form a perfect pair exactly when their larger magnitude is at most twice their smaller magnitude:

`max(|a|, |b|) <= 2 * min(|a|, |b|)`.

This is the entire mathematical core of the solution. Once the magnitudes are sorted, the condition describes a contiguous range rather than an arbitrary collection of partners.

**Sort magnitudes to make every valid partner adjacent in a range**

The source builds

`magnitudes = sorted(abs(value) for value in nums)`.

Suppose `magnitude = magnitudes[right]` is the current, larger endpoint. Every earlier position has magnitude no greater than it. An earlier value at position `p` forms a perfect pair with `right` precisely when

`magnitude <= 2 * magnitudes[p]`.

Because the array is sorted, if this condition holds at some position `p`, it also holds for every later position up to `right - 1`: later magnitudes are at least as large, so their doubled values are also large enough. Conversely, if it fails for `p`, it fails for every earlier, no-larger magnitude.

The valid earlier partners therefore form one suffix

`left, left + 1, ..., right - 1`.

The two-pointer loop maintains `left` as the first position in this suffix.

**Advance `left` past values that are too small**

For each `right`, the loop tests

`while magnitude > 2 * magnitudes[left]`.

This is the negation of the valid condition. While it is true, the magnitude at `left` is too small to pair with the current right endpoint, so `left` advances.

The strict greater-than sign is important. Equality `magnitude = 2 * magnitudes[left]` satisfies the original `<=` condition and must remain valid.

The pointer cannot advance beyond `right`. If it reaches the current element, the test becomes `magnitude > 2 * magnitude`, which is false for every non-negative magnitude. Thus the loop remains in bounds without an explicit `left < right` guard.

Once shrinking stops, exactly `right - left` earlier entries are valid partners. Adding that count to `answer` counts every perfect pair whose larger sorted endpoint is `right`.

**Why each original index pair is counted exactly once**

The problem identifies pairs by indices, not by distinct numeric values. Sorting rearranges the items, but it does not merge duplicates or remove their identities. Every two input occurrences appear as two positions in the sorted list.

The perfect-pair relation is symmetric: swapping `a` and `b` does not change any absolute-value expression. Therefore an original pair `i < j` can be counted using whichever occurrence appears later in magnitude order. Exactly one of the two sorted positions is the right endpoint, so the pair is counted once.

Equal magnitudes also work. Sorting places the occurrences at different positions, and each later occurrence counts all earlier equal occurrences. If a magnitude appears `q` times and all such pairs are valid, their contribution naturally becomes `q(q - 1)/2`.

No pair is counted with itself because the increment is `right - left`, covering positions strictly before `right`.

**Why `left` never needs to move backward**

As `right` increases, the current `magnitude` never decreases. The smallest valid partner must be at least half of that current magnitude, so the threshold also never decreases. A value discarded as too small for one right endpoint will remain too small for every later, equal-or-larger right endpoint.

This monotonicity lets one shared `left` pointer serve the entire scan. Although the `while` loop is nested inside the `for` loop, `left` advances at most `n` times in total.

**Trace the first example**

For `nums = [0, 1, 2, 3]`, the sorted magnitudes are unchanged.

- At magnitude zero, there is no earlier partner.
- At magnitude one, zero is too small because `1 > 2 * 0`. `left` moves to the one, so no pair is added.
- At magnitude two, `2 <= 2 * 1`, so one earlier partner is valid: magnitudes one and two.
- At magnitude three, magnitude one is too small because `3 > 2`. After `left` moves to magnitude two, the condition holds, producing the pair with magnitudes two and three.

The final answer is two.

For negative inputs, signs disappear safely. In `[-3, 2, -1, 4]`, magnitudes sort to `[1, 2, 3, 4]`. The same ratio rule counts `(1, 2)`, `(2, 3)`, `(2, 4)`, and `(3, 4)`, corresponding to four original index pairs.

## Complexity detail

Let `n` be the length of `nums`. Computing absolute values and creating the list takes `O(n)` time. Sorting dominates at `O(n log n)`.

The right pointer visits each sorted position once. The left pointer moves only forward and advances at most `n` times across the whole scan, so pair counting after sorting is `O(n)`. The total time complexity is therefore `O(n log n)`.

The sorted magnitude list stores `n` integers, requiring `O(n)` auxiliary space. The pointers and answer use `O(1)` additional storage. Python’s sort may also use temporary memory internally, but the overall auxiliary bound remains `O(n)`.

The returned count can be as large as `n(n - 1)/2` when every pair is perfect. Python integers handle that automatically. In a fixed-width language, the answer needs a 64-bit integer for `n = 10^5`.

## Alternatives and edge cases

- **Check every pair directly:** Evaluating both original inequalities for all `i < j` is straightforward but costs `O(n^2)`, which is too slow for `n = 10^5`.
- **Binary search per right endpoint:** After sorting, binary-search the first magnitude at least half of the current one. This gives `O(n log n)` counting after the sort; the monotone two-pointer scan improves that phase to `O(n)`.
- **Frequency map over magnitudes:** One could count repeated magnitudes and process sorted distinct keys with multiplicities. It may reduce scanning when duplicates are common but requires careful combination counting and does not improve the worst-case sorting bound.
- **Keep the original signs:** Signs do not affect the minimum and maximum of `|a-b|` and `|a+b|`. Retaining them obscures the one ratio condition without adding information.
- **Forget the second inequality:** It is safe to omit only after proving `x + y >= max(x, y)` for non-negative magnitudes. Dropping it without that derivation would leave the reduction unjustified.
- **Boundary ratio exactly two:** A pair with larger magnitude exactly twice the smaller is valid because the condition uses `<=`. The source’s `while` loop removes only strict violations.
- **Two zero values:** They form a perfect pair because all four relevant quantities are zero. The loop counts earlier zeros with a current zero.
- **One zero and one nonzero value:** The ratio condition becomes positive `<= 0`, which is false. The left pointer discards zeros before pairing a positive magnitude.
- **Equal nonzero magnitudes:** They always form a perfect pair because `x <= 2x`. Duplicate occurrences are counted as distinct index pairs.
- **All magnitudes far apart:** For values such as `[1, 10, 100, 1000]`, each new magnitude discards all earlier ones and the answer remains zero.
- **Negative values:** Applying `abs` is mathematically exact, not an approximation. A positive and negative value with the same magnitude behaves like any equal-magnitude pair.
- **Original index order:** The requirement `i < j` chooses one representation of each unordered index pair. Since the relation is symmetric, sorting occurrences and counting each pair once preserves the requested count.
- **Input preservation:** The generator computes new magnitudes and `sorted` returns a new list; `nums` itself is not modified.
