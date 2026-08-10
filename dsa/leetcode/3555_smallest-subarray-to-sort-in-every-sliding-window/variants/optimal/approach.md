## General

Each length-`k` window is solved independently. Inside one window `[i, j]`, the problem is the classic “shortest unsorted continuous segment” question: find the smallest interval which, when sorted, removes every inversion from that window.

An inversion here means an earlier value is greater than a later value. A non-decreasing sequence has no such pair. The helper `f(i, j)` finds the earliest position that acts as the left endpoint of some inversion and the latest position that acts as the right endpoint of some inversion. Those two positions are exactly the boundaries that must be sorted.

**Finding the right boundary with a prefix maximum**

The forward state `mx` is the greatest value seen so far while scanning from `i` toward `j`.

At position `t`:

- if `mx > nums[t]`, some earlier value is strictly greater than `nums[t]`, so `t` is the right endpoint of an inversion;
- otherwise, `nums[t]` is at least every earlier value, so it can extend the non-decreasing prefix and becomes the new `mx`.

Whenever the first case occurs, the code sets `r = t`. Since the scan proceeds left to right, the final `r` is the **rightmost** index in the window that has a greater value somewhere before it.

Why must every valid sorting segment reach at least this far? The inversion ending at `r` cannot be fixed while leaving `nums[r]` outside the sorted segment: an earlier larger value would still precede it. Therefore `r` is a necessary right boundary.

The strict comparison `mx > nums[t]` is deliberate. Equal adjacent or separated values are allowed in a non-decreasing sequence and do not form an inversion.

**Finding the left boundary with a suffix minimum**

At the same time, `p = j - t + i` moves in the opposite direction: when `t` runs from `i` through `j`, `p` runs from `j` down through `i`.

The reverse state `mi` is the smallest value seen so far to the right of `p`, including the current value after an update.

At position `p`:

- if `mi < nums[p]`, some later value is strictly smaller than `nums[p]`, so `p` is the left endpoint of an inversion;
- otherwise, `nums[p]` is no greater than every value already examined to its right and becomes the new `mi`.

Whenever a violation is found, the code sets `l = p`. Because `p` moves right to left, later assignments move `l` farther left. The final `l` is the **leftmost** index that has a smaller value somewhere after it.

Any sorting segment must start no later than `l`. Leaving `nums[l]` outside would preserve its inversion with that later smaller value.

**Two directional scans in one loop**

Although the helper contains one loop, it logically performs two independent scans:

- `t` advances the prefix-maximum scan;
- `p` advances the suffix-minimum scan.

This halves neither the asymptotic time nor the proof obligations; it simply combines the two linear passes. The loop variable named `k` inside the helper is local to that helper. It temporarily shadows the method parameter name, but it does not change the original window length used by the outer list comprehension.

Initial values `mx = -inf` and `mi = inf` make the first comparison in each direction safe for every allowed integer. The boundary markers `l = r = -1` mean that no inversion has yet been found.

**Why sorting exactly [l, r] is sufficient**

We have shown necessity: any valid segment must include `l` and `r`. It remains to show that sorting everything from `l` through `r` actually fixes the whole window.

Every index before `l` is not the left endpoint of an inversion. Therefore its value is no greater than every later value in the original window. In particular, those prefix values can remain outside: none is too large to stand before any value that will be sorted into `[l, r]`.

Every index after `r` is not the right endpoint of an inversion. Therefore its value is no smaller than every earlier value in the original window. Those suffix values can also remain outside: none is too small to stand after the sorted middle.

Sorting `nums[l:r+1]` puts the middle values in non-decreasing order. The unaffected prefix is already non-decreasing, the unaffected suffix is already non-decreasing, and the preceding relationships show that both boundaries fit the sorted middle. Thus the entire window becomes non-decreasing.

Since every solution must cover `l` through `r` and this exact interval is sufficient, its length `r - l + 1` is minimum.

**Recognizing an already sorted window**

If the window is already non-decreasing, the forward scan never sees `mx > nums[t]`. Consequently `r` remains `-1`. The helper returns zero immediately through

`0 if r == -1 else r - l + 1`.

There is no need to test `l` separately: a window has a left inversion endpoint if and only if it has a right inversion endpoint. Any inversion supplies both.

**Applying the helper to every window**

There are `n - k + 1` valid starts. For each start `i`, the list comprehension calls `f(i, i + k - 1)` and stores the minimum required length in the corresponding output position.

The source does not copy or sort the window. It only measures the boundaries that would need sorting. This is why the original `nums` remains unchanged and why the working memory for one window is constant.

## Complexity detail

For one window of length `k`, the helper performs exactly `k` loop iterations. Each iteration does constant-time comparisons, assignments, and index arithmetic, so one call costs `O(k)` time.

There are `n-k+1` windows. Total running time is

$$
O((n-k+1)k),
$$

matching the manifest. This can be quadratic when `k` is proportional to `n`, which is acceptable under the given `n \le 1000` constraint.

The helper stores only `mi`, `mx`, `l`, `r`, and loop indices. It does not allocate a length-`k` copy, so its auxiliary working space is `O(1)`. The returned list necessarily contains `n-k+1` integers, giving `O(n-k+1)` output space.

The manifest lists `O(k)` space, but that does not describe the exact source: no window-sized container is created. Depending on the convention, the faithful bound is `O(1)` auxiliary space or `O(n-k+1)` including the required answer. Only in special parameter relationships would `O(k)` happen to upper-bound the output, and it is not the implementation’s intrinsic storage bound.

## Alternatives and edge cases

- **Sort a copy of every window:** Comparing each window with its sorted copy can locate changed boundaries, but it costs `O(k \log k)` time and `O(k)` space per window instead of the source’s linear scan and constant working state.
- **Find a local inversion core and expand by extrema:** The standard multi-stage method first finds adjacent disorder, computes the middle minimum and maximum, then expands boundaries. It reaches the same result, but the prefix-maximum and suffix-minimum tests encode those expansions directly in two scans.
- **Reuse state across sliding windows:** More advanced data structures might maintain order information as one value leaves and another enters. However, deriving the exact shortest unsorted segment under deletions and insertions is substantially more complex, and the current `O((n-k+1)k)` method fits `n \le 1000`.
- **Window length one:** A single value is already non-decreasing. No forward violation occurs, so the answer is zero.
- **All values equal:** Strict comparisons never treat equality as disorder, and every window correctly returns zero.
- **Strictly decreasing window:** Every position after the first is a right inversion endpoint and every position before the last is a left inversion endpoint. The final boundaries cover the entire window.
- **Disorder only in the middle:** Ordered prefix and suffix values remain outside exactly when they are compatible with every value across the middle; the boundary scans test this global condition rather than merely looking at adjacent pairs.
- **Duplicate values around a boundary:** Non-decreasing order permits equality. Using `>` and `<`, not non-strict comparisons, prevents unnecessary expansion across equal values.
- **Already sorted window:** `r == -1` is a complete certificate that no inversion exists, so returning zero is correct even though `l` also remains `-1`.
- **Overlapping windows:** They are evaluated independently. A position may belong to many windows, but the algorithm never mutates it, so one result cannot affect another.
- **Input preservation:** The phrase “must be sorted” asks for a minimum length, not for the rearranged arrays. The source intentionally computes lengths without changing `nums`.
- **Maximum window length:** When `k == n`, there is exactly one helper call covering the entire array.
