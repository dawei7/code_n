# N-ary Tree Level Order Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 429 |
| Difficulty | Medium |
| Topics | Tree, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/n-ary-tree-level-order-traversal/) |

## Problem Description
### Goal
Given the root of an N-ary tree, group its node values by distance from the root. The root forms the first level, all of its children form the next, and later levels contain children of the preceding level.

Return one list per occupied depth from top to bottom. Within a level, preserve natural left-to-right order induced by each parent's original child list and by parent order on the prior level. Missing or empty child lists add no placeholders. An empty tree returns an empty outer list, while every existing node appears exactly once.

### Function Contract
**Inputs**

- `root`: the app representation of an N-ary node as `[value, children]`, recursively, or `None` for an empty tree

**Return value**

- Return a list of levels, where each level contains node values in their original child order.

### Examples
**Example 1**

- Input: `root = [1, [[3, [[5, []], [6, []]]], [2, []], [4, []]]]`
- Output: `[[1], [3, 2, 4], [5, 6]]`

**Example 2**

- Input: `root = [7, []]`
- Output: `[[7]]`

**Example 3**

- Input: `root = None`
- Output: `[]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(w)$

<details>
<summary>Approach</summary>

#### General

**Keep exactly the pending frontier in a queue**

Begin with the root. At the start of each outer iteration, the queue contains precisely one depth level. Record its current length, remove exactly that many nodes from the front, append their values to one level list, and add their children to the back in stored order.

**Use the level size as a boundary marker**

Children appended while processing a level must not be included in that same output group. Capturing the queue length before removals separates the current frontier from the next one without sentinels or per-node depth fields.

**Why grouping and order are preserved**

Initially the queue contains only depth zero. If it contains one level in left-to-right order, processing those nodes in queue order outputs that level correctly, and appending each node's children in order produces the complete next level in left-to-right order. Induction over the depths proves every node appears in exactly its proper group.

#### Complexity detail

Every node enters and leaves the deque once, so time is $O(n)$. The queue contains at most the tree's maximum width `w`, giving $O(w)$ auxiliary space; the returned levels are excluded.

#### Alternatives and edge cases

- **Depth-first grouping:** pass a depth through recursion and append into a per-depth list; this also takes $O(n)$ time with $O(h)$ call-stack space.
- **Rebuild the queue after every front removal:** remains correct but copying all remaining nodes can take $O(n^2)$ on a wide level.
- **Sentinel markers:** can delimit levels but require careful handling to avoid an extra empty level.
- **Empty tree:** return an empty outer list.
- **Single node:** return one level containing one value.
- **Uneven branching:** the saved frontier length keeps children of different parents in the next level.

</details>
