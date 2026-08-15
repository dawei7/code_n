# Calculator with Method Chaining

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2726 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Open problem](https://leetcode.com/problems/calculator-with-method-chaining/) |

## Problem Description

### Goal

Design a `Calculator` class whose constructor stores an initial numeric result. Instances support addition, subtraction, multiplication, division, and exponentiation. Every arithmetic method updates the stored result and returns the same calculator instance so that operations can be chained in their written order.

The `getResult` method returns the current numeric result. Division by zero is the exceptional case: `divide(0)` must throw an error whose message is exactly `"Division by zero is not allowed"`. Numerical answers within $10^{-5}$ of the exact result are accepted.

### Function Contract

Let $q$ be the number of actions in the evaluated operation sequence.

**Inputs**

- `value`: The constructor's initial numeric result.
- `add(value)`: Add `value` to the stored result and return this calculator.
- `subtract(value)`: Subtract `value` and return this calculator.
- `multiply(value)`: Multiply by `value` and return this calculator.
- `divide(value)`: Divide by nonzero `value` and return this calculator; throw the required error for zero.
- `power(value)`: Raise the current result to `value` and return this calculator.

An evaluated sequence contains between $2$ and $2\cdot10^4$ actions, begins with `Calculator`, and ends with `getResult`.

**Return value**

`getResult()` returns the current number after all preceding chained operations.

### Examples

#### Example 1

- **Input:** `new Calculator(10).add(5).subtract(7).getResult()`
- **Output:** `8`
- **Explanation:** Operations apply from left to right, giving $10+5-7$.

#### Example 2

- **Input:** `new Calculator(2).multiply(5).power(2).getResult()`
- **Output:** `100`
- **Explanation:** Multiplication occurs before the later exponentiation: $(2\cdot5)^2=100$.

#### Example 3

- **Input:** `new Calculator(20).divide(0).getResult()`
- **Output:** `"Division by zero is not allowed"`
- **Explanation:** Division by zero throws before a result can be returned.
