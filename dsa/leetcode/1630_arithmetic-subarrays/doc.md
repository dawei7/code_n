# Arithmetic Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1630 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/arithmetic-subarrays/) |

## Problem Description
### Goal
A sequence with at least two elements is arithmetic when every consecutive pair has the same difference. The elements may be rearranged before this condition is checked; constant sequences with difference zero are arithmetic as well.

Given an integer array `nums` and equal-length query arrays `l` and `r`, query `i` selects the inclusive, 0-indexed subarray from `l[i]` through `r[i]`. Return whether each selected multiset of values can be reordered into an arithmetic sequence. Queries are independent and may overlap.

### Function Contract
**Inputs**

- `nums`: an integer array of length $n$, where $2 \le n \le 500$ and $-10^5 \le \texttt{nums[i]} \le 10^5$.
- `l` and `r`: integer arrays of equal length $q$, where $1 \le q \le 500$ and $0 \le \texttt{l[i]} < \texttt{r[i]} < n$.
- Let

$$
S=\sum_{i=0}^{q-1}(\texttt{r[i]}-\texttt{l[i]}+1)
$$

be the total number of values examined across all queries.

**Return value**

Return a length-$q$ boolean array whose $i$th value is `true` exactly when the corresponding subarray can be rearranged into an arithmetic sequence.

### Examples
**Example 1**

- Input: `nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]`
- Output: `[true,false,true]`

The first range can become `[4,5,6]`, while the second has no constant-step ordering; the third can become `[3,5,7,9]`.

**Example 2**

- Input: `nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]`
- Output: `[false,true,false,false,true,true]`

**Example 3**

- Input: `nums = [1,3,5], l = [0], r = [2]`
- Output: `[true]`

The selected range is already arithmetic with common difference 2.
