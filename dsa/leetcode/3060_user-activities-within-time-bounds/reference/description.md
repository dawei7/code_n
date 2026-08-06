## Description

Each session belongs to a user and is classified as either `Viewer` or
`Streamer`. A user qualifies when two distinct sessions of the same type are
close enough in time; sessions of different types cannot form a qualifying
pair.

Find every user for whom a later session starts no more than twelve hours after
an earlier same-type session ends. The two sessions need not be adjacent in the
table or in the user's complete mixed-type history. The twelve-hour boundary
is inclusive. Return each qualifying user once, ordered by `user_id` ascending.
