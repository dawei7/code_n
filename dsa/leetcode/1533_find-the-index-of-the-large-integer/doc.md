# Find the Index of the Large Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1533 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Interactive |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-index-of-the-large-integer/) |

## Problem Description
### Goal

An inaccessible integer array contains equal values at every position except one, whose value is strictly larger. Locate the index of that unique larger integer without reading individual elements directly.

The supplied `ArrayReader` reports the array length and compares the sums of two inclusive subarrays. `compareSub(l, r, x, y)` returns 1, 0, or -1 according to whether the first sum is greater than, equal to, or less than the second. Use at most 20 sum-comparison calls and return the large value's index.

### Function Contract
**Inputs**

- `reader`: A read-only `ArrayReader` for an array of length $n$, where $2 \leq n \leq 5\cdot10^5$.
- Every hidden value lies from 1 through 100; exactly one is larger and all remaining values are equal.
- `reader.length()` returns $n$ in $O(1)$ time.
- `reader.compareSub(l, r, x, y)` compares two valid inclusive subarray sums in $O(1)$ time.

**Return value**

Return the zero-based index of the unique larger value while making at most 20 calls to `compareSub`.

### Examples
**Example 1**

- Hidden array: `[7, 7, 7, 7, 10, 7, 7, 7]`
- Output: `4`
- Explanation: Equal-length half comparisons isolate the half containing 10.

**Example 2**

- Hidden array: `[6, 6, 12]`
- Output: `2`
- Explanation: Comparing the first two singleton candidates gives equal sums, so the unpaired final index is larger.

**Example 3**

- Hidden array: `[9, 12]`
- Output: `1`
- Explanation: One singleton comparison identifies the larger side.

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Compare equal-size candidate halves**

Maintain an inclusive interval known to contain the unique larger value. Split it into equal-length left and right blocks. If the first sum is larger, the exceptional index lies in the left block; if the second is larger, it lies in the right block. Every ordinary value has an equal counterpart, so only the unique excess changes the comparison.

For an even interval, the two blocks cover every candidate. For an odd interval, leave the final index unpaired and compare the two equal blocks before it. A nonzero result selects the heavier block. Equality proves that neither compared block contains the excess, so the unpaired endpoint is the answer immediately.

**Halve until one index remains**

Each nonterminal comparison reduces the candidate interval to at most half its prior length. When its endpoints meet, that sole index must contain the larger value. The largest legal input needs at most $\lceil\log_2(500000)\rceil=19$ comparisons, within the strict 20-call limit.

The three-way result is used only after making the compared blocks equal in length. Comparing unequal blocks would let their different counts of the common value dominate the sum and invalidate the deduction.

#### Complexity detail

Every query performs $O(1)$ work and halves the candidate count, so the algorithm uses $O(\log n)$ time and at most 19 `compareSub` calls on the legal domain. It stores only interval endpoints and split indices, giving $O(1)$ auxiliary space.

The accompanying asymptotic-optimality certificate records that distinguishing one exceptional position among $n$ possibilities with a constant-outcome comparison oracle requires $\Omega(\log n)$ information, matching the upper bound.

#### Alternatives and edge cases

- **Compare adjacent singletons:** eventually finds the larger value but can require $O(n)$ calls and violates the 20-query limit.
- **Unequal subarray comparison:** the ordinary values no longer cancel, so the result need not reveal which block contains the exception.
- **Materialize hidden values:** direct array access is unavailable and would violate the interactive contract.
- **Two elements:** one comparison determines the answer.
- **Odd candidate count:** equality between the paired blocks identifies the unpaired endpoint.
- **Exception at an endpoint:** the interval updates retain either boundary correctly.
- **Maximum length:** binary halving uses 19 comparisons, leaving one call of margin.
- **Value magnitude:** only relative excess matters; the actual common and exceptional values need not be known.

</details>
