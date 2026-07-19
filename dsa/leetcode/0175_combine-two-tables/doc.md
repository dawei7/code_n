# Combine Two Tables

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 175 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/combine-two-tables/) |

## Problem Description
### Goal
The `Person` table stores each person's identifier, last name, and first name. The `Address` table stores optional address records with a person identifier, city, and state. A person can exist even when no corresponding address row is available.

Write a query that returns every person in any order, with columns `firstName`, `lastName`, `city`, and `state`. Fill the location columns from the matching address when one exists, while preserving people without a match and returning `NULL` for their city and state. Address-only rows with no matching person do not create output people.

### Function Contract
**Inputs**

- `Person(personId, lastName, firstName)`: one row per person
- `Address(addressId, personId, city, state)`: optional address rows linked by person id

**Return value**

A result grid with columns `firstName`, `lastName`, `city`, and `state`; unmatched address columns are null.

### Examples
**Example 1**

Person `Allen Wang` has a matching Seattle address and `Bob Alice` has none.

- Output rows: `[Allen, Wang, Seattle, Washington]`, `[Bob, Alice, null, null]`

**Example 2**

An empty Address table still returns every Person row with null location columns.

**Example 3**

Address rows whose person id is absent from Person do not create output rows.
