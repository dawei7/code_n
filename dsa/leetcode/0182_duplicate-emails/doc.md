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

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

The output asks one question per email value: how many source rows contain it? `GROUP BY email` collects all equal addresses into one group, and `COUNT(*)` gives that group's exact multiplicity. Keep only groups with `COUNT(*) > 1` using `HAVING`, then alias the grouped value as `Email`.

`HAVING` is the correct stage because the duplicate condition depends on an aggregate result. `WHERE` filters individual input rows before groups and therefore cannot test the final group count.

Grouping also provides the requested output cardinality automatically. If an address appears two, three, or a thousand times, it forms one group and produces one result row rather than one row for every duplicate occurrence.

Each group contains all and only `Person` rows with one particular email. Its count is therefore greater than one exactly when that email is duplicated. The `HAVING` predicate retains every duplicated-email group and rejects every unique-email group. Since each retained group emits its key once, the result contains every duplicated address exactly once.

#### Complexity detail

A sort-based grouping plan takes $O(n \log n)$ time and up to $O(n)$ intermediate storage. A hash aggregate can run in expected $O(n)$ time with $O(u)$ storage for `u` distinct emails. The actual choice depends on indexes and the optimizer.

#### Alternatives and edge cases

- A self-join on equal email values may generate quadratically many row pairs for a frequent address and still needs `DISTINCT`.
- A window count can annotate every row, but requires a final deduplication step to meet the one-row-per-email result.
- `WHERE COUNT(*) > 1` is invalid SQL because aggregate filtering occurs after grouping.
- A one-row or all-unique table yields no rows; any multiplicity above one still yields one row.
- The contract states emails are non-null. With nullable emails, the desired treatment of the single SQL null group would need to be specified.

</details>
