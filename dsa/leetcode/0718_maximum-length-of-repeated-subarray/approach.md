## General

**The word “subarray” makes continuity the central requirement**

We need the greatest length of a sequence that appears contiguously in both arrays. A common subsequence is not enough: we may not skip a mismatching element and continue the same match afterward. This distinction determines the dynamic-programming state.

The exact solution defines `f[i][j]` as the length of the longest equal suffix of the two prefixes `nums1[:i]` and `nums2[:j]`. Equivalently, it is the length of the matching contiguous run that ends exactly at `nums1[i - 1]` and `nums2[j - 1]`.

The phrase “ends exactly” is essential. It gives the state a precise local transition. It also explains why this table is different from the classic longest-common-subsequence table.

**Why equal values extend the diagonal**

Suppose `nums1[i - 1] == nums2[j - 1]`. The newest elements can extend a repeated subarray ending one position earlier in both arrays. The preceding run has length `f[i - 1][j - 1]`, so the new run has length

`f[i][j] = f[i - 1][j - 1] + 1`.

The move is diagonal because a contiguous match consumes one new element from each array. Moving only upward or leftward would skip an element in one array and would no longer describe equal contiguous slices.

For example, if the equal suffixes ending at positions `i - 2` and `j - 2` have length `3`, and the next two values also match, the equal suffix ending at `i - 1` and `j - 1` has length `4`.

**Why a mismatch resets the state to zero**

If `nums1[i - 1] != nums2[j - 1]`, no nonempty repeated subarray can end at both of those positions. Even if earlier elements matched, the mismatch breaks continuity. Therefore `f[i][j]` must be `0`.

The table is initialized with zeroes, and the code writes a cell only in the equality branch. A mismatching cell consequently remains zero without needing an explicit `else` assignment.

This reset is the most important difference from longest common subsequence. A subsequence recurrence may carry a best value from `f[i - 1][j]` or `f[i][j - 1]` because skipping is allowed. Doing that here would incorrectly join pieces separated by mismatches.

**Why the table has one extra row and column**

The table dimensions are `(m + 1) x (n + 1)`. Row `0` represents an empty prefix of `nums1`, and column `0` represents an empty prefix of `nums2`. An empty prefix has no nonempty matching suffix, so those boundary cells are zero.

The extra boundary makes the transition uniform. Even when `i = 1` or `j = 1`, the diagonal predecessor `f[i - 1][j - 1]` exists. The loops can use one-based table coordinates while reading zero-based array positions `i - 1` and `j - 1`, with no special case for the first elements.

**Why a separate global answer is required**

The best repeated subarray can end anywhere. The bottom-right state describes only a match ending at the final element of both arrays, so returning `f[m][n]` would miss an earlier optimum.

Whenever the solution extends a matching suffix, it updates `ans` with the larger of its current value and `f[i][j]`. Since every possible pair of ending positions is visited, every repeated subarray appears as the suffix represented by some table cell. Taking the maximum over all such cells therefore finds the desired length.

There is no need to update `ans` on mismatches because those cells are zero and cannot improve a nonnegative maximum.

**A concrete trace**

Consider `nums1 = [1, 2, 3, 2, 1]` and `nums2 = [3, 2, 1, 4, 7]`. The optimal repeated subarray is `[3, 2, 1]`.

- When the two `3` values are compared, their diagonal predecessor contributes zero, so the new state is `1`.
- At the following pair of `2` values, the diagonal state is `1`, so the run extends to `2`.
- At the following pair of `1` values, the diagonal state is `2`, so the run extends to `3`.
- Any later mismatch leaves its state at zero, preventing that run from being continued across unrelated values.

Other equal pairs also create states, but none exceeds `3`. The global maximum therefore returns `3`.

**The correctness chain**

For each table coordinate, the state definition is correct by induction over the loops. Boundary states are zero, matching the empty-prefix definition. For an interior cell, unequal final values admit no common nonempty suffix, so zero is correct. Equal final values belong to the same suffix, and removing them leaves exactly the common suffix measured by the diagonal predecessor; adding one is therefore exact.

Every repeated subarray has a final position in each source array. At the table cell for those final positions, the state is at least that subarray’s length, and because the state represents the longest such suffix, it records the greatest length ending there. Conversely, every positive state corresponds to genuinely equal contiguous slices by the recurrence. The maximum state is thus neither too small nor too large, proving that `ans` is the required result.

## Complexity detail

Let `m = len(nums1)` and `n = len(nums2)`. The nested loops visit all `m * n` pairs of elements. Each visit performs constant-time comparison, indexing, addition, and possibly a maximum update. The time complexity is `O(mn)`.

The exact implementation allocates the complete `(m + 1) x (n + 1)` table, so its auxiliary space complexity is `O(mn)`. This is an important property of the code as written. A one-dimensional optimization can reduce the space to `O(min(m, n))`, but that optimization is not present in this exact implementation and should not be attributed to it.

The result variable and loop indices use only constant extra space beyond the table. The output is a single integer.

## Alternatives and edge cases

- **One-dimensional dynamic programming:** Keep only one row because each state needs only the previous diagonal value. Updating from right to left prevents overwriting that predecessor before it is used. By choosing the shorter array as the row width, this gives `O(mn)` time and `O(min(m, n))` auxiliary space. It is a valuable memory refinement, but its reverse update order is easier to implement incorrectly than the explicit two-dimensional table.

- **Align-and-scan method:** Slide one array across the other and measure the longest equal run in every overlap. Across all alignments this also takes `O(mn)` time and can use `O(1)` auxiliary space. It avoids a table but requires careful overlap-bound calculations.

- **Binary search with rolling hashes:** Test whether a repeated subarray of a chosen length exists and binary-search the length. This can be faster for some bounds, but collision handling or double hashing complicates correctness. The dynamic program is deterministic and straightforward.

- **Suffix structures:** A suffix array, suffix automaton, or suffix tree can model common contiguous sequences, but those structures add substantial implementation complexity and are unnecessary under moderate array lengths.

- **Do not use longest-common-subsequence transitions:** Carrying values from the top or left permits skipped elements. It can return a length that does not correspond to any contiguous subarray and therefore solves a different problem.

- **No common value:** Every interior cell remains zero, so `ans` remains zero and the method returns `0`.

- **Identical arrays:** Matching positions repeatedly extend their diagonal chain. The maximum becomes the full array length.

- **Repeated values:** Multiple table cells may represent different alignments of the same value. Treating each pair of ending positions separately is intentional and ensures that all possible contiguous alignments are considered.

- **A best match away from both ends:** The global `ans` preserves the run even after later mismatches. Returning only the last table cell would fail this common case.
