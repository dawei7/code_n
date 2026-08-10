## General

A final array is valid after choosing an ordered pair of distinct residues:

- residue $x$ for every even index;
- residue $y$ for every odd index;
- with $x\ne y$ and both residues between zero and $k-1$.

For a fixed pair $(x,y)$, elements can be adjusted independently. The source computes the cheapest change for every position, sums those costs, and tries every distinct residue pair.

**Important source defects and manifest mismatch**

The exact source assigns `ans = inf`, but `inf` is neither imported nor defined. Execution reaches that line only after the first loop has already replaced every input value by its residue. It then raises `NameError: name 'inf' is not defined`. Thus a failed call also leaves the caller's `nums` list mutated.

If `inf` is supplied externally, the remaining enumeration produces the correct minimum. However, its complexity does not match the manifest. The manifest describes precomputing parity-to-residue costs in $O(NK)$ time and $O(K)$ space. The source instead scans all $N$ elements inside both residue loops, taking $O(NK^2)$ time, and it does not allocate the claimed cost arrays.

This document explains the exact nested-loop method and records both discrepancies without modifying the solution.

**Reduce every value to its current residue**

The first loop performs

`nums[i] = v % k`

in place. For deciding how many unit changes are needed to reach a target residue, the quotient of `v` by `k` is irrelevant; only its residue matters. Values that differ by a multiple of `k` have the same position on the residue cycle.

After this loop, each `nums[i]` lies from zero through $k-1$. This simplifies every later distance calculation.

The mutation is not necessary—residues could be computed while reading—but it is the exact source behavior. It permanently destroys the original magnitudes, even if the later undefined `inf` causes an exception.

**Distance between two residues**

Suppose an element currently has residue $v$ and needs target residue $t$. Let

$$
d=\lvert t-v\rvert.
$$

One option is to move directly along residue values, using $d$ increments or decrements. The other option crosses the wraparound between zero and $k-1$, costing $k-d$ operations.

The minimum possible cost is therefore

$$
\min(d,k-d).
$$

For example, with $k=10$, changing residue $9$ to residue $1$ does not require eight increments in the direct numeric direction. Two increments change a number congruent to 9 first to residue 0 and then to residue 1, so the circular distance is $\min(8,2)=2$.

This formula corresponds to actual integer changes, not an operation that explicitly applies modulo. Increasing or decreasing the integer by one naturally moves its residue one step around the cycle.

No route wrapping around more than once can improve the result because it adds a full $k$ operations without changing the final residue.

**Evaluate one ordered residue pair**

The outer loops enumerate every `x` from zero through $k-1$ and every `y` in the same range. Pairs with `x == y` are skipped because the definition requires distinct residues.

For a retained pair, `cnt` starts at zero. At position `i`:

- if `i` is even, `target = x`;
- if `i` is odd, `target = y`.

The source computes the circular distance from the stored residue `v` to that target and adds it to `cnt`.

This sum is the exact minimum for the fixed pair. Each operation changes only one element, so work on one position cannot help another position. Conversely, applying the shorter direction separately at every position constructs an array having the chosen parity residues with exactly `cnt` operations.

After scanning the array, `ans = min(ans, cnt)` keeps the cheapest valid residue pair seen so far.

**Why enumerating all pairs finds the global optimum**

Every valid final array has some even residue $x$ and some different odd residue $y$. The nested loops include that ordered pair. When they reach it, the elementwise distance sum is no greater than the operations used by that final array, because it is independently minimal at every index.

The algorithm also constructs a feasible transformation for every evaluated sum. Taking the minimum over all distinct pairs therefore cannot be too high or too low: it is the global optimum.

The order of $(x,y)$ matters. Choosing $(1,2)$ assigns residue 1 to even indices and 2 to odd indices, while $(2,1)$ makes the opposite assignment and can have a different cost. The two loops correctly test both.

Since the constraints guarantee $k\ge2$, at least one distinct pair exists. If `inf` were properly defined, `ans` would always be replaced by a finite count before return.

## Complexity detail

Let $N$ be the array length and $K=k$. Reducing all elements modulo $K$ takes $O(N)$ time.

There are $K(K-1)$ ordered distinct residue pairs. The source scans all $N$ elements for each one, so its actual time is

$$
O(NK^2).
$$

This contradicts the manifest's $O(NK)$ claim. The claimed faster approach would first compute one length-$K$ cost array for even positions and one for odd positions, then combine distinct choices without rescanning `nums` for every pair.

Apart from mutating the input array in place, the source uses only loop variables and scalar counters. Its actual auxiliary space is $O(1)$, not the manifest's $O(K)$. The original input storage remains $O(N)$ but is not newly allocated.

These runtime statements are conditional on defining `inf`. As checked, the exact method raises `NameError` after the $O(N)$ mutation pass.

## Alternatives and edge cases

- **Required source repair:** Replace or define `inf`, for example with a sufficiently large integer or a proper infinity import. Without that, no valid input reaches a return statement.
- **Precompute parity costs:** Build `even_cost[x]` and `odd_cost[y]` in $O(NK)$, then choose distinct residues. This is the approach described by the manifest, not the present source.
- **Use the best and second-best odd costs:** After precomputation, remember the cheapest two odd residues. Each even choice can combine with the cheapest odd residue unless it is equal, otherwise with the second cheapest, reducing combination work to $O(K)$.
- **Use direct absolute difference only:** This misses cheaper transformations crossing the modulus boundary, such as residue 9 to residue 1 modulo 10.
- **Allow `x == y`:** That violates the defining alternating-residue condition and can produce an artificially smaller answer.
- **Input mutation:** The source replaces every value by its residue. Callers retaining the list observe the changed contents, even when the later missing `inf` raises an exception.
- **Single-element array:** There are no odd-indexed elements, but a distinct unused `y` can always be chosen because $K\ge2$. Keeping the element's existing residue gives cost zero.
- **Only one parity has elements:** The empty parity contributes zero for every target; the nonempty parity is still optimized subject to the existence of a distinct other residue.
- **Residues already alternate with distinct targets:** The matching pair has zero distance at every position, so the minimum is zero.
- **Distance exactly $K/2$ for even $K$:** Both directions cost the same. The `min` formula returns that shared cost.
- **Large original values:** Taking modulo first is arithmetically safe because the nearest-congruence distance depends only on the original residue.
- **Residue zero from a positive multiple of `k`:** It is treated as the valid residue zero, not confused with the original integer value zero.
- **Ordered pair symmetry:** Swapping `x` and `y` changes which index parity receives each residue, so both orders must remain in the search.
