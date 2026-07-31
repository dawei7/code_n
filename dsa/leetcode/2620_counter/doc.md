# Counter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2620 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/counter/) |

## Problem Description

### Goal

Given an integer `n`, create and return a JavaScript counter function. The first invocation of that returned function must produce `n`. Every later invocation must produce one more than the value returned by the preceding invocation, yielding the sequence `n`, `n + 1`, `n + 2`, and so on.

The counter must preserve its current value between calls. The starting value is between $-1000$ and $1000$, inclusive, and the returned function may be invoked from $0$ through $1000$ times.

### Function Contract

**Inputs**

- `n`: The integer returned by the counter on its first invocation.

The local case adapter also receives `calls`, an array containing one `"call"` entry for each invocation to perform.

**Return value**

Return a function with no parameters. Its successive return values must start at `n` and increase by exactly one after each call.

### Examples

**Example 1**

- Input: `n = 10`, `calls = ["call", "call", "call"]`
- Output: `[10, 11, 12]`
- Explanation: The closure first returns its starting value, then advances by one per invocation.

**Example 2**

- Input: `n = -2`, `calls = ["call", "call", "call", "call", "call"]`
- Output: `[-2, -1, 0, 1, 2]`
- Explanation: Incrementing continues normally through zero.

**Example 3**

- Input: `n = 7`, `calls = []`
- Output: `[]`
- Explanation: Creating a counter does not itself emit a value; values are produced only when it is called.
