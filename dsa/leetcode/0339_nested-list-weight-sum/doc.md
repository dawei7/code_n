# Nested List Weight Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 339 |
| Difficulty | Medium |
| Topics | Depth-First Search, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/nested-list-weight-sum/) |

## Problem Description
### Goal
Given a recursively nested list of integers and sublists, assign depth `1` to integers directly inside the outer list. Entering each additional nested list increases the depth by one, regardless of whether sibling lists have different shapes.

Return the sum of `value * depth` for every contained integer. Negative values contribute negative weighted amounts, empty nested lists contribute zero, and each integer occurrence is counted independently. The app represents nesting with ordinary lists, while the native problem supplies `NestedInteger` objects; both forms require traversing the same logical hierarchy rather than weighting list containers themselves.

### Function Contract
**Inputs**

- `nested_list`: a list whose elements are integers or recursively nested lists of the same form. The app represents the abstract nested values with ordinary Python lists; LeetCode supplies its `NestedInteger` interface to the native submission.

**Return value**

- An integer equal to the sum of `value * depth` over all contained integers.

### Examples
**Example 1**

- Input: `nested_list = [[1, 1], 2, [1, 1]]`
- Output: `10`
- Explanation: The four `1` values are at depth `2`, while `2` is at depth `1`.

**Example 2**

- Input: `nested_list = [1, [4, [6]]]`
- Output: `27`
- Explanation: The contributions are $1 \cdot 1 + 4 \cdot 2 + 6 \cdot 3$.

**Example 3**

- Input: `nested_list = [0]`
- Output: `0`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(D)$

<details>
<summary>Approach</summary>

#### General

**Carry the current depth through the traversal**

The nested input is naturally a forest: each integer is a value node, while each list owns the nodes one level below it. The only context an integer needs is the depth of the list that directly contains it, so a depth-first traversal can carry that depth as a parameter.

Begin with depth `1` for the outermost list. For each element:

- If it is an integer, add `integer * depth` to the running total.
- If it is a list, recursively process its children at `depth + 1`.

**Trace one chain of nested lists**

For `[1, [4, [6]]]`, the traversal adds `1` at depth `1`, descends once to add `8` for the `4`, then descends again to add `18` for the `6`. The three contributions total `27`.

**Why every integer contributes exactly once**

Each recursive call returns the complete weighted contribution of its own nested list at the supplied depth. This statement is immediate for an empty list. For a non-empty list, integer elements contribute exactly their required weighted values, and recursive elements return the correct contributions of all descendants one level deeper. Adding those disjoint contributions therefore gives the correct sum for the current list and, at depth `1`, for the entire input.

#### Complexity detail

Let `N` count every integer and list entry visited by the traversal, and let `D` be the maximum nesting depth. Each element is inspected once, so the running time is $O(N)$. A depth-first traversal keeps at most one recursive frame per nesting level, using $O(D)$ auxiliary space. The result itself is a scalar.

#### Alternatives and edge cases

- **Breadth-first traversal:** is equally valid and remains $O(N)$ time, but its queue may hold an entire level and use $O(W)$ space for maximum width `W`.
- **Explicit depth-first stack:** avoids recursion but can still hold $O(N)$ pending elements in the worst case.
- **One traversal per depth:** can cost $O(ND)$ because the same structure is revisited for each of `D` levels.
- Zero contributes nothing at any depth, while a negative integer retains its sign after weighting.
- Empty nested lists contribute zero and should not alter the total.
- A deeply nested single integer must be multiplied by every containing level, including the outermost list.

</details>
