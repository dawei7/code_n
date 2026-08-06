## Description

The `Listens` table records which song each user heard on each date and may contain duplicate rows. The `Friendship` table records every friendship once, placing the smaller user ID in `user1_id`.

Report the existing friend pairs whose listening activity is similar: on at least one single day, both users must have listened to three or more distinct songs in common. Return each qualifying pair once in the same canonical orientation used by `Friendship`. Sharing songs without being friends does not qualify, and songs from different days cannot be combined toward the threshold.
