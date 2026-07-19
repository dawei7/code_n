# Solve the Equation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 640 |
| Difficulty | Medium |
| Topics | Math, String, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/solve-the-equation/) |

## Problem Description
### Goal
Given a valid linear equation containing the variable `x`, integer constants, `+`, `-`, and exactly one `=`, solve for `x`. Terms may appear on both sides, and an omitted coefficient before `x` represents `1` or `-1` according to its sign.

If there is exactly one solution, return it as the string `"x=value"`; the input guarantees that this value is an integer. Return `"No solution"` when the variable terms cancel but unequal constants remain, and `"Infinite solutions"` when both sides reduce to the same expression.

### Function Contract
**Inputs**

- `equation`: two linear integer expressions separated by `=`, containing `x`, nonnegative integer literals, `+`, and `-`, without spaces

**Return value**

- `"x=value"` for the unique integer solution
- `"Infinite solutions"` when both sides reduce to the same expression
- `"No solution"` when the variable terms cancel but the constants differ

### Examples
**Example 1**

- Input: `equation = "x+5-3+x=6+x-2"`
- Output: `"x=2"`

**Example 2**

- Input: `equation = "x=x"`
- Output: `"Infinite solutions"`

**Example 3**

- Input: `equation = "2x=x"`
- Output: `"x=0"`
