## General
**Normalize the three medal columns**

Create one `(contest_id, user_id)` stream by combining gold, silver, and bronze projections with `UNION ALL`. Each contest contributes three medal wins. Once medal position is removed, the consecutive-contest rule becomes a sequence problem per user.

**Turn consecutive IDs into stable groups**

Within each user, order wins by `contest_id` and assign `ROW_NUMBER()`. For consecutive IDs, `contest_id - row_number` remains constant: both values increase by one at every next contest. Group by the user and this difference; any group with at least three rows proves a qualifying consecutive run. A gap changes the difference and starts a new group.

**Evaluate the gold rule separately**

Group the original contest rows by `gold_medal` and retain users with at least three rows. Gold contests need not be adjacent, so no sequence calculation belongs in this branch.

**Deduplicate candidates before attaching profile data**

Combine streak candidates and gold candidates with `UNION`, which removes a user found by both rules. Join those identifiers to `Users` to return only `name` and `mail`.

Every streak result has at least three medal wins whose IDs form one consecutive run by the constant-difference property. Every gold result has at least three distinct contest rows with that gold medalist. Conversely, any user satisfying either rule is retained by its corresponding aggregation, so the union is exact.

## Complexity detail
Unpivoting creates exactly $3C$ rows. Window ordering of these rows dominates at $O(C\log C)$ time; grouping the numbered wins, grouping gold medals, deduplicating candidate IDs, and joining up to $U$ user rows add linear work. The normalized wins, window state, groups, and candidate/user relations require $O(C+U)$ space.

## Alternatives and edge cases
- **Three self-joins on consecutive contests:** Joining each contest to the next two and comparing all medal columns is possible, but it expands many predicates and can be repeatedly evaluated per user.
- **`LAG` or `LEAD`:** Comparing each win with the win two positions away also detects a three-contest run and has the same sorting requirement; gaps-and-islands naturally supports runs longer than three.
- **Correlated checks per user:** They mirror the rules but can rescan the contest table for every user, degrading to $O(UC)$ work.
- **Changing medal colors:** Gold, silver, and bronze all count equally toward the consecutive rule.
- **Nonconsecutive gold medals:** They qualify under the separate gold rule.
- **Nonconsecutive non-gold medals:** Their total count does not qualify the user.
- **Run longer than three:** It forms one group with count above three and still produces one candidate ID.
- **Two separate short runs:** Counts from different gap groups must not be combined.
- **Both rules:** `UNION` prevents a duplicate output row.
- **Output order:** No sorting clause is necessary.
