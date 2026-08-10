## General

To minimize the sum of $k$ unique positive integers absent from `nums`, the chosen values must be the $k$ smallest missing positive integers. If a chosen value were larger than an available smaller value, replacing it would preserve uniqueness and validity while reducing the sum.

The exact solution sorts the excluded values, examines each numeric gap between consecutive exclusions, and takes as many smallest values from each gap as still needed. Arithmetic-series formulas sum whole portions without enumerating up to $k$, which may be $10^8$.

**Add lower and upper sentinels**

The code appends zero and `2 * 10**9` to `nums`.

Zero is below every allowed appended value. The gap after zero begins at one, so the first pair naturally exposes missing positive integers before the smallest original number.

The large upper sentinel guarantees a final gap containing enough candidates even if all earlier gaps are exhausted. Original values are at most $10^9$, and at most $10^8$ additional numbers are needed. Values immediately above the largest exclusion stay below $1.1\cdot10^9$, safely before the $2\cdot10^9$ sentinel.

**Sort exclusions to reveal continuous missing intervals**

After sorting, each adjacent pair `a, b` bounds the integers strictly between them:

$$
a+1,a+2,\ldots,b-1.
$$

Their count is `b - a - 1` when the endpoints are distinct and ordered with a gap.

Duplicate values are not removed by the exact source. For equal endpoints the computed gap is negative one. The surrounding `max(0, ...)` turns that into zero, so duplicate exclusions simply contribute no candidates and do not harm correctness.

**Take only what is still required**

For each gap, the line

`m = max(0, min(k, b - a - 1))`

chooses the number of values to take.

It cannot exceed the gap size, because only those missing integers are available there. It cannot exceed remaining `k`, because the algorithm must select exactly the requested total. The outer maximum prevents negative counts for duplicate adjacent exclusions.

Since gaps are processed in ascending numeric order, the chosen values are the first `m` integers of the gap:

$$
a+1,a+2,\ldots,a+m.
$$

**Sum a selected interval arithmetically**

The first selected value is $a+1$, the last is $a+m$, and there are $m$ terms. Their sum is

$$
\frac{(a+1+a+m)m}{2}.
$$

The implementation adds exactly `(a + 1 + a + m) * m // 2`.

The product is always even because it is the standard integer arithmetic-series sum, so integer division loses nothing.

After adding the interval, `k -= m` records how many more values are needed. Once `k` reaches zero, later pairs calculate `m = 0` and add nothing.

**Why processing gaps greedily is optimal**

All numbers in an earlier sorted gap are smaller than every number in a later gap. If the solution skipped an available earlier number but selected a later one, exchanging the later selection for the skipped smaller value would decrease the sum.

Therefore every minimum-sum set must exhaust earlier missing values before taking later ones, except possibly in the final used gap where only the smallest required prefix is taken.

The algorithm does exactly that, so its chosen set is the unique set of $k$ smallest missing positive integers and has minimum possible sum.

For `nums = [1,4,25,10,25]` and `k = 2`, sorting with sentinels exposes the gap between one and four. It takes two and three, sums them as five, and needs nothing from later gaps. The duplicate 25 creates a zero-size gap.

**Understand the input mutation**

`nums.extend` changes the caller-provided list by adding the sentinels, and `nums.sort()` reorders it in place. The returned sum is correct, but the original array contents and order are not preserved by this exact implementation.

## Complexity detail

Let $n$ be the original array length. Extending is constant time for two elements, sorting $n+2$ values takes $O(n\log n)$ time, and the pairwise gap scan takes $O(n)$. Total time is $O(n\log n)$.

Python's sort may use $O(n)$ temporary memory, and the mutated input itself contains $n+2$ entries. Apart from sorting, the algorithm uses constant scalar state. The manifest's $O(n)$ space is appropriate for the Python sorting implementation.

The method never loops $k$ times, so a value of $10^8$ affects only arithmetic, not iteration count.

## Alternatives and edge cases

- **Deduplicate before sorting:** Sorting `set(nums)` makes every gap nonnegative and may reduce scan work, but allocates a separate set; the exact source safely keeps duplicates.
- **Increment a candidate one by one:** A set membership scan is simple but can require $O(k+n)$ iterations, too many for $k=10^8$.
- **Prefix arithmetic from one through `k`:** Start with the sum of one through `k` and shift the endpoint for excluded values. This can also work after sorting distinct exclusions but requires careful updates.
- **Original number one:** The zero-to-one gap is empty, so selection begins afterward.
- **No small exclusions:** The first gap supplies `1,2,\ldots,k` directly.
- **Duplicate exclusions:** Adjacent equal values produce `m = 0` and are ignored without double exclusion.
- **Very large original values:** They do not affect the early smallest missing choices unless all smaller gaps are exhausted.
- **Large upper sentinel:** It is guaranteed beyond every candidate that could be required under the constraints.
- **`k` becomes zero early:** Remaining gaps contribute zero automatically.
- **Positive-only rule:** Sentinel zero is never selected; it only establishes the first lower boundary.
- **Unique appended values:** Taking distinct integers from nonoverlapping gaps guarantees uniqueness.
- **Integer sum safety:** Python handles totals beyond fixed-width 32-bit range.
- **Input mutation:** Callers needing the original array must pass a copy; the exact source extends and sorts in place.
