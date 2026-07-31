## General

Let $T$ be the sum of the complete array. Suppose a candidate value $x$ occupies the outlier index, and let $s$ be the element representing the sum of all special numbers. The special positions themselves also sum to $s$, so

$$
T=x+s+s=x+2s.
$$

Therefore a candidate outlier fixes the only possible sum-element value:

$$
s=\frac{T-x}{2}.
$$

Build a frequency map and evaluate each distinct candidate `x`. If `T - x` is odd, no integer sum element can pair with it. Otherwise compute `s` and check whether a corresponding index remains after reserving one occurrence for the outlier. This is exactly `count[s] - (s == x) > 0`; the subtraction enforces distinct indices while still allowing equal values.

Whenever that availability test succeeds, all other indices can serve as special numbers: their sum is $T-x-s=s$ by the equation above. The condition is thus both necessary and sufficient. Track the greatest valid candidate to obtain the requested largest potential outlier.

The remotely Accepted native method and the app-local `solve(nums)` function preserve this same total-and-frequency scan.

## Complexity detail

Let $n$ be the length of `nums` and $u$ the number of distinct values. Summing the array and building its frequency map take $O(n)$ time. Candidate validation takes $O(u)$ expected time with hash-map operations, and $u\leq n$, so total expected time is $O(n)$. The frequency map stores $O(u)$ entries, bounded by $O(n)$ space.

The benchmark defines `size` as $n$. Each tier contains $n-2$ balanced special values, their sum element `0`, and outlier `777`. The reference makes linear passes. A correct baseline that scans the array for the required sum-element index separately for every candidate performs $\Theta(n^2)$ work and must fail the scaling verdict while retaining correct outputs.

## Alternatives and edge cases

- **Remove two indices explicitly:** Enumerating outlier and sum-element positions is direct but costs $O(n^2)$.
- **Sort the array:** Sorting can aid searches but raises time to $O(n\log n)$ and still needs duplicate-index accounting.
- **Binary-search each candidate:** It also costs $O(n\log n)$ after sorting and is less direct than frequency lookup.
- **Ignore parity:** When `T - x` is odd, integer division invents a sum element that cannot satisfy $T=x+2s$.
- **Equal outlier and sum value:** At least two occurrences are required because the roles must use distinct indices.
- **Duplicate special values:** Frequencies naturally retain every distinct position without special handling.
- **Negative totals:** Parity and integer division remain valid for negative integers.
- **Multiple valid assignments:** Evaluate all candidates and retain the numerically largest outlier.
- **Guaranteed existence:** The answer sentinel is always replaced by at least one valid candidate under the source contract.
