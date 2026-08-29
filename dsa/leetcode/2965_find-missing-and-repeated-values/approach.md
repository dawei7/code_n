## General

**Count the complete promised value range**

An $n \times n$ grid contains values intended to be exactly the integers from $1$ through $n^2$, except that one value appears twice and one value is absent. The implementation creates a frequency array `cnt` of length `n * n + 1`. Index zero is unused, while `cnt[v]` records how many times value `v` occurs in the grid.

It then scans every row and every value, incrementing the corresponding frequency. A second scan over `x = 1, 2, ..., n * n` finds the exceptional counts:

- if `cnt[x] == 2`, `x` is assigned to `ans[0]` as the repeated value;
- if `cnt[x] == 0`, `x` is assigned to `ans[1]` as the missing value.

The output order matters: repeated comes first and missing comes second. Initializing `ans = [0, 0]` supplies the two slots before the range scan fills them.

**Why frequency counting exactly matches the guarantees**

Under a perfect grid containing every allowed value once, each frequency from one through $n^2$ would equal one. The problem changes that multiset by replacing one occurrence of the missing value with an extra occurrence of the repeated value. Therefore, exactly one frequency becomes zero, exactly one becomes two, and every other frequency remains one.

The grid scan records this multiset without depending on row or column position. Position is irrelevant to the requested result; only how often each allowed value appears matters. During the range scan, the unique frequency two identifies the repeated number and the unique frequency zero identifies the missing number. Frequencies equal to one are ordinary and require no action.

For example, in a $2 \times 2$ grid containing `[[1, 3], [2, 2]]`, the frequency array over values one through four is `[1, 2, 1, 0]` when the unused zero slot is omitted. The second scan places two in the first result slot and four in the second, producing `[2, 4]`.

**Why the unused zero slot is helpful**

Allowed values begin at one. Giving `cnt` a length of $n^2+1$ lets the value itself be used directly as an index, with no repeated subtraction or offset conversion. The unused `cnt[0]` does not participate in the final scan, so it cannot be mistaken for the missing value.

This direct-address table is appropriate because the value domain is dense, known, and only as large as the number of grid cells. It also gives deterministic constant-time updates and lookups rather than expected-time hashing.


After scanning any prefix of grid cells, `cnt[v]` equals the number of processed cells containing `v`, because it begins at zero and is incremented exactly once for every encountered occurrence. After all $n^2$ cells have been processed, this is the exact full-grid frequency for every allowed value.

The problem’s guarantee then implies there is exactly one `a` with `cnt[a] == 2` and exactly one `b` with `cnt[b] == 0`. The second loop examines every allowed candidate. When it reaches `a` it writes `a` to the repeated slot, and when it reaches `b` it writes `b` to the missing slot. No other value can overwrite either slot because no other frequency has the corresponding exceptional count. The returned array is therefore exactly `[a, b]`.

**The exact implementation differs from a constant-space arithmetic method**

The Optimal manifest describes constant auxiliary space, but the protected Python solution shown here does not use sums and squared sums. It allocates `n^2 + 1` integer counters. Its real auxiliary-space complexity is therefore $O(n^2)$, not $O(1)$.

That discrepancy is important for understanding the code accurately. The method is still asymptotically optimal in running time because every grid cell must be inspected in the worst case, but it trades linear-in-cell-count memory for particularly simple, robust logic. The approach document follows the executable implementation rather than claiming the manifest’s different technique.

The method also assumes the source guarantee that all grid values lie in $[1,n^2]$ and that exactly one duplicate/missing pair exists. Without those guarantees, direct indexing could fail for out-of-range values and the fixed two-slot result would not describe multiple anomalies.

## Complexity detail

Let $N$ denote the side length of the grid, so there are $N^2$ cells. The nested grid scan takes $O(N^2)$ time. The subsequent scan of values one through $N^2$ also takes $O(N^2)$ time. Their sum remains $O(N^2)$.

The frequency list has $N^2+1$ entries, so the exact auxiliary space of this Python implementation is $O(N^2)$. The two-element result and loop variables use $O(1)$ additional space. The input grid is not modified.

If complexity is expressed in terms of $C=N^2$, the number of cells, both time and auxiliary space are $O(C)$. This makes clear that the algorithm is linear in the size of the supplied data even though it is quadratic in the grid dimension.

## Alternatives and edge cases

- **Sum and squared-sum equations:** Comparing the actual sums with those of $1$ through $n^2$ can solve two equations for the repeated and missing values in $O(1)$ auxiliary space, but it requires careful arithmetic and is not the technique used by the exact solution.
- **Sign marking in a flattened mutable grid:** Values can sometimes encode visited status in place, but a two-dimensional layout and input mutation make this less direct, and restoring the input may be required.
- **Hash set detection:** A set can identify the repeated value while a total-sum difference identifies the missing one. It still uses $O(N^2)$ worst-case space and has expected rather than deterministic lookup behavior.
- **Sorting all cells:** Flattening and sorting exposes a duplicate and gap in $O(N^2\log N)$ time and requires storage or input rearrangement, so it is slower.
- **Smallest valid grid:** The guarantees still produce one repeated and one missing value; direct indexing needs no special boundary case.
- **Repeated value before or after the missing value:** The output order is semantic, not numeric. The code writes by frequency type, so it works regardless of which value is larger.
- **Unused index zero:** The final loop deliberately starts at one; including zero would falsely classify the unused counter as missing.
- **Manifest mismatch:** Readers should use $O(N^2)$ auxiliary space for this exact implementation, despite any $O(1)$ space claim associated with an arithmetic variant.
- **Input preservation:** Every grid cell is read only; all counts live in the separate list.
