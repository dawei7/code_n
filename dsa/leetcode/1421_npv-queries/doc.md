# NPV Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1421 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open Problem](https://leetcode.com/problems/npv-queries/) |

## Problem Description

### Goal

The `NPV` table stores a net present value for some `(id, year)` pairs. The `Queries` table lists the pairs whose values must be reported. A requested pair may be absent from `NPV`.

Return every row from `Queries` with columns `id`, `year`, and its matching `npv`. When no matching stored row exists, report `0` instead. The query pairs themselves must never be dropped.

### Function Contract

**Inputs**

- `NPV(id, year, npv)`: stored values keyed by the pair `(id, year)`.
- `Queries(id, year)`: requested pairs, also unique by `(id, year)`.

Let $P$ be the number of rows in `NPV` and $Q$ the number of rows in `Queries`.

**Return value**

- Columns `id`, `year`, and `npv` for every requested pair, using zero for a missing stored value. This package orders rows by `id` and then `year` for deterministic output.

### Examples

**Example 1**

- Input: `Queries` contains `(1, 2019)`, and `NPV` contains `(1, 2019, 113)`.
- Output: `(1, 2019, 113)`.

**Example 2**

- Input: `Queries` contains `(7, 2018)`, with no matching `NPV` row.
- Output: `(7, 2018, 0)`.

**Example 3**

- Input: several query pairs share an `id` but use different years.
- Output: each year is matched independently by the complete two-column key.
