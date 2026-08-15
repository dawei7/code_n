# Count Special Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3404 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-special-subsequences/) |

## Problem Description

### Goal

You are given an array `nums` of positive integers. A special subsequence is determined by four indices $(p,q,r,s)$ in strictly increasing order. Its values must satisfy

$$
\texttt{nums[p]}\cdot\texttt{nums[r]}=\texttt{nums[q]}\cdot\texttt{nums[s]}.
$$

The selected indices may not be adjacent: at least one unselected array element must lie between each consecutive pair. Equivalently, $q-p>1$, $r-q>1$, and $s-r>1$. Return the number of distinct index quadruples that meet both the spacing rules and the product equality. Equal value sequences chosen from different indices count separately.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers.

The constraints are $7\le n\le1000$ and $1\le\texttt{nums[i]}\le1000$.

**Return value**

- The number of special subsequences, counted by their index quadruples.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 3, 4, 3, 6, 1]`
- **Output:** `1`

The sole valid quadruple is $(0,2,4,6)$, producing values $(1,3,3,1)$. Both products equal 3, and every neighboring selected pair has one intervening index.

#### Example 2

- **Input:** `nums = [3, 4, 3, 4, 3, 4, 3, 4]`
- **Output:** `3`

The valid index quadruples are $(0,2,4,6)$, $(1,3,5,7)$, and $(0,2,5,7)$. Their corresponding products match while respecting all three required gaps.
