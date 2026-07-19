# Friend Requests I: Overall Acceptance Rate

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 597 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/friend-requests-i-overall-acceptance-rate/) |

## Problem Description
### Goal
Given tables of sent friend requests and accepted friend requests, compute the overall acceptance rate. Count distinct directed `(sender, recipient)` pairs in `FriendRequest` and distinct directed `(requester, accepter)` pairs in `RequestAccepted`, because the same pair may appear on more than one date.

Divide the number of distinct accepted pairs by the number of distinct requested pairs and return the value as `accept_rate`, rounded to two decimal places. When there are no friend requests, return `0.00` rather than dividing by zero. The calculation is one overall rate, not a separate rate per user or date.

### Function Contract
**Inputs**

- `FriendRequest(sender_id, send_to_id, request_date)`: friend-request events
- `RequestAccepted(requester_id, accepter_id, accept_date)`: acceptance events

**Return value**

- A one-row result grid with column `accept_rate`
- Count each directed user pair once in each table even if it appears on several dates
- Return zero when there are no distinct requests

### Examples
**Example 1**

- Input: four distinct requested pairs and two distinct accepted pairs
- Output: `0.5`

**Example 2**

- Input: the same pair is requested on several dates and accepted once
- Output: `1.0`

**Example 3**

- Input: three distinct requests and two accepted pairs
- Output: `0.67`
