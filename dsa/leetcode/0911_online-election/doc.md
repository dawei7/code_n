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

### Required Complexity
- **Time:** $O(v+r\log v)$
- **Space:** $O(v)$

<details>
<summary>Approach</summary>

#### General

**Record the leader after every vote**

Process the vote history once in chronological order. Maintain each candidate's current count, the current leader, and that leader's count. After incrementing the new recipient's count, replace the leader whenever the recipient's total is greater than or equal to the current leading total. The equality is essential: the current vote is the most recent vote among tied candidates, so its recipient wins the tie.

Append the resulting leader to `leaders` at the same index as the vote time. After preprocessing, `leaders[i]` is exactly the election leader immediately after the vote at `times[i]`. This follows inductively: the count map contains all votes through that index, and the greater-than-or-equal update applies both the maximum-count rule and the recency tie rule.

**Locate the latest counted vote**

For `q(t)`, binary-search `times` for the insertion position to the right of `t`. Subtract one to obtain the last vote index whose time is at most `t`, then return the leader stored at that index. The query constraint guarantees that at least the first vote has occurred.

The binary search includes a vote cast exactly at `t` because it uses the right insertion boundary. Every earlier vote was summarized during preprocessing, and no later vote is included, so the returned candidate is precisely the required leader. The app-local adapter constructs the class once and applies this query method to every requested time.

#### Complexity detail

Preprocessing all $v$ votes takes $O(v)$ expected time for hash-table updates. Each of the $r$ queries performs an $O(\log v)$ binary search, giving $O(v+r\log v)$ total time. The counts, leader history, and copied time reference use $O(v)$ space.

#### Alternatives and edge cases

- **Rescan votes for every query:** Recounting the prefix through `t` is correct but takes $O(v)$ time per query and $O(vr)$ over a long trace.
- **Sort queries offline:** Processing queries chronologically with the votes can run in $O(v+r\log r)$ time, but it must restore the original query order and does not implement independent online calls as directly.
- **Store only leader-change times:** Compressing consecutive equal leaders can save space on some histories while retaining binary search, but the full per-vote array is simpler and remains $O(v)$.
- **Exact vote time:** Use a right-boundary binary search so the vote at `t` counts.
- **Time between votes:** Return the leader after the latest earlier vote; no state changes in the gap.
- **Repeated ties:** The greater-than-or-equal update makes every newest vote recipient win whenever it reaches the leading count.
- **Nonconsecutive candidate numbers:** A hash table tracks only candidates that actually receive votes.
- **Queries out of order:** Each binary search is independent, so query order does not affect any answer.

</details>
