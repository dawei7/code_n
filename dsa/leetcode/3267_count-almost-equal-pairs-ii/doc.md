# Count Almost Equal Pairs II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3267 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Counting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-almost-equal-pairs-ii/) |

## Problem Description

### Goal

Two positive integers are almost equal when they can be made equal using at most two operations in total. Each operation chooses either one of the two integers and swaps any two digit positions within that chosen integer. Both swaps, when used, may be performed on the same chosen integer; doing nothing or using only one swap is also allowed.

A swap may move zero to the front. Leading zeros are discarded when the resulting digit sequence is interpreted as an integer, so values with different displayed digit lengths can still be almost equal.

Given `nums`, count index pairs `(i, j)` with $i < j$ whose values are almost equal. Repeated equal values at different indices form separate pairs.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $2 \le n \le 5000$ and every value is less than $10^7$.

Let $d$ be the maximum decimal digit count, so $d \le 7$.

**Return value**

- The number of index pairs that can be made equal using zero, one, or two digit swaps applied to either member of the pair.

### Examples

#### Example 1

- **Input:** `nums = [1023,2310,2130,213]`
- **Output:** `4`

The qualifying pairs are `(1023,2310)`, `(1023,213)`, `(2310,2130)`, and `(2310,213)`.

#### Example 2

- **Input:** `nums = [1,10,100]`
- **Output:** `3`

Every pair qualifies through a swap that moves a nonzero digit past one or more leading zeros.

#### Example 3

- **Input:** `nums = [123456,456123]`
- **Output:** `0`

These arrangements differ by three disjoint position swaps, so two operations are insufficient.
