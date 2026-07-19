## General
**Store the next legal timestamp, not every event**

For each message text, a hash table records the earliest timestamp at which that message may be printed again. A message absent from the table has never been accepted, so it can be printed immediately. If it is present, compare the current timestamp with the stored threshold.

**Update state only after an accepted print**

When `timestamp >= next_allowed[message]`, accept the message and set its next legal timestamp to `timestamp + 10`. When the comparison fails, return `False` without changing the table. This distinction matters: repeated rejected arrivals must not keep extending the rate-limit window.

**Why the threshold represents the full history**

After an accepted occurrence at time `t`, the contract rejects exactly the timestamps below $t + 10$ and accepts $t + 10$ itself. The stored threshold captures that entire condition in one number. Since input timestamps arrive chronologically, no earlier event needs to be revisited; induction over the stream shows that every decision matches the most recent accepted occurrence of that message.

## Complexity detail
Each operation performs one expected constant-time hash lookup and, only when accepted, one update, so its expected time is $O(1)$. If `m` distinct messages have appeared, the table uses $O(m)$ space. The app adapter's returned list additionally uses one Boolean per operation.

## Alternatives and edge cases
- **Scan accepted log history:** can find the latest matching message but grows to $O(n)$ work per event and $O(n^2)$ over a stream.
- **Queue plus hash table with eviction:** can remove expired messages and bound memory to the active ten-second window, at the cost of maintaining synchronized queue entries.
- **Store the last accepted timestamp:** is equally valid; the comparison becomes `timestamp - last_printed >= 10`.
- A message at exactly ten seconds after its last accepted occurrence is allowed.
- Different message strings have independent rate limits, even at the same timestamp.
- A rejected occurrence must not modify the next legal timestamp.
- Chronological timestamps allow the state to summarize the past without rollback handling.
