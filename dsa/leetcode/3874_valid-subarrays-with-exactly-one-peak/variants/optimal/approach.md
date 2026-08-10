## General

**Peak status belongs to the original array**

An index is a peak only when it is internal to the complete `nums` array and its value is strictly greater than both original neighbors. The status is not recomputed relative to a selected subarray.

This means a one-element subarray `[i,i]` can contain one peak when `i` is a peak of `nums`, even though that subarray itself has no internal neighbors. The algorithm must first identify global peak indices and then reason only about which of those indices lie inside each interval.

The source scans indices one through `N-2` and appends every strict peak to `peaks`. Because the scan is left to right, this list is sorted by index.

**Attribute every valid subarray to its unique peak**

A valid interval contains exactly one peak. Therefore it can be counted under that peak and under no other.

Fix peak `p=peaks[j]`. A left endpoint `l` must satisfy:

- `l\le p` so the interval contains the peak;
- `p-l\le k`, equivalently `l\ge p-k`;
- `l\ge0`; and
- if a previous peak exists, `l>peaks[j-1]` so that peak is excluded.

Combining the lower bounds gives

$$
leftMin=
\max(p-k,0,peaks[j-1]+1),
$$

omitting the previous-peak term when `j=0`.

The source computes this in two steps with `max`.

**Why only the nearest previous peak matters**

All earlier peaks lie at or before `peaks[j-1]`. If `l` is greater than the nearest previous peak, it is automatically greater than every earlier one, so none can lie in `[l,p]`.

Conversely, if `l\le peaks[j-1]`, the nearest previous peak lies inside the interval because the right endpoint must be at least `p`. The interval would then contain at least two peaks. The nearest previous peak is therefore the exact exclusion boundary.

**Symmetric right-endpoint bounds**

A right endpoint `r` must satisfy:

- `r\ge p`;
- `r-p\le k`, equivalently `r\le p+k`;
- `r\le N-1`; and
- if a next peak exists, `r<peaks[j+1]`.

Thus

$$
rightMax=
\min(p+k,N-1,peaks[j+1]-1),
$$

with the next-peak term omitted for the last peak.

Again, excluding the nearest next peak automatically excludes all later peaks.

**Multiply independent endpoint choices**

The legal left endpoints are every integer from `leftMin` through `p`, inclusive. Their count is

$$
p-leftMin+1.
$$

The legal right endpoints are every integer from `p` through `rightMax`, with count

$$
rightMax-p+1.
$$

Any legal left choice can be paired with any legal right choice. The resulting interval contains `p`, respects both distance limits, excludes the nearest peak on each side, and consequently contains no other peak.

The number of valid intervals whose unique peak is `p` is the product

$$
(p-leftMin+1)(rightMax-p+1).
$$

The source adds this product for every peak.

**No interval is missed or counted twice**

Take any valid interval. By definition it contains one peak `p`. Its endpoints obey the array and distance bounds. Since it contains no other peak, its left endpoint is after the previous peak and its right endpoint is before the next. It appears among the endpoint pairs counted for `p`.

It cannot appear in the product for another peak because it contains no other peak. Thus the sum is a one-to-one count of all valid subarrays.

**Examples**

For `nums=[1,3,2]` and `k=1`, peak `p=1` has no neighboring peaks. `leftMin=max(0,0)=0` and `rightMax=min(2,2)=2`. There are two left choices and two right choices, producing four intervals.

For `nums=[4,3,5,1]` and `k=2`, peak two has `leftMin=0` and `rightMax=3`. There are three left choices and two right choices, giving six.

If `nums` is strictly increasing, `peaks` is empty. The second loop performs no iterations and `ans` remains zero.

When peaks are close, their exclusion boundaries can be stronger than the distance bound. For example, a previous peak at `p-2` forces `l\ge p-1` even if `k` would otherwise allow a much earlier left endpoint.

## Complexity detail

The first pass checks each possible peak index once, taking `O(N)` time. The second pass processes each of `P` peaks with constant work, taking `O(P)`, where `P\le N`. Total time is `O(N)`.

The `peaks` list stores up to `O(N)` indices, so auxiliary space is `O(N)`. All other variables are scalar. These bounds match the manifest.

The answer can be quadratic in `N` because many endpoint combinations may surround peaks, so fixed-width implementations should use a 64-bit accumulator. Python integers handle it automatically.

## Alternatives and edge cases

- **Enumerate every subarray:** Check its contained peaks and distances directly in `O(N^2)` intervals. Peak boundaries allow counting whole rectangles of endpoint choices at once.
- **Prefix sum of peak indicators:** It can test whether an interval contains exactly one peak in constant time, but enumerating all intervals remains quadratic unless combined with additional boundary logic.
- **Two pointers:** A window can maintain peak count, but the separate distance bound around the unique peak complicates direct counting. Neighbor-peak formulas are simpler.
- **Recompute peaks inside each subarray:** Incorrect. Peak status is defined using neighbors in the original array.
- **Length-one subarray containing a peak:** It is valid because the global peak is contained and both distances are zero.
- **No peaks:** The result is zero.
- **One peak:** Only array and distance bounds restrict endpoints; both neighboring-peak terms are absent.
- **Several peaks:** The nearest peak on each side is sufficient to exclude all others.
- **Strict comparisons:** Equal neighboring values do not form a peak because the definition requires greater than both.
- **Endpoint indices zero and `N-1`:** They can never be peaks but may be subarray endpoints around an internal peak.
- **Large `k`:** Array bounds and neighboring peaks still cap choices; `k` does not force an interval to extend fully.
- **Peaks two positions apart:** Both are valid global peaks with a valley between. The previous-plus-one and next-minus-one boundaries still leave legal intervals centered on either peak without overlap in contained peak sets.
- **Independent multiplication:** Once boundaries are fixed, choosing a left endpoint does not constrain a legal right endpoint beyond both containing `p`, so the product is exact.
