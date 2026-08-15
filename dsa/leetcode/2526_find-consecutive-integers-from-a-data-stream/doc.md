# Find Consecutive Integers from a Data Stream

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2526 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Design, Queue, Counting, Data Stream |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/) |

## Problem Description

### Goal

Design a `DataStream` object that begins with an empty integer stream and is configured with a target `value` and a positive length `k`. Values arrive one at a time through calls to `consec(num)`, and every call appends `num` to the stream permanently.

After appending a value, `consec` must report whether the last `k` integers in the stream are all equal to the configured `value`. It returns `false` while fewer than `k` integers have arrived, and any non-target value prevents the condition from holding until at least `k` new consecutive target values follow it.

### Function Contract

**Inputs**

- `commands`: An operation sequence beginning with `DataStream`, followed by `consec` calls.
- `inputs`: Arguments aligned with `commands`; construction receives `[value, k]`, and every `consec` call receives `[num]`.

The values `value` and `num` satisfy $1 \le \texttt{value},\texttt{num} \le 10^9$, while $1 \le k \le 10^5$. Let $q$ be the number of `consec` calls; $q \le 10^5$.

**Return value**

Return a list aligned with the operations. Construction contributes `null`; every `consec` call contributes the Boolean result after its integer has been appended.

### Examples

#### Example 1

- **Input:** `commands = ["DataStream", "consec", "consec", "consec", "consec"]`, `inputs = [[4, 3], [4], [4], [4], [3]]`
- **Output:** `[null, false, false, true, false]`
- **Explanation:** The first two calls have not supplied three integers. The third completes a run of three `4`s, and the following `3` immediately breaks that run.
