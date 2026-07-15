# Uncrossed Lines

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1035 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/uncrossed-lines/) |

## Problem Description

### Goal

Write the integers of `nums1` and `nums2`, in their given orders, on two separate horizontal lines.

You may connect `nums1[i]` to `nums2[j]` with a straight line only when `nums1[i] == nums2[j]`. No chosen connecting line may intersect another non-horizontal connecting line, even at an endpoint, so each array element can participate in at most one connection.

Return the maximum number of connecting lines that can be drawn under these rules.

### Function Contract

**Inputs**

- `nums1`: an integer array of length $M$, where $1 \le M \le 500$.
- `nums2`: an integer array of length $N$, where $1 \le N \le 500$.
- Every value in both arrays lies between $1$ and $2000$, inclusive.

**Return value**

- The largest number of equal-value pairs that can be connected without crossings or shared endpoints.

### Examples

**Example 1**

- Input: `nums1 = [1,4,2], nums2 = [1,2,4]`
- Output: `2`
- Explanation: Connecting all three equal values would force the lines for `4` and `2` to cross.

**Example 2**

- Input: `nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]`
- Output: `3`

**Example 3**

- Input: `nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]`
- Output: `2`

### Required Complexity

- **Time:** $O(MN)$
- **Space:** $O(\min(M,N))$

<details>
<summary>Approach</summary>

#### General

**Translate geometry into index order:** Two lines do not cross exactly when their matched indices increase in the same order in both arrays. Requiring equal endpoint values and forbidding shared endpoints therefore asks for the longest common subsequence.

**Define prefix states:** For prefixes ending before `i` and `j`, store the maximum number of lines. If the current values match, extend the diagonal prefix by one. Otherwise, skip one current value and keep the larger result from the prefix above or to the left.

**Keep only two rows:** Each new DP row depends only on the previous row and values already written in the current row. Make the shorter input the column dimension, so these two arrays use $O(\min(M,N))$ memory.

Every DP transition constructs legal increasing index pairs. Conversely, the last line of any optimal drawing either connects the current equal values or leaves at least one current endpoint unused, matching one of the recurrence branches. Induction over the two prefix lengths proves the final state is optimal.

#### Complexity detail

The algorithm evaluates all $M\cdot N$ prefix pairs with constant work per pair, taking $O(MN)$ time. Two rows of length $min(M,N)+1$ use $O(\min(M,N))$ auxiliary space.

#### Alternatives and edge cases

- **Full DP table:** Store every prefix state for the same $O(MN)$ time but $O(MN)$ space; this is useful only when reconstructing the actual lines.
- **Recursive memoization:** Express the same recurrence top-down, but recursion and memo entries can consume $O(MN)$ space.
- **Match-pair chain DP:** Create every equal index pair and find the longest chain increasing in both coordinates. A direct comparison of all match pairs can take $O(K^2)$ time for $K$ matches.
- **No shared values:** The answer is zero.
- **Repeated values:** Each occurrence remains a distinct endpoint and can be used at most once.
- **Reversed order:** Equal sets do not imply many lines when their index orders oppose one another.
- **Unequal lengths:** Using the shorter array for columns changes memory use, not the result.

</details>
