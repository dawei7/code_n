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

### Required Complexity

- **Time:** $O(m)$
- **Space:** $O(size)$

<details>
<summary>Approach</summary>

#### General

**Store the live window and its total**

The active values form a first-in, first-out window. A queue keeps those values in expiration order, while a running sum avoids adding the whole queue again for every request.

When `next(val)` is called, append `val` and add it to the sum. If the queue now contains more than `size` entries, remove its oldest value and subtract that value from the sum. The average is then `running_sum / len(queue)`.

**Why the queue and sum stay synchronized**

After each update, the queue contains exactly the last `min(values_seen, size)` stream values and the running sum equals their total. Appending establishes the invariant for the enlarged suffix; if it is too long, removing the unique oldest value restores the required length and subtracting the same value keeps the sum synchronized. Dividing by the queue length therefore returns precisely the required average.

**Trace one expiration**

With window size three, values `1`, `10`, and `3` accumulate to sum `14`. When `5` arrives, `1` expires, so the sum becomes `18` and the new average is $18 / 3 = 6$.

#### Complexity detail

Each value is appended once and removed at most once. Queue operations and running-sum updates are $O(1)$, so each `next` call is $O(1)$ and a stream of `m` values takes $O(m)$ total time. The queue stores at most `size` values, using $O(size)$ space.

#### Alternatives and edge cases

- **Recompute the window sum:** is correct but costs $O(size)$ per call and $O(m \cdot size)$ over `m` stream values.
- **Circular array:** provides the same constant-time updates and fixed capacity as a deque but requires manual overwrite-index and filled-length bookkeeping.
- Before the window fills, divide by the number of values present rather than by the capacity.
- A window of size one always returns the newest value.
- Negative values and zero participate in the running sum normally.

</details>
