## Description

The `Contests` table records each contest's unique `contest_id` and the user IDs of its gold, silver, and bronze medalists. Contest IDs advance consecutively without skipped values. The `Users` table maps each unique `user_id` to a `name` and `mail`.

A user is an interview candidate when either of two independent rules holds: the user won any medal in at least three consecutive contests, or the user won gold in at least three different contests even when those contests are not consecutive. Report the `name` and `mail` of every qualifying user. A user satisfying both rules must still appear only once, and result order is unrestricted.
