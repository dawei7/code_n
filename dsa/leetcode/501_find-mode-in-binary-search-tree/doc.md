# Find Mode in Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 501 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/find-mode-in-binary-search-tree/) |

## Problem Description
### Goal
Given a nonempty binary search tree that may contain duplicate values, count how often every stored value occurs. The tree permits equal keys on either side under its ordering definition, so repeated values remain separate nodes even though they contribute to the same frequency.

Return all modes: every value whose occurrence count equals the maximum frequency in the tree. If several values tie, return them in any order and list each mode once. The result contains values rather than nodes or counts. Meet the follow-up without extra auxiliary space beyond the implicit recursion stack when using the BST's inorder ordering.

### Function Contract
**Inputs**

- `root`: the root node of a nonempty binary search tree

**Return value**

- All tree values whose occurrence count equals the maximum frequency

### Examples
**Example 1**

- Input: `root = [1, null, 2, 2]`
- Output: `[2]`

**Example 2**

- Input: `root = [0]`
- Output: `[0]`

**Example 3**

- Input: `root = [1, null, 2]`
- Output: `[1, 2]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Exploit sorted inorder order**

An inorder traversal of a binary search tree lists values in nondecreasing order. Equal values therefore form one contiguous run, so their frequencies can be measured without a hash table.

**Track the current run and best run**

Visit nodes iteratively with an explicit stack. If the current value equals the previous value, extend the run; otherwise start a new run of length one. When the run exceeds the best frequency, replace the modes with the current value. When it ties, append the value.

**Why each mode is recorded exactly once**

All occurrences of one value are consecutive, and only the final node of its run can reach that value's full frequency. A later distinct value starts a new run. Comparing every run length against the global maximum therefore retains precisely all and only maximum-frequency values.

**Use iteration for deep trees**

The explicit traversal stack avoids recursion-depth failure on a highly skewed tree while preserving the same inorder sequence.

#### Complexity detail

Every one of the `n` nodes is pushed and popped once, giving $O(n)$ time. The traversal stack uses $O(h)$ space for tree height `h`, and the returned modes can contain $O(n)$ values, giving $O(n)$ total space including output.

#### Alternatives and edge cases

- **Frequency dictionary:** counts values during any traversal in $O(n)$ time but uses $O(k)$ extra space for `k` distinct values.
- **Recursive inorder:** uses the same run logic but can overflow the language recursion limit on a skewed tree.
- **Count each value by rescanning:** is correct but takes $O(n^2)$ time when many values are distinct.
- **All values distinct:** every value is a mode.
- **All values equal:** return that value once.
- **Negative values:** the previous-value state must not use a numeric sentinel that could collide.
- **Multiple modes:** output order is not significant.

</details>
