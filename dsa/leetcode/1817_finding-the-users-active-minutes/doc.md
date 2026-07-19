# Finding the Users Active Minutes

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/finding-the-users-active-minutes/) |
| Frontend ID | 1817 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

The array `logs` records user actions. Each entry `[user_id, minute]` means that the identified user performed an action during that minute. Different users may act simultaneously, and the same user may generate several log entries during one minute.

A user's user active minutes (UAM) is the number of distinct minutes in which that user acted. Repeated actions by that user during the same minute contribute only once. Given `k`, construct an array of length `k` whose position $j-1$ contains the number of users with UAM exactly $j$, for every $1 \le j \le k$. Return this distribution; positions with no matching users contain zero.

### Function Contract

**Inputs**

- `logs`: between 1 and $10^4$ pairs `[user_id, minute]`, where $0 \le \textit{user_id} \le 10^9$ and $1 \le \textit{minute} \le 10^5$.
- `k`: an integer between the maximum UAM of any recorded user and $10^5$.
- Let $n = \lvert\texttt{logs}\rvert$.

**Return value**

- Return a length-`k` integer array where index $j-1$ counts users with exactly $j$ distinct active minutes.

### Examples

**Example 1**

- Input: `logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5`
- Output: `[0,2,0,0,0]`

User 0 is active in minutes 2 and 5; the repeated action at minute 5 does not add another minute. User 1 is active in minutes 2 and 3. Both therefore contribute to UAM 2.

**Example 2**

- Input: `logs = [[1,1],[2,2],[2,3]], k = 4`
- Output: `[1,1,0,0]`

User 1 contributes to UAM 1, while user 2 contributes to UAM 2.

### Required Complexity

- **Time:** $O(n + k)$
- **Space:** $O(n + k)$

<details>
<summary>Approach</summary>

#### General

**Deduplicate minutes separately for every user**

Maintain a hash map from each user ID to a set of minutes. For every `[user_id, minute]` log, insert the minute into that user's set. Set insertion naturally collapses repeated actions in the same minute, while the outer map keeps equal minute values belonging to different users independent.

**Convert per-user sets into the requested distribution**

Create `answer` with `k` zeros. For each set in the map, its size is that user's UAM. A UAM of $j$ belongs at zero-based index $j-1$, so increment that position once. The constraint on `k` guarantees every observed set size has a valid position.

**Why each user is counted once in the correct bucket**

After processing all logs, a user's set contains a minute exactly when at least one of that user's actions occurred then. Its cardinality is therefore precisely the defined UAM, regardless of duplicate log rows. The second pass visits each recorded user once and increments only the bucket corresponding to that cardinality, yielding the required count for every UAM value.

#### Complexity detail

Across all users, at most $n$ distinct `(user, minute)` associations are stored. Expected hash insertion time over all logs is $O(n)$, iterating the user sets' cardinalities is $O(n)$ in the worst case, and initializing the result costs $O(k)$. Total time and output-inclusive space are $O(n+k)$.

#### Alternatives and edge cases

- **Rescan all logs for each user:** It can reconstruct every user's minute set correctly, but may revisit all $n$ entries for each of $\Theta(n)$ users and take $O(n^2)$ time.
- **Store minutes in lists:** Avoiding duplicates with linear list membership checks can also degrade to $O(n^2)$ when one user has many distinct minutes.
- **Duplicate log entries:** Multiple identical `[user_id, minute]` rows still contribute one active minute.
- **Shared minute across users:** Each user counts that minute independently because UAM is defined per user.
- **Sparse distribution:** Most of the `k` buckets may be zero, but the returned array must still have exactly `k` positions.
- **Large user IDs:** IDs are map keys rather than array indices, so values near $10^9$ require no oversized allocation.
- **UAM equal to `k`:** Increment the final array position, index `k - 1`.

</details>
