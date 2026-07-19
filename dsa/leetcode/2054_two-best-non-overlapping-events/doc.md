# Two Best Non-Overlapping Events

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2054 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/two-best-non-overlapping-events/) |

## Problem Description

### Goal

Each entry `[start, end, value]` describes an event available throughout an inclusive time interval and the value gained by attending it. Choose no more than two events and maximize their combined value.

Chosen events must not overlap. Because endpoints are inclusive, an event beginning at the exact time another ends is incompatible; after an event ending at time $t$, a second event must start at least at $t+1$. Attending only one event is allowed when it is better than every compatible pair.

### Function Contract

**Inputs**

- `events`: an array of $n$ triples `[start, end, value]`, where $2 \le n \le 10^5$, $1 \le start \le end \le 10^9$, and $1 \le value \le 10^6$.

**Return value**

- Return the maximum total value obtainable from at most two pairwise non-overlapping events.

### Examples

**Example 1**

- Input: `events = [[1,3,2],[4,5,2],[2,4,3]]`
- Output: `4`
- Explanation: The first two events are compatible and contribute $2+2$.

**Example 2**

- Input: `events = [[1,3,2],[4,5,2],[1,5,5]]`
- Output: `5`
- Explanation: The single long event is worth more than the available pair.

**Example 3**

- Input: `events = [[1,5,3],[1,5,1],[6,6,5]]`
- Output: `8`
- Explanation: Choose the value-$3$ event followed by the event at time $6$.
