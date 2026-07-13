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

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Accept both permitted referee states**

A customer qualifies when the stored referee identifier is not 2. A null referee also qualifies because no customer referred that row, but SQL does not treat `NULL <> 2` as true. Express the filter as `referee_id <> 2 OR referee_id IS NULL`.

**Why the filter is complete**

Every row has either a concrete referee identifier or null. Concrete identifier 2 is the only forbidden state. Every other concrete identifier satisfies the inequality, and the explicit null branch retains customers with no referee, so exactly the requested rows remain.

**Order only for deterministic local output**

The platform permits any row order. Ordering by name and identifier makes local fixtures stable without changing which customers qualify.

#### Complexity detail

Filtering examines `n` customer rows in $O(n)$ time. The deterministic output sort costs $O(n \log n)$ time and $O(n)$ working space; without an ordering requirement, the semantic query itself is linear.

#### Alternatives and edge cases

- **`COALESCE(referee_id, 0) <> 2`:** is concise when valid referee identifiers are positive, but the explicit null branch states the contract more directly.
- **Correlated anti-existence test:** can identify rows not marked with referee 2, but may rescan the customer table for every row and take $O(n^2)$ time.
- **`referee_id <> 2` alone:** incorrectly drops null referees because the comparison evaluates to unknown.
- **Referee exactly 2:** must be excluded.
- **Different referee:** qualifies regardless of that referee's own row details.
- **No referee:** must be included.
- **Customer with identifier 2:** is not automatically excluded; qualification depends on that customer's `referee_id`.
- **Duplicate names:** each qualifying customer row remains a separate result row.

</details>
