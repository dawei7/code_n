# Print Zero Even Odd

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1116 |
| Difficulty | Medium |
| Category | Concurrency |
| Topics | Concurrency |
| Supported Languages | Python |
| Official Link | [LeetCode](https://leetcode.com/problems/print-zero-even-odd/) |

## Problem Description

### Goal

The callback `printNumber(x)` writes the integer `x`. One shared `ZeroEvenOdd` instance stores a positive integer `n` and is passed to three asynchronous threads. One thread calls `zero(printNumber)` and may print only zeroes, one calls `even(printNumber)` and may print only even values, and one calls `odd(printNumber)` and may print only odd values.

Coordinate the three methods so the combined callback sequence alternates a zero with each integer from `1` through `n`: `0, 1, 0, 2, 0, 3, ...`. The sequence contains exactly $2n$ callback invocations and must remain correct regardless of thread start order or operating-system scheduling.

### Function Contract

**Inputs**

- `n`: the greatest positive integer to print, with $1 \le n \le 1000$.
- `printNumber`: a callback accepting one integer; the three methods run on separate threads sharing the same `ZeroEvenOdd` object.

**Return value**

- The methods return `None`; their combined side effects must be `0,1,0,2,...,0,n` in exactly that order.

### Examples

**Example 1**

- Input: `n = 2`
- Output: `"0102"`

**Example 2**

- Input: `n = 5`
- Output: `"0102030405"`

The display concatenates callback values without separators; values are still passed to the callback as integers.
