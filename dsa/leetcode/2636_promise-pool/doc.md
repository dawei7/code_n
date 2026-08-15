# Promise Pool

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2636 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/promise-pool/) |

## Problem Description

### Goal

Given an ordered array of asynchronous functions and a positive pool limit `n`, return a promise that resolves after every function's promise has resolved. At no instant may more than `n` produced promises remain pending.

Start as many functions as the limit allows. Functions must begin in array order: `functions[i]` starts before `functions[i + 1]`. Whenever one pending promise resolves, immediately start the next unstarted function if one exists, keeping the pool as full as possible until the input is exhausted. When the final pending promise resolves, the returned promise must resolve as well.

All input functions are guaranteed not to reject. The resolving value of the returned promise is unrestricted.

### Function Contract

**Inputs**

- `functions`: An ordered array containing from zero through ten no-argument asynchronous functions, each returning a promise that resolves.
- `n`: The maximum number of pending promises, where $1 \le n \le 10$.

Let $m$ be `functions.length` and $c = \min(m,n)`. For the app-local serializable adapter, `durations[i]` is the deterministic duration of `functions[i]`; the adapter returns the resulting schedule so concurrency and progress can be checked without wall-clock timing noise.

**Return value**

Return a promise that resolves only after all $m$ input functions have completed. The execution must respect input start order, never exceed `n` pending promises, and start the next available function whenever capacity opens.

### Examples

#### Example 1

- **Input:** `durations = [300,400,200]`, `n = 2`
- **Output:** start times `[0,0,300]`, finish times `[300,400,500]`, pool completion `500`
- **Explanation:** The first two functions start immediately. When the first finishes at $300$, the third starts and finishes $200$ time units later.

#### Example 2

- **Input:** `durations = [300,400,200]`, `n = 5`
- **Output:** start times `[0,0,0]`, finish times `[300,400,200]`, pool completion `400`
- **Explanation:** The limit exceeds the number of functions, so all three start immediately and the slowest determines completion.

#### Example 3

- **Input:** `durations = [300,400,200]`, `n = 1`
- **Output:** start times `[0,300,700]`, finish times `[300,700,900]`, pool completion `900`
- **Explanation:** A limit of one forces strictly serial execution in input order.
