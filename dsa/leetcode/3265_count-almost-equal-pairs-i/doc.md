# Count Almost Equal Pairs I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3265 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Counting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-almost-equal-pairs-i/) |

## Problem Description

### Goal

Two positive integers are almost equal when they can be made equal using at most one operation in total. The operation chooses either integer and swaps any two digit positions within that chosen number. Performing no swap is allowed, so equal values are already almost equal.

A swap may place zero at the front. Such leading zeros are discarded when the resulting digit sequence is interpreted as an integer; for example, swapping the digits of `30` can produce `03`, which represents `3`.

Given `nums`, count index pairs `(i, j)` with $i < j$ whose values are almost equal. Equal values at different indices form distinct pairs.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $2 \le n \le 100$ and $1 \le \texttt{nums[i]} \le 10^6$.

Let $d$ be the maximum number of decimal digits in an input value, so $d \le 7$.

**Return value**

- The number of index pairs whose two values are equal after zero or one digit swap applied to either member of the pair.

### Examples

#### Example 1

- **Input:** `nums = [3,12,30,17,21]`
- **Output:** `2`

The qualifying value pairs are `3` with `30`, and `12` with `21`.

#### Example 2

- **Input:** `nums = [1,1,1,1,1]`
- **Output:** `10`

All $\binom{5}{2}$ index pairs contain equal values.

#### Example 3

- **Input:** `nums = [123,231]`
- **Output:** `0`

Moving from one order to the other requires more than one digit swap.
