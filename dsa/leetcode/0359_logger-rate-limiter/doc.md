# Logger Rate Limiter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 359 |
| Difficulty | Easy |
| Topics | Hash Table, Design, Data Stream |
| Official Link | [LeetCode](https://leetcode.com/problems/logger-rate-limiter/) |

## Problem Description
### Goal
Design a logger that receives chronological calls `shouldPrintMessage(timestamp, message)`. A message may be printed when it has never been printed before or when at least ten seconds have elapsed since its most recent permitted print.

Return `True` for a permitted occurrence and record that timestamp. Return `False` for an occurrence arriving sooner, and do not let a rejected call restart or extend the waiting interval. Rate limits are tracked independently by exact message text, so different messages do not block one another. Process every call against persistent state and return one boolean per operation.

### Function Contract
**Inputs**

- `operations`: for the app adapter, a chronological list of `["shouldPrintMessage", timestamp, message]` operations

**Return value**

- A Boolean result for every operation, where `True` means the message should be printed. Native LeetCode calls `Logger.shouldPrintMessage(timestamp, message)` directly.

### Examples
**Example 1**

- Input: `operations = [["shouldPrintMessage",1,"foo"],["shouldPrintMessage",2,"bar"],["shouldPrintMessage",3,"foo"],["shouldPrintMessage",8,"bar"],["shouldPrintMessage",10,"foo"],["shouldPrintMessage",11,"foo"]]`
- Output: `[True,True,False,False,False,True]`

**Example 2**

- Input: `operations = [["shouldPrintMessage",1,"notice"],["shouldPrintMessage",11,"notice"]]`
- Output: `[True,True]`

**Example 3**

- Input: `operations = [["shouldPrintMessage",5,"a"],["shouldPrintMessage",5,"b"],["shouldPrintMessage",5,"a"]]`
- Output: `[True,True,False]`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(m)$

<details>
<summary>Approach</summary>

#### General

**Store the next legal timestamp, not every event**

For each message text, a hash table records the earliest timestamp at which that message may be printed again. A message absent from the table has never been accepted, so it can be printed immediately. If it is present, compare the current timestamp with the stored threshold.

**Update state only after an accepted print**

When `timestamp >= next_allowed[message]`, accept the message and set its next legal timestamp to `timestamp + 10`. When the comparison fails, return `False` without changing the table. This distinction matters: repeated rejected arrivals must not keep extending the rate-limit window.

**Why the threshold represents the full history**

After an accepted occurrence at time `t`, the contract rejects exactly the timestamps below $t + 10$ and accepts $t + 10$ itself. The stored threshold captures that entire condition in one number. Since input timestamps arrive chronologically, no earlier event needs to be revisited; induction over the stream shows that every decision matches the most recent accepted occurrence of that message.

#### Complexity detail

Each operation performs one expected constant-time hash lookup and, only when accepted, one update, so its expected time is $O(1)$. If `m` distinct messages have appeared, the table uses $O(m)$ space. The app adapter's returned list additionally uses one Boolean per operation.

#### Alternatives and edge cases

- **Scan accepted log history:** can find the latest matching message but grows to $O(n)$ work per event and $O(n^2)$ over a stream.
- **Queue plus hash table with eviction:** can remove expired messages and bound memory to the active ten-second window, at the cost of maintaining synchronized queue entries.
- **Store the last accepted timestamp:** is equally valid; the comparison becomes `timestamp - last_printed >= 10`.
- A message at exactly ten seconds after its last accepted occurrence is allowed.
- Different message strings have independent rate limits, even at the same timestamp.
- A rejected occurrence must not modify the next legal timestamp.
- Chronological timestamps allow the state to summarize the past without rollback handling.

</details>
