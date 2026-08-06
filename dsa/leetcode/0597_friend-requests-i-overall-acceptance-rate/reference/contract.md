## Function Contract

**Inputs**

`FriendRequest(sender_id, send_to_id, request_date)` stores request events. `RequestAccepted(requester_id, accepter_id, accept_date)` stores acceptance events.

Let $R$ and $A$ be the respective event-row counts. Dates do not distinguish the directed user pairs counted in the ratio.

**Return value**

Return a one-row table with `accept_rate` equal to the distinct acceptance-pair count divided by the distinct request-pair count, rounded to two decimals. Return `0.00` when there are no requests.
