## Description

The `Friends` table stores friendships between pairs of users on a social platform. A friendship is undirected: if a row contains `user1 = a` and `user2 = b`, then each user counts the other as a friend even though the reverse row need not be present.

For every user appearing anywhere in the table, compute the user's number of distinct friends divided by the total number of distinct platform users, multiply that ratio by $100$, and round the result to two decimal places. Return one row per user under the column name `percentage_popularity`, ordered by `user1` in ascending order.
