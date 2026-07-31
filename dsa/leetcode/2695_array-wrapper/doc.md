# Array Wrapper

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2695 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Open problem](https://leetcode.com/problems/array-wrapper/) |

## Problem Description

### Goal

Create an `ArrayWrapper` class whose constructor receives an array of integers. Instances must customize JavaScript's primitive conversion in two distinct contexts.

When two wrappers are operands of the `+` operator, JavaScript must obtain a numeric value from each wrapper. Their sum must equal the total of every integer stored in both wrapped arrays. Empty arrays contribute zero.

When `String()` converts one wrapper, it must produce the array's comma-separated representation enclosed in square brackets. The representation contains no spaces: for example, an array containing `1`, `2`, and `3` becomes `"[1,2,3]"`.

### Function Contract

**Inputs**

- `nums`: The integer array passed to one `ArrayWrapper` constructor. Its length is from $0$ through $1000$, and each value is from $0$ through $1000$.

The judge either creates two wrappers and adds them or creates one wrapper and converts it with `String()`.

**Return value**

`valueOf()` returns the sum of the wrapped integers so arithmetic coercion works. `toString()` returns the bracketed, comma-separated array representation.

### Examples

**Example 1**

- Input: `nums = [[1,2],[3,4]]`, `operation = "Add"`
- Output: `10`

**Example 2**

- Input: `nums = [[23,98,42,70]]`, `operation = "String"`
- Output: `"[23,98,42,70]"`

**Example 3**

- Input: `nums = [[],[]]`, `operation = "Add"`
- Output: `0`
