# Maximum Strength of K Disjoint Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3077 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/) |

## Problem Description

### Goal

You are given an integer array `nums` of length $n$ and a positive odd integer $k$. Select exactly $k$ non-empty, pairwise disjoint subarrays, denoted in their left-to-right order by $sub_1, sub_2, \ldots, sub_k$. For every $1 \le i < k$, the final element of $sub_i$ must occur before the first element of $sub_{i+1}$ in `nums`.

If $\operatorname{sum}(sub_i)$ is the sum of the elements in the $i$-th selected subarray, define the combined strength as

$$
\sum_{i=1}^{k} (-1)^{i+1}(k-i+1)\operatorname{sum}(sub_i).
$$

Thus the first subarray has coefficient $k$, the second has coefficient $-(k-1)$, and the coefficient magnitude continues decreasing until the final subarray has coefficient $1$. The selected subarrays may leave unused elements before, between, or after them; they do not need to cover the entire array.

Return the maximum strength obtainable from any valid selection of exactly $k$ subarrays.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$.
- `k`: A positive odd integer giving the exact number of ordered, disjoint, non-empty subarrays to select.

The constraints are $1 \le n \le 10^4$, $-10^9 \le \texttt{nums[i]} \le 10^9$, $1 \le k \le n$, and $1 \le nk \le 10^6$.

**Return value**

- The maximum possible strength of exactly $k$ valid subarrays.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, -1, 2]`, `k = 3`
- Output: `22`
- Explanation: Choose `nums[0..2]`, `nums[3..3]`, and `nums[4..4]`. Their strength is $3(1+2+3)-2(-1)+2=22$.

**Example 2**

- Input: `nums = [12, -2, -2, -2, -2]`, `k = 5`
- Output: `64`
- Explanation: Five non-empty subarrays require each element to stand alone. The resulting strength is $5(12)-4(-2)+3(-2)-2(-2)+(-2)=64$.

**Example 3**

- Input: `nums = [-1, -2, -3]`, `k = 1`
- Output: `-1`
- Explanation: With one selected subarray, strength is its ordinary sum. The best choice is the single element `-1`.
