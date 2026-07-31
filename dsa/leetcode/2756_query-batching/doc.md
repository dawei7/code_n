# Query Batching

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2756 |
| Difficulty | Hard |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Open problem](https://leetcode.com/problems/query-batching/) |

## Problem Description

### Goal

Implement a JavaScript class `QueryBatcher` that groups closely timed single-key requests into calls to a supplied asynchronous bulk query.

The constructor receives `queryMultiple`, an async function that accepts an array of string keys and fulfills with an equally long value array whose indices correspond to those keys, plus a throttle interval `t` in milliseconds. The bulk query is guaranteed not to reject.

Calling `getValue(key)` must return a promise for that key's individual string value. The first request after an idle interval triggers `queryMultiple` immediately with its key. Any requests arriving before another bulk query may legally start are queued together. Exactly when $t$ milliseconds have elapsed since the previous bulk-query start, dispatch all queued keys in one batch and resolve each waiting promise with its corresponding result.

Throttle query start times, not completion times. A slow earlier bulk query may remain in flight while a later legal batch starts. Every input key is unique. The throttle satisfies $0 \le t \le 1000$, and a schedule contains at most ten calls.

### Function Contract

Let $c$ be the total number of calls to `getValue`.

**Inputs**

- `queryMultiple`: An async function from an array of unique string keys to an equally long array of corresponding string values. Its promise never rejects.
- `t`: The minimum number of milliseconds between consecutive starts of `queryMultiple`, with $0 \le t \le 1000$.
- Each `getValue(key)` call supplies one unique string of length from 1 through 100.

The complete schedule has $0 \le c \le 10$.

**Return value**

The constructor creates a batcher. Each `getValue(key)` returns a promise that fulfills with the value at the matching position of the bulk query that contains `key`.

### Examples

**Example 1**

- Input: `t = 100`, immediate bulk queries, and calls `a` at 10 ms, `b` at 20 ms, and `c` at 30 ms.
- Output: `a!` resolves at 10 ms; `b!` and `c!` resolve together at about 110 ms.
- Explanation: `a` starts an immediate one-key query, while `b` and `c` share the next legal batch.

**Example 2**

- Input: the same schedule, but every bulk query takes 100 ms.
- Output: `a!` resolves at about 110 ms; `b!` and `c!` resolve at about 210 ms.
- Explanation: Query latency shifts fulfillment times but does not shift the next batch's 110 ms start.

**Example 3**

- Input: `t = 100`, bulk latency of 100 ms per key, and requests arriving while earlier batches remain in flight.
- Output: Later legal batches may resolve before an earlier larger batch.
- Explanation: Only consecutive query start times must be separated by the throttle.
