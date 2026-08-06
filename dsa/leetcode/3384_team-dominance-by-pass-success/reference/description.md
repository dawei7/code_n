## Description

The `Teams` table assigns every player in a match to a team. The `Passes` table records the player sending each pass, its `time_stamp`, and the player receiving it.

Score every recorded pass for the sender's team. A pass received by a teammate contributes $+1$; a pass received by a player on another team contributes $-1$. Compute these contributions separately for the first half, from `00:00` through `45:00` inclusive, and the second half, from `45:01` through `90:00` inclusive.

Return one row for every team and half that has at least one recorded outgoing pass. Each row contains the team name, half number, and summed dominance score. Sort the result by `team_name` and then `half_number`, both in ascending order.
