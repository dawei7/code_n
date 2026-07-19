# Average Waiting Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1701 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/average-waiting-time/) |

## Problem Description
### Goal

A restaurant has one chef and receives customers in the order listed by `customers`. Each pair contains that customer's arrival time and the time needed to prepare the order. Arrival times are sorted in non-decreasing order, and every customer gives the chef an order upon arriving.

The chef handles only one order at a time and preserves the input order. If the chef is idle when a customer arrives, preparation begins immediately; otherwise that customer waits until all earlier work finishes. A customer's waiting time covers the complete interval from arrival until their own order is finished. Return the average waiting time over all customers. An answer within $10^{-5}$ of the exact value is accepted.

### Function Contract
**Inputs**

- `customers`: a list of $n$ pairs `[arrival, preparation]` in service order
- `arrival` is the customer's arrival time and `preparation` is the duration of that order, with both values between $1$ and $10^4$.
- Arrival times are sorted in non-decreasing order, and $1 \le n \le 10^5$.

**Return value**

The arithmetic mean of `finish - arrival` across all customers, returned as a floating-point value.

### Examples
**Example 1**

- Input: `customers = [[1, 2], [2, 5], [4, 3]]`
- Output: `5.00000`

The orders finish at times `3`, `8`, and `11`, giving waits of `2`, `6`, and `7`; their average is `5`.

**Example 2**

- Input: `customers = [[5, 2], [5, 4], [10, 3], [20, 1]]`
- Output: `3.25000`

The waits are `2`, `6`, `4`, and `1`. The chef becomes idle before the final arrival, so that order starts at time `20` rather than at the previous finish time.

**Example 3**

- Input: `customers = [[1, 1], [2, 2], [3, 3]]`
- Output: `2.33333`

The corresponding waits are `1`, `2`, and `4`, whose average is $7 / 3$.
