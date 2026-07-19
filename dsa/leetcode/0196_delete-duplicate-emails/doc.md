# Delete Duplicate Emails

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 196 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/delete-duplicate-emails/) |

## Problem Description
### Goal
The `Person` table stores a unique `id` and an email address, and several rows may share the same email. Modify the table so that only one row remains for each distinct email value.

For every duplicated email, retain the original row with the smallest identifier and delete all rows for that email having larger identifiers. Emails that occur once remain untouched. Delete the duplicates in place rather than writing a query that merely displays deduplicated values; the post-operation table must contain the reduced rows with the retained identifiers and emails unchanged.

### Function Contract
**Inputs**

- `Person(id, email)`: people whose email values may repeat

**Return value**

Mutate `Person` so each distinct email remains once, represented by its minimum original id.

### Examples
**Example 1**

- Rows: `(1, a), (2, b), (3, a)`
- Remaining rows: `(1, a), (2, b)`

**Example 2**

- Every email is distinct
- Remaining rows: unchanged

**Example 3**

- Three rows share one email
- Remaining row: the one with the smallest id
