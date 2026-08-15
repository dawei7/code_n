# Custom Interval

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2805 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/custom-interval/) |

## Problem Description

### Goal

Implement `customInterval(fn, delay, period)`, which repeatedly invokes `fn` according to a linearly increasing waiting-time pattern and returns a numeric identifier for that repeating task. Before the first invocation, wait `delay` milliseconds. After each invocation, increase the next wait by `period`: if `count` is the number of invocations already completed, the next delay is `delay + period * count`.

Also implement `customClearInterval(id)`. It receives an identifier returned by `customInterval` and prevents that task from invoking `fn` again. The identifier must be a number even though Node.js timer functions return timer objects, so the implementation must maintain its own numeric identity independently of the native timeout handle.

### Function Contract

**Inputs**

- `fn`: The function to invoke on the custom schedule.
- `delay`: The initial waiting time in milliseconds, where $20 \leq \texttt{delay} \leq 250$.
- `period`: The amount added to each successive waiting time, where $20 \leq \texttt{period} \leq 250$.
- `id`: A numeric identifier previously returned by `customInterval`.

For the app-local deterministic adapter, `cancelTime` is the time at which cancellation occurs, where $20 \leq \texttt{cancelTime} \leq 1000$. Let $k$ be the number of invocations strictly before cancellation, and let $a$ be the number of active custom intervals stored at one time.

**Return value**

`customInterval` returns a unique numeric `id`. `customClearInterval` returns no value. The app-local adapter returns the theoretical invocation times, in milliseconds, that occur strictly before `cancelTime`.

### Examples

#### Example 1

- **Input:** `delay = 50`, `period = 20`, `cancelTime = 225`
- **Output:** `[50, 120, 210]`
- **Explanation:** The successive waits are `50`, `70`, and `90` milliseconds, so the cumulative invocation times are $50$, $120$, and $210$.

#### Example 2

- **Input:** `delay = 20`, `period = 20`, `cancelTime = 150`
- **Output:** `[20, 60, 120]`
- **Explanation:** Waiting `20`, then `40`, then `60` milliseconds produces the three invocation times before cancellation.

#### Example 3

- **Input:** `delay = 100`, `period = 200`, `cancelTime = 500`
- **Output:** `[100, 400]`
- **Explanation:** The first two waits are `100` and `300` milliseconds. The next invocation would occur after cancellation.
