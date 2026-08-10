## General

**Count valid starts for each fixed ending position**

Every subarray is uniquely identified by its start and end. Instead of generating all $O(n^2)$ pairs, the solution scans the end index `i` from left to right and counts how many starts produce a valid subarray ending exactly at `i`. Adding those counts covers every subarray once.

A fixed-bound subarray needs three facts:

- It cannot contain a value below `minK` or above `maxK`.
- It must contain at least one occurrence of `minK`.
- It must contain at least one occurrence of `maxK`.

The scan maintains the latest position relevant to each fact:

- `k` is the latest invalid position containing a value outside the allowed interval.
- `j1` is the latest occurrence of `minK`.
- `j2` is the latest occurrence of `maxK`.

All begin at -1, meaning the corresponding event has not yet appeared.

**The latest invalid position sets a strict lower bound**

If `nums[k]` lies outside `[minK,maxK]`, any subarray containing it has a minimum below `minK` or a maximum above `maxK`. Therefore a valid subarray ending at the current `i` must start strictly after `k`.

Only the latest invalid position matters. Starting after it automatically excludes all earlier invalid values as well. When the current value is invalid, `k=i`, and no subarray ending at that same position can be valid.

**The latest bounds set an upper bound on the start**

To include both required values, the start must be no later than the latest occurrence of each. Thus it must satisfy

$$
\text{start} \le \min(j1,j2).
$$

Why use the earlier of the two latest positions? If `j1 < j2`, starting after `j1` would exclude the most recent `minK`, and there is no later occurrence before the current endpoint. The same reasoning applies symmetrically.

Combining conditions, valid starts are exactly the integers satisfying

$$
k < \text{start} \le \min(j1,j2).
$$

The number of integers in that interval is `min(j1,j2) - k` when positive, and zero otherwise. That is the expression

`max(0, min(j1, j2) - k)`.

**Why these conditions also guarantee exact minimum and maximum**

Starting after `k` ensures every included value lies between `minK` and `maxK`, inclusive. Including an occurrence of `minK` makes the subarray minimum at most `minK`; the allowed-range condition makes it at least `minK`, so it equals `minK`. Similarly, including `maxK` forces the maximum to equal `maxK`.

Thus the positional conditions are not merely necessary; together they are sufficient.

**Trace the first example**

For `nums = [1,3,5,2,7,5]` with bounds 1 and 5:

- At index 0, `j1=0` while `j2=-1`, so no start includes both bounds.
- At index 1, 3 is allowed but changes none of the tracked positions.
- At index 2, `j2=2`. With `k=-1`, valid starts range from 0 through 0, contributing one subarray `[1,3,5]`.
- At index 3, the tracked positions stay the same, so start 0 again contributes `[1,3,5,2]`.
- At index 4, value 7 is invalid and `k=4`, making the contribution zero.
- At index 5, a new `maxK` appears, but the latest `minK` remains before the invalid 7. Since `min(j1,j2)-k` is negative, no subarray qualifies.

The total is 2.

**When `minK == maxK`**

Both equality checks execute for the same value, so `j1` and `j2` are updated together. A valid subarray must contain that value and may contain no different value because anything smaller or larger is outside the now-singleton allowed interval.

For four copies of 1, no invalid position appears. Contributions are 1, 2, 3, and 4, totaling 10, which counts every subarray.


After processing endpoint `i`, the three variables store their latest qualifying indices at or before `i`. The update statements plainly preserve this invariant. The formula then counts exactly the starts satisfying the necessary and sufficient interval above. Because every valid subarray has one unique endpoint, summing these endpoint-specific counts returns the full answer without duplication.

## Complexity detail

Let $n$ be the array length. The loop visits each value once and performs only constant-time comparisons, assignments, minimum/maximum operations, and arithmetic. Total time is $O(n)$.

The algorithm stores three indices, the running answer, and loop scalars, so auxiliary space is $O(1)$. It does not allocate windows, prefix arrays, or a result collection.

The number of subarrays can reach $n(n+1)/2$, about five billion for $n=10^5$. Python integers handle this safely. A fixed-width implementation should use a 64-bit answer type.

## Alternatives and edge cases

- **Enumerate every subarray:** Maintain minimum and maximum while extending each start. This still takes $O(n^2)$ time and is too slow at $10^5$ elements.
- **Two independent window counts:** Count subarrays whose values stay in a range and use inclusion-exclusion on bounds. It can work but is less direct than tracking the latest required positions.
- **Segment tree or sparse table:** Range minimum and maximum queries become fast, yet there remain quadratically many subarrays to classify unless additional counting logic is added.
- **Invalid current value:** Setting `k=i` makes the contribution zero because no subarray ending there can exclude that endpoint.
- **One required bound not seen:** Its latest position remains -1, and the formula contributes zero.
- **Latest bound before latest invalid:** It cannot serve a subarray starting after the invalid value, so the formula correctly yields zero.
- **Repeated bounds:** Only the latest occurrence is needed because it permits the largest set of possible starts for the current endpoint.
- **Equal bounds:** Both latest positions move together, and only runs of that single value contribute.
- **Values exactly at a bound:** They are allowed and update the corresponding required position.
- **Contiguity:** The start interval counts contiguous slices ending at `i`; no elements can be skipped around an invalid position.
