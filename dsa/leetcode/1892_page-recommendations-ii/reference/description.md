## Description

`Friendship` stores pairs of users who are friends, and each friendship applies in both directions even though it is recorded as one row. `Likes` records which pages each user likes. Both tables use their two columns as composite primary keys, so a friendship pair or user-page like is not duplicated.

For every user participating in the friendship graph, recommend each page liked by at least one of that user's friends but not already liked by the user. Return one row per recommended user-page pair and count how many of the user's friends like that page as `friends_likes`. Result rows may appear in any order.
