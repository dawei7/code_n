## Description

The `Friends` table stores pairs of users who are friends with each other. A
third user is a mutual friend of a pair when that third user is directly
connected to both endpoints.

Find every stored friendship whose two users have no mutual friend. Friendship
is undirected even though its endpoints occupy two separate columns, so a
connection must be recognized from either orientation. Return the original
`user_id1` and `user_id2` values, ordered by both columns ascending.
