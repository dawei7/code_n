# Bus Routes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 815 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/bus-routes/) |

## Problem Description

### Goal

You are given several bus routes. Route `i` repeatedly cycles through every stop in `routes[i]`, so after boarding that bus at any one of its stops, a passenger may ride to any other stop listed on the same route. A transfer is possible wherever two routes share a stop.

The trip begins at `source` while the passenger is not on a bus and ends upon reaching `target`. Determine the fewest buses that must be boarded; the number of intermediate stops traveled does not affect this cost. If the endpoints are identical, no bus is needed. If the route network cannot connect distinct endpoints, return `-1`.

### Function Contract

**Inputs**

- `routes`: a list in which `routes[i]` contains the distinct stops served by bus route `i`.
- `source`: the stop where the trip begins.
- `target`: the destination stop.

**Return value**

- The minimum number of buses that must be boarded, or `-1` when the destination is unreachable.

### Examples

**Example 1**

- Input: `routes = [[1,2,7],[3,6,7]], source = 1, target = 6`
- Output: `2`
- Explanation: Take the first route to stop `7`, then transfer to the second route.

**Example 2**

- Input: `routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12`
- Output: `-1`
- Explanation: The routes containing `15` and those containing `12` lie in disconnected groups.

**Example 3**

- Input: `routes = [[5,8,11]], source = 8, target = 8`
- Output: `0`
- Explanation: No bus is needed when the trip already starts at its destination.
