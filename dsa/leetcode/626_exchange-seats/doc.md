# Exchange Seats

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 626 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/exchange-seats/) |

## Problem Description
### Goal
Given a `Seat` table whose unique identifiers start at `1` and increase continuously, swap the seat `id` of every two consecutive students: exchange the students at `1` and `2`, at `3` and `4`, and so on.

If the number of students is odd, leave the student with the final `id` in the same seat because no partner remains. Return the resulting `id` and `student` rows ordered by `id` in ascending order; student names move between identifiers, while the identifier sequence itself remains complete.

### Function Contract
**Inputs**

- `Seat(id, student)`: consecutive seat identifiers starting at 1 and their students

**Return value**

- The same ordered `id` values with adjacent student names exchanged
- If the largest ID is odd, its student remains at that seat
- Rows are ordered by `id`

### Examples
**Example 1**

- Input rows: `(1, Abbot)`, `(2, Doris)`, `(3, Emerson)`, `(4, Green)`, `(5, Jeames)`
- Output rows: `(1, Doris)`, `(2, Abbot)`, `(3, Green)`, `(4, Emerson)`, `(5, Jeames)`

**Example 2**

- Input row: `(1, Solo)`
- Output row: `(1, Solo)`

### Required Complexity

- **Time:** $O(R \log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Order the neighboring names once**

Use window functions over `ORDER BY id`. `LEAD(student)` gives the next seat's name and `LAG(student)` gives the previous seat's name without changing the seat row itself.

**Choose the partner by parity**

For an odd `id`, use the next name; for an even `id`, use the previous name. Consecutive IDs guarantee that these are exactly the requested pairs.

**Preserve an unmatched final seat**

If the final row has an odd ID, `LEAD` returns null because there is no partner. `COALESCE` falls back to that row's original student. Every other odd row has a successor, and every even row has a predecessor.

**Why every pair is exchanged exactly once**

Within pair $(2k - 1, 2k)$, the odd row selects the even row's name and the even row selects the odd row's name. IDs stay fixed, so the two names exchange positions and cannot affect another pair. The only unpaired row is handled by the fallback.

#### Complexity detail

For `R` seats, ordering for the window takes $O(R \log R)$ time and $O(R)$ execution space in the general database model. Neighbor lookup and final projection are linear after ordering.

#### Alternatives and edge cases

- **Self-join by partner ID:** left-join each row to `id + 1` when odd or `id - 1` when even, then use the partner name when present; with indexing it is similarly efficient.
- **Rewrite output IDs:** map odd IDs to `id + 1` and even IDs to `id - 1`, preserving the final odd ID with a row-count check; it works but moves identifiers rather than directly expressing name exchange.
- **Correlated partner lookup:** search `Seat` separately for every row's partner; without an index this can take $O(R^2)$ time.
- A one-row table remains unchanged.
- An odd number of rows leaves only the largest-ID student unmoved.
- Duplicate student names are still exchanged as rows even if the output text looks unchanged.
- Output must be sorted by the original seat IDs.

</details>
