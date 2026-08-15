# Minimum Levels to Gain More Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3096 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-levels-to-gain-more-points/) |

## Problem Description

### Goal

Alice and Bob play a game containing $n$ levels, described in their fixed order by the binary array `possible`. A level with value `1` can always be cleared, while a level with value `0` is impossible for either player to clear. Clearing a level awards one point; failing an impossible level loses one point.

Alice plays a non-empty prefix of the levels beginning at index zero. Bob then plays every remaining level, also receiving at least one level. Both players maximize the score available from their assigned levels. Find the minimum number of levels Alice must play so that her score is **strictly greater** than Bob's score. Return `-1` if no valid split gives Alice a strict lead.

### Function Contract

**Inputs**

- `possible`: A binary list of length $n$, where $2 \le n \le 10^5$ and every value is either `0` or `1`.

The split preserves the given order. Alice receives indices $0$ through $i-1$ and Bob receives indices $i$ through $n-1$ for some $1 \le i < n$.

Each `1` contributes $+1$ to its player's score, and each `0` contributes $-1$.

**Return value**

Return the smallest valid prefix length for which Alice's score is greater than Bob's. Return `-1` if no such prefix exists.

### Examples

#### Example 1

- **Input:** `possible = [1, 0, 1, 0]`
- **Output:** `1`
- **Explanation:** Alice scores `1` on the first level, while Bob scores `-1 + 1 - 1 = -1` on the remaining levels.

#### Example 2

- **Input:** `possible = [1, 1, 1, 1, 1]`
- **Output:** `3`
- **Explanation:** With three levels Alice scores `3` and Bob scores `2`; shorter valid prefixes do not give Alice a strict lead.

#### Example 3

- **Input:** `possible = [0, 0]`
- **Output:** `-1`
- **Explanation:** Each player must take one level and scores `-1`, so Alice does not score strictly more.
