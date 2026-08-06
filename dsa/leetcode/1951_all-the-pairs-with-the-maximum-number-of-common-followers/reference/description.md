## Description

The `Relations` table records directed following relationships: `follower_id`
follows `user_id`. For every pair of different users, their common followers
are follower IDs that have a row for both users.

Find the greatest common-follower count attained by any user pair, then return
every pair attaining that maximum. A pair must appear once in canonical order,
with its smaller user ID first. If several pairs tie for the greatest count,
all of them belong in the result.
