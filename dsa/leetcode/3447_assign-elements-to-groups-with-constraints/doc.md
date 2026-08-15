# Assign Elements to Groups with Constraints

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3447 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/assign-elements-to-groups-with-constraints/) |

## Problem Description

### Goal

You are given integer arrays `groups` and `elements`. Each value `groups[i]` is the size of one group. Assign exactly one element index to a group when possible: index `j` is eligible for group `i` precisely when `groups[i]` is divisible by `elements[j]`.

When several elements divide the same group size, choose the smallest eligible index. Record `-1` when no element value divides that group. The same element index may be assigned to any number of groups, and repeated element values remain distinct indices even though only their earliest occurrence can ever be selected.

### Function Contract

Let $G=\lvert\texttt{groups}\rvert$, $E=\lvert\texttt{elements}\rvert$, and $V=\max(\texttt{groups})$.

**Inputs**

- `groups`: An array of $G$ positive group sizes, where $1\le G\le10^5$.
- `elements`: An array of $E$ positive candidate values, where $1\le E\le10^5$.

Every value in either array lies between $1$ and $10^5$, inclusive.

**Return value**

Return an array `assigned` of length $G$. For each index `i`, `assigned[i]` is the smallest index `j` for which `groups[i] % elements[j] == 0`, or `-1` when no such index exists.

### Examples

#### Example 1

- **Input:** `groups = [8,4,3,2,4], elements = [4,2]`
- **Output:** `[0,0,-1,1,0]`

Value `4` at index `0` handles every group divisible by four; group size `2` uses index `1`, and size `3` has no match.

#### Example 2

- **Input:** `groups = [2,3,5,7], elements = [5,3,3]`
- **Output:** `[-1,1,0,-1]`

The duplicate `3` at index `2` cannot replace its earlier occurrence at index `1`.

#### Example 3

- **Input:** `groups = [10,21,30,41], elements = [2,1]`
- **Output:** `[0,1,0,1]`

Even group sizes use index `0`; the remaining sizes are divisible by `1` at index `1`.
