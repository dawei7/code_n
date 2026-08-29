## General

**A match is an ordered pair of different teams**

The home and away roles matter. A match with team `A` at home and team `B` away is different from the match with `B` at home and `A` away.

Therefore the desired result is not a collection of unordered two-team combinations. It is every ordered pair

`(home_team, away_team)`

whose two names differ.

With `t` teams, each team has `t - 1` possible opponents while it is home, so the output contains `t(t - 1)` rows.

**Use two independent aliases of the same table**

The query reads `Teams` twice:

- `t1` supplies the home-team candidate;
- `t2` supplies the away-team candidate.

Joining a table to itself forms every possible pairing between a row from the first role and a row from the second role. Before filtering, this includes `t^2` ordered pairs.

Aliases are required because both sources have a column named `team_name`. `t1.team_name` and `t2.team_name` make the role of each reference unambiguous.

**Remove self-matches**

The condition

`t1.team_name != t2.team_name`

eliminates pairs in which the same team occupies both roles. The uniqueness guarantee means equal names identify the same team, so this test removes exactly the `t` diagonal self-pairs.

Every remaining row contains two distinct teams and is a legal match.

The query uses `JOIN Teams AS t2` without an `ON` relation and places the relationship in `WHERE`. In MySQL this acts as a Cartesian self-join followed by the inequality filter. Writing `CROSS JOIN` would make the Cartesian intent more explicit, while `JOIN ... ON t1.team_name != t2.team_name` would express the same result.

**Why both home-away directions appear**

For distinct teams `A` and `B`, the Cartesian product contains both:

- `t1 = A, t2 = B`;
- `t1 = B, t2 = A`.

The inequality accepts both. The selected aliases turn the first into `(A, B)` and the second into `(B, A)`. Hence every two-team pairing produces exactly the required two matches.

There is no multiplication by two and no second union query because role reversal already arises naturally from the self-join.

**Why no result row is missing or duplicated**

Take any required match with distinct home team `H` and away team `A`. Uniqueness provides exactly one `Teams` row for `H` and exactly one for `A`. Their Cartesian pairing appears once, passes the inequality, and projects to the required row.

Conversely, every emitted row comes from two unequal names, so it represents a legal match between different teams. Unique source names ensure no second pair of source rows can produce the same ordered name pair.

Thus the output contains every legal directed matchup exactly once.

**No final order is necessary**

The problem permits any result order, so the query intentionally omits `ORDER BY`. SQL does not guarantee a stable order without that clause, but no ordering promise is needed.

The column aliases `home_team` and `away_team` provide the requested output schema and clearly distinguish the two roles.

## Complexity detail

Let `t` be the number of teams. The Cartesian self-join considers `t^2` candidate row pairs and filters `t` self-pairs, so time is `O(t^2)`. This is also asymptotically unavoidable because the required output itself contains `t(t-1) = O(t^2)` rows.

The query text uses no explicit auxiliary table, aggregate, sort, or window structure, which motivates the manifest's `O(1)` auxiliary-space description beyond database execution and output. In an actual engine, join buffering and result materialization may use implementation-dependent memory. Required output storage is `O(t^2)` if materialized rather than streamed.

Comparing two team-name strings has a cost dependent on their lengths and collation in a low-level analysis; the standard row-count complexity treats schema values as bounded comparison units.

## Alternatives and edge cases

- **`CROSS JOIN` with a WHERE filter:** This is the clearest spelling of the same Cartesian pairing and inequality logic.
- **Inequality in the `ON` clause:** `JOIN Teams t2 ON t1.team_name != t2.team_name` returns the same directed pairs.
- **Use `t1.team_name < t2.team_name`:** This emits only one unordered orientation per team pair and would miss the reverse home-away match.
- **Union two orientations of unordered pairs:** Select each pair once, then union its reversal. This is correct but longer than allowing the Cartesian product to generate both naturally.
- **Include equality:** That creates invalid matches in which a team plays itself.
- **One team:** The Cartesian product has one self-pair, the filter removes it, and the correct result is empty.
- **Two teams:** Exactly two rows remain, one for each home-away direction.
- **Unique names:** They ensure equality identifies the same team and prevent duplicate ordered outputs.
- **Duplicate-name invalid input:** Without uniqueness, source-row duplicates could multiply identical match names.
- **Null names:** The stated team-name model is used as an identifier. Under SQL three-valued logic, null inequality would be unknown; valid source data is expected to provide actual unique names.
- **Any output order:** No sort is required, avoiding unnecessary work.
- **Column aliases:** Without them, both output expressions would share the source name `team_name` and fail to present the requested role labels clearly.
- **Output-size lower bound:** Any correct solution must produce quadratic rows for many teams, so quadratic time is inherent.
- **No aggregation:** Each pair is already one desired match and should not be grouped.
