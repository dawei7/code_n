# Find the Missing IDs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1613 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-missing-ids/) |

## Problem Description
### Goal
Table `Customers` contains existing customer identifiers and their names, but the positive identifier sequence may have gaps. Let $m$ be the greatest `customer_id` currently present.

Find every integer ID from 1 through $m$ that does not occur in `Customers`. Return those absent IDs in ascending order. Values above the current maximum are outside the requested range and must not be generated.

### Function Contract
**Inputs**

- `Customers(customer_id, customer_name)`, with one row per existing customer and a unique positive `customer_id`.
- Let $c$ be the number of customer rows and $m=\max(\texttt{customer_id})$.

**Return value**

Return a relation with one column named `ids`, containing every missing integer in the inclusive range from 1 through $m$, sorted ascending.

### Examples
**Example 1**

- Input: customer IDs `[1, 4, 5]`
- Output: IDs `[2, 3]`

**Example 2**

- Input: customer IDs `[1, 2, 3]`
- Output: no rows, because the range is consecutive.

**Example 3**

- Input: the only customer ID is `5`
- Output: IDs `[1, 2, 3, 4]`

### Required Complexity
- **Time:** $O((m+c)\log(c+1))$
- **Space:** $O(m+c)$

<details>
<summary>Approach</summary>

#### General

**Generate the complete bounded ID domain.** A recursive common table expression starts with 1 and repeatedly adds 1 while the current value is below `MAX(customer_id)`. This produces exactly the candidates from 1 through $m`: no lower positive ID is omitted, and the stopping condition prevents values above the existing maximum.

**Apply an anti-join against existing customers.** Left join each generated candidate to `Customers` by ID and keep rows whose customer side is `NULL`. A retained candidate has no matching customer row, while every omitted candidate has a witness in the table. Sorting `candidate_ids.ids` then supplies the required ascending output.

The generated relation covers the entire requested domain once, and the anti-join partitions it into present and missing IDs. Selecting the missing partition is therefore both complete and free of IDs outside the contract.

#### Complexity detail

Generating $m$ candidates takes $O(m)$ work. Under a portable indexed or comparison-based join model, matching them against $c$ customer rows and ordering the output fits within $O((m+c)\log(c+1))$ time. The recursive relation, join state, and result may occupy $O(m+c)$ space. Database-specific indexing or hashing can reduce the matching portion toward linear expected time.

#### Alternatives and edge cases

- **Numbers table:** Joining a permanent integer table against `Customers` is efficient and avoids recursion, but such a helper table is not part of the supplied schema.
- **Correlated count per candidate:** Testing each generated ID with a fresh scan of `Customers` is correct but can take $O(mc)$ time.
- **Detect only gaps between adjacent IDs:** Window functions can locate gap boundaries, but expanding every multi-ID gap still requires a number generator or recursion.
- If ID 1 is absent, the output begins with 1.
- Consecutive customer IDs produce an empty result.
- A gap can contain several consecutive missing values, all of which must be returned.
- The upper bound is the current maximum ID; no larger positive integers belong in the result.
- Results are ordered numerically by `ids`, not by customer name.

</details>
