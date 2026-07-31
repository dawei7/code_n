# Button with Longest Push Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3386 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/button-with-longest-push-time/) |

## Problem Description

### Goal

A child presses a sequence of keyboard buttons. Each entry `events[i] = [index_i, time_i]` identifies the button pressed and the absolute time when that press finishes. The events are sorted by strictly increasing finish time.

The first press begins at time zero, so its duration is `time_0`. Every later press begins when the preceding one finishes, making its duration `time_i - time_(i - 1)`.

Return the index of the button associated with the longest single press. When several presses have the same maximum duration, choose the smallest button index among them.

### Function Contract

**Inputs**

- `events`: A list of $n$ two-element lists `[index, time]`, ordered by strictly increasing `time`.

The bounds are $1 \le n \le 1000$ and $1 \le \texttt{index}, \texttt{time} \le 10^5$.

**Return value**

Return the button index whose press has maximum duration, breaking duration ties by smaller index.

### Examples

**Example 1**

- Input: `events = [[1, 2], [2, 5], [3, 9], [1, 15]]`
- Output: `1`
- Explanation: The durations are 2, 3, 4, and 6. The last press of button 1 is longest.

**Example 2**

- Input: `events = [[10, 5], [1, 7]]`
- Output: `10`
- Explanation: The first press lasts 5 units, while the second lasts 2.
