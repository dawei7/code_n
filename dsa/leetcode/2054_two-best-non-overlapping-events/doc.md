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

### Required Complexity

- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Best future value after each position**

Sort events by start time and record the sorted starts. Build a suffix array where each position stores the greatest single-event value from that position onward. This makes the best value among every sufficiently late event available in constant time.

**Locating a compatible partner**

For each sorted event, binary-search for the first start strictly greater than its inclusive end. Combine the current value with the suffix maximum at that position; the sentinel suffix value zero also represents choosing no second event. Track the greatest combination.

The binary search excludes exactly the overlapping events, including those sharing an endpoint. Every compatible later event lies in the selected suffix, whose stored maximum is the best possible partner. Evaluating every event as the first choice therefore considers an optimal pair or optimal singleton.

#### Complexity detail

Sorting costs $O(n\log n)$. Building suffix maxima is $O(n)$, and $n$ binary searches cost another $O(n\log n)$. The starts and suffix arrays use $O(n)$ space.

#### Alternatives and edge cases

- **End-time sweep with a heap:** Process starts in order while removing finished events from a min-heap and retaining the best completed value; this also runs in $O(n\log n)$ time.
- **Enumerate every pair:** Testing all event pairs is correct but costs $O(n^2)$ time.
- Events with `next_start == current_end` overlap because both include that time.
- The best answer may use just one event; the suffix sentinel must permit a zero-valued second choice.
- Events may share starts, ends, and values without affecting the method.

</details>
