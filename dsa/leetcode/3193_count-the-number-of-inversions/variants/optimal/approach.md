## General

**Translate prefix requirements into direct lookup.** The input gives pairs `[end, cnt]`, meaning that the prefix ending at index `end`—and therefore having length `end + 1`—must contain exactly `cnt` inversions. The code creates an array `req` of length $n$, initialized to $-1$. A value of $-1$ means there is no requirement at that prefix length; otherwise `req[i]` is the one allowed inversion total after constructing positions $0$ through $i$.

A length-one permutation has zero inversions. If `req[0] > 0`, no permutation can satisfy it, so the method immediately returns zero. Whether a zero requirement was supplied or no requirement was supplied, `req[0] = 0` is then safe because the only possible state at length one has inversion count zero.

The constraints guarantee a requirement for `end = n - 1`. This matters at the return statement: `req[n - 1]` is a real nonnegative target, not the sentinel $-1$.

**Count permutations by length and inversion total.** Define

$$
f[i][j]
$$

as the number of permutations of the values $\{0,1,\ldots,i\}$ whose total inversion count is exactly $j$ and that satisfy every prefix requirement through index $i$. The length is $i+1$. The code stores these values modulo $10^9+7$.

At $i=0$, the only permutation is `[0]`, which has zero inversions. Therefore `f[0][0] = 1` and every other base state is zero.

This value-set interpretation is valid even though the original goal concerns prefixes of a final permutation. Standardizing the relative ranks of any prefix produces a permutation of `0..i` without changing inversion relationships. Conversely, the insertion construction below builds every final permutation through its relative order.

**Insert the new largest value.** To grow a length-$i$ permutation into a length-$(i+1)$ permutation, insert the new largest value $i$. There are $i+1$ insertion positions. If exactly $k$ existing elements are placed to the right of $i$, the new largest value forms an inversion with each of those $k$ elements and with no element to its left. It creates exactly $k$ new inversions, where

$$
0\le k\le i.
$$

To finish with $j$ inversions, the previous permutation must therefore have $j-k$ inversions. This gives the transition

$$
f[i][j]=\sum_{k=0}^{\min(i,j)}f[i-1][j-k].
$$

The upper bound `min(i, j)` enforces both facts: an insertion can create at most $i$ inversions, and `j-k` must not be negative. The exact code implements this sum with the inner loop

`for k in range(min(i, j) + 1)`.

**Enforce a requirement at the moment its prefix is complete.** Without a requirement at index `i`, the code computes `f[i][j]` for every stored total from zero through `m`. If `req[i] >= 0`, it sets `l = r = req[i]` and computes only that one column. Every other state in row `i` remains zero.

This is more than a performance shortcut. It makes the state definition enforce all requirements seen so far. Any construction with a wrong inversion count at this prefix is discarded permanently and cannot contribute to longer permutations. Later insertions do not change inversion relationships among the already placed elements, so a violated earlier prefix can never be repaired.

The variable `m = max(req)` is the largest required inversion count. There is no reason to store totals larger than `m`. Inversions never decrease as the next largest value is inserted: every transition adds $k\ge0$. Once a partial permutation exceeds the largest target needed anywhere, it cannot return to a relevant total.

**Why insertion counts every valid permutation exactly once.** Take any permutation of `0..i`. Remove its largest value $i$. The remaining relative sequence is a unique permutation of `0..i-1`. The removed value had a unique number $k$ of elements to its right, so the original permutation corresponds to exactly one previous state and one transition term. Conversely, inserting $i$ at the position with $k$ elements to its right creates one unique longer permutation and exactly $k$ new inversions. Thus the transition neither loses nor duplicates permutations.

Inductively, row $i-1$ counts exactly the shorter permutations satisfying all earlier requirements. Summing all valid insertion positions counts exactly the length-$(i+1)$ permutations with total $j$. Restricting to `req[i]` when present keeps exactly the new requirement's solutions. At the final row, `f[n - 1][req[n - 1]]` is therefore precisely the requested count.

