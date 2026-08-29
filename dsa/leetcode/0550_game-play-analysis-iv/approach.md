## General

The requested fraction has one denominator unit per distinct player and a numerator unit for players who logged in exactly one day after their first login. The query first creates one earliest-login row per player, then left-joins the matching next-day activity and averages a Boolean indicator.

**Find each player's first date.** Derived table `a` runs:

`SELECT player_id, MIN(event_date) AS event_date FROM Activity GROUP BY 1`.

`GROUP BY 1` means grouping by the first selected expression, `player_id`. `MIN(event_date)` returns the earliest chronological date in each player's group.

The derived table therefore contains exactly one row per distinct player. This property is crucial: the final average must weight players equally, not weight frequent players by their number of activity rows.

**Look for activity on the immediately following day.** Table `a` is left-joined to `Activity AS b` on the same `player_id` and:

`DATEDIFF(a.event_date, b.event_date) = -1`.

MySQL `DATEDIFF(x, y)` computes `x - y` in days. A result of negative one means `b.event_date` is one day after `a.event_date`.

Writing the arguments in this order can be easy to misread. The negative result is intentional:

$$
\text{first date}-\text{candidate date}=-1
$$

implies candidate date equals first date plus one day.

The composite primary key `(player_id, event_date)` guarantees at most one matching `b` row for a player on that date. Thus each derived player row produces exactly one joined row whether a match exists or not.

**Why the join must be left, not inner.** With a left join, a player without next-day activity remains in the result and receives `NULL` for `b.event_date`. That player must count in the denominator with indicator zero.

An inner join would discard such players entirely, leaving only successful players and incorrectly making the fraction one whenever any match exists.

**Turn match existence into zero or one.** MySQL expression:

`b.event_date IS NOT NULL`

evaluates to one for a successful next-day match and zero for an unmatched left-join row.

Since there is one joined row per player, `AVG` of these indicators equals:

$$
\frac{\text{players with next-day login}}{\text{all players}}.
$$

No separate count or division expression is needed.

**Round and name the result.** `ROUND(..., 2)` rounds the fraction to two decimal places, and `AS fraction` gives the only output column its required name.

In the example, derived table `a` contains first dates for players one, two, and three. Only player one has activity exactly one day after the first date. Their indicator rows are one, zero, zero, whose average is one third and rounds to 0.33.

Later activity that is not exactly the next calendar day does not qualify. A player returning two days later, or years later, receives no match under the date-difference condition.

Games played and device identifiers do not affect this question. The query reads only player identity and dates.

**Why every successful indicator is correct.** A non-null joined date belongs to the same player and satisfies the exact one-day difference from that player's minimum date. It therefore proves the required return login.

**Why every qualifying player is found.** If a player has an activity row on first date plus one day, the primary derived row and that activity row satisfy both join conditions. The left join contains the match, making the indicator one.

The final query returns one aggregate row even though the join contains one row per player.

## Complexity detail

Let $A$ be the number of activity rows and $P$ the number of distinct players. A typical plan groups or orders $A$ rows to obtain minima, costing up to $O(A\log A)$ without helpful indexing, then joins the $P$ first-date rows back to activity.

With indexes on the primary key, next-day lookups can be efficient. The manifest's representative bound is $O(A\log A)$ time and $O(P)$ aggregation state. Actual SQL cost depends on optimizer choices, indexes, hashing, sorting, and temporary storage.

The logical joined result has one row per player because the primary key makes the target date unique.

## Alternatives and edge cases

- **Inner join:** It removes non-returning players and corrupts the denominator.
- **Correlated `EXISTS`:** For each player's first date, test whether next-day activity exists. It is logically valid and may optimize similarly.
- **Conditional distinct counts:** Divide qualifying distinct players by all distinct players explicitly; this is more verbose than averaging one indicator per player.
- **Use any login instead of `MIN`:** The criterion is specifically relative to the first login.
- **Return two days later:** It does not satisfy the exact `DATEDIFF = -1` condition.
- **Multiple later logins:** Only the one exact next-day row affects the Boolean result.
- **One player:** The fraction is either 1.00 or 0.00 depending on a next-day row.
- **No qualifying players:** Every indicator is zero and the average is zero.
- **Primary-key uniqueness:** It prevents multiple next-day join rows from overweighting a player.
- **Rounding:** `ROUND(..., 2)` applies only after averaging all players.
- **`GROUP BY 1`:** It is valid MySQL positional syntax, though naming `player_id` explicitly may be clearer.
