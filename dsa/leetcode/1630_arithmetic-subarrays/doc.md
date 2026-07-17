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

### Required Complexity
- **Time:** $O(S)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Derive the only possible common difference.** For a query of length $k$, find its minimum and maximum. If the values can form an arithmetic progression, those extremes occupy its endpoints, so the common difference must be

$$
d=\frac{\max-\min}{k-1}.
$$

If the span is not divisible by $k-1$, no integer ordering can work. If the span is zero, every value equals the minimum and the query succeeds immediately.

**Check each required position exactly once.** For positive $d$, every value must equal $\min+jd$ for an integer position $j$ from 0 through $k-1$. Scan the subarray, reject a value whose offset from the minimum is not divisible by $d$, and reject a position that appears twice. Since there are $k$ values and exactly $k$ possible positions, distinct valid positions imply that every required progression value appears once.

The extrema argument proves that no other difference needs consideration. A successful occupancy scan supplies every element of the unique candidate progression, so sorting by position yields a valid arithmetic sequence. Every rejection identifies a missing, duplicated, or off-grid value that no rearrangement can repair.

#### Complexity detail

For a length-$k$ query, slicing, finding extrema, and checking positions take $O(k)$ time. Summed across all queries, this is $O(S)$. The current slice and its occupied-position set use $O(k)\subseteq O(n)$ auxiliary space and are discarded before the next query.

#### Alternatives and edge cases

- **Sort every range:** Sorting each selected slice and comparing adjacent differences is straightforward but takes $O(k\log k)$ per query rather than linear time.
- **Boolean occupancy array:** A length-$k$ array can replace the hash set with the same asymptotic bounds and predictable indexing.
- **Try every permutation:** Permutation enumeration is unnecessary and grows factorially.
- Every two-element range is arithmetic because its sole adjacent difference is automatically constant.
- Equal values are valid only when the common difference is zero; duplicates invalidate a positive-step candidate.
- Negative values do not change the offset-and-divisibility reasoning because the minimum anchors nonnegative offsets.
- Overlapping queries must be answered independently without modifying `nums`.

</details>
