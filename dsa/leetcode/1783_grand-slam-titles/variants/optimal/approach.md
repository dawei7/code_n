## General

**Unpivot four winner columns into one stream**

Each `Championships` row stores four tournament winners in separate columns. Counting titles by player is easier when every title is represented as one row with one `player_id`.

The common table expression `T` selects `Wimbledon`, `Fr_open`, `US_open`, and `Au_open` in four branches, aliasing each as `player_id`. `UNION ALL` concatenates those branches.

For every championship year, `T` therefore contains exactly four rows, one per Grand Slam title.

**Why UNION ALL is essential**

The same player can win several tournaments or win across several years. Every occurrence is a separate title and must be counted.

Plain `UNION` would remove duplicate player identifiers and destroy multiplicity. `UNION ALL` preserves every winner occurrence, so repeated IDs correctly represent repeated victories.

The `year` column is not needed after unpivoting because the task asks only for total titles, not a year-by-year report.

**Join winner identifiers to player names**

`T JOIN Players USING (player_id)` matches every title occurrence to its player row.

The inner join returns only winner IDs that exist in `Players` and supplies `player_name` for output. Under the schema's intended referential data, every championship winner corresponds to a player.

Players who never won have no row in `T`, so they cannot enter the join. This naturally satisfies the requirement to omit zero-title players without a `HAVING` clause.

**Group occurrences by player**

`GROUP BY 1` groups by the first selected expression, `player_id`. Every joined title occurrence for the same player enters one group.

`COUNT(1)` counts rows in that group. Because each CTE row represents exactly one tournament victory, the count is the player's total Grand Slam titles across all four columns and all years.

`player_name` is selected without being separately grouped. In MySQL, it is functionally dependent on primary-key `player_id`: one ID identifies exactly one name. Therefore every row in a player group has the same name.

**Trace the sample**

The three championship rows create twelve CTE rows.

Player one appears twice as Wimbledon winner, three times as French Open winner, once as US Open winner, and once as Australian Open winner. Seven CTE occurrences join to Nadal and `COUNT(1)` returns seven.

Player two appears five times and receives count five. Player three never appears in `T`, so no Novak group is created.

**Why null-filling is unnecessary**

This is not a report that must list every player with zero. Starting from title occurrences is desirable because only winners belong in the result.

A left join from `Players` would create zero-win rows and then require grouping plus a filter. The exact inner-join direction expresses the inclusion rule more directly.

**Any-order result**

No `ORDER BY` appears because row order is unrestricted. The engine may output player groups in any physical order.

The selected column order is fixed as `player_id`, `player_name`, and `grand_slams_count`.

**Why the query is correct**

The CTE maps every tournament column in every year to one retained row, so there is a one-to-one relationship between rows of `T` and titles.

Joining labels each title with its player, and grouping counts all occurrences per ID. Non-winners have no occurrence and are omitted. Thus every returned count is exact and every required winning player appears.

## Complexity detail

Let $C$ be the number of championship-year rows and $K$ the number of distinct winning players. The four CTE branches scan or project $4C=O(C)$ title occurrences.

With indexed player lookup and hash aggregation, joining and grouping take expected $O(C+K)$ time. The CTE stream or materialization and group state use $O(C+K)$ space in a conservative plan, matching the manifest.

A database optimizer may scan `Championships` separately for each UNION ALL branch, but four is a fixed factor. Physical sort-based grouping can add $O(C\log C)$ work; SQL does not prescribe the execution plan.

## Alternatives and edge cases

- **Four joins or correlated counts:** They repeat logic and are more verbose than unpivoting once.
- **UNION instead of UNION ALL:** It is incorrect because it removes repeated wins by the same player.
- **Conditional aggregation per Players row:** Count matches across four columns, but it can require cumbersome joins and expressions.
- **Player wins multiple tournaments in one year:** Each column contributes a separate CTE row and title.
- **Player wins across years:** Repeated rows remain and are all counted.
- **Player wins nothing:** No CTE occurrence exists, so the player is omitted.
- **One winning player:** All title rows group under one identifier.
- **Primary-key player name:** Grouping by ID determines one consistent name.
- **Year not selected:** It is irrelevant to the requested lifetime total.
- **Four fixed tournaments:** Exactly four UNION ALL branches cover the schema.
- **COUNT(1):** It counts every joined title row, equivalent to `COUNT(*)` here.
- **Inner join:** It deliberately begins from winners rather than retaining every player.
- **Ordinal grouping:** `GROUP BY 1` depends on `player_id` being the first selected expression.
- **Any output order:** No ordering clause is required.
