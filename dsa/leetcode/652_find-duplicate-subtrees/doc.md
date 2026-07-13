# Find Duplicate Subtrees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 652 |
| Difficulty | Medium |
| Topics | Hash Table, Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/find-duplicate-subtrees/) |

## Problem Description
### Goal
Given the root of a binary tree, find every kind of subtree that occurs at least twice. Two subtrees are duplicates only when they have the same structure and the same node values, including the placement of null children.

Return the root node of any one occurrence for each kind of duplicate subtree. A kind that appears three or more times still contributes only one representative, and representatives may be returned in any order. Occurrences may be rooted at different depths and may overlap through ancestor-descendant relationships.

### Function Contract
**Inputs**

- `root`: the root node of a binary tree, or `None` for an empty tree

**Return value**

- A list containing one representative node for each duplicated subtree; representatives may appear in any order

### Examples
**Example 1**

- Input: `root = [1, 2, 3, 4, null, 2, 4, null, null, 4]`
- Output: `[[2, 4], [4]]`

**Example 2**

- Input: `root = [2, 1, 1]`
- Output: `[[1]]`

**Example 3**

- Input: `root = [2, 2, 2, 3, null, 3, null]`
- Output: `[[2, 3], [3]]`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**A subtree is determined by three identities**

Two nodes head identical subtrees exactly when their values match and their left and right subtrees are respectively identical. A postorder traversal supplies the child identities before processing their parent, so each node can be described by the tuple `(value, left_id, right_id)`.

Reserve one identity for a missing child. Intern every new tuple in a hash table and assign it a compact integer ID. Equal tuples reuse the same ID, turning structural equality into constant-time integer equality at their parents.

**Report each duplicate class once**

Maintain a frequency for every structural ID. The first occurrence establishes the class, the second proves that it is duplicated, and later occurrences add no new answer class. Append the current node only when its ID's count changes from one to two.

**Why the returned representatives are complete and unique**

Postorder induction shows that equal IDs imply equal node values and equal child IDs, hence identical complete subtrees. The reverse also holds because identical children and values form the same interned tuple. Every duplicated structure therefore reaches count two and contributes a representative, while the count-two rule prevents a third or later copy from contributing another. The traversal returns exactly one node from every duplicate class.

#### Complexity detail

Each of the `N` nodes is visited once and performs expected $O(1)$ hash-table operations on a fixed-size tuple, giving $O(N)$ expected time. Structural IDs, frequencies, the traversal stack, and the result together use $O(N)$ space.

#### Alternatives and edge cases

- **Serialize each subtree as a string:** is conceptually simple, but repeatedly copying long descendant serializations can require $O(N^2)$ time on a skewed tree.
- **Compare every pair of roots recursively:** avoids hashing but repeats the same structural comparisons and can become substantially worse than linear.
- **Hash full serializations:** can reduce stored key size, but collision handling is required for deterministic correctness; interned child IDs need no probabilistic assumption.
- An empty tree returns an empty list.
- Equal node values alone do not make duplicate subtrees; both descendant structures must also match.
- A structure occurring three or more times still contributes only one representative.
- Leaf duplicates are valid duplicate subtrees and use the missing-child identity on both sides.

</details>
