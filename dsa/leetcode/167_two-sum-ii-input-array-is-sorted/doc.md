# Two Sum II - Input Array Is Sorted

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 167 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) |

## Problem Description
### Goal
Given a one-indexed array of integers sorted in non-decreasing order, find two positions whose values add exactly to `target`. The first chosen position must precede the second, and the input guarantee states that exactly one valid pair exists.

Return the two one-based indices as `[index1, index2]` with `index1 < index2`. Duplicate values may supply the pair when they occur at separate positions, but you may not use the same element twice. Preserve the sorted input and meet the constant-extra-space requirement; the output contains indices rather than the matched values.

### Function Contract
**Inputs**

- `numbers`: a nondecreasing list of integers
- `target`: required sum of exactly two distinct positions

**Return value**

The pair of one-based indices `[index1, index2]` with `index1 < index2`.

### Examples
**Example 1**

- Input: `numbers = [2,7,11,15], target = 9`
- Output: `[1,2]`

**Example 2**

- Input: `numbers = [2,3,4], target = 6`
- Output: `[1,3]`

**Example 3**

- Input: `numbers = [-1,0], target = -1`
- Output: `[1,2]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Sorting changes Two Sum from a lookup problem into an elimination problem. Put `left` at the smallest value and `right` at the largest, then inspect their sum.

- If the sum equals `target`, these are the required positions.
- If the sum is too small, increment `left`. Keeping that left value and choosing any smaller right endpoint could only decrease the sum, so the current left position cannot belong to a solution inside the remaining interval.
- If the sum is too large, decrement `right`. Keeping that right value and choosing any larger left endpoint could only increase the sum, so the current right position cannot belong to a solution.

The key is that each comparison eliminates an entire row or column of possible pairs, not just one pair. For `[2, 7, 11, 15]` and target `9`, $2 + 15$ is too large, so `15` is discarded; $2 + 11$ is also too large, so `11` is discarded; $2 + 7$ matches. Convert the zero-based pointer positions to the required one-based result `[1, 2]`.

Throughout the scan, the promised solution remains between `left` and `right`. When a boundary is removed, monotonic order proves that the boundary value cannot pair with any still-eligible position to reach the target. Because a valid pair is guaranteed, the pointers must encounter it before crossing.

Suppose the current sum is below the target. Every candidate partner for `numbers[left]` within the remaining interval is at most `numbers[right]`, so all such sums are at most the already-too-small current sum. Discarding `left` cannot discard a solution. The symmetric argument proves that a too-large sum allows `right` to be discarded safely. Thus every update preserves the valid pair in the candidate interval. When the current sum equals the target, the two distinct boundary indices form the required pair, so returning them is correct.

#### Complexity detail

Each pointer moves only inward and can move at most $n - 1$ times. The total running time is $O(n)$, and the two indices plus current sum use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- A hash map also finds complements in $O(n)$ time, but uses $O(n)$ space and ignores the sorted-order guarantee.
- Binary-searching for each complement uses constant auxiliary space but costs $O(n \log n)$ time.
- Nested loops test $O(n^2)$ pairs.
- Equal values may form the answer when they occupy different positions; the pointer condition naturally preserves distinct indices.
- Negative values and boundary pairs need no special handling.
- The output indices are one-based even though most implementations use zero-based pointers internally.

</details>
