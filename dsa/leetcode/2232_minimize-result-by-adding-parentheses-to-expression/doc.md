# Minimize Result by Adding Parentheses to Expression

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2232 |
| Difficulty | Medium |
| Topics | String, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/) |

## Problem Description

### Goal

The string `expression` has the form `"<num1>+<num2>"`, where both operands are positive integers written with digits from `1` through `9`. Insert exactly one opening parenthesis somewhere before the plus sign and one closing parenthesis somewhere after it.

The resulting text must be a valid mathematical expression. Digits outside the parentheses act as multiplicative factors: for example, `"2(47+38)"` means $2(47+38)$, while `"1(2+3)4"` means $1(2+3)4$. Return a valid placement whose evaluated value is as small as possible. If several placements attain the same minimum, any one is acceptable.

### Function Contract

**Inputs**

- `expression`: A length-three-to-ten string containing exactly one plus sign, with a nonempty positive integer on each side.

Every permitted placement and its value fit in a signed 32-bit integer.

**Return value**

Return `expression` with one legal pair of parentheses added so that its mathematical value is minimal.

### Examples

**Example 1**

- Input: `expression = "247+38"`
- Output: `"2(47+38)"`

**Example 2**

- Input: `expression = "12+34"`
- Output: `"1(2+3)4"`

**Example 3**

- Input: `expression = "999+999"`
- Output: `"(999+999)"`
