# Clone N-ary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1490 |
| Difficulty | Medium |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/clone-n-ary-tree/) |

## Problem Description
### Goal

An N-ary tree node stores an integer value and an ordered list of zero or more child nodes. Given the tree's root, construct a deep copy of the entire tree.

The returned root must belong to a newly allocated tree. For every original node, its copy must hold the same value, and the copied node's children must be the copies of the original children in the same left-to-right order. No node object in the result may be one of the original node objects. Return null when the input tree is empty.

### Function Contract
**Inputs**

Let $N$ be the number of nodes and $H$ the tree height.

- Native `cloneTree(root)` receives the root of an N-ary tree whose nodes expose `val` and an ordered `children` list.
- The structure is a tree: every non-root node occurs in exactly one parent's child list.
- A node may be a leaf with an empty child list, and `root` may be null.
- The app-local `solve(root)` receives the same structure serialized recursively as `[value, children]`, where every element of `children` is another encoded node.

**Return value**

Return the root of a newly allocated N-ary tree with the same values, shape, and child ordering as the input. For the app-local representation, return an equal but independently allocated nested `[value, children]` structure. Return `None` for an empty tree.

### Examples
**Example 1**

- Input: `root = [1, [[3, [[5, []], [6, []]]], [2, []], [4, []]]]`
- Output: `[1, [[3, [[5, []], [6, []]]], [2, []], [4, []]]]`
- Explanation: The clone preserves the root's child order `3, 2, 4` and the two children below node `3`, but every encoded node list is newly allocated.

**Example 2**

- Input: `root = [1, [[2, []], [3, [[6, []], [7, [[11, [[14, []]]]]]]], [4, [[8, [[12, []]]]]], [5, [[9, [[13, []]]], [10, []]]]]]`
- Output: `[1, [[2, []], [3, [[6, []], [7, [[11, [[14, []]]]]]]], [4, [[8, [[12, []]]]]], [5, [[9, [[13, []]]], [10, []]]]]]`
- Explanation: Different branching factors and depths are copied without flattening or reordering the tree.

**Example 3**

- Input: `root = None`
- Output: `None`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Copy identities rather than merely repeating values**

A deep copy is about node identity. Returning the original root, reusing an original child, or constructing only a matching traversal would not satisfy the contract even if all visible values looked correct. Each original node therefore needs one distinct copied node, and every copied edge must lead to another copied node.

Unlike a general graph, this input is guaranteed to be a tree. Each non-root node is reached from exactly one parent, so there is no need to deduplicate shared targets or break cycles. A hash table is useful for a graph-shaped extension, but it would store information that the tree contract already supplies.

**Create a root copy and carry corresponding node pairs**

Handle a null root immediately. Otherwise allocate `[root_value, []]` for the app-local copy and place the pair `(original_root, copied_root)` on a stack.

When a pair is removed, scan the original node's children from left to right. For each original child, allocate `[child_value, []]`, append it immediately to the copied parent's child list, and place the new `(original_child, copied_child)` pair on the stack. Appending during the scan fixes sibling order before later traversal order can matter.

The platform-native artifact applies exactly the same construction to `Node` objects. It never inserts an original node into a copied `children` list.

**Why every node is copied exactly once**

The root gets one copy before traversal begins. Every other original node has one unique parent. It is encountered exactly once while that parent's child list is scanned, and that encounter creates exactly one copy. Consequently there is a one-to-one correspondence $c$ from original nodes to newly allocated nodes.

For every original edge from parent $u$ to its $i$-th child $v$, processing $u$ appends $c(v)$ at index $i$ of $c(u)$'s child list. Thus the construction preserves both adjacency and child order. Values are assigned when each copy is created, so corresponding nodes also preserve their values. Induction from the root over tree depth proves that the returned structure is a complete, ordered deep copy.

**Why an explicit stack is useful**

A recursive depth-first clone expresses the same recurrence elegantly, but N-ary trees can be much deeper than typical balanced examples. The explicit stack stores unfinished node pairs on the heap and avoids depending on the language's call-stack limit. It also makes the object-allocation boundary visible: a child copy is created before that pair is scheduled.

#### Complexity detail

Every one of the $N$ original nodes is paired, pushed, popped, and copied once. Across the whole traversal, all child lists contain exactly $N-1$ edges, so scanning and appending those edges takes $O(N)$ time.

The returned tree itself contains $N$ newly allocated nodes and is required output. Excluding output, the explicit stack can contain $O(N)$ pending pairs for a wide tree. The app-local nested lists likewise require $O(N)$ output space. Therefore the stated total space bound is $O(N)$.

#### Alternatives and edge cases

- **Recursive depth-first clone:** return a new node whose child list is formed by recursively cloning each original child. This is also $O(N)$ time, but a very deep tree can overflow the call stack.
- **Breadth-first clone:** keep corresponding original/copy pairs in a queue instead of a stack. It has the same $O(N)$ bounds and may make level-by-level inspection easier, but can retain an entire wide level.
- **Identity map:** map every original node to its copy before wiring edges. This is necessary for DAGs, shared children, or cycles, but the guaranteed tree has one incoming parent edge per non-root node, so the map is optional overhead here.
- **Repeated child-list concatenation:** building `children = children + [copy]` copies the entire partial list on every append; a wide node can therefore turn an otherwise linear clone into $O(N^2)$ time.
- **Return the original root:** preserves all values and edges but is a shallow alias, not a clone.
- **Reuse original leaves:** still violates deep-copy identity even though leaves have no outgoing edges.
- **Empty tree:** return null without allocating a node.
- **Single node:** allocate one leaf with the same value and an empty child list.
- **Wide root:** preserve every sibling's original index; using a stack must not reverse the copied child list.
- **Deep chain:** the explicit stack avoids recursive call-depth failure.
- **Repeated values:** values do not identify nodes; equal-valued nodes still require separate copies.
- **Empty child lists:** preserve leaves as leaves rather than using null in place of the list.
- **Mutation independence:** changing a copied value or copied child list must not modify the original tree.

</details>
