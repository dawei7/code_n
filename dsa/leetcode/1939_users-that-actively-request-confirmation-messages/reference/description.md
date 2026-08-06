## Description

The `Signups` table records registered users. The `Confirmations` table records
each confirmation-message request, including its user, request timestamp, and
whether the request was confirmed or timed out.

Find every user who made at least two confirmation requests no more than 24
hours apart. A separation of exactly 24 hours qualifies. The request actions
do not affect eligibility; only timestamps belonging to the same user matter.
Return the qualifying user IDs in any order.
