# Find Candidates for Data Scientist Position II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3278 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Find Candidates for Data Scientist Position II](https://leetcode.com/problems/find-candidates-for-data-scientist-position-ii/) |

## Problem Description

### Goal

The `Candidates` table records each candidate's proficiency from `1` through `5` in individual skills. Its `(candidate_id, skill)` pairs are unique. The `Projects` table similarly lists every skill required by a project and its importance from `1` through `5`; `(project_id, skill)` is its primary key.

A candidate is suitable for a project only when the candidate possesses every required skill. Score each suitable pair from a base of `100`: add `10` for every required skill whose proficiency exceeds its importance, subtract `5` when proficiency is lower, and make no change when they are equal.

For each project that has at least one suitable candidate, return only the candidate with the greatest score. Break a score tie in favor of the smaller `candidate_id`. Omit projects with no suitable candidate, and order the final rows by `project_id` ascending.

### Function Contract

**Inputs**

- `Candidates(candidate_id, skill, proficiency)`: Unique candidate-skill rows with proficiency levels from `1` through `5`.
- `Projects(project_id, skill, importance)`: Unique project-skill rows with importance levels from `1` through `5`.

Let $C$ and $P$ be the numbers of candidate-skill and project-skill rows, and let $J$ be the number of rows produced by joining them on `skill`.

**Return value**

Return columns `project_id`, `candidate_id`, and `score`, with at most one row per project and rows ordered by `project_id` ascending.

### Examples

#### Example 1

- **Input:** Project `501` requires Python, Tableau, and PostgreSQL; candidates `101`, `102`, and `103` have the proficiencies shown in the source example.
- **Output:** `[[501, 101, 105]]`
- **Explanation:** All three suitable candidates tie at `105`, so candidate `101` wins by ID.

#### Example 2

- **Input:** One project requires Python and SQL; candidate `1` has both skills while candidate `2` has only Python.
- **Output:** The project is assigned to candidate `1`; candidate `2` is excluded before ranking.

#### Example 3

- **Input:** A project has required skills that no single candidate fully covers.
- **Output:** No row is returned for that project.
