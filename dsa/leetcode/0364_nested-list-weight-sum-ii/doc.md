# Nested List Weight Sum II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 364 |
| Difficulty | Medium |
| Topics | Stack, Depth-First Search, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/nested-list-weight-sum-ii/) |

## Problem Description
### Goal
Given a recursively nested list of integers and sublists, assign ordinary depth `1` to integers directly in the outer list and increase depth when entering each nested list. Let the maximum depth be the deepest level that actually contains an integer.

Weight integers inversely: values at that maximum depth receive weight `1`, and each level closer to the outside increases weight by one. Return the sum of every integer times its inverse-depth weight. Empty sublists contribute no value and do not by themselves create a deeper integer level. Negative values and repeated occurrences are counted independently.

### Function Contract
**Inputs**

- `nested_list`: a list whose elements are integers or recursively nested lists. The app uses ordinary Python lists; LeetCode supplies the native `NestedInteger` interface.

**Return value**

- The sum of each integer multiplied by `maximum_integer_depth - its_depth + 1`.

### Examples
**Example 1**

- Input: `nested_list = [[1,1],2,[1,1]]`
- Output: `8`

**Example 2**

- Input: `nested_list = [1,[4,[6]]]`
- Output: `17`

**Example 3**

- Input: `nested_list = [0]`
- Output: `0`
