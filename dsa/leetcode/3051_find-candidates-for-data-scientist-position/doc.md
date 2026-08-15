# Find Candidates for Data Scientist Position

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3051 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-candidates-for-data-scientist-position/) |

## Problem Description

### Goal

The `Candidates` table records one skill for a candidate in each row. A Data
Scientist opening has three mandatory proficiencies: `Python`, `Tableau`, and
`PostgreSQL`. A candidate is suitable only when their recorded skills include
all three exact names; knowing one or two of them is insufficient.

Find every suitable candidate and return only their `candidate_id`. Other
skills neither help nor disqualify a candidate, so a person may have the three
required skills plus any number of additional proficiencies. Order the result
by `candidate_id` in ascending order.

### Function Contract

**Inputs**

- `Candidates(candidate_id, skill)`: Each row associates a candidate with one
  skill; the pair `(candidate_id, skill)` is the table's primary key.

Let $n$ be the number of input rows and $c$ the number of qualifying candidates.

**Return value**

- An ordered one-column table named `candidate_id` containing every candidate
  who has `Python`, `Tableau`, and `PostgreSQL`, sorted in ascending ID order.

### Examples

#### Example 1

Candidates 123 and 147 each have all three required skills, so the result is:

| candidate_id |
|---:|
| 123 |
| 147 |

#### Example 2

A candidate with `Python`, `Tableau`, and `Java` is omitted because
`PostgreSQL` is missing.

#### Example 3

A candidate who has the three required skills plus `R` still qualifies;
unrelated additional skills do not change the result.
