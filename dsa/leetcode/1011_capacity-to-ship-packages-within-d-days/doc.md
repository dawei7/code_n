# Capacity To Ship Packages Within D Days

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1011 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) |

## Problem Description

### Goal

A conveyor belt holds packages that must be shipped from one port to another within `days` days. Package `i` has weight `weights[i]`.

Each day, load consecutive packages from the conveyor belt in their given order without exceeding the ship's maximum weight capacity. Packages cannot be reordered, and a package is never split between days. Return the least ship capacity that allows every package to be shipped within `days` days.

### Function Contract

**Inputs**

- `weights`: an array of $N$ package weights in shipping order, where $1\le N\le5\cdot10^4$ and $1\le\texttt{weights[i]}\le500$.
- `days`: the maximum number of shipping days, where $1\le\texttt{days}\le N$.

Define the total package weight as

$$
S=\sum_{w\in\texttt{weights}}w.
$$

**Return value**

- The minimum integer ship capacity that completes the ordered shipment within `days` days.

### Examples

**Example 1**

- Input: `weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days = 5`
- Output: `15`
- Explanation: Capacity `15` supports daily groups `[1,2,3,4,5]`, `[6,7]`, `[8]`, `[9]`, and `[10]`; capacity `14` cannot preserve this order within five days.

**Example 2**

- Input: `weights = [3, 2, 2, 4, 1, 4], days = 3`
- Output: `6`
- Explanation: The packages can be shipped as `[3,2]`, `[2,4]`, and `[1,4]`.

**Example 3**

- Input: `weights = [1, 2, 3, 1, 1], days = 4`
- Output: `3`
- Explanation: Use daily groups `[1]`, `[2]`, `[3]`, and `[1,1]`.

### Required Complexity

- **Time:** $O(N\log S)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Bound the capacity answer:** The ship must hold the heaviest individual package, so `max(weights)` is the smallest candidate. Capacity $S$ ships everything in one day and is always feasible, giving an inclusive search interval containing the optimum.

**Test one capacity greedily:** Scan packages in order, adding each weight to the current day's load. If the next package would exceed `capacity`, begin a new day with that package. This greedy choice packs every day as fully as the fixed order permits, so no other schedule with the same capacity can use fewer days.

**Binary-search the feasibility transition:** If a capacity succeeds, every larger capacity also succeeds; if it fails, every smaller capacity fails. Test the midpoint, retaining the lower half when feasible and the upper half otherwise. When the bounds meet, that value is the least feasible capacity.

The greedy test exactly determines whether a candidate can meet the deadline, and feasibility is monotone in capacity. Binary search therefore discards only values that cannot be the minimum and terminates at the requested optimum.

#### Complexity detail

Computing the bounds costs $O(N)$. Each feasibility test scans at most $N$ weights, and binary search performs $O(\log S)$ tests, for $O(N\log S)$ total time. The bounds, counters, and current load use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Try every capacity:** Testing integers from `max(weights)` upward is correct but can require $O(NS)$ time.
- **Dynamic programming over day boundaries:** It can represent all partitions but uses substantially more time and space than monotone answer search.
- **One day:** The capacity must equal $S$.
- **One day per package:** The minimum capacity is `max(weights)`.
- **Order constraint:** A feasible schedule partitions the array into contiguous groups; arbitrary redistribution between days is invalid.

</details>
