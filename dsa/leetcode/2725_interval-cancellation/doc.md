# Interval Cancellation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2725 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Open problem](https://leetcode.com/problems/interval-cancellation/) |

## Problem Description

### Goal

Given a function `fn`, an argument array `args`, and an interval length `t`, start a repeating invocation schedule and return a cancellation function. Call `fn(...args)` immediately, then call it again every `t` milliseconds.

The caller will invoke the returned function after `cancelTimeMs` milliseconds. Once cancellation occurs, no later interval invocation may run. The immediate call happens at time zero and every recorded call must receive the same arguments. The external harness supplies `cancelTimeMs`; it is not an argument to `cancellable` itself.

### Function Contract

**Inputs**

- `fn`: The function to invoke repeatedly.
- `args`: A valid JSON array containing between $1$ and $10$ arguments passed to each invocation.
- `t`: The interval in milliseconds, where $30 \le t \le 100$.

The returned cancellation function is invoked after `cancelTimeMs`, where $10 \le \texttt{cancelTimeMs} \le 500$.

**Return value**

Return a zero-argument function that stops the repeating timer. Before cancellation, `fn(...args)` runs at time zero and at each subsequent interval boundary.

### Examples

**Example 1**

- Input: `fn = (x) => x * 2, args = [4], t = 35, cancelTimeMs = 190`
- Output: Calls at times $0,35,70,105,140,175$, each returning $8$.
- Explanation: The next interval would occur after cancellation.

**Example 2**

- Input: `fn = (x1,x2) => x1 * x2, args = [2,5], t = 30, cancelTimeMs = 165`
- Output: Six calls from time $0$ through $150$, each returning $10$.
- Explanation: Both arguments are spread into every invocation.

**Example 3**

- Input: `fn = (x1,x2,x3) => x1+x2+x3, args = [5,1,3], t = 50, cancelTimeMs = 180`
- Output: Calls at $0,50,100,150$, each returning $9$.
- Explanation: Cancellation prevents the call that would otherwise occur at $200$ ms.
