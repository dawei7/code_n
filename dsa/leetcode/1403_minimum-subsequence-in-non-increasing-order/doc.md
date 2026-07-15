# Minimum Subsequence in Non-Increasing Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1403 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/) |

## Problem Description

### Goal

Given an array `nums` of positive integers, select some of its elements as a subsequence so that their sum is strictly greater than the sum of all unselected elements. The relative positions do not constrain the returned presentation.

Use the minimum possible number of elements. If several minimum-length selections work, choose one with the greatest selected sum. Return the selected values arranged in non-increasing order.

### Function Contract

**Inputs**

- `nums`: an array of $n$ positive integers, where $1 \le n \le 500$ and $1 \le \texttt{nums[i]} \le 100$.

**Return value**

- The minimum-length qualifying selection, using the maximum sum among ties and listed in non-increasing order.

### Examples

**Example 1**

- Input: `nums = [4,3,10,9,8]`
- Output: `[10,9]`

**Example 2**

- Input: `nums = [4,4,7,6,7]`
- Output: `[7,7,6]`

**Example 3**

- Input: `nums = [6]`
- Output: `[6]`

### Required Complexity

- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

Sort all values in non-increasing order. Starting from the largest, append values to the answer and maintain their selected sum. Stop as soon as the selected sum is strictly greater than the total sum minus the selected sum.

For any fixed length $k$, the $k$ largest values have at least as much total satisfaction as any other $k$-element selection. Therefore, if this prefix does not exceed the remaining sum, no length-$k$ selection can qualify. The first prefix that does qualify consequently has minimum length.

The same dominance also resolves the tie rule: among selections of that minimum length, the largest-value prefix has maximum possible sum. It is already in the required non-increasing order.

#### Complexity detail

Sorting takes $O(n\log n)$ time and the prefix scan takes $O(n)$. The sorted copy and returned subsequence use $O(n)$ space in the worst case.

#### Alternatives and edge cases

- **Repeated maximum extraction:** Find and remove the maximum one element at a time. It produces the same order but costs $O(n^2)$ time.
- **Subset enumeration:** Testing combinations can establish minimality directly but takes exponential time.
- **Strict inequality:** Stop only when the selected sum is greater than the remainder; equality is insufficient.
- **Single element:** The only value must be returned.
- **Equal values:** More than half of the elements are necessary, and any occurrences yield the same output values.
- **Tie by length:** The required maximum-sum tie break is achieved by taking the largest values.

</details>
