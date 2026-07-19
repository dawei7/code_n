## General
**Turn range sums into prefix differences:** The sum of the subarray from index `a` through `b - 1` is $P_b-P_a$. This difference is divisible by $K$ exactly when $P_a$ and $P_b$ have the same remainder modulo $K$.

**Count earlier matching remainders:** Keep a frequency table for remainders of prefixes already visited. The empty prefix contributes remainder zero before any array element is processed, so initialize its frequency to one. After adding each value to the running prefix, compute its normalized remainder. Every earlier prefix with that same remainder defines one valid non-empty subarray ending at the current position, so add the stored frequency to the answer and then increment it.

This counts every valid subarray once: its ending prefix discovers its unique starting prefix. It counts no invalid subarray because equal remainders imply their prefix difference is a multiple of $K$.

**Handle negative values without branching:** Python's `prefix % k` already produces a remainder from `0` through `k - 1`. In languages whose remainder operator can be negative, normalize with `((prefix % k) + k) % k` before indexing the frequency table.

## Complexity detail
Each of the $N$ values performs constant-time arithmetic and one frequency lookup, for $O(N)$ time. The table has exactly $K$ counters, so it uses $O(K)$ space.

## Alternatives and edge cases
- **Enumerate every subarray:** Extending a running sum from every starting index is correct but requires $O(N^2)$ time.
- **Store all prefix sums:** Testing every pair of prefixes restates the same quadratic search; grouping prefixes by remainder is the information-preserving compression.
- **Zero values:** A zero contributes the same remainder as the preceding prefix, correctly adding subarrays whose sum is zero.
- **Negative totals:** Remainders must be normalized consistently so mathematically equivalent residues share one counter.
- **Whole-array match:** Seeding remainder zero accounts for any prefix, including the entire array, whose sum is divisible by $K$.
