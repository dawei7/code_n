# Minimum Adjacent Swaps to Alternate Parity

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3587 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/) |

## Problem Description

### Goal

You receive an array `nums` whose integer values are distinct. One operation exchanges two adjacent elements, so moving an element across several positions costs one operation per crossed neighbor.

An arrangement is valid when adjacent elements always have different parity: every neighboring pair contains one even value and one odd value. The relative order of values having the same parity does not matter to validity, but adjacent swaps may be used to reach whichever valid arrangement is cheapest.

Return the minimum number of adjacent swaps needed to produce a valid arrangement. If the counts of even and odd values make alternation impossible, return `-1`.

### Function Contract

**Inputs**

- `nums`: An array of $n$ distinct positive integers, where $1 \le n \le 10^5$ and every value is at most $10^9$.

**Return value**

Return the minimum adjacent-swap count as an integer, or `-1` when no alternating-parity arrangement exists.

### Examples

#### Example 1

- **Input:** `nums = [2, 4, 6, 5, 7]`
- **Output:** `3`
- **Explanation:** Three adjacent swaps can produce `[2, 5, 4, 7, 6]`.

#### Example 2

- **Input:** `nums = [2, 4, 5, 7]`
- **Output:** `1`
- **Explanation:** Swapping the middle pair produces `[2, 5, 4, 7]`.

#### Example 3

- **Input:** `nums = [1, 2, 3]`
- **Output:** `0`
- **Explanation:** The input already alternates between odd and even values.

#### Example 4

- **Input:** `nums = [4, 5, 6, 8]`
- **Output:** `-1`
- **Explanation:** Three even values and one odd value cannot alternate.
