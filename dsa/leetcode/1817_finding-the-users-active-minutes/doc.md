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
