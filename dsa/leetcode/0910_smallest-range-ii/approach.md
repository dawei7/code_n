## General

Every value must receive either $+k$ or $-k$. After sorting, the key structural fact is that an optimal assignment can be represented by one breakpoint:

- a prefix of smaller values receives $+k$;
- the remaining suffix of larger values receives $-k$.

The algorithm tests every breakpoint.

**Why crossed signs are unnecessary.** Suppose sorted values $a\le b$ receive $-k$ and $+k$, respectively. Their transformed gap becomes

$$
(b+k)-(a-k)=b-a+2k,
$$

which pushes them farther apart. Giving the smaller value $+k$ and the larger value $-k$ brings them closer instead. Repeatedly removing such inversions transforms an optimal sign assignment into one where all plus choices occur before all minus choices, without increasing the range.

To make the exchange precise, replace transformed pair $(a-k,b+k)$ with $(a+k,b-k)$. The new values lie inside or closer to the interval spanned by the old pair: $a+k\ge a-k$ and $b-k\le b+k$. Even if their internal order crosses, both remain between the old outer endpoints. The replacement therefore cannot lower the global minimum or raise the global maximum, so it cannot increase the score.

Thus there is some split index `i` such that indices below `i` are raised and indices `i` onward are lowered.

**Find extremes for one split.** For split `i` between `i - 1` and `i`:

- The raised prefix's smallest value is `nums[0] + k`.
- The raised prefix's largest value is `nums[i - 1] + k`.
- The lowered suffix's smallest value is `nums[i] - k`.
- The lowered suffix's largest value is `nums[-1] - k`.

The overall minimum is therefore

```text
min(nums[0] + k, nums[i] - k)
```

and the overall maximum is

```text
max(nums[i - 1] + k, nums[-1] - k)
```

Their difference is the score for that breakpoint.

**Why only four values matter.** Sorting makes every transformed prefix value lie between its transformed first and last elements, and every transformed suffix value lie between its transformed first and last elements. No interior value can exceed the candidate maximum or fall below the candidate minimum.

The loop considers `i = 1` through `n - 1`, every split with nonempty parts. Before the loop, `ans = nums[-1] - nums[0]` covers the two missing boundary cases: giving every value $+k$ or every value $-k$. Uniformly shifting the whole array leaves its range unchanged.

It is not enough to inspect only the two values adjacent to the breakpoint. The smallest result can be either the raised original minimum or the lowered first suffix value. The largest can be either the raised last prefix value or the lowered original maximum. The `min` and `max` calls compare exactly these possibilities, including cases where a large $k$ makes the two transformed groups cross.

For `[1,3,6]` with $k=3$:

- Original range is 5.
- Split after 1 yields transformed groups `[4]` and `[0,3]`, range 4.
- Split after 3 yields `[4,6]` and `[3]`, range 3.

The minimum is 3.

For `[0,10]` with $k=2$, the only nonuniform split raises 0 to 2 and lowers 10 to 8, giving score 6. The initial uniform case has score 10. Comparing both shows why the original range is an upper bound rather than always the final answer.
The exchange argument guarantees at least one optimal solution has a prefix-plus/suffix-minus form. Every such form is evaluated by either the initial uniform case or one loop iteration. The computed `mi` and `mx` are exact extremes for that form. Taking the minimum across them therefore returns the global minimum score.

The solution sorts `nums` in place. The signs are analyzed mathematically; it does not need to construct each transformed array.

## Complexity detail

Let $n$ be the array length. Sorting costs $O(n\log n)$ and the breakpoint scan costs $O(n)$.

- **Time complexity:** $O(n\log n)$.
- **Space complexity:** The manifest states $O(n)$, accounting for Python sorting workspace. The scan itself uses $O(1)$ scalar space.

The input array's order is mutated by `sort`.

## Alternatives and edge cases

- **Enumerate all sign assignments:** There are $2^n$ possibilities. The sorted breakpoint theorem reduces them to $n+1$ cases.
- **Greedily move every value toward the original midpoint:** Local choices can miss the best final extremes; testing breakpoints is the proven global method.
- **Reuse Smallest Range I formula:** That problem allows any adjustment in `[-k,k]`, while this one requires exactly `+k` or `-k`. The answers can differ.
- **One value:** Original range is zero and the split loop is empty.
- **`k = 0`:** Every transformed value equals the original, so all candidate scores equal the original range.
- **All values equal:** Assigning different signs may widen the range, while the initial uniform case preserves score zero.
- **Duplicate values:** Sorting and breakpoints treat occurrences independently; any optimal sign boundary is still representable.
- **Negative transformed values:** They are allowed; only the final range matters.
- **Uniform sign choice:** Both all-plus and all-minus preserve the original score and are covered by initial `ans`.
- **Breakpoint extremes:** Use `nums[i - 1]` for the raised prefix maximum and `nums[i]` for the lowered suffix minimum; mixing these indices changes the candidate.
- **Input mutation:** Sort a copy if the caller needs the original order.
- **Any operation at every index:** Unlike Smallest Range I, no element may remain unchanged unless $k=0$; the split assigns a sign to all elements.
