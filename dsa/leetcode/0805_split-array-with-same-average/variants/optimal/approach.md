## General
**Turn equal averages into a zero sum**

Let `T` be the total and `n` the length. A subset of size `k` and sum `S` has the full-array average exactly when $S \cdot n = T \cdot k$. Replace each value `x` by $n \cdot x - T$; the transformed sum of that subset is then $n \cdot S - T \cdot k$, so the required condition becomes an exact zero-sum test with integers.

Before enumeration, check whether any size `1` through $\lfloor n/2 \rfloor$ can satisfy $T \cdot k$ divisible by `n`. If none can, neither that size nor its complementary size can work.

**Meet in the middle**

Split the transformed values into two halves and enumerate every subset sum within each half. A nonempty zero-sum subset contained in either half is immediately valid. Otherwise, for every nonempty right-half subset sum `s`, look for `-s` among nonempty left-half sums.

The one forbidden combination is choosing both complete halves, because that selects the entire array and always sums to zero. When the right subset is full, consult only sums made by non-full left subsets. Every accepted combination is therefore nonempty and proper, and every valid subset decomposes into exactly one left and one right choice that the search examines.

## Complexity detail
Each half contains at most $\left\lceil n / 2 \right\rceil$ values, so enumerating and storing its subset sums takes $O(2^{n/2})$ time and space up to ceiling factors. Hash lookups combine complementary sums in expected constant time per right subset.

## Alternatives and edge cases
- **Subset-sum DP by cardinality:** Track reachable sums for each chosen size and test $T \cdot k / n$; this is effective for bounded sums but has pseudo-polynomial dependence on the values.
- **Enumerate every subset:** Directly test all $2^{n}$ masks and exclude empty/full selections; it repeats work that meet-in-the-middle removes.
- **Floating-point averages:** Comparing division results risks precision errors; cross multiplication or the integer transformation is exact.
- **Single element:** No split into two nonempty groups exists.
- **All values equal:** Any nonempty proper subset works.
- **Complement symmetry:** It is sufficient to consider candidate sizes up to $\lfloor n/2 \rfloor$ in the divisibility check.
- **Whole-array zero sum:** The transformed total is always zero, so the full subset must be excluded explicitly.
