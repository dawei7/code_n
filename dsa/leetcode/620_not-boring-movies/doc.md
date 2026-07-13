# Not Boring Movies

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 620 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/not-boring-movies/) |

## Problem Description
### Goal
Given a `Cinema` table containing movie identifiers, names, descriptions, and ratings, find the movies with an odd-numbered `id` and a `description` that is not exactly `boring`. Both conditions must hold for a row to qualify.

Return every original column for the qualifying movies, ordered by `rating` in descending order so the highest-rated result appears first. An even identifier is excluded regardless of rating, and a row whose description is exactly `boring` is excluded even when its identifier is odd.

### Function Contract
**Inputs**

- `Cinema(id, movie, description, rating)`: movie records with unique integer identifiers

**Return value**

- Every original column for rows with an odd `id` and `description <> 'boring'`
- Rows are ordered by descending `rating`

### Examples
**Example 1**

- Input: movie 5 is interesting with rating `9.1`; movie 1 is great with rating `8.9`; movie 3 is `boring`
- Output order: movie 5, then movie 1

**Example 2**

- Input: all odd-ID movies have description `boring`
- Output: no rows

### Required Complexity

- **Time:** $O(R \log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Apply both eligibility predicates**

Use the remainder of `id` divided by two to retain odd identifiers, and require `description <> 'boring'`. The predicates are conjunctive: satisfying only one is insufficient.

**Sort only the qualifying rows**

Order the filtered result by `rating DESC`. Adding `id ASC` as a secondary key makes local output deterministic when ratings tie without violating the required rating order.

**Why the result is exact**

Every returned row passes both public conditions because both appear in the `WHERE` clause. Every input row that passes them survives the filter, and `ORDER BY` changes only its position, not membership. The descending key places any higher-rated qualifying movie before a lower-rated one.

#### Complexity detail

For `R` cinema rows, filtering is $O(R)$ and sorting up to `R` qualifying rows is $O(R \log R)$ time. The sort may use $O(R)$ execution space; the returned rows themselves are also linear in the worst case.

#### Alternatives and edge cases

- **`MOD(id, 2) = 1`:** expresses the same odd-ID test and is portable to engines that do not use `%` as a remainder operator.
- **Bitwise oddness:** testing the low bit can identify odd positive IDs, but modulo is clearer SQL for this contract.
- **Correlated rank calculation:** count higher-rated eligible rows separately for every movie and sort by that rank; it is correct but can take $O(R^2)$ time.
- Even-ID movies are excluded regardless of rating or description.
- An odd-ID movie described exactly as lowercase `boring` is excluded.
- Rating ties may appear in either order under the platform contract; the local query uses ascending ID for stability.
- If no row qualifies, return an empty relation with the same columns.

</details>
