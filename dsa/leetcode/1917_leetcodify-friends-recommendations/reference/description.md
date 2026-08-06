## Description

The `Listens` table records songs heard by users on particular dates and may contain duplicate rows. The `Friendship` table stores existing undirected friendships once, with the smaller user ID in `user1_id`.

Two users qualify for a recommendation when they are not already friends and, on at least one single day, both listened to at least three distinct common songs. Return both recommendation directions for every qualifying unordered pair: if users `x` and `y` qualify, emit `(x,y)` and `(y,x)`. Each directed pair must appear only once even if the users qualify on multiple days.
