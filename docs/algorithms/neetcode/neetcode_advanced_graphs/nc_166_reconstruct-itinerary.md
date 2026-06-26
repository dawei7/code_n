## Problem Description & Examples
### Goal
You are given a list of airline tickets where `tickets[i] = [from_i, to_i]` represent the departure and arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from `"JFK"`. Thus, the itinerary must begin with `"JFK"`. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

### Function Contract
**Inputs**

- `tickets`: List[List[str]]

**Return value**

List[str] - itinerary sequence

### Examples
**Example 1**

- Input: `tickets = [["JFK", "SFO"], ["SFO", "JFK"]]`
- Output: `["JFK", "SFO", "JFK"]`

**Example 2**

- Input: `tickets = [['JFK', 'ORD'], ['ORD', 'ATL']]`
- Output: `['JFK', 'ORD', 'ATL']`

**Example 3**

- Input: `tickets = [['JFK', 'LAX'], ['LAX', 'JFK']]`
- Output: `['JFK', 'LAX', 'JFK']`

---

## Underlying Base Algorithm(s)
- [Dijkstra shortest path](graph_04_dijkstra.md)
- [Kruskal minimum spanning tree](graph_08_kruskal-s-mst.md)
- [Prim minimum spanning tree](graph_10_prim-s-mst.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
