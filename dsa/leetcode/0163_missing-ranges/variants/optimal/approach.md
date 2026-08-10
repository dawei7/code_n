## General

**Missing values form maximal gaps**

Because `nums` is sorted, unique, and entirely inside `[lower, upper]`, every
missing integer belongs to one of three locations:

- before the first array value;
- between two consecutive array values;
- after the last array value.

Within any such location, all consecutive integers are missing. Combining them
into one inclusive pair gives the shortest representation. Splitting one gap
would add unnecessary ranges, while merging across an existing number would
incorrectly include that number.

The selected method handles the empty array separately, then checks the leading
boundary, every internal neighboring pair, and the trailing boundary.

**Cover an empty array in one range**

If `nums` has no elements, every integer from `lower` through `upper` is
missing. The shortest exact answer is therefore `[[lower, upper]]`.

This early return is also necessary for safe indexing: all later boundary
checks read `nums[0]` or `nums[-1]`.

Even when `lower == upper`, the pair `[lower, upper]` is the correct
single-number range. The output schema always uses two-element numeric lists;
it does not convert singleton gaps to a special string format.

**Check the leading and trailing gaps**

If `nums[0] > lower`, the integers from `lower` through `nums[0] - 1` do not
appear in the array. The source appends exactly
`[lower, nums[0] - 1]`.

If `nums[0] == lower`, there is no leading gap, so nothing is appended. Values
below `lower` are outside the requested interval and must never appear.

The symmetric trailing check compares `nums[-1]` with `upper`. If the last
present number is smaller, `[nums[-1] + 1, upper]` is missing. Equality means
the upper endpoint is already covered by `nums`.

These checks use strict inequalities, preventing invalid ranges whose start
would exceed their end.

**Detect every internal gap from adjacent values**

`pairwise(nums)` produces consecutive pairs `(a, b)` in sorted order. Since
the values are unique, $b>a$.

If $b-a=1$, the integers are consecutive and nothing lies between them. If
$b-a>1$, the missing integers are exactly:

$$
a+1,\ a+2,\ \ldots,\ b-1.
$$

The shortest inclusive representation of that complete run is `[a + 1,
b - 1]`, which the source appends.

No other internal position needs examination. Every integer between `lower`
and `upper` either is a listed value or lies between the closest listed value
before it and the closest one after it.

**Trace the main example**

For `nums = [0,1,3,50,75]`, `lower = 0`, and `upper = 99`, the first value
equals the lower bound, so there is no leading range.

The pair `(0,1)` is consecutive. Pair `(1,3)` leaves only two, producing
`[2,2]`. Pair `(3,50)` produces `[4,49]`. Pair `(50,75)` produces `[51,74]`.
Finally, 75 is below 99, so the trailing range is `[76,99]`.

The ranges appear automatically in ascending order because the scan follows
the sorted input from left to right.

For `nums = [-1]` with both bounds equal to `-1`, neither boundary inequality
holds and there are no adjacent pairs. The returned list is empty, correctly
indicating no missing number.

**Why the result is exact and shortest**

Every appended range is bounded by either the interval boundary or present
array values immediately outside it. Therefore it contains only missing
numbers.

Conversely, take any missing integer. If the array is empty, the early range
covers it. Otherwise it is before the first value, between some consecutive
values, or after the last; the corresponding check includes it. Thus every
missing value is covered.

Each produced pair is a maximal consecutive run: extending it would include a
present value or leave `[lower, upper]`. Any exact cover must use at least one
range for each separated run, so using exactly one per run is shortest.

**Exact-source dependencies**

The source uses `List` annotations and `pairwise` without imports. A standalone
Python 3.10+ module needs `from typing import List` and
`from itertools import pairwise`. Earlier Python versions need an equivalent
adjacent-pair iteration. These are execution dependencies, not changes to the
gap algorithm.

## Complexity detail

Let $n$ be `len(nums)`. The pairwise scan examines $n-1$ adjacent pairs, and
the boundary work is constant. Time is $O(n)$.

Apart from the returned answer, the method stores only scalars and each current
pair, so auxiliary space is $O(1)$. The output can contain up to $n+1$ ranges
and therefore occupies $O(n)$ required result space; the manifest's $O(1)$ is
the conventional auxiliary-space bound excluding output.

## Alternatives and edge cases

- **Sentinel scan:** Treat `lower - 1` and `upper + 1` as virtual present values, allowing one uniform loop over every gap.
- **Enumerate every integer:** Simple but can take time proportional to `upper - lower`, far larger than `n`.
- **Empty `nums`:** Return the complete inclusive interval as one range.
- **No missing values:** Boundary checks and consecutive pairs append nothing.
- **Singleton gap:** It remains `[x, x]` under the required numeric-pair schema.
- **Negative bounds:** Addition, subtraction, and ordering work unchanged.
- **Boundary presence:** Equality at either bound prevents an empty or reversed range.
- **Unique sorted guarantee:** It makes every adjacent difference positive and ranges naturally ordered.
- **Output space:** The result itself may be linear even though working storage is constant.
- **Missing imports:** `List` and `pairwise` must be supplied for standalone execution.
