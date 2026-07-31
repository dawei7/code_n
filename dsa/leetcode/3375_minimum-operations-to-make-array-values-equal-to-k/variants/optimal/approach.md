## General

First inspect reachability. Every operation replaces some values by a smaller threshold, so no element can ever increase. If any `nums[i] < k`, making that position equal to `k` is impossible and the answer is `-1`.

Assume all values are at least `k`. Let the distinct values above `k` be

$$
v_1>v_2>\cdots>v_t>k.
$$

At any moment, a valid threshold can change only the single greatest distinct value. If it crossed two existing levels at once, then the values greater than that threshold would include two different numbers, contradicting validity. Therefore every operation can eliminate at most one of the $t$ distinct levels, so at least $t$ operations are necessary.

That lower bound is attainable. Lower $v_1$ to $v_2$, then the merged maximum to $v_3$, and continue through the descending levels. For the last step, lower the remaining value above `k` to `k`. Each chosen threshold is valid because all values above it are the current common maximum. This construction uses exactly $t$ operations, whether or not `k` appeared initially.

Scan the array once. Reject immediately upon seeing a value below `k`; otherwise insert every value greater than `k` into a set. The set size is precisely $t$, the proven minimum.

## Complexity detail

Let $n$ be the array length and $u$ the number of distinct values above `k`. With expected constant-time hash-set insertion, the scan takes $O(n)$ time and stores $O(u)$ values. Here $u\leq99$ under the source constraints, but retaining $u$ makes the dependence explicit.

The benchmark defines `size` as $n$ and supplies nearly all distinct legal values above `k`, followed by duplicates only when the 100-value domain is exhausted. The reference performs one set insertion per item. A correct direct simulation repeatedly finds the next threshold and rewrites the current maximum tier, taking quadratic work and failing scaling without failing any expected output.

## Alternatives and edge cases

- **Sort distinct values:** Sorting makes the descending operation sequence explicit but costs $O(n\log n)$ time instead of the needed set scan.
- **Linear-list uniqueness:** Testing `value not in seen_values` on a list is correct but takes $O(n^2)$ time when most values are distinct.
- **Simulate every operation:** Repeatedly rewriting the array reaches the same count but adds work without changing which distinct levels disappear.
- **Value below `k`:** Return `-1` immediately because operations never increase an entry.
- **Already equal:** If every value is `k`, the set is empty and the answer is zero.
- **`k` absent:** The smallest distinct value above `k` still needs one final operation to become `k`, so every stored level counts.
- **Duplicates:** Any number of copies of the same value are lowered together and contribute only one operation.
- **Single element:** Return zero when it equals `k`, one when it is greater, and `-1` when it is smaller.
- **Maximum target:** With `k = 100`, only an all-100 array is feasible under the given value bounds.
