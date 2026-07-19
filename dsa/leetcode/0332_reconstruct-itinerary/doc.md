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
