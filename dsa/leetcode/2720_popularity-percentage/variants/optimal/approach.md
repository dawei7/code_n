## General

**Normalize the undirected relation**

Each input row is stored in one orientation, but both endpoints must receive a friendship. Build a common table expression containing the original ordered pair and its reversed pair. Using `UNION` instead of `UNION ALL` also collapses a reciprocal duplicate such as both `(a, b)` and `(b, a)`, so each ordered user-to-friend relationship appears once.

After normalization, every user occurs in the first column, and the number of normalized rows for a given `user1` is exactly that user's distinct friend count. The number of distinct values in the same column is the total platform-user count because reversing the pairs brought every original second endpoint into that position.

Group the normalized rows by `user1`. Divide each group's row count by the single global user count, multiply by $100$, and round to two decimal places. Normalization establishes a one-to-one correspondence between a user's distinct friends and the rows in that group, so the numerator is correct. The denominator counts every endpoint exactly once as a distinct user. The final ascending sort satisfies the output contract.

## Complexity detail

Let $R$ be the number of rows in `Friends`. Set union, grouping, and final ordering require $O(R\log R)$ time in the general comparison-based model and $O(R)$ working space. Database engines may use hashing for expected linear grouping, but the manifest records the portable worst-case bound. The benchmark uses `size` as $R$.

## Alternatives and edge cases

- **`UNION ALL` plus `COUNT(DISTINCT ...)`:** Retaining both orientations and counting distinct friends per user is correct, but reciprocal input rows require careful deduplication in both the numerator and user set.
- **Correlated degree subquery:** Enumerating users and rescanning all normalized friendships for each one is correct but can take $O(R^2)$ time.
- **Count only the original `user1` column:** This omits users that appear exclusively as `user2` and undercounts their friendships.
- Friendship is undirected even when only one orientation appears in the input.
- Reciprocal rows must not count the same friendship twice.
- The denominator is global across disconnected components, not the size of a user's component.
- Percentages are rounded only after multiplying the exact ratio by $100$.
- Output rows must be ordered by the reported user identifier.
