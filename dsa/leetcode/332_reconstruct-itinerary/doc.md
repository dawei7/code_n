# Reconstruct Itinerary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 332 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Depth-First Search, Graph Theory, Sorting, Heap (Priority Queue), Eulerian Circuit |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reconstruct-itinerary/) |

## Problem Description
### Goal
Each airline ticket is a directed flight `[departure, arrival]`. Starting at `"JFK"`, construct an itinerary in which consecutive airport codes follow tickets and every supplied ticket occurrence is used exactly once. Duplicate ticket pairs represent separate flights and must each be consumed.

At least one valid itinerary is guaranteed to exist. When several complete routes are possible, return the lexicographically smallest airport sequence, comparing codes at the earliest differing position. The result therefore contains `len(tickets) + 1` airport codes. Do not stop after using only a reachable subset or choose a locally small flight that prevents all remaining tickets from being used.

### Function Contract
**Inputs**

- `tickets`: directed pairs `[departure, arrival]`

**Return value**

An airport sequence of length `len(tickets) + 1` describing the smallest valid complete itinerary from `JFK`.

### Examples
**Example 1**

- Input: `tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]`
- Output: `["JFK","MUC","LHR","SFO","SJC"]`

**Example 2**

- Input: `tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]`
- Output: `["JFK","ATL","JFK","SFO","ATL","SFO"]`

**Example 3**

- Input: `tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]`
- Output: `["JFK","NRT","JFK","KUL"]`

### Required Complexity

- **Time:** $O(E \log E)$
- **Space:** $O(E)$

<details>
<summary>Approach</summary>

#### General

**Tickets are edges of an Eulerian trail**

Every ticket must be used once, so the itinerary is an Eulerian trail in a directed multigraph, fixed to start at `JFK`. A simple greedy walk that permanently chooses the smallest next airport is unsafe: in the third example, choosing `KUL` immediately reaches a dead end and strands two tickets.

Hierholzer's algorithm postpones committing airports to the final route. Walk through unused edges while possible. Only when the current airport has no outgoing ticket left is it appended to the route; then backtrack to the previous airport. Reversing this dead-end order produces the complete Eulerian itinerary.

**Consume lexical choices cheaply**

Build one destination list per departure and sort each list in reverse lexical order. The smallest available destination is then at the end and can be removed in constant time. Keep an explicit stack beginning with `JFK`: if its top has an unused destination, push that destination; otherwise pop the airport into the reversed route.

Duplicate edges appear as duplicate list entries, so each ticket is naturally consumed once. An iterative stack also avoids recursion-depth failures on long itineraries.

**Postorder placement resolves necessary dead ends**

When an airport is appended, all tickets reachable from its current walk position have already been consumed, so that airport must be the end of the remaining Eulerian segment. Backtracking splices completed cycles and terminal segments into the correct trail, and every edge removal contributes exactly one transition to the final reversed route.

Choosing the smallest available edge whenever a walk advances gives the smallest lexical choice that can occupy the earliest still-unfixed route position. Edges that lead to terminal segments are placed correctly during reversal rather than invalidating the walk. Therefore Hierholzer's construction uses all tickets and produces the lexicographically smallest complete itinerary.

#### Complexity detail

Let `E` be the number of tickets. Sorting all adjacency lists costs at most $O(E \log E)$. Every edge is popped once and every airport occurrence is pushed and popped once, so traversal is $O(E)$. Adjacency lists, stack, and route use $O(E)$ space.

#### Alternatives and edge cases

- **Backtrack over unused tickets:** is correct but may scan or explore a combinatorial number of ticket choices.
- **Always append the smallest next destination directly to the answer:** can get trapped before all tickets are used.
- **Use a min-heap per departure:** gives the same $O(E \log E)$ bound without reverse sorting.
- Duplicate tickets must remain separate. A one-ticket input returns two airports, and lexical comparison applies to whole airport codes.

</details>
