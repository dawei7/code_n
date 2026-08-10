## General

The requested result has one row per player, while `Activity` may have many rows for the same player. This is a grouped aggregation problem:

- `player_id` determines the group;
- the earliest `event_date` inside that group is the desired value.

SQL's `MIN` aggregate applies directly because dates have chronological ordering. The minimum date is the earliest login date.

**Group rows by player.** The query ends with `GROUP BY 1`. In MySQL, the number one refers to the first expression in the `SELECT` list, which is `player_id`. It is therefore shorthand for `GROUP BY player_id`.

After grouping, all activity rows for one player belong to one logical group. The database produces one output row per distinct `player_id` because that identifier is the non-aggregated selected expression.

Using the explicit column name would usually be clearer and less fragile if select-list order changed, but the positional form in the exact source is valid MySQL syntax.

**Reduce each player's dates to its minimum.** `MIN(event_date)` examines the date values in the current player group and returns the earliest. The alias `AS first_login` gives the output column the exact required name.

The other source columns are irrelevant. `device_id` says where the login occurred, and `games_played` says what happened during the session; neither affects which date is first.

Because `event_date` is a date-typed column, `MIN` compares chronological date values rather than treating the displayed text as an arbitrary label. No conversion to a string or numeric timestamp is needed. This keeps the query aligned with the table contract and lets MySQL use its native date semantics.

For player one in the example, the grouped dates are `2016-03-01` and `2016-05-02`. Their minimum is `2016-03-01`. Player two has only one row, so its minimum is that row's date. Player three's minimum is `2016-03-02` rather than `2018-07-03`.

**Why the primary key matters.** The composite primary key `(player_id, event_date)` guarantees one activity row at most for a player on a given date. This query would still return the same minimum date even if duplicate date rows existed, but the key establishes the source's player-date identity and ensures its activity facts are unambiguous.

The query does not use `ORDER BY` because the contract permits any result order. `GROUP BY` does not promise a portable ordering; leaving it unspecified is both sufficient and potentially avoids an unnecessary final sort.

Correctness follows group by group. Every source row for player `p` is placed in exactly the group keyed by `p`. `MIN` returns a date no later than any other date in that group, so it is exactly `p`'s first login. The query outputs the group key and that minimum once. Repeating this for every group yields all and only the required player rows.

Notice that aggregation performs both necessary transformations together. Grouping changes many activity rows into one logical player unit, and `MIN` changes that unit's many dates into its single requested fact. There is no later filtering step that could accidentally remove a player: every nonempty player group necessarily produces one row.

This is preferable to taking the global minimum, which would return only the first login among all players. It is also different from selecting arbitrary `event_date` beside `player_id`; without aggregation, SQL would retain multiple activity rows or choose an undefined group member under permissive modes.

The source comment is ignored by MySQL and merely identifies the expected query language. The executable statement is the `SELECT` through `GROUP BY` block.

## Complexity detail

Let $A$ be the number of activity rows and $P$ the number of distinct players. A hash-aggregation execution plan scans the $A$ rows once and maintains one current minimum per player, giving $O(A)$ expected processing time and $O(P)$ aggregation state, matching the manifest.

Actual database cost depends on indexes, storage layout, optimizer choice, and whether grouping uses hashing, sorting, or an index-ordered scan. A sort-based plan can cost $O(A\log A)$ comparison work. The result itself contains $P$ rows. SQL complexity notation describes a representative logical execution rather than prescribing one physical plan.

## Alternatives and edge cases

- **Window `FIRST_VALUE`:** Partition by player and order by date, then use `DISTINCT` to collapse repeated output rows. It works but is more machinery than grouped `MIN`.
- **Window ranking:** Assign `ROW_NUMBER()` within each player ordered by date and keep row one. This is useful when other columns from the first row are required, but only the date is needed here.
- **Correlated subquery:** Compare each row's date with that player's minimum. It can return the same result but may repeat logical work and still needs deduplication if the schema allowed ties.
- **One activity row for a player:** Its date is trivially both minimum and first login.
- **Many activities on later dates:** They remain in the group but cannot change a smaller existing minimum.
- **Output order:** No `ORDER BY` is necessary because any order is accepted.
- **Column alias:** Without `AS first_login`, the computed value would not have the required output name.
- **`GROUP BY 1` portability:** MySQL supports positional grouping; `GROUP BY player_id` communicates intent more explicitly across database systems.
