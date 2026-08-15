# Flatten Deeply Nested Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2625 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/flatten-deeply-nested-array/) |

## Problem Description

### Goal

Given a multidimensional array `arr` and a nonnegative depth limit `n`, return a version in which nested arrays are expanded only while their nesting depth is less than `n`.

A multidimensional array is recursive: each entry is either an integer or another multidimensional array. Entries of the outer array are at depth zero. When an array entry is expanded, its own entries take that array's place in the same left-to-right order. Arrays at the depth limit remain intact, including everything nested inside them.

For example, a limit of zero preserves the original top-level structure, while a limit larger than the maximum nesting depth removes every nested array boundary. Implement this behavior without calling JavaScript's built-in `Array.flat` method.

### Function Contract

**Inputs**

- `arr`: A multidimensional array containing integers and nested arrays.
- `n`: The maximum number of nesting levels to flatten, with $0 \le \texttt{n} \le 1000$.

The input contains at most $10^5$ numbers and at most $10^5$ subarrays, its maximum nesting depth is at most $1000$, and every integer is between $-1000$ and $1000$.

Let $V$ be the number of array entries inspected before the depth cutoff, and let $D$ be the greatest nesting depth traversed by the algorithm.

**Return value**

Return a new array whose entries retain their original order, with exactly those nested array boundaries above depth `n` removed.

### Examples

#### Example 1

- **Input:** `arr = [1,2,3,[4,5,6],[7,8,[9,10,11],12],[13,14,15]]`, `n = 0`
- **Output:** `[1,2,3,[4,5,6],[7,8,[9,10,11],12],[13,14,15]]`
- **Explanation:** No nested array has a depth less than zero, so none is expanded.

#### Example 2

- **Input:** `arr = [1,2,3,[4,5,6],[7,8,[9,10,11],12],[13,14,15]]`, `n = 1`
- **Output:** `[1,2,3,4,5,6,7,8,[9,10,11],12,13,14,15]`
- **Explanation:** Arrays encountered at depth zero are expanded, but `[9,10,11]` is encountered at depth one and remains nested.

#### Example 3

- **Input:** `arr = [[1,2,3],[4,5,6],[7,8,[9,10,11],12],[13,14,15]]`, `n = 2`
- **Output:** `[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]`
- **Explanation:** Every nested array occurs above the limit of two, so the result is completely flat.
