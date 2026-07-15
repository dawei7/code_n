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

### Required Complexity

- **Time:** $O(P+Q)$
- **Space:** $O(P+Q)$

<details>
<summary>Approach</summary>

#### General

**Keep every query row.** Use `Queries` as the left side of a `LEFT JOIN` to `NPV`. Match on both `id` and `year`; matching only the identifier could attach a value from the wrong year or duplicate a request.

For a matched row, select the stored `npv`. For an unmatched row, the joined value is `NULL`, so replace it with zero using `COALESCE`. Ordering by the two key columns is not required by the source relation but makes local results deterministic.

The left join emits exactly one row for each unique query key. The composite join condition supplies its value if and only if that exact stored key exists, and `COALESCE` handles precisely the remaining unmatched case. Therefore every requested pair receives the required value without adding unrelated NPV rows.

#### Complexity detail

With a hash table or composite-key index for the stored rows, building or reading the lookup and probing all requests takes $O(P+Q)$ time. The join structures and returned rows require $O(P+Q)$ space under the stated bound.

#### Alternatives and edge cases

- **Correlated scalar subquery:** Look up `NPV` separately for every query row. It is concise but can degrade to $O(PQ)$ without a composite index.
- **Inner join:** This incorrectly discards requested pairs that lack a stored value.
- **Join on id only:** Different years for one identifier would match incorrectly.
- **Stored zero:** A real `npv = 0` and a missing row both display zero, as required.
- **Empty NPV table:** Every query still appears with zero.
- **Deterministic order:** Sorting is useful for fixtures even though relational result order is otherwise unspecified.

</details>
