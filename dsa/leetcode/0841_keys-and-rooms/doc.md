# Keys and Rooms

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 841 |
| Difficulty | Medium |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/keys-and-rooms/) |

## Problem Description
### Goal
There are `n` rooms labeled from `0` through `n - 1`. Every room except room `0` starts locked, and a locked room can be entered only after obtaining its key. Upon visiting a room, you may take all of the distinct numbered keys stored there; each key unlocks the room bearing that number.

The array `rooms` lists the keys found in every room. Starting from room `0` and retaining every collected key, return `true` if all rooms can eventually be visited, or `false` if at least one room remains unreachable.

### Function Contract
**Inputs**

- `rooms`: a list of $n$ key lists, where $2 \leq n \leq 1000$.
- `rooms[i]` contains distinct room labels from `0` through `n - 1`.
- Define the total number of stored keys as

$$
K = \sum_{i=0}^{n-1} \lvert \texttt{rooms}[i] \rvert,
$$

with $1 \leq K \leq 3000$.

**Return value**

Return whether every room is reachable by repeatedly entering unlocked rooms and collecting all keys inside them.

### Examples
**Example 1**

- Input: `rooms = [[1], [2], [3], []]`
- Output: `true`

Rooms can be visited in order `0`, `1`, `2`, `3`.

**Example 2**

- Input: `rooms = [[1, 3], [3, 0, 1], [2], [0]]`
- Output: `false`

The only key to room `2` is trapped inside room `2` itself.

**Example 3**

- Input: `rooms = [[1], []]`
- Output: `true`

### Required Complexity
- **Time:** $O(n+K)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

Interpret every key `j` stored in room `i` as a directed edge from `i` to `j`. The question becomes whether all graph vertices are reachable from vertex `0`.

Mark room `0` as seen and place it on a stack. Repeatedly remove one discovered room, inspect all of its keys, and add each previously unseen destination room to both the seen set and the stack. Marking at discovery time prevents cycles, self-keys, or keys repeated across different rooms from scheduling the same room more than once.

Every processed room is reachable because it was either room `0` or was unlocked by a key in an already reachable room. Conversely, whenever a reachable room is processed, all rooms directly unlockable from it are discovered. By induction along any key path from room `0`, the traversal finds every visitable room. Therefore all rooms can be visited exactly when the seen count reaches `n`.

#### Complexity detail

Each room is pushed and processed at most once, and every stored key is inspected once. The total time is $O(n+K)$. The seen structure and traversal stack contain at most $n$ room labels, giving $O(n)$ space.

#### Alternatives and edge cases

- **Breadth-first search:** A queue explores the same reachable set with identical $O(n+K)$ time and $O(n)$ space.
- **Repeatedly rescan all rooms:** Looking for newly unlocked but unprocessed rooms in full passes is correct, but a chain revealed in reverse index order can require $O(n)$ scans of $n$ rooms, for $O(n^2+K)$ time.
- **Self-key:** A room containing its own key does not make that room reachable if no already reachable room unlocks it.
- **Cycles:** Rooms may unlock one another; the seen check prevents endless traversal without treating a disconnected cycle as reachable.
- **Duplicate destination across rooms:** Keys are distinct only within one room, so several rooms may unlock the same destination; it is still visited once.
- **Keys to room zero:** Such keys add no new reachability because room `0` begins unlocked.

</details>
