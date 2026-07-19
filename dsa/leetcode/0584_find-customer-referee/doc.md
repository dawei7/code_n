# Find Customer Referee

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 584 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/find-customer-referee/) |

## Problem Description
### Goal
Given a `Customer` table containing each customer's identifier, name, and optional `referee_id`, find the customers who were not referred by the customer whose `id` is `2`. This includes customers referred by any other customer as well as customers who were not referred by anyone.

Return only the qualifying customers' names, in any order. A null `referee_id` represents the absence of a referrer and must be included explicitly; it must not be lost through a comparison that treats SQL `NULL` as unequal in the ordinary Boolean sense.

### Function Contract
**Inputs**

- `Customer(id, name, referee_id)`: customers and their optional referrer identifiers

**Return value**

- A one-column result grid named `name`
- Include rows where `referee_id` differs from 2 or is `NULL`

### Examples
**Example 1**

- Input: Alice has `referee_id = 1`
- Output: `Alice`

**Example 2**

- Input: Bob has `referee_id = 2`
- Output: no row for Bob

**Example 3**

- Input: Cara has `referee_id = NULL`
- Output: `Cara`
