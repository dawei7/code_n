## General
**Give the session table two roles**

Self-join `LogInfo` so one alias represents the first session and the other represents a possible conflicting session. Match only rows with equal `account_id` and unequal `ip_address`.

**Use the complete interval-overlap condition**

Two closed intervals `[login1, logout1]` and `[login2, logout2]` overlap exactly when neither finishes before the other begins:

$$
\texttt{login1} \le \texttt{logout2}
\quad\land\quad
\texttt{login2} \le \texttt{logout1}.
$$

This covers partial overlap, containment, equal starts, and a shared endpoint. Requiring both inequalities avoids treating separated sessions as simultaneous.

**Collapse multiple conflicts to one account**

An account may have several conflicting session pairs, and the symmetric join can see each pair in both directions. Select `DISTINCT account_id` and order it for deterministic local output; only membership is semantically required.

## Complexity detail
Without a specialized interval index, the self-join can compare $O(R^2)$ session pairs in the worst case. Deduplication stores at most one state for each of the $B$ banned accounts, using $O(B)$ result or hash space. Database indexes on `account_id` can reduce comparisons between unrelated accounts but do not change the all-one-account worst case.

## Alternatives and edge cases
- **Correlated existence check:** `EXISTS` can stop after one conflict per account, but still has a quadratic worst case without suitable indexing.
- **Application-side sweep line:** Sorting events by account and time can detect active distinct IPs in $O(R\log R)$ time, but moves the task outside the required SQL query and needs careful endpoint ordering.
- **Same IP address:** Overlap alone is insufficient; the two addresses must differ.
- **Different accounts:** Their sessions never conflict with each other.
- **Contained interval:** A session fully inside another is an overlap.
- **Shared endpoint:** Closed session intervals that meet at one timestamp count as simultaneous.
- **Several violations:** Return the account only once.
- **Sequential reuse:** A later session beginning after the earlier logout is allowed.
