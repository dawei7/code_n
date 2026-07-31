## General

**Classify every pass for its sender's team.** Join `Passes` to `Teams` twice: the first alias finds the team that attempted the pass, and the second finds the receiver's team. Equality of those two names produces a `successful` flag of one; an interception produces zero. The sender's team remains the partition key even when another team receives the ball.

**Turn interceptions into island boundaries.** Within each sender-team partition, sort by `time_stamp` and take a cumulative sum of interception flags. Every interception increments that sum, so all successful passes after one interception and before the next receive the same `streak_group`. Passes sent by other teams are in different window partitions and therefore cannot split this team's streak.

Group by `team_name` and `streak_group` after filtering to successful rows. Summing the flags gives the length of each positive streak. The filter also removes teams whose outgoing passes are all intercepted, matching the remotely verified output domain. Finally, take the maximum streak length per team and sort by team name.

For any team, two successful passes have the same group exactly when no interception by that team occurs between them: the cumulative boundary count changes at every and only every failed outgoing pass. Consequently each grouped sum is one maximal successful streak, and the maximum of those sums is the requested answer.

## Complexity detail

Let $t$ be the number of players and $p$ the number of passes. Indexed endpoint lookups cost $O(p\log t)$ under a comparison-index model. The partitioned window ordering costs $O(p\log p)$ in the worst case, while the two aggregation stages are linear apart from engine-managed grouping and final output ordering. The stated bound is therefore $O(p\log p+p\log t)$ time and $O(p)$ working space for the joined, ordered, and grouped intermediate rows.

The benchmark defines `size` as $p$, uses $t=2p$ players, and supplies tiers of 16, 64, and 256 passes. The accepted-class query joins each endpoint once, sorts the pass rows once for the window, and aggregates them. A correct slower baseline resolves both endpoint teams with correlated scans inside every pass row, producing quadratic work as both tables grow.

## Alternatives and edge cases

- **Compare adjacent rows with `LAG`:** This can locate interception boundaries, but a cumulative boundary label is still needed to aggregate complete islands cleanly.
- **Use one global pass sequence:** Passes from another team do not break the current team's streak; the window must partition by the sender's team.
- **Partition by the receiver's team:** The streak belongs to the team attempting the pass, including its intercepted attempts.
- **Count all rows in each group:** The interception row starts a new label but is not part of a successful streak, so only rows with `successful = 1` may contribute.
- **Return a zero for every team:** The verified platform behavior omits teams that never complete a successful outgoing pass.
- **Leading or trailing interceptions:** They may create empty logical streaks, which disappear when failed rows are filtered before aggregation.
- **Several players on one team:** Partition by `team_name`, not `pass_from`, so their outgoing passes form one chronological team sequence.
- **Timestamp ordering:** The fixed zero-padded `MM:SS` representation sorts chronologically as text.
- **Output ordering:** Explicitly order by `team_name`; neither CTE nor grouping order is guaranteed.
