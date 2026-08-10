## General

**Build larger permutations by inserting the new largest value.** Let `count(i, j)` mean the number of permutations of `1..i` having exactly `j` inverse pairs. Suppose a permutation of `1..i-1` is already known. The new value `i` is larger than every existing value, so the only new inversions involving `i` are created by placing smaller values to its right.

If `i` is inserted at the end, it creates 0 new inversions. Moving it one position left puts one smaller value to its right and creates 1. At the front, all `i-1` smaller values lie to its right, creating `i-1` inversions. Thus insertion can add any value `p` from 0 through `i-1`, exactly once for each insertion position.

To finish with `j` inversions after adding `p`, the shorter permutation must have `j-p` inversions. Therefore,

$$
\operatorname{count}(i,j)
=
\sum_{p=0}^{\min(j,i-1)}
\operatorname{count}(i-1,j-p).
$$

This recurrence counts every target permutation exactly once. Removing the largest value `i` from any permutation uniquely reveals both its shorter permutation and how many smaller values were to its right. Conversely, inserting `i` in the corresponding position reconstructs that permutation.

**Why the direct recurrence is still too slow.** There are about $nk$ states, and summing as many as `i` previous states for every one can add another factor of $n$. The exact solution replaces each repeated range sum with subtraction of prefix sums.

**Define the one-dimensional arrays carefully.** After finishing a row, `f[j]` stores the exact count for the current number of elements and inversion total `j`. The auxiliary array `s` stores an exclusive prefix sum of that row:

$$
\texttt{s}[q]
=
\sum_{r=0}^{q-1}\texttt{f}[r].
$$

The loop constructs it with

`s[j] = (s[j - 1] + f[j - 1]) % mod`.

Consequently, the sum of `f[left]` through `f[right]`, inclusive, is

`s[right + 1] - s[left]`.

**Translate the insertion recurrence into one subtraction.** For state `(i, j)`, the shorter permutation's inversion count ranges from

$$
\max(0,j-(i-1))
$$

through `j`. The lower bound corresponds to adding at most `i-1` new inversions; zero prevents a negative prior count. The source therefore computes

`f[j] = (s[j + 1] - s[max(0, j - (i - 1))]) % mod`.

At that moment, `s` still represents the previous row, so overwriting `f` in place is safe. No updated `f[j]` is read to calculate another state in the same row. Only after all `j = 1..k` values are finished does the second inner loop rebuild `s` from the new row.

**Understand the base state.** `f = [1] + [0] * k` represents the empty construction for inversion counting: there is one way to have zero inversions and no way to have a positive count. `f[0]` never needs recomputation because every set size has exactly one zero-inversion permutation, the ascending order.

The prefix array begins as all zero. During `i = 1`, every positive `j` remains zero, which is correct because a one-element permutation has no inverse pair. The second loop then builds the useful prefix sums for the next iteration.

For `n = 3` and `k = 1`:

- with one element, counts are `[1, 0]`;
- inserting 2 gives `count(2,1) = count(1,1) + count(1,0) = 1`;
- inserting 3 gives `count(3,1) = count(2,1) + count(2,0) = 2`.

Those two permutations are `[1,3,2]` and `[2,1,3]`.

**Why modulo is applied throughout.** Counts grow extremely quickly. Every range subtraction and prefix addition is reduced modulo $10^9+7$. Modular arithmetic preserves sums and differences, so later recurrence values remain congruent to the true counts. Python's `%` returns a nonnegative residue even when the raw prefix difference is negative, which avoids a special correction branch.

**Why impossible values become zero naturally.** The maximum inversion count for `i` elements is $i(i-1)/2$. The exact loops still compute columns beyond that limit, but the previous-row windows contain only zero counts, so those states stay zero. If the requested `k` exceeds the maximum for `n`, `f[k]` is therefore correctly returned as 0.

## Complexity detail

The outer loop runs $n$ times. Each iteration updates at most $k$ exact counts and then $k+1$ prefix entries. Every update is constant time, so total time is $O(nk)$.

`f` has length $k+1$ and `s` has length $k+2$. They are reused for every value of `i`, so auxiliary space is $O(k)$. There is no recursion and no two-dimensional table. These bounds match the manifest.

The modulo keeps stored integers bounded, though Python arithmetic would not overflow even without it. Skipping columns above $i(i-1)/2$ could improve constants but would not change the stated worst-case bound when $k$ is reachable.

## Alternatives and edge cases

- **Three-loop dynamic programming:** Implement the insertion recurrence literally. It is easiest to derive but costs $O(nk\min(n,k))$ time.
- **Two-dimensional prefix DP:** Store every row for clearer visualization, using $O(nk)$ space rather than the two reusable arrays.
- **Maximum-inversion pruning:** Restrict each row to `j <= i * (i - 1) // 2`. This saves unnecessary constant work for small `i`.
- **`k = 0`:** `f[0]` remains 1 for every `n`, representing the unique ascending permutation.
- **`n = 1`:** Only `k = 0` is possible; every positive column remains zero.
- **Impossible large `k`:** The recurrence returns zero without a separate feasibility test.
- **In-place overwrite:** It is safe only because `s` freezes all previous-row information. Reading partially updated `f` directly would corrupt the recurrence.
- **Prefix indexing:** `s[q]` excludes `f[q]`, so an inclusive right endpoint `j` requires `s[j + 1]`.
- **Negative modular subtraction:** Python normalizes it; languages with negative remainder need to add the modulus before reducing.
- **Maximum descending permutation:** It has $n(n-1)/2$ inversions and contributes exactly one way at that extreme.
