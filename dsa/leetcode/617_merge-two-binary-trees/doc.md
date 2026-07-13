# Merge Two Binary Trees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 617 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/merge-two-binary-trees/) |

## Problem Description
### Goal
Given two binary trees `root1` and `root2`, place their roots and corresponding child positions over one another and merge them into a new binary tree. When both trees contain a node at the same position, the merged node's value is the sum of their values.

When only one tree contains a node at a position, use that non-null node and its structure in the merged tree. Begin the process at the two roots and apply the same rule recursively to left and right children. Return the root of the merged tree; if one input root is null, the other tree supplies the result.

### Function Contract
**Inputs**

- `root1`: the root of the first binary tree, or null
- `root2`: the root of the second binary tree, or null

**Return value**

- The root of a binary tree whose shape is the union of the input shapes
- At a shared position, the result value is the sum of both input values
- At a position occupied by only one tree, the result carries that node's value and descendants

### Examples
**Example 1**

- Input: `root1 = [1,3,2,5]`, `root2 = [2,1,3,null,4,null,7]`
- Output: `[3,4,5,5,4,null,7]`

**Example 2**

- Input: `root1 = [1]`, `root2 = [1,2]`
- Output: `[2,2]`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Define the result at one tree position**

If both corresponding nodes are null, the merged position is null. Otherwise create a result node whose value is the first value when present plus the second value when present. Treating an absent value as zero handles shared and one-sided positions uniformly.

**Carry corresponding positions in a worklist**

Create the merged root, then keep triples containing a result node and the two input nodes that produced it. For each left and right direction, create a child whenever either input has one, attach the summed child, and enqueue the new triple. A deque keeps every removal constant-time and avoids recursion-depth limits on skewed trees.

**Why the construction is exact**

The initial node has the required root sum. Whenever a processed triple is correct, each child triple is created exactly when at least one corresponding input child exists and receives exactly the values present there. Breadth-first induction therefore establishes the union shape and required sum at every reachable position; positions absent from both trees are never created.

**Keep the inputs independent**

Creating fresh nodes also for one-sided regions avoids sharing result subtrees with either input. That is not required by the platform, but it gives the app-local reference a clear nonmutating contract.

#### Complexity detail

Let `N` be the number of occupied positions in the union of the two tree shapes. Each such position is created and processed once, so time is $O(N)$. The fresh result contains `N` nodes and the deque holds at most one level's width, giving $O(N)$ total space.

#### Alternatives and edge cases

- **Mutate the first tree:** add second-tree values into existing nodes and attach missing subtrees; this can reduce allocations but changes an input and may share nodes with the result.
- **Recursive depth-first merge:** expresses the positional recurrence compactly in $O(N)$ time, but a legal deeply skewed tree can exceed Python's recursion limit.
- **Repeated root-to-position lookup:** construct each result node by navigating its full path again from the root; it is correct but costs $O(N^2)$ time on a chain.
- **Breadth-first merge with `list.pop(0)`:** functionally correct, but repeated front deletion can add avoidable shifting on a wide traversal.
- If both roots are null, return null.
- If only one tree occupies a region, copy that entire region unchanged in value and shape.
- Positive and negative values are added normally and may cancel to zero without removing the node.
- Different input heights require no padding; missing children are treated as null.

</details>
