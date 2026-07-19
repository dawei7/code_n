# Count All Valid Pickup and Delivery Options

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1359 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/) |

## Problem Description

### Goal

There are $n$ distinct orders. Order $i$ contributes two labeled events: pickup $P_i$ and delivery $D_i$. Count the sequences containing all $2n$ events exactly once in which every delivery occurs after the pickup belonging to the same order.

Events from different orders may be interleaved in any way, and their pickup or delivery order need not match. Because the number of valid sequences grows rapidly, return the count modulo $10^9+7$.

### Function Contract

**Inputs**

- `n`: the number of distinct pickup-and-delivery orders.

**Return value**

- The number of permutations of the $2n$ labeled events satisfying $P_i$ before $D_i$ for every order $i$, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `n = 1`
- Output: `1`
- Explanation: only `P1, D1` respects the order constraint.

**Example 2**

- Input: `n = 2`
- Output: `6`
- Explanation: six interleavings place each delivery after its matching pickup.

**Example 3**

- Input: `n = 3`
- Output: `90`
