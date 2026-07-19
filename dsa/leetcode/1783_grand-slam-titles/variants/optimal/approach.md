## General
**Turn four winner columns into one relation**

The winner data is stored in a wide format: one championship row contains four player IDs. Use four `SELECT` branches joined by `UNION ALL`, giving each selected value the common name `player_id`. The normalized relation has exactly four rows per year.

`UNION ALL` is essential. Two tournament columns may name the same player in the same year, and those occurrences represent two distinct titles. Plain `UNION` would remove duplicates and undercount such a clean sweep.

**Attach the player identity**

Join every normalized winner row to `Players` by `player_id`. The inner join naturally excludes players whose IDs never occur in a championship column: without a winner row, they have nothing to join.

The primary-key lookup supplies the requested `player_name` without changing the multiplicity of title rows.

**Aggregate title occurrences**

Group the joined rows by both `player_id` and `player_name`, then apply `COUNT(*)`. Every input to a group represents one tournament victory, so the count is exactly that player's total number of Grand Slam titles.

Normalization preserves every title once, the join assigns each title to its unique player, and grouping combines precisely the titles belonging to the same player. Therefore every reported total is correct, every winner appears, and every nonwinner is absent.

## Complexity detail
Four fixed `UNION ALL` branches scan the $C$ championship rows and produce $4C$ normalized winner rows, which is $O(C)$ work and data. With primary-key player lookups and hash aggregation, each normalized row requires constant expected processing, and emitting the $K$ groups costs $O(K)$. Total logical time is $O(C + K)$.

The normalized relation, aggregation state, and result require $O(C + K)$ space in a materializing execution. A database optimizer may pipeline the branches and use only $O(K)$ aggregation state, but the stated bound remains valid.

## Alternatives and edge cases
- **Four joins followed by addition:** Aggregate each tournament column separately and join the four count tables. This can work, but it is verbose and needs careful outer joins and null handling when a player wins only some tournaments.
- **Conditional self-join predicates:** Joining a player when its ID equals any of the four columns identifies winning years, but one joined row cannot directly preserve multiple titles won by that player in the same year without additional expressions.
- **Correlated counts per player:** Four correlated subqueries can sum tournament-specific counts, but they repeatedly scan `Championships` for players and scale poorly.
- **Repeated winner in one year:** Each tournament is a separate title, so duplicate player IDs across columns must remain duplicate normalized rows.
- **Player with no titles:** The player must not appear with a zero; the inner join omits that row.
- **Tied totals:** Players with equal counts remain separate groups.
- **Noncontiguous identifiers:** Group and join by the stored `player_id`; no numeric sequence is implied.
- **Output order:** The platform accepts any row order. The app-local query adds `ORDER BY player_id` only to keep local fixtures deterministic.
