# Order Two Columns Independently

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2159 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open](https://leetcode.com/problems/order-two-columns-independently/) |

## Problem Description

### Goal

The `Data` table contains two integer columns, `first_col` and `second_col`,
and may include duplicate rows. Reorder the values in the two columns
independently rather than preserving their original row pairings.

The result's `first_col` values must appear in ascending order, while its
`second_col` values must appear in descending order. Preserve every occurrence
from each input column, including duplicates, and pair values solely by their
positions in these two independently sorted sequences.

### Function Contract

**Inputs**

- `Data(first_col, second_col)`: the source table of integer pairs; duplicate
  rows may occur.

**Return value**

A result table with columns `first_col` and `second_col`, where the former is
ascending and the latter is descending.

### Examples

#### Example 1

Input table `Data`:

| first_col | second_col |
|---:|---:|
| 4 | 2 |
| 2 | 3 |
| 3 | 1 |
| 1 | 4 |

- **Output:** 

| first_col | second_col |
|---:|---:|
| 1 | 4 |
| 2 | 3 |
| 3 | 2 |
| 4 | 1 |
