# Maximum Length of Repeated Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 718 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Dynamic Programming, Sliding Window, Rolling Hash, Hash Function |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) |

## Problem Description
### Goal
Given two integer arrays `nums1` and `nums2`, find a subarray that appears in both arrays. A subarray is a contiguous sequence, so its values must occur in the same order at consecutive positions in each input.

Return the maximum length of any repeated subarray. The matching occurrences may begin at different indices in the two arrays, and equal values outside the selected ranges do not matter. If the arrays share no value, return `0`; noncontiguous common subsequences do not qualify.

### Function Contract
**Inputs**

- `nums1`: the first nonempty integer array
- `nums2`: the second nonempty integer array

**Return value**

- The length of their longest common contiguous subarray, or `0` when they share no value

### Examples
**Example 1**

- Input: `nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]`
- Output: `3`

**Example 2**

- Input: `nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]`
- Output: `5`

**Example 3**

- Input: `nums1 = [1,2,3], nums2 = [4,5,6]`
- Output: `0`

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(\min(m, n))$

<details>
<summary>Approach</summary>

#### General

**Describe a repeated subarray by where it ends**

For a position in each array, define a state as the length of the common suffix ending immediately before those two positions. This ending-based state preserves contiguity: extending it by one is allowed only when the newly considered values match.

**Use the diagonal transition**

If `nums1[i] = nums2[j]`, the suffix ending at that pair has length one plus the suffix ending at $i - 1$ and $j - 1$. If the values differ, the suffix length is zero because a contiguous match cannot skip either value. Track the greatest state seen anywhere rather than only the state at the arrays' ends.

**Compress the shorter dimension**

Keep one row whose columns correspond to the shorter array. Process its columns from right to left. The transition for column $j + 1$ reads column `j` from the preceding conceptual row; reverse order ensures that value has not yet been overwritten by the current row.

**Why the maximum state is the answer**

Every common contiguous subarray has a final value at some index pair, and the state at that pair counts its entire length by following equal diagonal predecessors. Conversely, every positive state represents exactly that many equal consecutive pairs. Taking the maximum therefore includes every candidate and cannot count a noncontiguous sequence.

#### Complexity detail

The algorithm evaluates every pair of positions once, taking $O(mn)$ time for lengths `m` and `n`. The row has one entry per position in the shorter array, so it uses $O(\min(m, n))$ extra space.

#### Alternatives and edge cases

- **Full two-dimensional table:** it uses the same recurrence and time but stores $O(mn)$ states, which is unnecessary when only the previous row is read.
- **Slide every relative alignment:** compare the overlapping portion under each offset; the total work remains $O(mn)$ and uses $O(1)$ extra space.
- **Binary search with rolling hashes:** test whether a common window of a chosen length exists in near-linear time per search step, but hash collisions require direct confirmation or multiple hashes.
- **Extend every matching start pair:** it is straightforward, but repeatedly rescanning the same equal runs can take $O(mn \min(m, n))$ time.
- A common subsequence with gaps does not qualify; every counted value must occupy consecutive indices in both arrays.
- If no pair of values matches, every state remains zero.
- Duplicate values can start many candidates, so the algorithm must retain the best ending pair rather than stop at the first match.
- A complete match of the shorter array is the largest possible answer.

</details>
