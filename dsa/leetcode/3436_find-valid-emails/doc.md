# Find Valid Emails

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3436 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-valid-emails/) |

## Problem Description

### Goal

The `Users` table stores one unique `user_id` and one email address per row. Select only addresses with exactly one `@` symbol and a final `.com` suffix.

The non-empty portion before `@` may contain only letters, digits, and underscores. The non-empty domain between `@` and `.com` may contain letters only. Return each qualifying user's id and email, ordered by `user_id` in ascending order.

### Function Contract

**Input table**

`Users`

| Column | Type | Meaning |
|---|---|---|
| `user_id` | int | Unique user identifier |
| `email` | varchar | Address to validate |

**Return value**

Return columns `user_id` and `email` for valid addresses, sorted by ascending `user_id`.

### Examples

**Example 1**

Input table `Users`:

| user_id | email |
|---:|---|
| 1 | `alice@example.com` |
| 2 | `bob_at_example.com` |
| 3 | `charlie@example.net` |
| 4 | `david@domain.com` |
| 5 | `eve@invalid` |

Output:

| user_id | email |
|---:|---|
| 1 | `alice@example.com` |
| 4 | `david@domain.com` |
