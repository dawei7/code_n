# Gray Code

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 89 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Backtracking, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/gray-code/) |

## Problem Description
### Goal
For a positive bit width `n`, consider every integer representable by exactly `n` binary bits, from `0` through $2^{n} - 1$. Arrange all of them in one sequence beginning with zero.

Consecutive values must differ in exactly one bit, and the final value must also differ from the initial zero in exactly one bit, making the ordering cyclic. Return any sequence satisfying these properties, with every value appearing once; more than one Gray-code cycle may be valid.

### Function Contract
**Inputs**

- `n`: the positive bit width

**Return value**

A valid list of all $2^{n}$ integers; more than one ordering may be correct.

### Examples
**Example 1**

- Input: `n = 2`
- Output: `[0,1,3,2]`

**Example 2**

- Input: `n = 1`
- Output: `[0,1]`

**Example 3**

- Input: `n = 3`
- Output: one valid cycle such as `[0,1,3,2,6,7,5,4]`
