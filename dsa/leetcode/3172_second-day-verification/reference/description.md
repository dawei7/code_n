## Description

The `emails` table records an email identifier, its user, and the datetime when that user signed up. The `texts` table records messages associated with email identifiers, whether each message reports a verified or unverified signup, and the datetime of that action.

Find the users who have a `Verified` text whose action date is the calendar day immediately after the corresponding signup date. A user should appear only once even if several qualifying records exist.

Return the qualifying `user_id` values in ascending order.
