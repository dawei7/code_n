## General

First compute each voter's number of non-null selections with

`COUNT(candidate) OVER (PARTITION BY voter)`.

The window count is repeated on every row belonging to that voter. Because `COUNT(expression)` ignores `NULL`, an abstention receives a count of zero and cannot accidentally create a candidate contribution.

Discard the null-candidate rows, then give every remaining row the contribution `1.0 / choices`. Group by `candidate` and sum these contributions to obtain each candidate's total. Rank those totals in descending order with `DENSE_RANK`, retain rank one, and finally sort the surviving names ascending.

**Why allocation and ranking produce exactly the winners**

If voter $v$ selected $d_v$ candidates, the query contributes $1/d_v$ to each of those candidates. Their contributions sum to $d_v(1/d_v)=1$, exactly the single vote owned by $v$. An abstaining voter contributes no grouped row. Summing by candidate therefore reconstructs every candidate's election total.

A candidate receives dense rank one exactly when no other total is larger. Equal maximum totals share rank one, so every tied winner survives and no lower-scoring candidate does. The last ordering step affects presentation only.

## Complexity detail

Let $R$ be the number of rows in `Votes`. Partitioning rows by voter, grouping by candidate, and ranking candidate totals require $O(R\log R)$ time in the general comparison-based execution model. Database indexes or hash aggregation can reduce parts of the physical work, but do not worsen that bound. The window, aggregate, and ranking intermediates use $O(R)$ working space.

## Alternatives and edge cases

- **Correlated selection count:** Recount a voter's choices in a scalar subquery for every vote row. It is correct, but without a suitable index it can rescan the table repeatedly and approach $O(R^2)$.
- **Join to a per-voter aggregate:** Compute each voter's choice count in one grouped CTE and join it back to `Votes`. This is also linearithmic and valid, though the window expression keeps the accepted query more direct.
- **Maximum-total subquery:** Compare each grouped total with a separately computed `MAX`. This works, but ranking expresses the all-ties rule without duplicating the aggregate relation.
- **Integer division:** Use a decimal numerator such as `1.0`; plain integer division in some SQL dialects would erase fractional votes.
- **Abstention rows:** `candidate IS NULL` contributes nothing and must never appear in the output.
- **Split votes:** The denominator is the number of candidates selected by that voter, not the total number of rows or candidates in the election.
- **Tied maximum:** `DENSE_RANK` preserves every candidate with the greatest total.
- **Output order:** Ranking is by total descending, but the final required order is candidate name ascending.

