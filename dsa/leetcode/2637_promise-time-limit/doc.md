# Promise Time Limit

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2637 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/promise-time-limit/) |

## Problem Description

### Goal

Given an asynchronous function `fn` and a time limit `t` in milliseconds, return a new asynchronous function that accepts and forwards any supplied arguments to `fn` while enforcing that limit.

If `fn` settles successfully before the limit expires, the returned function must resolve with the same value. If `fn` rejects first, preserve that rejection. If the limit expires before `fn` settles, reject with the exact string `"Time Limit Exceeded"` instead. The original asynchronous work need not be cancelled after a timeout; only the returned promise's settlement is governed by the race.

### Function Contract

**Inputs**

- `fn`: An asynchronous function that returns a promise.
- `t`: A time limit in milliseconds, where $0 \le t \le 1000$.

The returned function receives an argument array `inputs` with length $a$, where $0 \le a \le 10$, and forwards those arguments positionally to `fn`.

For the app-local deterministic adapter, `duration` describes when the source promise settles, `behavior` selects its resolved or rejected result, and `inputs` supplies the forwarded arguments. Immediate behaviors settle through the promise microtask queue without a timer.

**Return value**

Return an asynchronous function. Each invocation returns a promise that mirrors the source promise if it settles first, or rejects with `"Time Limit Exceeded"` when the timeout wins.

### Examples

**Example 1**

- Input: a function that resolves to $n^2$ after $100$ ms, `inputs = [5]`, `t = 50`
- Output: rejection `"Time Limit Exceeded"` at $50$ ms
- Explanation: The timeout wins before the function can produce `25`.

**Example 2**

- Input: the same $100$ ms square function, `inputs = [5]`, `t = 150`
- Output: resolved value `25` at about $100$ ms
- Explanation: The source promise settles before the longer limit.

**Example 3**

- Input: a function that returns `a + b` after $120$ ms, `inputs = [5,10]`, `t = 150`
- Output: resolved value `15` at about $120$ ms
- Explanation: Both arguments are forwarded and the function finishes within the limit.

**Example 4**

- Input: an async function that immediately throws `"Error"`, `inputs = []`, `t = 1000`
- Output: rejection `"Error"` immediately
- Explanation: The source rejection settles the race long before the timeout.
