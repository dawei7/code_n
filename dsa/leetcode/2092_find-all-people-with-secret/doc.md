# Find All People With Secret

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2092 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Union-Find, Graph Theory, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/find-all-people-with-secret/) |

## Problem Description

### Goal

There are $n$ people numbered from `0` through `n - 1`. Each meeting `[x, y, time]` connects people `x` and `y` at that time, and a person may participate in several simultaneous meetings. Person `0` knows a secret and shares it with `firstPerson` at time `0`.

Whenever a meeting occurs, either participant who already knows the secret shares it with the other. Sharing is instantaneous: someone may learn the secret in one meeting and pass it through another meeting at the same time. Process all meetings according to time and return every person who eventually knows the secret, in any order.

### Function Contract

**Inputs**

- `n`: the number of people, where $2 \le n \le 10^5$.
- `meetings`: $M$ triples `[x, y, time]`, where $1 \le M \le 10^5$.
- Each meeting joins two different valid people at a time from $1$ through $10^5$.
- `firstPerson`: a person from `1` through `n - 1` who learns the secret at time `0`.

**Return value**

Return all people who know the secret after every meeting. The order of the returned identifiers does not matter.

### Examples

**Example 1**

- Input: `n = 6`, `meetings = [[1,2,5],[2,3,8],[1,5,10]]`, `firstPerson = 1`
- Output: `[0,1,2,3,5]`
- Explanation: Knowledge passes from `1` to `2`, later to `3`, and from `1` to `5`.

**Example 2**

- Input: `n = 4`, `meetings = [[3,1,3],[1,2,2],[0,3,3]]`, `firstPerson = 3`
- Output: `[0,1,3]`
- Explanation: The time-`2` meeting cannot transmit retroactively. At time `3`, people `0`, `3`, and `1` are connected.

**Example 3**

- Input: `n = 5`, `meetings = [[3,4,2],[1,2,1],[2,3,1]]`, `firstPerson = 1`
- Output: `[0,1,2,3,4]`
- Explanation: At time `1`, person `2` learns and immediately passes the secret to `3`.

### Required Complexity

- **Time:** $O(M \log M + n)$
- **Space:** $O(M+n)$

<details>
<summary>Approach</summary>

#### General

**Why meetings must be grouped by time**

Chronological ordering prevents a later secret from affecting an earlier meeting. Within one timestamp, however, input order has no meaning because sharing is instantaneous. All meetings at that time form an undirected temporary graph, and the secret reaches an entire connected component if any person in that component knew it before or during that timestamp.

**Finding every informed component in a batch**

Sort meetings by time and build an adjacency list for one equal-time group. Initialize a breadth-first search with the group's participants who are already in the global `informed` set. Traversal reaches exactly the temporary components seeded with the secret. Add all reached people to `informed`, discard the temporary graph, and continue to the next timestamp.

**Why temporary connectivity must not persist**

Two people who met without either knowing the secret do not remain connected for future transmission. Discarding each batch graph enforces this: only knowledge persists between timestamps. Conversely, breadth-first closure inside the batch permits an arbitrary same-time chain to transmit immediately, as required.

Every person added by the traversal is connected through meetings at the current time to someone who knew the secret, so the addition is valid. Every valid transmission chain at that time lies in such a component and is traversed, so no eligible person is missed.

#### Complexity detail

Sorting $M$ meetings costs $O(M \log M)$. Each meeting contributes two temporary adjacency entries and is traversed only within its own batch, for another $O(M)$ work. Producing or maintaining the informed set costs up to $O(n)$. The total is $O(M \log M+n)$ time and $O(M+n)$ space in the largest batch.

#### Alternatives and edge cases

- **Union-find with batch reset:** Union all participants at one time, keep components connected to person `0`, and reset the others; this matches the same temporal rule but requires careful rollback or parent restoration.
- **Earliest-time priority queue:** Treat each meeting as an edge usable only at or after its timestamp and compute earliest knowledge times, giving another $O(M \log n)$ approach.
- **Single pass in input order:** This can miss a same-time chain when its meetings appear in an unfavorable order.
- **Permanent union-find:** Keeping every historical meeting edge incorrectly allows a future secret to travel through an earlier uninformed meeting.
- People `0` and `firstPerson` always belong to the answer even if they attend no meetings.
- A meeting before either participant learns the secret is never revisited.
- The answer is a set semantically, so its returned order is irrelevant.

</details>
