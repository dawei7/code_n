## General

**Avoid comparison sorting by preserving only bucket extremes**

If the array were sorted, the answer would be the largest difference between
neighboring values. Comparison sorting costs $O(n\log n)$, so the solution
instead partitions the numeric range into ordered buckets.

Within a bucket, it stores only the smallest and largest assigned values. It
does not need the internal order, because the bucket width is chosen so that a
global maximum adjacent gap can be found between nonempty buckets.

Arrays with fewer than two values return zero immediately, because there is no
pair of successive sorted elements.

**Derive a useful bucket width**

Let `mi` and `mx` be the minimum and maximum input values, and let $n$ be the
array length. The sorted array has $n-1$ adjacent gaps whose sum is
$mx-mi$. Therefore at least one gap is no smaller than the average:

$$
\frac{mx-mi}{n-1}.
$$

The source chooses
`bucket_size = max(1, (mx - mi) // (n - 1))`. This positive integer width is
at most the average whenever the range is nonzero.

Values mapped to the same bucket differ by less than `bucket_size` under the
integer interval partition. Hence a gap meeting or exceeding the average lower
bound cannot be strictly hidden between two values in the same bucket. A
maximum gap is exposed between the maximum of one occupied bucket and the
minimum of the next occupied bucket.

The `max(1, ...)` guard handles equal values and small ranges without division
by zero in later bucket indexing.

**Map every value to an ordered bucket**

The number of allocated buckets is:

`(mx - mi) // bucket_size + 1`.

Value `v` belongs to index `(v - mi) // bucket_size`. Subtracting `mi` makes
the minimum map to zero. The formula for the count ensures the maximum maps
within the final index, including when the numeric range is an exact multiple
of the width.

Each bucket begins as `[inf, -inf]`, an unmistakable empty state. On insertion,
the first component becomes the smallest value seen there and the second
becomes the largest. Repeated values and arbitrary input order cause no
problem.

Although the floor-width formula can allocate slightly more than $n$ buckets,
the count remains $O(n)$. If the width is one, then the range is below
$2(n-1)$; for larger widths, dividing the range by that width gives the same
constant-factor bound.

**Scan consecutive occupied buckets**

Buckets are stored in increasing value-range order. The source scans them from
left to right and skips any whose minimum is greater than its maximum—the
original sentinel state.

`prev` is the maximum of the preceding nonempty bucket. For a current occupied
bucket, `curmin - prev` is the gap between consecutive groups in sorted order.
No actual values lie in skipped empty buckets, and no value in either occupied
bucket lies between those two extrema. Therefore they are successive elements
of the globally sorted sequence.

After measuring the gap, `prev` becomes `curmax`, preparing the comparison with
the next occupied bucket.

The source initializes `prev = inf`. For the first nonempty bucket,
`curmin - prev` is negative infinity and cannot increase `ans`, which starts at
zero. Then `prev` becomes that bucket's real maximum. This is an unusual but
functional way to avoid a separate first-bucket case.

**Trace `[3,6,9,1]`**

Here $n=4$, `mi = 1`, and `mx = 9`. The integer bucket width is
`(9 - 1) // 3 = 2`. Values are distributed by their offset from one. Each
occupied bucket records only its local minimum and maximum.

Scanning occupied buckets in order exposes the transitions corresponding to
the sorted sequence `[1,3,6,9]`. The largest difference is three, appearing
between three and six and again between six and nine.

For `[10]`, the early return gives zero. For `[5,5,5]`, the width guard chooses
one and all values occupy the same bucket. There is no inter-bucket gap, so the
answer remains zero.

**Why internal bucket values cannot hide a larger answer**

Any two values in one width-$b$ integer bucket differ by at most $b-1$. The
averaging argument guarantees a global adjacent gap of at least the average,
and the chosen $b$ does not exceed that average. Thus some maximum gap occurs
across bucket boundaries.

For adjacent nonempty buckets in the scan, the only candidate that can be
successive in global sorted order is the next bucket's minimum minus the
previous bucket's maximum. Taking the maximum of all such transitions therefore
returns the required gap without reconstructing the full sorted order.

**Exact-source dependencies**

The selected source uses `List` and the name `inf` without imports. Standalone
Python needs `from typing import List` and a definition such as
`from math import inf`. Without them, the algorithm does not execute.

## Complexity detail

Let $k$ be the bucket count. Distributing $n$ values takes $O(n)$ time and
scanning buckets takes $O(k)$. The chosen width guarantees $k=O(n)$, so total
time is $O(n)$.

The bucket array stores two numbers per bucket, giving $O(k)=O(n)$ auxiliary
space. All other state is constant. These bounds match the manifest.

## Alternatives and edge cases

- **Comparison sorting:** Sort and scan adjacent differences in $O(n\log n)$ time; it is simpler but violates the required linear-time target.
- **Radix sort:** The nonnegative bounded integers can be sorted digit by digit in linear time for a fixed number of digits, using $O(n)$ extra storage.
- **Fewer than two values:** No adjacent sorted pair exists, so return zero.
- **All values equal:** One occupied bucket yields no positive gap.
- **Duplicate values:** They only update the same extrema and do not affect the maximum.
- **Empty buckets:** They are skipped; the gap spans directly between consecutive occupied buckets.
- **Minimum and maximum:** The bucket-count formula includes both endpoints safely.
- **First occupied bucket:** The infinity initialization deliberately suppresses a nonexistent gap before the minimum.
- **Nonnegative contract:** Bucket indexing uses offsets and also works algebraically for negatives, but the stated domain is nonnegative.
- **Missing imports:** `List` and `inf` must be available in a standalone runtime.
