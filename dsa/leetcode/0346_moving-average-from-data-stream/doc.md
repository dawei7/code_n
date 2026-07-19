# Moving Average from Data Stream

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 346 |
| Difficulty | Easy |
| Topics | Array, Design, Queue, Data Stream |
| Official Link | [LeetCode](https://leetcode.com/problems/moving-average-from-data-stream/) |

## Problem Description
### Goal
Construct a moving-average object with a positive window capacity `size`. Integers arrive one at a time through `next(val)`, and each call adds the new value to the persistent stream after all earlier arrivals.

Return the arithmetic mean of the most recent at most `size` values after every insertion. Before the window fills, average all values seen so far; after it fills, each new value expels the oldest retained value. Report floating-point averages and handle negative values normally. The app adapter supplies a full stream and returns each prefix result, while the native object exposes one stateful call at a time.

### Function Contract
**Inputs**

- `size`: the positive maximum window length
- `stream`: for the app-local adapter, the values passed to `next` in order. The native LeetCode interface receives `size` in the constructor and one value per `next(val)` call.

**Return value**

- The app adapter returns the moving average after every stream value. Native `next(val)` returns the newest average directly.

### Examples
**Example 1**

- Input: `size = 3, stream = [1, 10, 3, 5]`
- Output: `[1.0, 5.5, 4.666666666666667, 6.0]`

**Example 2**

- Input: `size = 1, stream = [4, -2, 7]`
- Output: `[4.0, -2.0, 7.0]`

**Example 3**

- Input: `size = 5, stream = [2, 4]`
- Output: `[2.0, 3.0]`
