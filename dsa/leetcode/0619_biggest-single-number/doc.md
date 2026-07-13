# Biggest Single Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 619 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/biggest-single-number/) |

## Problem Description
### Goal
Given a `MyNumbers` table that may contain duplicate integer values, define a single number as a number that appears exactly once in the entire table. Identify all values meeting that frequency condition.

Return the largest single number in a one-column, one-row result named `num`. If no value appears exactly once, still return one row whose value is `NULL`; do not return an empty result. A numerically large value that appears more than once is not a single number and cannot qualify.

### Function Contract
**Inputs**

- `MyNumbers(num)`: a multiset of integer values

**Return value**

- One column named `num`
- Its value is the maximum integer whose total frequency is one
- If no such integer exists, the query still returns one row containing null

### Examples
**Example 1**

- Input values: `8, 8, 3, 3, 1, 4, 5, 6`
- Output: `6`

**Example 2**

- Input values: `8, 8, 7, 7, 3, 3, 3`
- Output: `null`

### Required Complexity

- **Time:** $O(R \log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Reduce the multiset to single values**

Group rows by `num` and retain only groups whose `COUNT(*)` equals one. Each surviving group represents exactly one value that occurs once in the complete table.

**Select the greatest survivor**

Apply an outer `MAX(num)` to the filtered groups. Since every eligible value appears once in that derived relation, the maximum is precisely the greatest single number.

**Preserve the empty-result contract**

An aggregate without `GROUP BY` always emits one row. Therefore, when the filtered relation is empty, `MAX` yields null rather than omitting the result row. This distinguishes the required answer from simply sorting the filtered groups and taking a row.

#### Complexity detail

For `R` rows, grouping distinct values takes $O(R \log R)$ time in the comparison-based database model and $O(R)$ execution space in the worst case where every value is distinct. The outer maximum scans at most `R` groups and does not increase those bounds.

#### Alternatives and edge cases

- **Window frequency:** attach `COUNT(*) OVER (PARTITION BY num)` to each row, filter frequency one, and take `MAX`; it has the same asymptotic bound and retains row-level data longer.
- **Correlated frequency count:** count matching rows separately for every input row; it is correct but can take $O(R^2)$ time.
- **Order and limit:** sorting single groups descending with `LIMIT 1` returns no row when no single exists unless another outer aggregate or null-producing wrapper is added.
- Negative values are compared normally; the greatest may still be negative.
- Zero is a valid single number.
- A value appearing two or more times is excluded regardless of how large it is.
- When exactly one row exists, its value is the answer.

</details>
