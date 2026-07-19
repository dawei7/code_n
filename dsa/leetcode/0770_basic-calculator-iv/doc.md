# Basic Calculator IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 770 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, Math, String, Stack, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/basic-calculator-iv/) |

## Problem Description

### Goal

Given a valid arithmetic `expression` containing non-negative integers, lowercase variables, parentheses, `+`, `-`, and `*`, substitute each variable in `evalvars` with its corresponding integer from `evalints`. Leave every unlisted variable symbolic and evaluate the expression into a simplified polynomial.

Combine terms with identical sorted variable factors and omit terms whose coefficient becomes zero. Return each remaining term as its coefficient followed by `*variable` factors, ordered first by descending total degree and then lexicographically among equal-degree factor lists. Return an empty list for the zero polynomial.

### Function Contract

**Inputs**

- `expression`: a valid infix expression using integers, variables, spaces, `+`, `-`, `*`, and parentheses.
- `evalvars`: variable names to substitute.
- `evalints`: corresponding integer values, where `evalvars[i]` maps to `evalints[i]`.

**Return value**

- Simplified term strings sorted by descending total degree and then lexicographically by their sorted variable factors. Each string begins with its coefficient, followed by `*variable` factors; return an empty list for the zero polynomial.

### Examples

**Example 1**

- Input: `expression = "e + 8 - a + 5"`, `evalvars = ["e"]`, `evalints = [1]`
- Output: `["-1*a","14"]`
- Explanation: Substituting $e = 1$ leaves $-a + 14$.

**Example 2**

- Input: `expression = "e - 8 + temperature - pressure"`, `evalvars = ["e","temperature"]`, `evalints = [1,12]`
- Output: `["-1*pressure","5"]`
- Explanation: The substituted constants combine while `pressure` remains symbolic.

**Example 3**

- Input: `expression = "(e + 8) * (e - 8)"`, `evalvars = []`, `evalints = []`
- Output: `["1*e*e","-64"]`
- Explanation: Expansion combines the opposite linear terms and cancels them.
