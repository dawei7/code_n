# Online Election

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 911 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Design |
| Official Link | [LeetCode](https://leetcode.com/problems/online-election/) |

## Problem Description
### Goal
Two parallel arrays describe an election. The vote at index `i` was cast for candidate `persons[i]` at time `times[i]`, and the vote times are strictly increasing.

Design `TopVotedCandidate` so that `q(t)` returns the candidate leading after every vote cast at or before time `t` has been counted. A vote cast exactly at `t` is included. When several candidates are tied for the greatest vote total, the candidate who received the most recent vote among those tied candidates is considered the leader.

The constructor receives the complete vote history, and many query times may arrive afterward.

### Function Contract
Let $v=\lvert\texttt{persons}\rvert$ be the number of votes and $r=\lvert\texttt{queries}\rvert$ be the number of app-local queries.

**Inputs**

- `persons`: an integer array of length $v$, where $1 \leq v \leq 5000$ and $0 \leq \texttt{persons}[i] < v$.
- `times`: a strictly increasing integer array of length $v$, where $0 \leq \texttt{times}[i] \leq 10^9$.
- `queries`: query times in the range $\texttt{times}[0] \leq t \leq 10^9$. At most $10^4$ calls are made to `q`.

**Return value**

The native class returns one leader from each `q(t)` call. The app-local `solve` adapter returns the leaders for `queries` in the same order.

### Examples
**Example 1**

- Input: `persons = [0,1,1,0,0,1,0], times = [0,5,10,15,20,25,30], queries = [3,12,25,15,24,8]`
- Output: `[0,1,1,0,0,1]`

At time $25$, candidates $0$ and $1$ each have three votes, and candidate $1$ wins the tie because the vote at time $25$ is the most recent tied vote.

**Example 2**

- Input: `persons = [0], times = [5], queries = [5,100]`
- Output: `[0,0]`

**Example 3**

- Input: `persons = [0,1,0,1], times = [1,2,3,4], queries = [1,2,3,4]`
- Output: `[0,1,0,1]`

Each new vote creates a tie and makes its recipient the current leader.
