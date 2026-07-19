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
