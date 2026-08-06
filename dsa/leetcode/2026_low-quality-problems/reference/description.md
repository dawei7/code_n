## Description

The `Problems` table records the numbers of likes and dislikes received by
each problem. A problem is considered low quality when its likes form strictly
less than 60% of all votes cast for it.

Return the identifiers of every low-quality problem, ordered by `problem_id`
in ascending order. A problem whose like percentage is exactly 60% does not
qualify. The result contains no vote-count columns.
