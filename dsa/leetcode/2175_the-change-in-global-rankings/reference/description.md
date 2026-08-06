## Description

`TeamPoints` stores each national team's identifier, unique country name, and
current global-ranking points. `PointsChange` contains exactly one signed
points adjustment for every team: a positive value adds points, a negative
value removes points, and zero leaves the total unchanged.

A ranking orders teams by points in descending order. When point totals tie,
the country name in lexicographical order breaks the tie. Apply every points
change, rank the teams again under the same rules, and report how far each team
moved. Define `rank_diff` as the old rank minus the new rank, so an improvement
is positive, a decline is negative, and an unchanged position is zero. Return
one row per team in any order.
