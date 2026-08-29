## General

**Join each pass to both endpoint teams.** `PassesWithTeams` joins `pass_from` to `Teams t1` and `pass_to` to `Teams t2`. Unique player IDs and foreign keys make each pass produce one enriched row.

`team_from` is the team whose streak is being measured. `same_team_flag` is one when passer and receiver team names match and zero for an interception.

**Treat streaks independently per passer team.** The window in `StreakGroups` partitions by `team_from`. Passes made by another team do not enter this team's ordered sequence. Within one team's passes, an interception breaks its streak.

**Create a group number by counting failures.** In timestamp order, the cumulative expression adds one whenever `same_team_flag=0`. Successful rows do not change the total.

Before the first interception, successful passes have group zero. The interception increments the group, and later successes receive the new group ID until another interception increments it again. Equal group IDs therefore identify one island of successful passes between failures.

The interception row itself shares the newly incremented group but is later filtered out, so it does not add to streak length.

**Count each successful island.** `StreakLengths` keeps only rows where `same_team_flag=1` and groups by team and cumulative `group_id`. `COUNT(*)` becomes that island's number of consecutive successful passes.

Filtering after the window computation is crucial. If interceptions were removed before calculating the cumulative sum, the rows that break streaks would disappear and every successful pass by a team could collapse into one false group.

**Take the largest island per team.** `LongestStreaks` groups those island lengths by team and takes `MAX`. The final query orders team names ascending.

**Trace Arsenal.** Three same-team passes occur before its first interception, all with group zero, producing length three. The interception raises Arsenal's group ID. Two later Arsenal successes share the next group and produce length two. Maximum is three.

**Why other-team events do not interrupt a team-specific streak.** Because the window partitions by passer team, Chelsea passes between two Arsenal passes are absent from Arsenal's sequence. This matches the exact query's interpretation of “consecutive passes” as consecutive attempts by that team, not consecutive rows globally.

**A team with no successful pass is omitted.** Filtering before `StreakLengths` removes all rows for a team whose passes are all intercepted. No later CTE restores that team with zero. If “each team” requires explicit zero rows, this exact query would need a Teams-derived outer join.

**Timestamp ties are underspecified in the source.** The primary key is `(pass_from,time_stamp)`, so different passers on the same team can share a timestamp. The window orders only by `time_stamp` and uses MySQL's default frame. Peer rows can share cumulative behavior without a deterministic within-timestamp pass order. The local problem does not state how simultaneous team passes should order, so this is a material edge case.

**Why the island method works when order is defined.** The cumulative failure count changes exactly at streak-breaking rows and remains constant across successes between them. Grouping successes by that count partitions the sequence into maximal successful streaks. Counting and maximizing returns the longest.

**Follow two consecutive interceptions.** The first failure raises the group from zero to one and the second raises it to two. Because neither row survives the successful-pass filter, there is no length-zero or fake streak between them. The next success belongs to group two and starts a new island of length one.

**Output cardinality follows successful teams, not the Teams table.** The final relation originates from `StreakLengths` rather than a list of distinct team names. A team appears once only if at least one same-team pass exists. This is an observable consequence of the exact CTE chain.

## Complexity detail

Let $p$ be the number of passes and $t$ the player count. Indexed joins are typically $O(p\log t)$ or better. Partitioned timestamp ordering costs up to $O(p\log p)$, and subsequent grouping is linear or hash/sort dependent. This matches the manifest's high-level time bound.

Window rows and grouped intermediates can require $O(p)$ working space. Physical SQL memory and disk spilling depend on the MySQL plan.

## Alternatives and edge cases

- **`LAG` plus cumulative breaks:** Compare rows and assign islands explicitly; the flag already makes cumulative failures sufficient.
- **Procedural scan per team:** It works after sorting but is less natural in SQL.
- **First successful streak:** It uses group zero.
- **Interception:** It increments the group and is excluded from length.
- **Consecutive interceptions:** They create empty group IDs, which cause no harm.
- **Filter timing:** Failures must influence the window before being removed.
- **First success after failures:** It starts the group with the current cumulative failure count.
- **No successful passes:** The exact query omits the team instead of returning zero.
- **Other-team pass between attempts:** It does not break this query's team-partitioned streak.
- **Same timestamp peers:** Ordering and default window-frame behavior are not fully specified.
- **Duplicate pass row:** Primary-key rules prevent the same passer/timestamp pair.
- **Team-name collation:** It controls equality, grouping, and final sort.
- **Receiver team:** It determines success but does not own the streak row.
- **Ordinal grouping:** `GROUP BY 1,2` depends on select-list order.
- **Final ordering:** Only team name is returned as the sort key.
- **Read-only behavior:** The CTE chain does not modify source tables.
