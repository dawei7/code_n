## General

An accepted request creates an undirected friendship even though the table stores two directed roles: requester and accepter. Each row contributes one friend to both endpoints. To count friends uniformly, the query transforms every friendship edge into two endpoint rows, then counts occurrences of each person ID.

**Symmetrizing each friendship**

The common table expression `T` contains:

```sql
SELECT requester_id, accepter_id
FROM RequestAccepted
UNION ALL
SELECT accepter_id, requester_id
FROM RequestAccepted
```

For original friendship $(u,v)$, the first branch emits row $(u,v)$ and the second emits $(v,u)$. In both branches, the first column now means “the person whose friend count receives one.” The second column records the friend but is not needed for the final count.

For sample row $(1,2)$, user 1 gains one occurrence from the first branch and user 2 gains one from the swapped branch. Repeating this for every accepted request makes each person appear once per incident friendship.

`UNION ALL` is essential. Plain `UNION` removes duplicate rows across branches. Although the composite primary key prevents duplicate directed acceptance pairs, distinct friendships involving the same person must all remain as separate occurrences for counting. Deduplication is not part of this transformation.

**Grouping endpoint occurrences**

The outer query groups by the first column:

```sql
GROUP BY 1
```

Ordinal 1 refers to `requester_id AS id`. `COUNT(1)` counts endpoint rows in each person’s group, which equals that person’s number of friends under the one-row-per-friendship schema.

In the sample:

- user 1 appears for friendships with 2 and 3, count two;
- user 2 appears for friendships with 1 and 3, count two;
- user 3 appears for friendships with 1, 2, and 4, count three;
- user 4 appears once.

**Selecting the unique maximum**

`ORDER BY 2 DESC` refers to the second selected expression, `COUNT(1) AS num`. It ranks people from most friends to fewest. `LIMIT 1` keeps the first group.

The contract guarantees exactly one person has the maximum friend count, so no tie-breaking key is required. The follow-up removes that guarantee and would need a rank or comparison against the maximum rather than arbitrary top-one selection.

The final aliases `id` and `num` provide the requested schema.

**Why the algorithm is correct**

Every accepted row represents one friendship between its requester and accepter. Symmetric expansion creates exactly one endpoint occurrence for each of those two people. Therefore, for any person $p$, the number of expanded rows whose first column is $p$ equals the number of accepted friendship edges incident to $p$.

Grouping gathers exactly those occurrences, and `COUNT(1)` computes the true friend count. Descending ordering places the largest count first. Uniqueness of the maximum makes `LIMIT 1` return exactly the required person and count.

No acceptance date enters the calculation because it does not change friendship identity. The composite primary key ensures a directed pair occurs at most once.

This reasoning assumes requester and accepter are distinct people, as a friendship relation normally requires. If self-requests were permitted, symmetric expansion would count one self-row twice even though “number of friends” would need a clarified policy. The intended problem data models friendships between different users.

## Complexity detail

Let $n$ be the number of accepted-request rows and $u$ the number of distinct people. The CTE produces $2n$ rows, which is still $O(n)$. Hash grouping takes expected $O(n)$ time and $O(u)$ group state.

Sorting $u$ grouped results by count costs $O(u\log u)$; a top-one optimizer may avoid a complete sort, but the conservative manifest bound $O(n\log n)$ covers expansion, grouping, and ranking. Materializing the expanded relation and groups can use $O(n)$ space.

Indexes and optimizer strategies affect the actual SQL plan. The asymptotic output is one row.

## Alternatives and edge cases

- **Aggregate each role separately, then combine counts:** Count requester and accepter occurrences per ID and outer-join/sum the two results. Correct but more complicated than symmetric expansion.
- **Use `UNION` instead of `UNION ALL`:** Risks discarding occurrences and undercounting; every friendship endpoint contribution must remain.
- **Window `RANK`:** Group counts, rank descending, and keep rank one. This naturally returns all tied leaders for the follow-up.
- **Maximum-count subquery:** Compare each grouped count with the maximum grouped count to return every leader.
- **Count only requester IDs:** Misses friendships where a person was the accepter.
- **Count only accepter IDs:** Has the symmetric omission.
- **Unique maximum:** Justifies `LIMIT 1` without a secondary ordering rule.
- **Tie in generalized data:** Exact query returns only one arbitrary leader; use `RANK` for all.
- **One friendship:** Both endpoints have count one, creating a tie and therefore contradicting the unique-winner test guarantee.
- **Accept date:** Irrelevant to total friend degree and deliberately omitted.
- **Composite primary key:** Prevents duplicate directed friendship rows, so each accepted pair contributes once.
- **Self-friend row:** Would be emitted twice for one ID; intended friendship data should exclude it or define special handling.
- **Ordinal references:** `GROUP BY 1` and `ORDER BY 2` are concise but explicit aliases are easier to maintain.
- **Empty table:** No groups exist and no row is returned; intended tests supply a unique maximum.
