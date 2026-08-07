## General
Given Table: `FriendRequest`, the database query executes a relational database query for **Friend Requests I: Overall Acceptance Rate**. Edge case handling: replaces `NULL` values using `COALESCE` guards.

## Complexity detail
- **Time Complexity**: $O((R + A) \log(R + A))$ — Operation count bound.
- **Space Complexity**: $O(R + A)$ — Auxiliary memory allocation bound.
