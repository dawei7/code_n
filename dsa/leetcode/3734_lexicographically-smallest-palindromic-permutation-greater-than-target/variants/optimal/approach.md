## General

**A palindrome is determined by its first half and optional middle**

Count every letter in `s`. A palindromic permutation can exist only when at most one character has odd frequency. Every character away from the center must be paired with an identical mirrored character, while an odd-length palindrome may place one unpaired character in the middle.

The source gathers all odd-frequency letter indices. If there are more than one, it returns `""`. Parity of the total length guarantees that the remaining cases are consistent: an even total has zero odd counts, and an odd total has exactly one.

The middle character is the unique odd letter when present. Each first-half count is `frequency[c] // 2`. Once a first half `half` is chosen, the complete palindrome is forced:

`half + middle + half[::-1]`.

Therefore the search only needs to construct the lexicographically smallest feasible first half that leads to a full palindrome strictly greater than `target`.

**Match the target's first half as long as possible**

The list `remaining` stores unused first-half letter counts, and `matched` stores indices already chosen equal to `target`. Starting at position zero, the algorithm consumes `target[position]` whenever that half-letter remains available.

Matching is preferable to choosing a larger letter immediately because a longer equal prefix is lexicographically smaller than any candidate that becomes greater earlier. Choosing a smaller letter would make the entire palindrome smaller at the first difference and could never be repaired by mirrored characters later.

The forward scan stops when the next target letter is unavailable or the entire first half has been matched.

**Handle the case where the first half matches completely**

If all half positions match, the source builds the forced palindrome and compares the entire string with `target`. This comparison is necessary because when the first halves are identical, the middle or mirrored second half can decide the ordering.

If that palindrome is already strictly greater, it is optimal: no palindrome can have a smaller first half without becoming smaller than the target, and this one uses the exact target half.

If it is equal or smaller, the algorithm must change some position in the first half to a larger letter. It moves `position` back to the final half index and begins backtracking.

**Backtrack to the rightmost feasible larger pivot**

At a pivot position, the result will:

1. Match `target` before the pivot.
2. Use the smallest available letter greater than `target[position]`.
3. Put all remaining half letters in ascending order.
4. Mirror the half around the fixed middle.

When backtracking over a previously matched position, the source pops that letter and restores one copy to `remaining`. At the first forward-scan failure, no character was consumed at the failed position, so the conditional pop correctly does nothing.

The search for `replacement` scans letter indices from one above the target letter upward. The first available index is the smallest feasible greater choice. Once it is consumed, the source expands all remaining counts in alphabetic order to form the smallest suffix.

The half is built as

`target[:position] + replacement + sorted_suffix`.

Although it uses the target slice rather than the `matched` list, those characters are identical by the matching invariant. The first difference is the greater replacement, so the full palindrome is guaranteed to exceed `target` regardless of its middle and mirrored suffix.

If no greater replacement is available, the pivot moves one position left. Searching from right to left is essential: a candidate that matches the target through a later position is lexicographically smaller than every candidate forced to become greater earlier.

For `s="baba"`, half counts contain one `a` and one `b`. Against `target="abba"`, the exact half `"ab"` forms `"abba"`, which is not strictly greater. Backtracking replaces the first-half `a` with `b` and uses `a` afterward, producing half `"ba"` and palindrome `"baab"`.

**Why the first returned palindrome is globally smallest**

Any qualifying palindrome has a first position where it exceeds `target`, unless its first half matches and the middle/right side already makes it greater. The algorithm tests the complete-match case first. Otherwise it tries pivot positions from latest to earliest. At the first feasible pivot it chooses the smallest greater letter and the sorted-minimum suffix.

These choices follow lexicographic priority exactly: latest first difference, then smallest character at that difference, then smallest suffix. Every letter count is consumed from the half multiset and mirrored, so every returned string is a palindromic permutation of `s`. If all pivots fail, no qualifying palindrome exists.

## Complexity detail

Let `n` be the string length. Frequency counting, matching, suffix construction, mirroring, and final concatenation each take $O(n)$ time. Backtracking visits at most `n/2` positions, and each replacement search scans 26 letters, a fixed alphabet, so it is $O(n)$. Total time is $O(n)$.

The frequency arrays are constant-sized. `matched`, the constructed suffix, half, and returned palindrome use $O(n)$ space, giving $O(n)$ auxiliary/output construction space.

## Alternatives and edge cases

- **Enumerate palindromic permutations:** Even halving the permutation space remains factorial. Frequency-guided pivot construction jumps directly to the smallest successor.
- **Find a next permutation of an arbitrary half:** Sorting the half and repeatedly advancing can traverse many permutations. Matching and backtracking locate the successor relative to `target` directly.
- **Ignore odd frequencies:** More than one odd count makes mirrored pairing impossible, so this feasibility check must precede construction.
- **Compare only the first half:** When halves match, the middle and mirrored portion can determine whether the palindrome is greater; the source correctly compares the full palindrome.
- **Choose an earlier pivot first:** It produces a larger result than a feasible later pivot.
- **Choose a larger-than-necessary replacement:** For a fixed pivot, that immediately worsens the answer. Ascending scanning finds the smallest.
- **Leave the suffix unsorted:** Once the pivot guarantees strict greaterness, ascending suffix order minimizes the result.
- **Even length:** There is no middle character, and every frequency must be even.
- **Odd length:** The unique odd-frequency letter is forced into the center.
- **Length one:** The sole letter is the only palindrome; it is returned only when strictly greater than the one-character target.
- **Exact equality with target:** Equality fails the strict condition and triggers backtracking.
- **Restoring counts:** Every popped match must return to `remaining` or later pivots would search an incomplete multiset.
