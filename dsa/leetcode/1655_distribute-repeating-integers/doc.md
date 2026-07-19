# Distribute Repeating Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1655 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Dynamic Programming, Backtracking, Bit Manipulation, Counting, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/distribute-repeating-integers/) |

## Problem Description
### Goal
An inventory `nums` contains repeated integer values, and each entry can be given away at most once. Customer `i` requests exactly `quantity[i]` integers. Every integer received by one customer must have the same value, although different customers may receive the same value when enough copies exist.

Determine whether every customer can be satisfied simultaneously. Inventory entries may remain unused, but a customer may not combine different integer values or receive a quantity other than the exact request.

### Function Contract
**Inputs**

- `nums`: an array of length $n$, where $1 \le n \le 10^5$, every value is between 1 and 1000, and at most 50 distinct values occur.
- `quantity`: an array of $m$ positive customer demands, where $1 \le m \le 10$ and each demand is at most $10^5$.

Let $f=\min(m,\lvert\operatorname{distinct}(\texttt{nums})\rvert)$ after retaining the $f$ largest value frequencies.

**Return value**

Return `true` if all $m$ exact demands can be assigned to value frequencies without exceeding any frequency; otherwise return `false`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4], quantity = [2]`
- Output: `false`

No value occurs twice, and one customer cannot combine two different values.

**Example 2**

- Input: `nums = [1, 2, 3, 3], quantity = [2]`
- Output: `true`

Both copies of 3 satisfy the request; values 1 and 2 may remain unused.

**Example 3**

- Input: `nums = [1, 1, 2, 2], quantity = [2, 2]`
- Output: `true`

The two customers can receive the two copies of 1 and the two copies of 2, respectively.
