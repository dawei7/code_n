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
