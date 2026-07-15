# Minimum Cost Tree From Leaf Values

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1130 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Stack, Greedy, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/) |

## Problem Description

### Goal

Given an array `arr` of positive integers, consider every binary tree in which each node has either zero or two children and the leaf values encountered by an in-order traversal are exactly the values of `arr` in their given order. A node is a leaf if and only if it has no children.

For every non-leaf node, its value is the product of the largest leaf value in its left subtree and the largest leaf value in its right subtree. Among all trees satisfying these rules, return the smallest possible sum of all non-leaf node values. The answer is guaranteed to fit in a signed 32-bit integer.

### Function Contract

**Inputs**

- `arr`: an array of $n$ positive leaf values, where $2 \le n \le 40$ and $1 \le \texttt{arr[i]} \le 15$.

**Return value**

The minimum possible sum of the non-leaf node values over all valid full binary trees whose in-order leaf sequence is `arr`.

### Examples

**Example 1**

- Input: `arr = [6,2,4]`
- Output: `32`
- Explanation: The lower-cost tree has internal values `8` and `24`, whose sum is `32`; the other possible grouping costs `36`.

**Example 2**

- Input: `arr = [4,11]`
- Output: `44`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**View construction as eliminating leaves.** Whenever two neighboring components are joined, the smaller component maximum contributes its product with a neighboring value that survives above it. For a leaf value `mid`, using anything larger than the smaller of its nearest surviving greater-or-equal neighbors cannot improve the total. Thus, once both such boundaries are known, greedily pairing `mid` with the smaller boundary is safe; the larger value remains available for later joins.

**Expose those boundaries with a decreasing stack.** Start with an infinite sentinel. For each `value`, pop while `stack[-1] <= value`. Every popped `mid` has `value` as its first greater-or-equal value on the right and the new stack top as its nearest greater value on the left. Add `mid * min(stack[-1], value)`, which is the cheapest unavoidable partner for `mid`, then continue until the stack is decreasing and push `value`.

**Finish the decreasing suffix.** Values left after the scan have no greater-or-equal value to their right. Pop them from right to left and multiply each by its left neighbor. In a decreasing sequence that neighbor is the smaller available surviving partner. Every value except the global maximum is eliminated exactly once, producing exactly the $n-1$ internal-node products of a full binary tree. The exchange argument above shows no alternative tree can give an eliminated value a cheaper valid partner, so the sum is minimum.

#### Complexity detail

Each of the $n$ values is pushed once and popped once, so all stack operations take $O(n)$ time. The monotonic stack can contain $n$ values plus its sentinel, giving $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Interval dynamic programming:** Try every root split for every contiguous leaf interval using precomputed interval maxima; this is straightforward and correct but costs $O(n^3)$ time and $O(n^2)$ space.
- **Repeatedly remove the global smallest leaf:** Pairing the current minimum with its smaller neighbor is another greedy formulation, but finding and deleting minima naively costs $O(n^2)$.
- **Two leaves:** There is only one valid tree, so the answer is their product.
- **Equal values:** The `<=` pop condition may eliminate either equal copy first without changing the product or optimum.
- **Strictly decreasing input:** No value pops during the scan; the cleanup pairs adjacent surviving values from right to left.

</details>
