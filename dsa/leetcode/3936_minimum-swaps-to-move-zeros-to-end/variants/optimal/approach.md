## General

Only the distinction between zero and nonzero matters. The relative order of the nonzero values is not required to remain stable, and one operation may swap any two distinct positions rather than only adjacent positions.

The desired final shape is:

`[all nonzero values][all zero values]`.

A swap is useful exactly when it exchanges a zero that lies too far left with a nonzero that lies too far right. The source counts how many such pairs can be fixed; it does not need to perform the swaps or modify `nums`.

**Find the next misplaced zero from the left**

Pointer `i` starts at index zero. The loop

`while i < n and nums[i] != 0`

skips values that are already suitable for the nonzero prefix. It stops at the first zero not previously handled, or moves beyond the array if no zero remains.

That zero is not automatically wrong merely because it occurs somewhere in the array. It is wrong only if some nonzero still occurs to its right. If every later entry is zero, the array already has the required suffix from that point onward.

**Find the next misplaced nonzero from the right**

Pointer `j` starts at the final index. The loop

`while j and nums[j] == 0`

skips zeroes that are already suitable for the final suffix. It stops at a nonzero value or at index zero.

The condition `while j` means “while `j != 0`.” It deliberately avoids decrementing `j` below zero. This slightly unusual spelling is safe because the outer logic only forms a pair when `i < j`. If both pointers have met at index zero, no swap is needed.

**One crossing pair needs one swap**

After the scans, if `i < j`, then:

- `nums[i]` is zero;
- `nums[j]` is nonzero;
- the zero is to the left of the nonzero.

They are a mismatched pair relative to the desired nonzero-prefix/zero-suffix order. Swapping them would put a nonzero at `i` and a zero at `j`, correcting both positions in one operation.

The source increments `ans` and then advances `i` and decreases `j`. It does not physically exchange the array values. That omission is safe because the conceptual swap would make both boundary positions correct, and neither position will be inspected again. Everything between the new pointers is unchanged.

The next outer iteration skips any additional already-correct values and locates the next crossing pair.

**Why stopping when the pointers cross is enough**

If `i >= j`, no zero found by the left scan lies strictly before a nonzero found by the right scan. Therefore there is no remaining pattern in which a zero precedes a later nonzero. A binary classification with no such inversion must consist of all nonzero values followed by all zeroes.

For example, `[1, 2, 0]` makes `i` stop at the final index while `j` moves left past that trailing zero. The pointers meet or cross, so the source returns zero.

For `[0, 1, 0, 2]`, `i=0` and `j=3` form one pair. A conceptual swap yields `[2,1,0,0]`, and both pointers move inward. No crossing pair remains, so the minimum is one.

**Why the count is minimal**

Let $Z$ be the total number of zeroes. In every valid final array, the final $Z$ positions must all be zero. Count how many nonzero values currently occupy those reserved suffix positions. Every such nonzero must leave the suffix.

One arbitrary swap can fix at most one of these suffix mismatches because it can bring at most one zero into one suffix position. This count is therefore a lower bound on the number of operations.

The number of zeroes misplaced in the first $N-Z$ positions is equal to the number of nonzeroes misplaced in the last $Z$ positions: the array has the correct total count of each category, so mismatches balance. Each pair found by the two pointers matches one misplaced prefix zero with one misplaced suffix nonzero. Their conceptual swap fixes both. The source achieves the lower bound one pair at a time, so its count is minimal.

This also explains why adjacent-swap inversion counting would be wrong for this problem. A distant zero and nonzero can exchange in one allowed operation regardless of how many positions lie between them.

## Complexity detail

Let $N$ be the length of `nums`. Pointer `i` only increases and pointer `j` only decreases. Across all nested loops, each index is passed at most once from each direction. The total time complexity is $O(N)$ rather than $O(N^2)$.

The source stores only `ans`, `n`, and the two indices. It does not allocate another array, count table, or recursion stack, so additional space is $O(1)$.

The input is never changed. Skipping the physical swaps does not affect the count because handled endpoints are excluded from all future searches.

The $O(N)$ time is asymptotically optimal for an unsummarized input: in the worst case, the algorithm must inspect values across the array to determine whether a misplaced zero/nonzero pair exists.

## Alternatives and edge cases

- **Count nonzeroes in the reserved suffix:** First count $Z$, then count nonzero entries among the last $Z$ positions. This yields the same minimum in two linear passes and makes the mismatch lower bound explicit.
- **Actually perform each swap:** This returns the same count and constructs a valid arrangement, but mutation is unnecessary because only the minimum number is requested.
- **Stable two-pointer compaction:** Moving nonzeroes forward while preserving their relative order solves a stronger arrangement problem. Counting writes or adjacent movements would not equal the arbitrary-swap minimum.
- **Count zero-before-nonzero inversions:** That measures adjacent swaps. One arbitrary swap can eliminate many such inversions, so the inversion total overestimates the answer.
- **All zeroes:** The right pointer skips the zero suffix until the pointers meet, and no swap is counted.
- **No zeroes:** The left pointer reaches `n`, the pointers cross, and the result is zero.
- **Already partitioned array:** Every nonzero is skipped from the left and every trailing zero from the right; no crossing pair is formed.
- **All zeroes before all nonzeroes:** The algorithm pairs the outermost mismatches and returns the smaller of the zero and nonzero counts, which is exactly the number of wrong suffix positions.
- **One-element array:** The pointers start equal, so the loop exits with zero whether the value is zero or nonzero.
- **Zero at the left and nonzero at the right:** They can be exchanged directly in one operation even when far apart.
- **Repeated nonzero values:** Their identities do not matter; only whether each value is zero affects its target region.
- **The condition `while j` at index zero:** It does not inspect past the beginning. The later `i >= j` check prevents treating an unclassified index-zero value as a swappable right endpoint.
