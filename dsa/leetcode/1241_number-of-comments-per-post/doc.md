# Number of Comments per Post

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1241 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-comments-per-post/) |

## Problem Description

### Goal

The `Submissions` table stores both posts and comments. A row whose `parent_id` is `NULL` represents a post identified by `sub_id`; a row with a non-null `parent_id` represents a comment on the post whose identifier equals that parent value. Duplicate rows may occur.

For every distinct post, report how many distinct comment identifiers refer directly to it. A post with no comments must still appear with a count of zero. Ignore comments whose parent does not identify a listed post, and return the result ordered by `post_id` in ascending order.

### Function Contract

**Input tables**

- `Submissions(sub_id, parent_id)`: `parent_id IS NULL` marks a post; otherwise the row is a comment referring to `parent_id`.
- Let $r$ be the number of rows in `Submissions`.

**Return value**

- One row per distinct post with columns `post_id` and `number_of_comments`, ordered by `post_id ASC`.

### Examples

**Example 1**

`Submissions`

| sub_id | parent_id |
|---:|---:|
| 1 | NULL |
| 2 | NULL |
| 1 | NULL |
| 12 | NULL |
| 3 | 1 |
| 5 | 2 |
| 3 | 1 |
| 4 | 1 |
| 9 | 1 |
| 10 | 2 |
| 6 | 7 |

Output:

| post_id | number_of_comments |
|---:|---:|
| 1 | 3 |
| 2 | 2 |
| 12 | 0 |

**Example 2**

A distinct post with no matching comment rows is returned with `number_of_comments = 0`.

**Example 3**

Repeated rows for the same comment identifier count only once for that post.
