# Duplicate Emails

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 182 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/duplicate-emails/) |

## Problem Description
### Goal
The `Person` table contains an identifier and a non-null email address for each row. Several people may have the same email, and the rows carrying duplicate values need not be adjacent or have consecutive identifiers.

Return one column named `Email` containing every address that appears in more than one row, in any order. Each duplicated address must occur only once in the result, regardless of whether its source frequency is two or much larger. Addresses seen exactly once do not qualify, and comparison uses the stored email value rather than person identifiers.

### Function Contract
**Inputs**

- `Person(id, email)`: person rows with non-null email strings

**Return value**

One column named `Email` containing each duplicated email once.

### Examples
**Example 1**

- Emails: `a@b.com, c@d.com, a@b.com`
- Output: `a@b.com`

**Example 2**

- All emails unique
- Output: no rows

**Example 3**

- One email appears three times
- Output: one row for that email
