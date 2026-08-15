# Maximum Employees to Be Invited to a Meeting

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2127 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Depth-First Search, Graph Theory, Topological Sort |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/) |

## Problem Description

### Goal

A company has $n$ employees numbered from $0$ through $n-1$ and a circular
table that can hold any number of them. Every employee names exactly one
favorite employee, and nobody names themself.

An invited employee will attend only when their favorite is seated directly
beside them. Because each seat at the circular table has two neighbors, an
arrangement may satisfy several favorite relationships at once, but it cannot
give one person more than those two adjacent positions. Determine the largest
number of employees for which some circular seating satisfies every invited
employee.

### Function Contract

**Inputs**

- `favorite`: A 0-indexed integer array of length $n$, where `favorite[i]` is
  employee $i$'s favorite. It satisfies $2\le n\le 10^5$,
  $0\le \texttt{favorite[i]}<n$, and `favorite[i] != i`.

**Return value**

The maximum number of employees that can be invited and seated so each one is
adjacent to their favorite.

### Examples

#### Example 1

- **Input:** `favorite = [2, 2, 1, 2]`
- **Output:** `3`
- **Explanation:** Employees `0`, `1`, and `2` can be seated together. Inviting
  employee `3` as well would require employee `2` to have three neighbors.

#### Example 2

- **Input:** `favorite = [1, 2, 0]`
- **Output:** `3`
- **Explanation:** The three favorite links form one circular seating, so every
  employee can attend.

#### Example 3

- **Input:** `favorite = [3, 0, 1, 4, 1]`
- **Output:** `4`
- **Explanation:** Employees `0`, `1`, `3`, and `4` have a valid arrangement;
  employee `2` cannot also occupy a seat beside favorite employee `1`.
