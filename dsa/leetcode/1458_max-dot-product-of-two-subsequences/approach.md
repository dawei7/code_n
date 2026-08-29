## General

**Match elements in order or skip them.** A pair of subsequences must preserve the order of both original arrays and have equal nonzero length. Once `nums1[i - 1]` is paired with `nums2[j - 1]`, any earlier pairs must come from the prefixes before those positions. This makes two-dimensional dynamic programming natural.

Define `f[i][j]` as the maximum dot product of two nonempty equal-length subsequences chosen from the first `i` elements of `nums1` and the first `j` elements of `nums2`. The answer is `f[m][n]` for the complete prefixes.

Every table entry begins at negative infinity. This sentinel means no nonempty pair of subsequences is possible. In particular, row zero and column zero remain negative infinity because if either prefix is empty, at least one matched pair cannot be selected. This initialization enforces the problem's nonempty requirement inside the recurrence instead of repairing an incorrect zero answer later.

**Consider the three exhaustive decisions.** At cell `i, j`, let `x = nums1[i - 1]`, `y = nums2[j - 1]`, and `v = x * y`.

The first choice skips `x`. Any solution then comes from `f[i - 1][j]`. The second skips `y` and comes from `f[i][j - 1]`. These choices allow the algorithm to seek a better alignment elsewhere while preserving order.

The third choice pairs `x` with `y`. That pair may start new subsequences, giving dot product `v`, or extend a previously matched solution from `f[i - 1][j - 1]`, giving that value plus `v`.

The expression `max(0, f[i - 1][j - 1]) + v` combines those two pairing cases. If the prior dot product is positive, extending it improves the new result. If it is negative, discarding it and starting with the current pair is better. If it is negative infinity because no prior nonempty match exists, zero is selected and the current pair begins the subsequences.

Taking the maximum of the two skips and the pairing option gives `f[i][j]`.

**Why zero does not become an illegal empty answer.** Zero appears only inside the pairing expression and is immediately followed by `+ v`. The third choice always includes the current pair. The skip states trace back to table entries that were also created by at least one pair, because empty boundaries are negative infinity. Therefore every finite table value represents nonempty subsequences.

This detail is crucial for arrays such as `[-1, -1]` and `[1, 1]`. Every possible product is negative. A DP initialized with zero boundaries and allowed to skip everything might incorrectly return zero. Here, the best finite value is `-1`, corresponding to one required pair.

**Trace an improving combination.** For `nums1 = [2, 1, -2, 5]` and `nums2 = [3, 0, -6]`, pairing two with three gives six. Later, pairing negative two with negative six gives twelve. The diagonal predecessor allows those ordered pairs to combine, producing eighteen. Other table choices skip the one and the five where they do not improve this alignment.

The recurrence never pairs elements out of order. Moving to `f[i - 1][j - 1]` before adding the current pair means all earlier chosen indices are smaller in both arrays.

**Why the recurrence is complete.** Take an optimal solution for prefixes `i, j`. If it does not use `x`, it is represented by the first skip state. If it uses `x` but not `y`, it is represented after skipping `y`. If it pairs `x` and `y`, removing that last pair leaves either no pairs or a valid solution from the two shorter prefixes, exactly the third option. These cases cover every possible optimal alignment.

The two skip cases overlap in some represented solutions, but taking a maximum is unaffected by duplicate representation. Each cell stores a value, not a count of solutions.

**Filling order satisfies dependencies.** The loops increase `i` and `j`. When computing `f[i][j]`, the previous row `f[i - 1][j]`, the previous column in the current row `f[i][j - 1]`, and the diagonal `f[i - 1][j - 1]` have already been computed. No recursion or memo lookup is needed.

Induction over this row-major order proves each state contains the best nonempty dot product for its two prefixes. The bottom-right state therefore answers the full problem.

**Be precise about stored space.** The manifest advertises `O(min(m, n))` space, which is achievable with rolling rows. The exact source allocates `(m + 1)` lists each containing `n + 1` entries. Its actual auxiliary space is `O(mn)`. The recurrence and time are optimal, but the stored implementation does not perform the manifest's space compression.

## Complexity detail

There are `mn` non-boundary table cells. Each computes one multiplication, a constant number of additions and maximum comparisons, so total time is `O(mn)`.

The full table has `(m + 1)(n + 1)` numeric entries, giving `O(mn)` auxiliary space for this exact code. Loop variables use constant additional storage.

Only the previous row and the current row are needed at any moment. A rolling implementation can choose the shorter array as the column dimension and use `O(min(m, n))` space, matching the manifest. That optimization is an alternative, not present in the stored source.

Negative infinity is a constant sentinel in the arithmetic model. Python floating negative infinity combines safely with `max` and addition for these integer products; every reachable final value is an integer-valued result.

## Alternatives and edge cases

- **Rolling two rows:** Keep only the previous and current DP rows and orient columns along the shorter array. This preserves `O(mn)` time and achieves the manifest's `O(min(m,n))` space.
- **One carefully updated row:** With saved diagonal state, space can also be compressed further in constants, but update order becomes easier to get wrong.
- **Top-down memoization:** Recursively choose pair or skips and cache `i, j`. It has the same state count but adds call-stack overhead.
- **Initialize boundaries to zero:** Without extra special cases, this permits empty subsequences and can incorrectly return zero when every legal product is negative.
- **Always extend the diagonal:** Adding a negative previous dot product can make a new pair worse. `max(0, previous)` permits starting fresh at the current pair.
- **All cross-products negative:** The DP selects the least negative single pair rather than the illegal empty value zero.
- **Positive and negative pairs:** Two negative elements can produce a useful positive product, so sign-based greedy choices are unreliable.
- **Zeros in an array:** A nonempty pair can have dot product zero, and the DP represents it as a finite valid state.
- **One-element array:** The solution chooses the best pairing of that element with one element from the other array.
- **Different array lengths:** Skipping allows equal-length subsequences to be selected without requiring equal original lengths.
- **Relative order:** The diagonal predecessor preserves order in both arrays; sorting either input would change the problem.
- **Large products:** Values up to one thousand in magnitude and lengths up to five hundred fit the expected result range, and Python integers avoid overflow.
- **Nonempty condition:** Every finite state ultimately contains a pairing transition; negative-infinity boundaries prevent skip-only paths.
- **Space reporting:** Use `O(mn)` for this exact table. Use `O(min(m,n))` only after implementing rolling storage.
