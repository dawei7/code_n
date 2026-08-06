## Description

The `TeamStats` table contains one row per football team. For each team, calculate its league points as three points per win plus one point per draw; losses add no points.

Assign a competition position by descending points. Teams with equal point totals share the same position, and the next position must account for every preceding row. For example, two teams tied at position 1 are followed by position 3, not position 2.

Return `team_id`, `team_name`, `points`, and `position`. Sort the result by points from greatest to least, then alphabetically by `team_name` among tied teams.
