## Description

The `Teams` table assigns every match participant to a team. The `Passes` table records each attempted pass through its sender, receiver, and `time_stamp`. A pass is successful for the sender's team when both players belong to that same team; receiving the ball on another team is an interception.

For each team, consider only passes sent by that team's players and place them in chronological order. Successful passes extend the current streak, while an interception ends it. Passes sent by another team do not interrupt this team's sequence. Return the greatest positive streak attained by every team that completes at least one successful pass, omitting teams whose outgoing passes are all intercepted, and order the rows by `team_name` in ascending order.
