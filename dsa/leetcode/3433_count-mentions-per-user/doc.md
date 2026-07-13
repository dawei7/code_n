# Count Mentions Per User

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3433 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Sorting, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-mentions-per-user](https://leetcode.com/problems/count-mentions-per-user/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-mentions-per-user/).

### Goal
Given a number of users and a list of events (either "MESSAGE" or "OFFLINE"), track how many mentions each user receives. A "MESSAGE" can target specific user IDs, "ALL" users, or "HERE" (users currently online). Users go offline for a specified duration and become available again at a specific timestamp. We need to return an array representing the total mention count for each user ID from 0 to `numberOfUsers - 1`.

### Function Contract
**Inputs**

- `numberOfUsers` (int): The total number of users in the system.
- `events` (List[List[str]]): A list of events where each event is `["MESSAGE", timestamp, target]` or `["OFFLINE", timestamp, id]`.

**Return value**

- `List[int]`: An array of size `numberOfUsers` where the $i$-th element is the total number of mentions received by user $i$.

### Examples
**Example 1**

- Input: `numberOfUsers = 2, events = [["MESSAGE", "10", "id0"], ["OFFLINE", "11", "0"], ["MESSAGE", "12", "HERE"]]`
- Output: `[1, 1]`

**Example 2**

- Input: `numberOfUsers = 2, events = [["MESSAGE", "10", "id0"], ["OFFLINE", "11", "0"], ["MESSAGE", "12", "ALL"]]`
- Output: `[1, 2]`

**Example 3**

- Input: `numberOfUsers = 2, events = [["MESSAGE", "10", "id0"], ["OFFLINE", "11", "0"], ["MESSAGE", "12", "id0"]]`
- Output: `[2, 0]`

---

## Solution
### Approach
The problem is solved using a simulation approach. We maintain an `offline_until` array to track when each user becomes available again. Events are processed chronologically by sorting them by timestamp (and prioritizing "MESSAGE" over "OFFLINE" if timestamps are equal). We use string parsing to identify target types ("ALL", "HERE", or specific "idX") and update the mention counts accordingly.

### Complexity Analysis
- **Time Complexity**: $O(N \log N + M)$, where $N$ is the number of events (due to sorting) and $M$ is the number of users (for iterating through users during "HERE" or "ALL" mentions).
- **Space Complexity**: $O(N + M)$ to store the events and the status/mention counts for each user.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(numberOfUsers, events):
    ordered = sorted(events, key=lambda event: (int(event[1]), 0 if event[0] == "OFFLINE" else 1))
    mentions = [0] * numberOfUsers
    offline_until = [0] * numberOfUsers

    for event_type, timestamp_text, payload in ordered:
        timestamp = int(timestamp_text)
        if event_type == "OFFLINE":
            offline_until[int(payload)] = timestamp + 60
            continue

        if payload == "ALL":
            for user in range(numberOfUsers):
                mentions[user] += 1
        elif payload == "HERE":
            for user in range(numberOfUsers):
                if offline_until[user] <= timestamp:
                    mentions[user] += 1
        else:
            for token in payload.split():
                mentions[int(token[2:])] += 1

    return mentions
```
</details>
