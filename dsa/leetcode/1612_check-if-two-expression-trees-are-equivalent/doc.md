# Check If Two Expression Trees are Equivalent

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1612 |
| Difficulty | Medium |
| Topics | Hash Table, Tree, Depth-First Search, Binary Tree, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/) |

## Problem Description
### Goal
Two binary expression trees represent sums of lowercase variables. A leaf stores one variable, while an internal node stores `+` and combines the expressions represented by its left and right subtrees.

Determine whether `root1` and `root2` represent equivalent expressions: for every assignment of values to their variables, both trees must evaluate to the same result. Addition is associative and commutative, but repeated appearances of a variable contribute repeatedly and therefore must retain their multiplicity.

### Function Contract
**Inputs**

- `root1`: the non-null root of the first valid addition expression tree.
- `root2`: the non-null root of the second valid addition expression tree.
- Every internal node has value `+` and two expression children; every leaf is a lowercase English variable.
- Let $n_1$ and $n_2$ be the respective node counts, $h$ the greater tree height, and $u$ the number of distinct variables across both trees.

**Return value**

Return `true` exactly when both trees contain every variable with the same multiplicity, and therefore represent equivalent sums for all variable assignments.

### Examples
**Example 1**

- Input: `root1 = ["+", "a", "+", null, null, "b", "c"]`, `root2 = ["+", "+", "a", "b", "c"]`
- Output: `true`
- Explanation: The trees represent `a + (b + c)` and `(b + c) + a`.

**Example 2**

- Input: `root1 = ["+", "a", "+", null, null, "b", "c"]`, `root2 = ["+", "+", "a", "b", "d"]`
- Output: `false`
- Explanation: The first expression contains `c`, while the second contains `d`.

**Example 3**

- Input: `root1 = ["+", "a", "a"]`, `root2 = ["+", "a", "b"]`
- Output: `false`
- Explanation: Repeated variables are coefficients; `a + a` is not equivalent to `a + b`.
