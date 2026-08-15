# Symmetric Coordinates

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2978 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/symmetric-coordinates/) |

## Problem Description

### Goal

The `Coordinates` table stores integer ordered pairs `(X, Y)` and may contain
duplicate rows. Two physical rows form a symmetric pair when one stores
`(X1, Y1)` and the other stores `(Y1, X1)`.

Return each unique symmetric coordinate once, using only the orientation that
satisfies `X <= Y`. A diagonal coordinate `(X, X)` is symmetric only when that
row occurs at least twice, because the pair must use two rows.

Order the result first by `X` and then by `Y`, both ascending.

### Function Contract

**Inputs**

- `Coordinates(X, Y)`: integer coordinate rows; duplicate pairs are allowed

Let $R$ be the number of physical rows and $D$ the number of distinct ordered
coordinate pairs.

**Return value**

An ordered table with columns `x` and `y`, containing every unique symmetric
pair in its `x <= y` orientation.

### Examples

#### Example 1

For rows `(20,20)`, `(20,20)`, `(20,21)`, `(23,22)`, `(22,23)`, and
`(21,20)`, the ordered result is:

| x | y |
|---:|---:|
| 20 | 20 |
| 20 | 21 |
| 22 | 23 |

The diagonal appears because it has two occurrences; each off-diagonal pair
appears once in the orientation with the smaller first coordinate.
