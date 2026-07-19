# Process Restricted Friend Requests

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2076 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Union-Find, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/process-restricted-friend-requests/) |

## Problem Description

### Goal

A network contains `n` people labeled from $0$ through $n-1$. Every pair in `restrictions` identifies two people who must never belong to the same friendship component: they may be neither direct friends nor connected indirectly through other friendships. Initially, every person is isolated.

Process the given friend requests in order. Accepting a request permanently adds a direct friendship between its two people, so it can affect every later decision. A request succeeds exactly when adding that edge would preserve every restriction; a request between people who are already directly or indirectly connected is still successful. Return one Boolean decision for each request.

### Function Contract

**Inputs**

- `n`: the number of people, where $2 \le n \le 1000$.
- `restrictions`: a list of $R$ pairs `[x, y]`, where $0 \le R \le 1000$, both labels lie in `[0, n - 1]`, and `x != y`.
- `requests`: a list of $Q$ pairs `[u, v]`, where $1 \le Q \le 1000$, both labels lie in `[0, n - 1]`, and `u != v`.
- For the complexity bounds, let $S=\max(n,R,Q)$ and let $\alpha$ denote the inverse Ackermann function.

**Return value**

- Return a list of $Q$ Booleans whose entry at index $j$ is `true` exactly when request $j$ is accepted.

### Examples

**Example 1**

- Input: `n = 3, restrictions = [[0,1]], requests = [[0,2],[2,1]]`
- Output: `[true,false]`
- Explanation: Joining 0 with 2 is safe, but then joining 2 with 1 would indirectly connect the restricted pair 0 and 1.

**Example 2**

- Input: `n = 3, restrictions = [[0,1]], requests = [[1,2],[0,2]]`
- Output: `[true,false]`
- Explanation: The first request forms component `{1,2}`; merging person 0 into it would violate `[0,1]`.

**Example 3**

- Input: `n = 5, restrictions = [[0,1],[1,2],[2,3]], requests = [[0,4],[1,2],[3,1],[3,4]]`
- Output: `[true,false,true,false]`
- Explanation: The first and third requests are compatible. The second is directly restricted, and the final merge would connect restricted people 0 and 1 through the accumulated friendships.
