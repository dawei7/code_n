## General

**Expose the answer between value buckets**

The intended competitive method applies the same pigeonhole idea as the
optimal variant. It finds `min_val` and `max_val`, partitions their range into
uniform buckets, records only each bucket's minimum and maximum, and scans
those extrema in numeric order.

With fewer than two numbers, it returns zero. Otherwise the sorted sequence has
$n-1$ adjacent gaps totaling `max_val - min_val`. At least one gap is no
smaller than their average. Choosing a bucket width no larger than that average
ensures a maximum gap is not hidden entirely inside one bucket.

**Intended integer formulas**

Under integer division, the source intends:

- `gap = max(1, (max_val - min_val) // (n - 1))`;
- `bucket_size = (max_val - min_val) // gap + 1`;
- bucket index `(value - min_val) // gap`.

Here the variable called `gap` is really the bucket width, while
`bucket_size` is actually the number of buckets. The names are slightly
counterintuitive, but their roles are clear from allocation and indexing.

Each bucket is a dictionary initialized with positive infinity as its minimum
and negative infinity as its maximum. Both sentinels remaining unchanged mark
an empty bucket.

**Treat global endpoints separately**

During distribution, the source skips values equal to `min_val` or `max_val`.
It begins the later scan with `pre_bucket_max = min_val`, so the global minimum
already acts as the preceding occupied extreme.

After scanning all internal occupied buckets, it explicitly evaluates
`max_val - pre_bucket_max`. Thus the global maximum is incorporated as the
final endpoint even though it was not inserted.

This separation also handles repeated minimum and maximum values. They do not
create positive adjacent gaps among equal copies, so storing extra copies would
not alter the result.

**Measure only consecutive nonempty groups**

For each occupied bucket, the smallest current value is the next sorted value
after the previous nonempty bucket's maximum, because all intervening buckets
are empty. The source updates:

`max_gap = max(max_gap, bucket_min - pre_bucket_max)`.

It then records the current bucket maximum as the predecessor for the next
occupied bucket. Internal differences do not need examination: values sharing
a bucket differ by less than the chosen width, while the averaging argument
guarantees a maximum at least that large across some boundary.

Finally, comparing the global maximum with the last internal maximum covers the
last sorted transition.

**Trace the intended buckets**

For `[3,6,9,1]`, the global extremes are one and nine, and the intended width
is two. One and nine are skipped during distribution. Three and six update
their respective buckets.

The scan starts with predecessor one, measures the transition to three, then
the transition from three to six. The final explicit comparison measures nine
minus six. The maximum is three.

For all equal values, the range is zero and the width guard produces one
bucket. Every value is an endpoint and is skipped. The internal scan finds
nothing, and the final endpoint difference is zero.

**Python 3 execution defects**

The exact source uses `/` in all three formulas rather than `//`. In Python 3,
the first division produces a float. Consequently `bucket_size` is also a
float, and `range(bucket_size)` in the bucket allocation raises `TypeError`
because `range` requires an integer.

Even if that allocation were coerced, `(n - min_val) / gap` would produce a
float index, causing another `TypeError` when indexing `bucket`.

Under Python 2 with integer operands, `/` performed the intended integer
division. Under Python 3, each of these divisions must be changed to `//`.
This compatibility repair is required before the mathematical algorithm can
run.

**Why the intended result is correct**

The bucket width is positive and no larger than the average sorted gap.
Therefore the maximum adjacent gap occurs between distinct buckets. The scan
visits buckets in increasing range order, ignores empty ranges, and compares
the correct neighboring extrema. Separately seeded minimum and final maximum
complete the two ends.

Taking the largest of all those transitions returns the maximum successive
difference without sorting the original array.

## Complexity detail

After replacing all midpoint-style divisions with integer division, distributing
$n$ values costs $O(n)$ and scanning the $k=O(n)$ buckets costs $O(n)$. Intended
time is $O(n)$.

The bucket dictionaries occupy $O(k)=O(n)$ auxiliary space, while the remaining
variables are constant. These intended bounds match the manifest.

As stored under Python 3, the method fails during float-sized allocation and
does not produce a result; the asymptotic claims apply to the intended integer
formulas.

## Alternatives and edge cases

- **Optimal package variant:** Uses `//` and list-pair buckets, so it realizes the bucket algorithm under Python 3 once its `inf` dependency is supplied.
- **Radix sort:** Sort bounded nonnegative integers in linear digit passes, then scan adjacent values.
- **Comparison sort:** Concise but takes $O(n\log n)$ time.
- **One value:** Returns zero before any division.
- **All values equal:** Intended width guard avoids zero-width buckets and returns zero.
- **Repeated endpoints:** Skipping them is safe because equal copies create zero gaps.
- **Empty internal buckets:** The scan jumps across them, which is precisely where large gaps appear.
- **Variable naming:** `gap` is bucket width, while `bucket_size` is bucket count.
- **Fixed-width values:** The stated range is safe, while wider domains may require wider arithmetic for subtraction.
- **Python division:** Every `/` used for counts or indices must be `//` for Python 3.
