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

### Required Complexity
- **Time:** $O(n_1+n_2)$
- **Space:** $O(h+u)$

<details>
<summary>Approach</summary>

#### General

**Flatten algebraically rather than structurally.** Parenthesization and left/right placement do not affect a sum because addition is associative and commutative. What does affect the expression is the coefficient of each variable, which is exactly the number of leaves carrying that letter.

**Accumulate one signed frequency map.** Traverse `root1`, adding one for every variable leaf. Traverse `root2`, subtracting one for every variable leaf. At `+` nodes, recursively visit both children without recording the operator itself. After both traversals, every zero balance means the two expressions have identical coefficients.

If all balances are zero, evaluation under any variable assignment produces the same linear combination in both trees. Conversely, if one variable has nonzero balance, assigning that variable 1 and every other variable 0 makes the two evaluated results differ. The frequency condition is therefore both sufficient and necessary.

#### Complexity detail

Each node in both trees is visited once, so the running time is $O(n_1+n_2)$. Recursive calls use $O(h)$ stack space, and the frequency map stores $u$ variables, for $O(h+u)$ total auxiliary space. Since variables are lowercase English letters, $u$ is also bounded by 26.

#### Alternatives and edge cases

- **Collect and sort both leaf lists:** Comparing sorted variable sequences is correct but takes $O((n_1+n_2)\log(n_1+n_2))$ time.
- **Remove each first-tree leaf from a second-tree list:** This preserves multiplicity and is correct, but repeated linear searches and removals can take quadratic time.
- **Compare tree shapes and corresponding nodes:** This incorrectly rejects equivalent expressions whose variables are regrouped or reordered.
- A one-leaf tree is equivalent only to an expression with the same single variable multiplicity.
- Duplicate variables matter; equality of distinct-variable sets is insufficient.
- Different shapes and different left-to-right orders can still be equivalent.
- Internal `+` nodes affect grouping only and do not contribute a symbol to the variable counts.

</details>
