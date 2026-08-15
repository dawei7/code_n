# Apply Operations to Maximize Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2818 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Stack, Greedy, Sorting, Monotonic Stack, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/apply-operations-to-maximize-score/) |

## Problem Description

### Goal

You are given an array `nums` of $n$ positive integers and an integer `k`. Begin with a score of `1` and perform the following operation at most `k` times, never selecting the same subarray twice.

Choose any non-empty subarray `nums[l:r + 1]`. Within it, identify an element having the greatest prime score, where an integer's prime score is the number of its distinct prime factors. If several elements share that greatest score, the element with the smallest array index is selected. Multiply the current score by the selected element.

Choose the subarrays so that the final product is as large as possible. Return that maximum score modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers.
- `k`: The maximum number of distinct subarray operations.

Let $V = \max(\texttt{nums})$. The constraints are $1 \leq n \leq 10^5$, $1 \leq V \leq 10^5$, and

$$
1 \leq k \leq \min\left(\frac{n(n+1)}{2}, 10^9\right).
$$

**Return value**

Return the greatest product obtainable using at most `k` distinct subarrays, reduced modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `nums = [8,3,9,3,8], k = 2`
- **Output:** `81`
- **Explanation:** Subarrays `[9]` and `[9,3]` both select the value `9`, so the product is `9 * 9`.

#### Example 2

- **Input:** `nums = [19,12,14,6,10,18], k = 3`
- **Output:** `4788`
- **Explanation:** An optimal set of operations contributes `19`, `18`, and `14`, whose product is `4788`.

#### Example 3

- **Input:** `nums = [2,3], k = 3`
- **Output:** `12`
- **Explanation:** Both values have prime score one. The three subarrays contribute `2`, `3`, and `2`; their product is `12`.
