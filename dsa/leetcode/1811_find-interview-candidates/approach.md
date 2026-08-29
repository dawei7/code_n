## General

**Normalize three medal columns into one event stream**

The two candidate rules are easier to evaluate when every medal is represented as one row containing `contest_id`, `user_id`, and medal `type`.

CTE `S` creates that form with three branches:

- gold medalists receive `type = 1`;
- silver medalists receive `type = 2`;
- bronze medalists receive `type = 3`.

The branches use `UNION`. Because medal type differs across branches and each contest has one row, valid medal events are distinct; `UNION ALL` could avoid duplicate elimination, but plain `UNION` is the exact source.

After normalization, gold counting filters type one, while consecutive-contest detection ignores type and treats any medal equally.

**Detect consecutive contest IDs with row-number subtraction**

CTE `T` partitions medal events by `user_id` and orders each user's rows by `contest_id`. `ROW_NUMBER()` assigns 1, 2, 3, and so on within that user's medal history.

For each row it computes

`diff = contest_id - row_number`.

This is the gaps-and-islands technique. If a user medals in contests 190, 191, and 192, the row numbers are 1, 2, and 3, so all differences equal 189. Consecutive IDs increase by one at exactly the same rate as row number.

If a contest is missed, contest ID jumps by more than one while row number increases by only one, changing `diff` and starting a new group.

The statement guarantees globally consecutive contest IDs with no skipped ID. Thus adjacent numeric IDs truly mean adjacent contests, not merely adjacent stored rows.

**Build candidates satisfying either rule**

CTE `P` combines two user sets.

The first branch reads `S`, keeps `type = 1`, groups by user, and retains `COUNT(1) >= 3`. This finds users with at least three gold medals in any contests; consecutiveness is irrelevant.

The second branch groups `T` by `user_id, diff`. Each group is one consecutive run of contests in which that user won some medal. `HAVING COUNT(1) >= 3` retains runs of length at least three.

`SELECT DISTINCT user_id` removes duplicate user IDs when a user has multiple qualifying streak groups. The surrounding `UNION` also removes overlap between users qualifying by both rules.

**Join candidate IDs to user details**

The final query left-joins `P` to `Users` on `user_id` and selects `name` and `mail`.

Under the intended data model every medalist is a known user, so this returns their details. The exact source uses `LEFT JOIN`, which would preserve a candidate ID even if a matching user row were unexpectedly absent, producing null details.

No `ORDER BY` is needed because any output order is accepted.

**Following the sample**

Sarah has gold medals in contests 190, 193, and 196. The gold-count branch includes her even though those contests are not consecutive.

Bob has medals in 190, 191, and 192. Ordered row numbers subtract to one constant `diff`, forming a group of three. His later 194–196 streak can form another qualifying group, but `DISTINCT` and `UNION` still return him once.

Alice medals in 191, 192, and 193, producing one length-three island. Quarz medals in five consecutive contests, producing a group count five. All four IDs reach the final join.

**Why the streak grouping is exact**

Within one user's ordered medal rows, if consecutive rows have contest IDs differing by one, both contest ID and row number advance equally, so `diff` stays constant. Repeating this proves every consecutive run shares one difference.

Conversely, if a gap occurs, contest ID advances by at least two while row number advances by one, so the difference changes. Separate runs cannot accidentally merge. Therefore grouping by user and difference partitions medal history into maximal consecutive streaks.

Assuming one medal event per user per contest, which follows the contest medal roles, group count is exactly the number of contests in the streak.

**Why the final candidate set is correct**

The first `P` branch includes exactly users meeting the three-gold rule. The second includes exactly users having a medal streak of at least three contests. Set union implements the logical “at least one condition” and removes duplicates.

Joining those IDs to `Users` changes only representation, not qualification. The final rows are therefore precisely the requested interview candidates.

## Complexity detail

Let $C$ be the number of contests and $U$ the number of users. `S` produces at most $3C$ medal rows.

Window partitioning requires ordering medal rows by user and contest. A general sort costs $O(C\log C)$. Subsequent grouping and gold counting are linear or hash-based expected $O(C)$, and joining candidate IDs to Users is expected $O(U+C)$ with hashing or indexes.

This yields the manifest's $O(C\log C+U)$ time model and $O(C+U)$ working space. SQL physical plans, indexes, and `UNION` duplicate-elimination strategy can change constants or introduce additional sorting, but not the logical method.

## Alternatives and edge cases

- **Three self-joins for streaks of exactly three:** It can detect a three-contest window but becomes awkward for the follow-up parameter $n$; gaps-and-islands naturally supports arbitrary streak length.
- **`LAG` comparisons:** Checking previous IDs can mark streak continuations, but run-length aggregation still needs additional logic.
- **`UNION ALL` in `S`:** Valid medal events are already distinct, so it can avoid set deduplication.
- **Inner join to Users:** It is sufficient when every candidate ID is guaranteed to exist and avoids null detail rows.
- **User qualifies twice:** `UNION` returns the user only once.
- **Several qualifying streaks:** `DISTINCT` in the streak branch collapses them to one user ID.
- **Exactly three golds:** The `>= 3` condition includes the user.
- **Golds need not be consecutive:** Only the count matters in the first branch.
- **Any-medal streak:** Gold, silver, and bronze rows all participate equally in `T`.
- **Gap of one missed contest:** It changes `diff` and splits the streak.
- **Contest IDs start above one:** Subtraction grouping works regardless of the starting ID.
- **No skipped global IDs:** It makes numeric consecutiveness equivalent to contest consecutiveness.
- **One candidate condition:** Set union implements logical OR, not AND.
- **Any result order:** No final sorting is necessary.
- **Parameterized streak length:** Replace the second `HAVING COUNT(1) >= 3` threshold with the procedure parameter.
- **Participation-only follow-up:** The normalized medal events would need to be aligned with a participation table before defining consecutive considered contests.
