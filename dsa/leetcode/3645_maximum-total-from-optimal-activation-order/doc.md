# Maximum Total from Optimal Activation Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3645 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Greedy, Sorting, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-total-from-optimal-activation-order/) |

## Problem Description
### Goal

The arrays `value` and `limit` describe $n$ elements, all initially inactive. You may choose an inactive element `i` only while the current number of active elements is strictly smaller than `limit[i]`. Activating it permanently adds `value[i]` to the accumulated total.

After every activation, let $x$ be the new active count. Every element whose limit is at most $x$ then becomes permanently inactive, including elements that were active and elements that were never activated. Permanently inactive elements cannot be chosen later, while elements with larger limits remain in their current state.

Choose the activation order that maximizes the sum of values collected from all activation operations, and return that maximum total.

### Function Contract
**Inputs**

- `value`: Positive activation values, where `value[i]` belongs to element `i`.
- `limit`: Positive activation thresholds of the same length, with $1\le\texttt{limit[i]}\le n$.

Both arrays have length $n$, where $1\le n\le 10^5$, and each activation value is at most $10^5$.

**Return value**

Return the largest total value obtainable by a valid activation order.

### Examples
**Example 1**

- Input: `value = [3,5,8]`, `limit = [2,1,3]`
- Output: `16`
- Explanation: Activating indices 1, 0, and 2 collects all three values while threshold expirations keep each next activation legal.

**Example 2**

- Input: `value = [4,2,6]`, `limit = [1,1,1]`
- Output: `6`
- Explanation: The first activation makes the active count 1 and permanently disables every element, so choosing the largest value is optimal.

**Example 3**

- Input: `value = [4,1,5,2]`, `limit = [3,3,2,3]`
- Output: `12`
- Explanation: The single limit-2 value and all three limit-3 values can be collected in a valid order.
