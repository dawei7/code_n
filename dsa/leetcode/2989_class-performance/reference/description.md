## Description

The `Scores` table stores each uniquely identified student's name and scores
on three assignments. A student's total score is the sum of that student's
three assignment values.

Find the highest student total and the lowest student total, then return their
difference in one column named `difference_in_score`. The result contains one
row, so its ordering is irrelevant.

Compute each student's combined score before taking the two class-wide
extremes. If several students share either extreme, that does not add rows or
change the requested difference.
