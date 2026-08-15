# Timeout Cancellation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2715 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Open problem](https://leetcode.com/problems/timeout-cancellation/) |

## Problem Description

### Goal

Given a function `fn`, an argument array `args`, and a delay `t` in milliseconds, schedule one invocation of `fn(...args)` after that delay. Return a new function `cancelFn` immediately; calling it before the scheduled execution must prevent `fn` from running.

The external test harness separately chooses `cancelTimeMs` and invokes `cancelFn` after that many milliseconds. If cancellation occurs before $t$, the result log remains empty. Otherwise the scheduled function runs once and its returned value is recorded near time $t$. Timer measurements may differ slightly because callback execution depends on the event loop.

### Function Contract

**Inputs**

- `fn`: The function whose execution is to be delayed.
- `args`: A valid JSON array containing between $1$ and $10$ arguments for `fn`.
- `t`: The requested delay in milliseconds, where $20 \le t \le 1000$.

**Return value**

Return a function `cancelFn` that clears the pending delayed invocation when called before it executes.

The harness schedules `cancelFn` after `cancelTimeMs` milliseconds, where $10 \le \texttt{cancelTimeMs} \le 1000$; this value is not a parameter of `cancellable`.

### Examples

#### Example 1

- **Input:** `fn = (x) => x * 5, args = [2], t = 20, cancelTimeMs = 50`
- **Output:** `[{"time":20,"returned":10}]`
- **Explanation:** The function runs at about $20$ ms, before cancellation is attempted at $50$ ms.

#### Example 2

- **Input:** `fn = (x) => x ** 2, args = [2], t = 100, cancelTimeMs = 50`
- **Output:** `[]`
- **Explanation:** Cancellation occurs before the pending function becomes eligible to run.

#### Example 3

- **Input:** `fn = (x1, x2) => x1 * x2, args = [2,4], t = 30, cancelTimeMs = 100`
- **Output:** `[{"time":30,"returned":8}]`
- **Explanation:** The multiplication runs once before the later cancellation attempt.
