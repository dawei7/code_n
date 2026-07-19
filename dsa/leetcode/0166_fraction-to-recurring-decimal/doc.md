# Fraction to Recurring Decimal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 166 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/fraction-to-recurring-decimal/) |

## Problem Description
### Goal
Given an integer numerator and a nonzero integer denominator, represent their quotient exactly as a decimal string. Produce the ordinary integer part followed, when needed, by a decimal point and fractional digits; do not round or truncate a nonterminating result.

When fractional digits repeat forever, enclose the shortest repeating cycle in parentheses at its first occurrence, such as the repeating part of $1/6$. Add a leading minus sign exactly when the nonzero quotient is negative, never emit negative zero, and omit both the decimal point and parentheses for an exact integer. The output must work for finite decimals, recurring decimals, zero numerators, and extreme signed integer values.

### Function Contract
**Inputs**

- `numerator`: integer numerator
- `denominator`: nonzero integer denominator

**Return value**

The exact finite or recurring decimal string, with a leading minus sign exactly when the quotient is negative and nonzero.

### Examples
**Example 1**

- Input: `numerator = 1, denominator = 2`
- Output: `"0.5"`

**Example 2**

- Input: `numerator = 2, denominator = 3`
- Output: `"0.(6)"`

**Example 3**

- Input: `numerator = 4, denominator = 333`
- Output: `"0.(012)"`
