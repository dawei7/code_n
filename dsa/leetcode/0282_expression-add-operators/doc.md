# Expression Add Operators

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 282 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, String, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/expression-add-operators/) |

## Problem Description
### Goal
Given a string of decimal digits `num` and an integer `target`, insert any of the binary operators `+`, `-`, and `*` between selected adjacent digits. Digits that are not separated form one multi-digit operand, and their original order may not change.

Return every distinct valid expression whose standard arithmetic value equals `target`, in any order. Multiplication has its usual precedence over addition and subtraction. An operand may be exactly `0`, but no multi-digit operand may begin with zero. Operators cannot be placed before the first digit, after the last digit, or twice without an operand between them; use every input digit exactly once.

### Function Contract
**Inputs**

- `num`: a decimal digit string
- `target`: the desired integer value

**Return value**

All valid expressions reaching the target, in any order; operands may not contain leading zeros.

### Examples
**Example 1**

- Input: `num = "123", target = 6`
- Output: `["1+2+3","1*2*3"]`

**Example 2**

- Input: `num = "232", target = 8`
- Output: `["2+3*2","2*3+2"]`

**Example 3**

- Input: `num = "105", target = 5`
- Output: `["1*0+5","10-5"]`
