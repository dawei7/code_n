# Get Watched Videos by Your Friends

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1311 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Breadth-First Search, Graph Theory, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/get-watched-videos-by-your-friends/) |

## Problem Description
### Goal
There are $n$ people with IDs from 0 through $n-1$. For each person, `watchedVideos[i]` lists the videos that person watched, and `friends[i]` lists that person's friends. Friendship is mutual.

Starting from person `id`, consider only people whose shortest friendship-path distance is exactly `level`. Count every video occurrence in those people's watched lists. Return the distinct video names ordered by increasing frequency among that exact-level group; when two videos have the same frequency, order them in ascending alphabetical order.

### Function Contract
**Inputs**

- `watched_videos`: $n$ nonempty video lists, one for each person.
- `friends`: an undirected adjacency list of the same length, with no out-of-range IDs.
- $2\le n\le100$; each person has between 1 and 100 watched videos.
- Every video name is a nonempty string of at most 8 characters.
- `id`: the starting person's ID, where $0\le\texttt{id}<n$.
- `level`: the required shortest-path distance, where $1\le\texttt{level}<n$.

Let $E$ be the number of friendship edges, $S$ the total number of video entries watched by people at the target level, and $V$ the number of distinct titles among those entries.

**Return value**

The $V$ distinct target-level video titles, sorted first by increasing occurrence count and then alphabetically.

### Examples
**Example 1**

- Input: `watchedVideos = [["A","B"],["C"],["B","C"],["D"]]`, `friends = [[1,2],[0,3],[0,3],[1,2]]`, `id = 0`, `level = 1`
- Output: `["B","C"]`
- Explanation: People 1 and 2 are exactly one step away. `B` occurs once and `C` occurs twice.

**Example 2**

- Input: the same graph, `id = 0`, `level = 2`
- Output: `["D"]`

**Example 3**

- Input: `watchedVideos = [["self"],["B","A"],["A"]]`, `friends = [[1,2],[0],[0]]`, `id = 0`, `level = 1`
- Output: `["B","A"]`
- Explanation: `B` occurs once and `A` occurs twice, so frequency takes priority over alphabetical order.

### Required Complexity
- **Time:** $O(n+E+S+Vlog V)$
- **Space:** $O(n+V)$

<details>
<summary>Approach</summary>

#### General

**Use breadth-first layers to enforce shortest distance**

Begin a queue with `id` and mark that person visited. Repeat exactly `level` breadth-first expansions. During one expansion, remove every person currently in the queue and append each unvisited friend, marking on enqueue. After $k$ expansions, the queue contains exactly the people whose shortest distance from `id` is $k$.

This layer property holds because breadth-first search discovers vertices in nondecreasing shortest-path distance. Marking a person at first discovery prevents a cycle or a second path from placing the same person into a later layer. Therefore, after the requested number of expansions, neither closer people nor people first reachable farther away remain in the queue.

**Count and order only the final layer**

Accumulate a frequency map from the watched lists of people still in the queue. Sort its distinct keys by the pair `(frequency, title)`. Tuple ordering applies the required increasing count first and the alphabetical tie-break only when counts match.

#### Complexity detail

Breadth-first search visits at most $n$ people and examines at most $2E$ adjacency entries, taking $O(n+E)$ time. Counting takes $O(S)$, and sorting $V$ names takes $O(V\log V)$, for $O(n+E+S+V\log V)$ total time. The visited set and queue use $O(n)$ space, while the frequency map and output use $O(V)$.

#### Alternatives and edge cases

- **Depth-labeled DFS:** Recording the shortest known distance can work, but plain DFS may reach a person first by a longer path and requires extra correction; BFS represents exact shortest-distance layers directly.
- **Repeated frequency scans:** Collecting all target videos and rescanning that list once per distinct title is correct but can take $O(SV)$ time.
- **Cycles and multiple paths:** Mark people when they are enqueued so each contributes only at their shortest distance and at most once.
- **Frequency before alphabet:** A lexicographically smaller title must still come later when it has a larger count.
- **Duplicate titles for one person:** Every list occurrence contributes to the frequency; the contract counts watched-video entries, not merely viewers.
- **No person at the requested level:** The queue becomes empty and the correct result is an empty list.
- **Starting person's videos:** They are never counted because the legal target level is at least 1.

</details>