**Trace a small case.** Let $n=3$ and require two inversions at index $2$, with the unavoidable zero at index $0$. Row zero has `f[0][0]=1`. At length two, inserting $1$ can add zero or one inversion, producing one permutation at each total: `[0,1]` and `[1,0]`. At length three and target $j=2$, the transition sums:

$$
f[2][2]=f[1][2]+f[1][1]+f[1][0]=0+1+1=2.
$$

Those two constructions correspond to `[2,0,1]` and `[1,2,0]`, matching the example.

**Modulo does not change which states are possible.** Counts may be enormous, but addition modulo $10^9+7$ is compatible with the recurrence. Every state only adds counts; reducing after each addition yields the same final remainder as summing exact counts and reducing once.

## Complexity detail

Let $C=\max(\texttt{req})$, the largest required inversion count. The table has $n(C+1)$ entries, so the exact source allocates $O(nC)$ space. This directly contradicts the manifest's stated $O(n+C)$ space; no rolling-row optimization is present.

For each $i$ from $1$ through $n-1$, the source may examine every $j$ from $0$ through $C$. For each pair $(i,j)$ it loops over up to $\min(i,j)+1$ insertion counts. A simple worst-case bound is

$$
O\bigl(nC\min(n,C)\bigr).
$$

When $C\ge n$, this is $O(n^2C)$; when $C<n$, it is $O(nC^2)$. Requirements at intermediate rows can reduce actual work because a constrained row computes only one $j$, but the worst case can leave most intermediate rows unconstrained.

The manifest summary says the transitions use a sliding window and claims $O(nC)$ time. That describes a known optimization using prefix sums of the previous DP row, but it does not describe this checked-in source. The source has an explicit third loop over `k`, so its actual complexity is $O(nC\min(n,C))$ time and $O(nC)$ space. With the stated $n\le300$ and `cnt <= 400`, the bounded implementation may still run acceptably, but the mismatch is material.

## Alternatives and edge cases

- **Sliding-window transition:** Because `f[i][j]` sums a contiguous window of the previous row, maintain a running sum while increasing $j$: add `f[i-1][j]` and remove `f[i-1][j-i-1]` when it leaves the window. This reduces transition time to $O(nC)$ and is the algorithm described by the manifest, but it is not implemented in the exact source.
- **Rolling DP rows:** Only row $i-1$ is needed to build row $i$. Keeping two arrays, or one carefully managed new array, reduces the table from $O(nC)$ to $O(C)$ auxiliary space. Again, the exact source retains every row.
- **Enumerate all permutations:** Checking each of the $n!$ permutations is conceptually direct but becomes infeasible almost immediately. The DP merges permutations that share the only future-relevant facts: length and inversion count.
- **Memoized recursive insertion:** It can express the same state graph, but iterative rows avoid recursion overhead and make prefix requirement pruning direct.
- **Positive requirement at index zero:** A single element has no pair of indices and hence zero inversions. The early return is both necessary and sufficient for this immediate contradiction.
- **No explicit requirement at index zero:** Assigning `req[0]=0` adds no restriction beyond mathematical necessity.
- **Impossible large inversion count:** A prefix of length $i+1$ can have at most $i(i+1)/2$ inversions. A requirement above that bound receives no transitions and its row remains zero, so the final result becomes zero naturally.
- **Requirements cannot be repaired later:** Inserting new largest values preserves the relative order and inversion count among the existing prefix elements. A wrong count at a required prefix must be pruned immediately.
- **Nonmonotone required counts:** Total inversions cannot decrease as the construction grows. If a later requirement is smaller than an earlier one, all paths eventually vanish and the answer is zero.
- **Final requirement guarantee:** The return indexes `req[n-1]` directly. It would accidentally use column $-1$ if that requirement were absent, but the problem explicitly guarantees its presence.
- **Unique requirement endpoints:** The input guarantee prevents conflicting duplicate assignments to one `req[end]`. Without it, blindly overwriting would require conflict validation.
- **Modulo subtraction in an optimized version:** A sliding-window implementation must normalize after removing an expired term. The current triple-loop source only adds nonnegative counts and does not face that detail.
- **Manifest mismatch:** Complexity consumers should not infer $O(nC)$ time or $O(n+C)$ space from this artifact. Those bounds require optimizations absent from `solution.py`.
