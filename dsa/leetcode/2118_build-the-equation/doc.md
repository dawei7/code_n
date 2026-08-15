# Build the Equation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2118 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/build-the-equation/) |

## Problem Description

### Goal

The `Terms` table stores the nonzero terms of a one-variable polynomial. Each
row gives a unique integer `power` from $0$ through $100$ and a nonzero integer
`factor`.

Build one equation string whose left-hand side contains every table row in
descending power order and whose right-hand side is zero. Every term begins
with `+` or `-`, followed by the factor's absolute value. A power greater than
one appends `X^power`; power one appends only `X`; and power zero appends no
variable text. Finish the complete left-hand side with `=0`.

### Function Contract

**Inputs**

- `Terms(power, factor)`: `power` is unique, and `factor` is nonzero.

Let $N$ be the number of rows in `Terms`.

**Return value**

Return one row with one column named `equation`, containing all formatted terms
in descending `power` order followed by `=0`.

### Examples

#### Example 1

- **Input:** `Terms = [{power: 2, factor: 1}, {power: 1, factor: -4}, {power: 0, factor: 2}]`
- **Output:** `[{equation: "+1X^2-4X+2=0"}]`

#### Example 2

- **Input:** `Terms = [{power: 4, factor: -4}, {power: 2, factor: 1}, {power: 1, factor: -1}]`
- **Output:** `[{equation: "-4X^4+1X^2-1X=0"}]`

The absent powers do not create placeholder terms.
