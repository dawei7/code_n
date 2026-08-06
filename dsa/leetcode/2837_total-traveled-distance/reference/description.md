## Description

The `Users` table identifies every user and stores their name. The `Rides` table records completed rides, including the user responsible for each ride and its traveled distance. A user may have several ride rows, while some users may have no completed ride at all.

Produce one result row for every user. Report the user's identifier, name, and the sum of all their ride distances under the column name `traveled distance`. A user with no matching ride must receive a distance of `0`, not be omitted. Sort the final rows by `user_id` in ascending order.
