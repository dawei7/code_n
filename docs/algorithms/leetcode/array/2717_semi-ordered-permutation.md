# Semi-Ordered Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2717 |
| Difficulty | Easy |
| Topics | Array, Simulation |
| Official Link | [semi-ordered-permutation](https://leetcode.com/problems/semi-ordered-permutation/) |

## Problem Description & Examples
### Goal
Given a 0-indexed permutation of $n$ integers containing all numbers from $1$ to $n$, find the minimum number of adjacent swaps required to make the permutation **semi-ordered**. 

A permutation is defined as semi-ordered if:
1. The first element is $1$.
2. The last element is $n$.

### Function Contract
**Inputs**

- `nums`: `List[int]` — A 0-indexed permutation of $n$ integers from $1$ to $n$.

**Return value**

- `int` — The minimum number of adjacent swaps needed to make the array semi-ordered.

### Examples
**Example 1**

- Input: `nums = [2, 1, 4, 3]`
- Output: `2`
- Explanation: 
  1. Swap `nums[0]` and `nums[1]` to get `[1, 2, 4, 3]`.
  2. Swap `nums[2]` and `nums[3]` to get `[1, 2, 3, 4]`.
  The array is now semi-ordered. Total swaps = 2.

**Example 2**

- Input: `nums = [2, 4, 1, 3]`
- Output: `3`
- Explanation:
  1. Swap `nums[2]` and `nums[1]` to get `[2, 1, 4, 3]`.
  2. Swap `nums[1]` and `nums[0]` to get `[1, 2, 4, 3]`.
  3. Swap `nums[2]` and `nums[3]` to get `[1, 2, 3, 4]`.
  The array is now semi-ordered. Total swaps = 3.

**Example 3**

- Input: `nums = [1, 3, 2, 4]`
- Output: `0`
- Explanation: The array is already semi-ordered since `1` is at the first position and `4` is at the last position.

---

## Underlying Base Algorithm(s)
The problem can be solved efficiently by locating the indices of the elements `1` and `n` in the array. Let `idx_1` be the index of `1` and `idx_n` be the index of `n`.

1. **Moving `1` to the front**: To shift `1` to index `0` using only adjacent swaps, we need exactly `idx_1` swaps.
2. **Moving `n` to the end**: To shift `n` to index `n - 1` using only adjacent swaps, we need exactly `(n - 1) - idx_n` swaps.
3. **Handling Overlap**: If `idx_1 > idx_n`, the element `1` is located to the right of `n`. When we swap `1` to the left, it will eventually swap with `n`. This single swap moves `1` one step to the left and `n` one step to the right simultaneously. Thus, we save exactly $1$ swap from the independent sum of swaps.

The formula for the minimum swaps is:
$$\text{Swaps} = \text{idx\_1} + (n - 1 - \text{idx\_n}) - (1 \text{ if } \text{idx\_1} > \text{idx\_n} \text{ else } 0)$$

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — We perform a single pass (or two linear searches) over the array of size $n$ to find the indices of `1` and `n`.
- **Space Complexity**: $\mathcal{O}(1)$ — Only a few variables are used to store the indices and the array length, requiring constant auxiliary space.
