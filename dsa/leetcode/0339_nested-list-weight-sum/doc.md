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
