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

### Required Complexity

- **Time:** $O(S^2\alpha(S))$
- **Space:** $O(n+Q)$

<details>
<summary>Approach</summary>

#### General

**Represent indirect friendship by components**

Maintain a disjoint-set union structure over the people. Its root for a person identifies that person's entire current friendship component. Path compression and union by size keep root queries amortized almost constant, and only accepted requests modify this structure.

**Test the only newly possible violation**

For a request `[u, v]`, first find component roots `u_root` and `v_root`. If they are equal, the request creates no new connectivity and is successful immediately. Otherwise, a hypothetical acceptance would merge exactly those two components. An existing restriction `[x, y]` becomes violated by that merge precisely when the current roots of `x` and `y` are `u_root` and `v_root` in either order.

Scan all restrictions for that cross-component pattern. If one appears, reject the request and leave the disjoint-set state untouched. If none appears, union the two request components and record success. The state was valid before the request, and no component other than these two changes, so this test excludes every and only possible new violation. Processing in input order therefore preserves all restrictions after every accepted request.

**Keep rejected requests nonpersistent**

The restriction scan reads the current roots but performs no speculative union. Consequently, rejection needs no rollback: only the final accepted branch changes a parent pointer. This also ensures that an unsuccessful request cannot influence a later answer.

#### Complexity detail

Initialization costs $O(n)$. Each of the $Q$ requests performs constant-many disjoint-set operations and, unless its endpoints are already connected, scans up to $R$ restrictions with two finds per pair. The tight total bound is $O(n+Q(R+1)\alpha(n))$, which is $O(S^2\alpha(S))$ for $S=\max(n,R,Q)$. Parent and size arrays use $O(n)$ space, and the required result uses $O(Q)$.

#### Alternatives and edge cases

- **Copy the disjoint set for each request:** Speculatively unioning on a full copy and then checking all restrictions is correct, but copying $O(n)$ state per request adds avoidable work and storage churn.
- **Rebuild connectivity for every restriction:** Replaying all accepted edges separately for each restriction can reach cubic time when requests and restrictions both scale.
- **Already connected endpoints:** The request is successful because it creates no new path, even if the same direct request appeared earlier.
- **Rejected request:** It adds no friendship and must not alter the outcome of future requests.
- **No restrictions:** Every request succeeds, including repetitions and requests within an existing component.
- **Restriction orientation:** `[x, y]` is symmetric, so both root orderings must be checked.

</details>
