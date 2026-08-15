# Execute Asynchronous Functions in Parallel

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2721 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Open problem](https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/) |

## Problem Description

### Goal

Given an array `functions` of asynchronous zero-argument functions, call every function so that all returned promises begin running in parallel. Construct and return one new promise without using the built-in `Promise.all` operation.

If every invoked promise fulfills, the returned promise must fulfill after the last one completes. Its value is an array containing the fulfillment values in the same order as their functions in the input, regardless of completion order. If any invoked promise rejects, the returned promise must instead reject with the reason from the first rejection as soon as that rejection occurs.

### Function Contract

Let $n$ be the number of functions.

**Inputs**

- `functions`: An array of $n$ zero-argument functions, each returning a promise, where $1 \le n \le 10$.

**Return value**

Return a promise that fulfills with the input-ordered array of all fulfillment values after every operation succeeds, or rejects with the first rejection reason. All input functions must be invoked without waiting for an earlier promise to settle.

### Examples

#### Example 1

- **Input:** One function fulfills with `5` after $200$ ms.
- **Output:** The returned promise fulfills with `[5]` at approximately $200$ ms.
- **Explanation:** The only result occupies index $0$, and settlement waits for that promise.

#### Example 2

- **Input:** One function fulfills after $200$ ms while another rejects with `"Error"` after $100$ ms.
- **Output:** The returned promise rejects with `"Error"` at approximately $100$ ms.
- **Explanation:** A rejection settles the combined promise immediately; the slower operation need not finish first.

#### Example 3

- **Input:** Three functions fulfill with `4`, `10`, and `16` after $50$, $150$, and $100$ ms respectively.
- **Output:** The returned promise fulfills with `[4, 10, 16]` at approximately $150$ ms.
- **Explanation:** Completion order differs from input order, but the result array preserves the original indices.
