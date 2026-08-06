## Description

The `Genders` table contains one row per user. Its `gender` value is one of `female`, `male`, or `other`, and the table contains the same number of users in all three groups.

Rearrange every row into repeating groups ordered as `female`, then `other`, then `male`. Within each gender, users must appear by ascending `user_id`. Return both original columns in exactly this interleaved order; the sequence of output rows is part of the required result.
