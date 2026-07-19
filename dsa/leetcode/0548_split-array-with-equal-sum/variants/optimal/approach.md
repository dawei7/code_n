## General
**Express every section with exclusive prefix sums**

Let `prefix[t]` be the sum of `nums[0:t]`. For removed indices $i < j < k$, the four retained sums are `prefix[i]`, `prefix[j] - prefix[i + 1]`, `prefix[k] - prefix[j + 1]`, and `prefix[n] - prefix[k + 1]`. Each can then be evaluated in constant time.

**Fix the middle removed index**

Choose `j` from `3` through $n - 4$, which leaves room for a non-empty section and a removed index on both sides. Once `j` is fixed, the left choice `i` and right choice `k` interact only through their common section sum.

**Record all feasible left sums**

For every `i` from `1` through $j - 2$, compare the first and second section sums. When they match, insert that value into a set. The set represents every sum that the left half can realize for this `j`.

**Match a feasible right split**

For every `k` from $j + 2$ through $n - 2$, compare the third and fourth section sums. If they are equal and their value is in the left set, the same `i`, `j`, and `k` make all four sections equal.

**Why a set match is sufficient and necessary**

Every stored value comes from at least one legal left index whose first two sections share that sum. Every tested right value comes from a legal right index whose last two sections share it. Equality through the set therefore combines actual compatible indices around the fixed `j`. Conversely, any valid triple is examined when its middle index is fixed, its left sum is inserted, and its right index is tested, so the algorithm cannot miss a solution.

## Complexity detail
There are $O(n)$ choices for `j). For each one, the left and right scans together take $O(n)$ time, giving $O(n^2)$ total time. The prefix array and the per-middle set each use $O(n)$ space.

## Alternatives and edge cases
- **Enumerate all three removed indices:** prefix sums make each check constant-time, but the three nested choices still cost $O(n^3)$.
- **Recompute section sums directly:** adds another linear factor and can take $O(n^4)$ time.
- **Minimum length:** seven elements are required to leave four non-empty sections and remove three indices.
- **Zero sums:** zero is a valid shared sum and must be stored normally.
- **Negative values:** prefix sums need not be monotone, so two-pointer reasoning is invalid; hash-set equality still works.
- **Removed values:** the elements at `i`, `j`, and `k` contribute to none of the four sums.
- **Repeated feasible sums:** a set is sufficient because only existence, not the number of left indices, matters.
