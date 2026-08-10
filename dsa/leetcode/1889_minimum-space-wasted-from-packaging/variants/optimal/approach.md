## General

**For one supplier, every package should use the smallest fitting box.** A supplier offers unlimited boxes of each listed size. Once a supplier is fixed, choosing a larger box when a smaller offered box already fits can only increase waste and does not help another package because supply is unlimited. The optimal assignment for that supplier is therefore determined independently: map every package to the first offered box size that is at least as large.

**Sort packages and each supplier's sizes.** `packages.sort()` arranges package sizes in nondecreasing order. Inside the supplier loop, `box.sort()` arranges that supplier's distinct sizes from smallest to largest. These orders make packages assigned to one box size form a contiguous range. The source mutates the input package list and every inner supplier list; the problem does not require preserving their original order.

**Reject suppliers that cannot fit the largest package.** If `packages[-1] > box[-1]`, even the supplier's largest box is too small for the largest package. That supplier cannot pack all packages and is skipped. Conversely, if the largest package fits, every smaller sorted package also fits at least that largest box, so the later range scan will assign all packages.

**Use binary search to assign one package block at a time.** Variable `i` is the index of the first package not yet assigned for the current supplier. For box size `b`, `bisect_right(packages, b, lo=i)` returns index `j` just after the last remaining package whose size is at most `b`. Thus packages in half-open range `[i, j)` fit in `b`, while the next one, if any, is larger.

Because box sizes are processed increasingly, none of `packages[i:j]` fit an earlier smaller offered size; otherwise they would already have been consumed. Box `b` is therefore the smallest fitting size for every package in that range. The capacity used for the group is `(j - i) * b`, and setting `i = j` moves to the next unassigned package.

**Minimize total box capacity first.** Variable `s` accumulates the sum of selected box sizes, not waste directly. For a supplier, actual waste is

$$
\sum \text{selected box sizes}-\sum \text{package sizes}.
$$

The package-size sum is identical for every supplier, so the supplier with minimum selected capacity also has minimum waste. The code stores `ans = min(ans, s)` and subtracts `sum(packages)` only once after the best supplier is known. This avoids recomputing the same package total inside every supplier loop.

**Trace the first example.** Sorted packages are `[2, 3, 5]`. Supplier `[4, 8]` assigns the first two packages to size four because `bisect_right` returns index two; their selected capacity is eight. Size eight then consumes the remaining package, giving total capacity sixteen. Package sizes total ten, so waste is six. Supplier `[2, 8]` uses capacity two for the first package and sixteen for the remaining two, totaling eighteen and waste eight. The minimum capacity correctly selects the first supplier.

**Why leftover space and unused box sizes need no treatment.** The product `(j - i) * b` already charges one box of size `b` per assigned package. Any unused capacity in those boxes becomes waste after subtracting package sizes. Offered sizes that receive no package have `j == i` and add zero, which is correct because there is no obligation to use every box type.

**Apply the modulus only to the final minimum waste.** If at least one supplier works, `ans - sum(packages)` is nonnegative and equals the true minimum waste. The source then applies modulo $10^9+7$. Taking each supplier's capacity modulo before comparison would be wrong because modular order does not preserve ordinary numeric order. The code correctly compares full Python integers first.

**Why the assignment is globally optimal.** For a fixed viable supplier, each package receives the smallest fitting offered size by the sorted boundary construction; replacing any assignment cannot reduce its box size further. Hence `s` is that supplier's minimum possible total capacity. The outer loop evaluates every supplier that can pack all packages and takes the smallest such total. Subtracting the common package sum converts exactly that global capacity minimum into the requested global waste minimum.

## Complexity detail

Let $N$ be the number of packages, let $B$ be the total number of listed box sizes across all suppliers, and let $K$ be the largest number of sizes offered by one supplier. Sorting packages costs $O(N\log N)$. Sorting all supplier lists costs at most $O(B\log B)$ as a broad bound, or more precisely the sum of `b_j log b_j` over suppliers.

Each box size performs one `bisect_right` over packages, costing $O(\log N)$, so all boundary searches cost $O(B\log N)$. The final package sum is $O(N)$. Total time is $O(N\log N+B\log B+B\log N)$, matching the manifest.

Python's in-place sorts can use temporary storage. Package sorting may use $O(N)$ and processing one supplier may use up to $O(K)$ temporary space; supplier lists are handled sequentially. Thus $O(N+K)$ worst-case auxiliary sort workspace is a reasonable exact bound. Scalars and binary searches add constant state. The input lists themselves already exist and are mutated rather than copied.

## Alternatives and edge cases

- **Prefix sums of packages:** One can calculate each group's waste directly as `count * b - package_range_sum`. Prefix sums make range totals constant time but allocate $O(N)$ explicit storage; the source instead accumulates capacities and subtracts the one global sum.
- **Two-pointer scan per supplier:** Advancing a package pointer through sorted boxes can avoid binary search and run in $O(N+B_j)$ per supplier, but repeating an $O(N)$ scan for many suppliers can be worse than one binary search per box size.
- **Largest box too small:** The supplier is skipped immediately. If every supplier fails this test, `ans` remains infinity and the method returns `-1`.
- **Box size equal to package size:** `bisect_right` includes equal packages, giving them zero waste as required.
- **Duplicate package sizes:** The right boundary consumes all fitting occurrences together; each still receives its own box.
- **Unused small box types:** If no remaining package fits a size, `j == i` and it adds no capacity. Later larger sizes remain available.
- **Modulo timing:** Modulo is applied only after selecting the ordinary minimum. Applying it during supplier comparison can select the wrong supplier.
- **Input mutation:** The exact source sorts `packages` and each list in `boxes` in place. Callers needing original orders must pass copies.
- **Unlimited supply:** Multiplying a box size by a package count is valid only because any offered size can be used arbitrarily many times, as guaranteed.
