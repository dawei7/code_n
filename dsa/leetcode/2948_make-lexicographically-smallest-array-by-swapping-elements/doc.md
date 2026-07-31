# Make Lexicographically Smallest Array by Swapping Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2948 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Union-Find, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/) |

## Problem Description
### Goal
You are given a 0-indexed array of positive integers `nums` and a positive
integer `limit`. In one operation, choose any two indices `i` and `j`
whose current values satisfy
$\lvert\texttt{nums[i]}-\texttt{nums[j]}\rvert\le\texttt{limit}$, then
swap those values. Perform any number of operations.

Return the lexicographically smallest reachable array. Between two arrays, the
lexicographically smaller one has the smaller value at their first differing
index.

### Function Contract
**Inputs**

- `nums`: the positive values that may be swapped
- `limit`: the inclusive maximum difference permitted for one swap

Let $N=\lvert\texttt{nums}\rvert$. The contract guarantees
$1\le N\le10^5$, $1\le\texttt{nums[i]}\le10^9$, and
$1\le\texttt{limit}\le10^9$.

**Return value**

The lexicographically smallest array reachable through zero or more legal
swaps.

### Examples
**Example 1**

- Input: `nums = [1,5,3,9,8], limit = 2`
- Output: `[1,3,5,8,9]`
- Explanation: Values `1,3,5` form one swappable component and `8,9` form
  another.

**Example 2**

- Input: `nums = [1,7,6,18,2,1], limit = 3`
- Output: `[1,6,7,18,1,2]`
- Explanation: The component containing values `1,1,2` occupies indices
  `0,4,5`, while `6,7` occupy indices `1,2`; value `18` stays fixed.

**Example 3**

- Input: `nums = [1,7,28,19,10], limit = 3`
- Output: `[1,7,28,19,10]`
- Explanation: No pair of distinct values is close enough to connect, so the
  original array is already the smallest reachable one.
