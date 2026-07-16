# Friendly Movies Streamed Last Month

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1495 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/friendly-movies-streamed-last-month/) |

## Problem Description
### Goal

The `TVProgram` table records when a content item was streamed and on which channel. The `Content` table stores that item's title, whether it is intended for children, and its content category.

Report the distinct titles whose content is marked kid-friendly, whose category is exactly `Movies`, and which appeared in at least one television program during June 2020. A qualifying title must satisfy all three conditions through a matching `content_id`. Return the result rows in any order.

### Function Contract
**Inputs**

Let $P$ be the number of rows in `TVProgram`, $C$ the number of rows in `Content`, and $T$ the number of distinct qualifying titles.

**`TVProgram`**

| Column | Type | Meaning |
|---|---|---|
| `program_date` | date/datetime | Date and optional time when the program was streamed. |
| `content_id` | int | Identifier of the streamed content item. |
| `channel` | varchar | Channel carrying the program. |

- The composite key is (`program_date`, `content_id`).

**`Content`**

| Column | Type | Meaning |
|---|---|---|
| `content_id` | varchar | Primary identifier joined to `TVProgram.content_id`. |
| `title` | varchar | Display title of the content. |
| `Kids_content` | enum | `Y` for kid-friendly content and `N` otherwise. |
| `content_type` | varchar | Category such as `Movies` or `Series`. |

**Return value**

Return one column named `title`, containing each distinct title of a `Kids_content = 'Y'`, `content_type = 'Movies'` item with at least one matching stream timestamp from June 1, 2020 inclusive through July 1, 2020 exclusive. Output order is unrestricted.

### Examples
**Example 1**

Input `TVProgram`:

| program_date | content_id | channel |
|---|---:|---|
| 2020-06-10 08:00 | 1 | LC-Channel |
| 2020-05-11 12:00 | 2 | LC-Channel |
| 2020-05-12 12:00 | 3 | LC-Channel |
| 2020-05-13 14:00 | 4 | Disney Ch |
| 2020-06-18 14:00 | 4 | Disney Ch |
| 2020-07-15 16:00 | 5 | Disney Ch |

Input `Content`:

| content_id | title | Kids_content | content_type |
|---:|---|---|---|
| 1 | Leetcode Movie | N | Movies |
| 2 | Alg. for Kids | Y | Series |
| 3 | Database Sols | N | Series |
| 4 | Aladdin | Y | Movies |
| 5 | Cinderella | Y | Movies |

Output:

| title |
|---|
| Aladdin |

Only `Aladdin` satisfies the audience and type filters and has a June 2020 stream.

**Example 2**

- A kid-friendly movie streamed at `2020-06-01 00:00:00` qualifies.
- A kid-friendly movie streamed at `2020-07-01 00:00:00` does not qualify because July is outside the requested month.

**Example 3**

- If two different content IDs share the same title and both qualify, return that title only once.

### Required Complexity

- **Time:** $O(P + C + T \log T)$
- **Space:** $O(C + T)$

<details>
<summary>Approach</summary>

#### General

**Join stream events to content metadata**

Start from `TVProgram` and inner-join `Content` on `content_id`. A schedule row alone does not reveal whether an item is for children or whether it is a movie; a content row alone does not prove the item was streamed in the requested month. The inner join retains exactly the rows for which both kinds of evidence refer to the same content item.

Although the published schemas describe the two `content_id` columns with different integer/varchar types, their values are the relationship key. MySQL and the app-local SQLite fixtures compare the compatible identifier values correctly; no title-based join is valid because titles need not be unique.

**Express June as a half-open timestamp interval**

Filter `program_date >= '2020-06-01'` and `program_date < '2020-07-01'`. The lower bound includes the first instant of June, and the exclusive upper bound includes every time on June 30 without requiring a guessed end-of-day value.

This range form is preferable to `MONTH(program_date) = 6 AND YEAR(program_date) = 2020` or a formatting expression. It states the year and month together, handles timestamps as well as dates, and allows a database index on `program_date` to remain usable.

**Apply both content predicates independently**

Require `Kids_content = 'Y'` and `content_type = 'Movies'`. Kid-friendly series do not qualify, and non-kid movies do not qualify. Neither condition implies the other.

Predicate order in the written `WHERE` clause does not change relational semantics; the query optimizer may push selective content or date filters before the join.

**Deduplicate the projected title**

A movie can appear in multiple June program rows, and separate content records may even share one title. The requested output is a set of titles, so select `DISTINCT c.title` after all filters. This removes duplicate qualifying join rows without merging content records before their eligibility is known.

The source permits any result order. The local and native artifacts add `ORDER BY c.title` only to make practice output deterministic; this does not alter membership.

**Why every returned title and every omitted title is correct**

Every returned row originates from a joined pair with the same `content_id`. Its content row proves both kid eligibility and movie type, while its program row proves a stream timestamp inside the exact June interval. Thus every returned title qualifies.

Conversely, any qualifying movie has a content row satisfying both metadata predicates and at least one June program row with the same identifier. Those rows survive the join and filters, so its title is projected. `DISTINCT` preserves one occurrence even if several qualifying rows generate it. Therefore no qualifying title is omitted and no ineligible title is included.

#### Complexity detail

Under a hash-join execution, scanning $P$ program rows and building or probing metadata for $C$ content rows costs $O(P+C)$ expected time. Deduplicating and ordering the $T$ qualifying titles contributes up to $O(T \log T)$ time. Hash and result-order structures use $O(C+T)$ space. A database may choose equivalent indexed nested-loop, merge, hash, or sort plans based on statistics and indexes.

The benchmark scales the number of content rows and supplies one non-June plus one late-position June event per item. The join processes both relations together, while a correct correlated `EXISTS` formulation without a supporting fixture index repeatedly scans `TVProgram` for each content row and is rejected by scaling.

#### Alternatives and edge cases

- **Correlated `EXISTS`:** filter `Content` and test for a matching June stream in a subquery. It is semantically clean, but without an index on `(content_id, program_date)` it can rescan `TVProgram` for every content row.
- **Month and year functions:** `MONTH(program_date) = 6 AND YEAR(program_date) = 2020` is correct in MySQL, but applies functions to the column and is not portable to SQLite.
- **Formatted month string:** `DATE_FORMAT(program_date, '%Y-%m') = '2020-06'` is concise MySQL but similarly non-sargable and unavailable in SQLite.
- **Join on title:** incorrect because `TVProgram` carries `content_id`, not title, and distinct content may share a title.
- **Omit `DISTINCT`:** returns duplicate rows when one movie streamed more than once or multiple qualifying IDs share a title.
- **June 1 boundary:** include midnight and every later time that day.
- **July 1 boundary:** exclude midnight because the upper bound is strict.
- **June 30 with time:** include all times because they remain below July 1.
- **Other years:** June 2019 and June 2021 do not qualify.
- **Kid-friendly series:** exclude because type must be exactly `Movies`.
- **Adult movies:** exclude because `Kids_content` must be `Y`.
- **Multiple channels:** channel does not affect qualification.
- **No qualifying rows:** return the `title` column with an empty row set.
- **Repeated title:** output title distinctness is based on the projected string, not only on `content_id`.
- **Output ordering:** not required by the source; deterministic ordering is an allowed presentation choice.

</details>
