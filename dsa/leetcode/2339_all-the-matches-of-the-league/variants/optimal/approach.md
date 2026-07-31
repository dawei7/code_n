## General

A match is an ordered pair: changing which team is home creates a different required row. The Cartesian product of `Teams` with a second copy of itself enumerates every possible choice of home and away team.

That product also contains one invalid self-match per team. Filter rows where the two names are equal. Because `team_name` is unique, every remaining row identifies two distinct teams and appears exactly once. Conversely, every ordered pair of distinct teams is present in the Cartesian product and survives the filter, so no required match is omitted.

Alias the two copies as `home` and `away`, and project their names under the requested output column names. No ordering clause is needed because any output order is accepted.

## Complexity detail

Let $t$ be the number of teams. The result necessarily contains $t(t-1)$ rows, so producing it takes $O(t^2)$ time. Aside from the output relation and database execution buffers, the query maintains no problem-sized auxiliary structure, giving $O(1)$ logical auxiliary space. A database may materialize intermediate or result rows as an implementation detail.

## Alternatives and edge cases

- **Join with `<`:** Keeping only one lexical orientation produces one match per pair and omits the reverse home-away fixture.
- **`UNION ALL` of reversed pairs:** This can work after selecting one orientation, but duplicates the logic that the directed cross join expresses directly.
- **Self-pairings:** Rows with identical home and away names are not matches and must be excluded.
- **Unique team names:** The declared uniqueness prevents duplicate ordered pairs from repeated source names.
- **Output order:** Team names need not be sorted because the contract accepts any ordering.
