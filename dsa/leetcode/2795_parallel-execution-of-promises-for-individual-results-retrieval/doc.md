# Parallel Execution of Promises for Individual Results Retrieval

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2795 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [2795. Parallel Execution of Promises for Individual Results Retrieval](https://leetcode.com/problems/parallel-execution-of-promises-for-individual-results-retrieval/) |

## Problem Description

### Goal

Given an array `functions` whose elements are zero-argument functions returning promises, invoke every function so that their asynchronous work runs in parallel. Return one promise that waits until every produced promise has settled, whether by fulfillment or rejection.

For a fulfilled promise, place an object of the form `{ status: "fulfilled", value: resolvedValue }` in the output. For a rejected promise, place `{ status: "rejected", reason: rejectionReason }` instead. The returned promise itself resolves with the complete array; an individual rejection must be captured as a result record rather than rejecting the aggregate.

Each output object must occupy the index of its originating function even when the promises settle in a different order. Implement this behavior without calling `Promise.allSettled()`.

### Function Contract

Let $n$ be the number of input functions.

**Inputs**

- `functions`: An array of $n$ zero-argument functions, each returning a promise that may fulfill or reject, where $1 \le n \le 10$.

**Return value**

Return a promise that resolves after all $n$ produced promises settle. Its resolved value is an input-ordered array of fulfilled or rejected result objects containing the corresponding value or reason.

### Examples

#### Example 1

- **Input:** One function returns a promise that fulfills with `15` after $100$ ms.
- **Output:** `[{"status": "fulfilled", "value": 15}]` after approximately $100$ ms.
- **Explanation:** The only operation fulfills, so its result record occupies index $0$.

#### Example 2

- **Input:** Two functions return promises that fulfill with `20` and `15`, both after $100$ ms.
- **Output:** `[{"status": "fulfilled", "value": 20}, {"status": "fulfilled", "value": 15}]` after approximately $100$ ms.
- **Explanation:** Both operations begin together, and the output preserves their input positions.

#### Example 3

- **Input:** One promise fulfills with `30` after $200$ ms while another rejects with `"Error"` after $100$ ms.
- **Output:** `[{"status": "fulfilled", "value": 30}, {"status": "rejected", "reason": "Error"}]` after approximately $200$ ms.
- **Explanation:** The aggregate waits for every promise to settle and records the rejection as data.
