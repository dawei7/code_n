# Maximum Subarray Sum After One Operation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1746 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/) |

## Problem Description

### Goal

You are given an integer array `nums`. Perform exactly one operation: choose one array element and replace it by its square. After that replacement, select a nonempty contiguous subarray.

Return the largest subarray sum that can be achieved by choosing both the squared position and the subarray optimally. The squared element may originally be positive, negative, or zero, and the selected subarray may start and end anywhere.

### Function Contract

**Inputs**

- `nums`: a nonempty integer array with $1 \le n \le 10^5$ and $-10^4 \le \texttt{nums[i]} \le 10^4$.

**Return value**

- Return the maximum sum of a nonempty contiguous subarray after exactly one element of `nums` has been replaced by its square.

### Examples

**Example 1**

- Input: `nums = [2,-1,-4,-3]`
- Output: `17`
- Explanation: Squaring `-4` gives the subarray `[2,-1,16]`, whose sum is $17$.

**Example 2**

- Input: `nums = [1,-1,1,1,-1,-1,1]`
- Output: `4`
- Explanation: Squaring a selected `-1` changes it to `1`, allowing a best sum of $4$.

**Example 3**

- Input: `nums = [-5]`
- Output: `25`
- Explanation: The only element must be squared and is also the only nonempty subarray.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Separate subarrays by whether the operation has occurred**

While scanning left to right, keep `plain`, the largest sum of a subarray ending at the previous position with no squared element, and `squared`, the corresponding largest sum with exactly one squared element. Only the second state is eligible for the final answer.

**Update the unsquared state like Kadane's algorithm**

For current value `x`, an unsquared subarray ending here either starts at `x` or extends the previous unsquared subarray:

$$
\texttt{new_plain}=\max(x,\texttt{plain}+x).
$$

This state remains available for using the operation at a later position.

**Account for all ways the squared state can end here**

A valid squared subarray ending at `x` has exactly three possibilities: start with `x * x`, extend the previous plain state and square `x`, or extend a state whose operation was already used and keep `x` unchanged:

$$
\texttt{new_squared}
=
\max(x^2,\texttt{plain}+x^2,\texttt{squared}+x).
$$

The alternatives are exhaustive and mutually identify where the one operation occurs relative to the current endpoint. Record the maximum squared state over all endpoints, because the optimal subarray need not reach the final array element.

#### Complexity detail

Each of the $n$ values performs a constant number of arithmetic operations and comparisons, for $O(n)$ time. The two previous states, two new states, and global maximum use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Try every squared position:** Running Kadane's algorithm after each possible replacement is correct but takes $O(n^2)$ time.
- **Prefix and suffix best sums:** Combining positive contributions around every squared position can also run in $O(n)$ time, but requires additional arrays or careful rolling logic.
- **Single element:** The only possible result is that value squared.
- **All negative values:** Squaring the most useful negative can create a positive one-element optimum or connect neighboring contributions.
- **Zero and one:** Squaring either leaves its value unchanged, but still satisfies the mandatory operation.
- **Optimal subarray starts at the squared element:** The `x * x` transition discards every harmful prefix.
- **Operation before the current element:** The `squared + x` transition preserves a previously used operation.
- **Large magnitude:** Squaring an endpoint value can reach $10^8$, and a longer sum can exceed ordinary 16-bit ranges.

</details>
