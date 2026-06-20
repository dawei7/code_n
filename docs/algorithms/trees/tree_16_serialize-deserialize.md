# Serialize and Deserialize Binary Tree

| | |
|---|---|
| **ID** | `tree_16` |
| **Category** | trees |
| **Complexity (required)** | $O(N)$ Time, $O(N)$ Space |
| **Difficulty** | 7/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) |

## Problem statement

Design an algorithm to serialize and deserialize a binary tree.
Serialization is the process of converting a data structure into a sequence of bits (or a string) so that it can be stored in a file or transmitted across a network.
Deserialization is the process of taking that string and reconstructing the exact original tree structure in memory.

**Input:** A binary tree `root` node (to serialize), or a `string` (to deserialize).
**Output:** A `string` (from serialize), or a binary tree `root` node (from deserialize).

## When to use it

- To save the exact topological state of a Tree Data Structure to a hard drive or database.
- The definitive test of whether you truly understand how Tree Traversals map to 1D arrays.

## Approach

**1. The "Null" Pointer Problem:**
If you just do a standard Pre-Order traversal (`[1, 2, 3]`), it is mathematically impossible to reconstruct the tree! Why? Because `[1, 2, 3]` could be a tree where 1 is root, 2 is left, 3 is left of 2. OR 1 is root, 2 is right, 3 is right of 2. They look identical!
The ONLY way to perfectly capture the topology of a tree is to record EXACTLY where the leaves end by explicitly storing `null` pointers!
We will represent `null` as the string `"N"`.
Our Pre-Order serialization for `1 -> 2 -> null` will be: `"1,2,N,N,N"`.

**2. Serialization (Tree to String):**
We use a standard DFS Pre-Order traversal.
1. If the node is `null`, append `"N"` to our array.
2. Otherwise, append `str(node.val)`.
3. Recursively serialize the Left child.
4. Recursively serialize the Right child.
Finally, we join the array with commas: `"1,2,N,N,3,N,N"`.

**3. Deserialization (String to Tree):**
We split the string by commas into a Queue of values (or a List with an Iterator).
Because the string was generated via Pre-Order (Root, Left, Right), the very first element in the Queue is GUARANTEED to be the Root!
We write a recursive function:
1. Pop the first element from the Queue.
2. If it is `"N"`, return `None` (we hit a leaf boundary).
3. Otherwise, create a new `TreeNode(val)`.
4. Recursively call the function to build its `left` child!
5. Recursively call the function to build its `right` child!
6. Return the constructed Node.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for tree_16: Serialize / Deserialize.

Standard format: preorder traversal with 'N' for null,
comma-separated. The serialize-then-deserialize round-trip
preserves the structure on a valid binary tree. Deserialization
uses the original node indices from the tokens so the round-trip
is a structural identity.
"""


def solve(children, root, n):
    """Serialize the tree, then deserialize it. Return the new children list."""
    # Serialize: preorder with 'N' for null.
    parts = []

    def ser(u):
        if u == -1:
            parts.append("N")
            return
        parts.append(str(u))
        ser(children[u][0])
        ser(children[u][1])

    ser(root)
    tokens = ",".join(parts).split(",")

    # Deserialize: pre-register each new node at the index named
    # by the token, then recurse on left/right.
    idx = [0]
    new_children = []

    def build():
        tok = tokens[idx[0]]
        idx[0] += 1
        if tok == "N":
            return -1
        node_idx = int(tok)
        while len(new_children) <= node_idx:
            new_children.append([-1, -1])
        new_children[node_idx][0] = build()
        new_children[node_idx][1] = build()
        return node_idx

    build()
    return new_children
```

</details>

## Walk-through

Tree:
```text
    1
   / \
  2   3
```

**Serialize:**
1. `dfs(1)`: Append `"1"`.
   2. `dfs(2)`: Append `"2"`.
      3. `dfs(null)`: Append `"N"`.
      4. `dfs(null)`: Append `"N"`.
   5. `dfs(3)`: Append `"3"`.
      6. `dfs(null)`: Append `"N"`.
      7. `dfs(null)`: Append `"N"`.
String: `"1,2,N,N,3,N,N"`.

**Deserialize:**
`vals = ["1", "2", "N", "N", "3", "N", "N"]`. `i = 0`.
1. `dfs()` reads `"1"`. Creates `Node(1)`. Calls `dfs()` for left.
   2. `dfs()` reads `"2"`. Creates `Node(2)`. Calls `dfs()` for left.
      3. `dfs()` reads `"N"`. Returns `None`. (Node 2's left is null).
      4. `dfs()` reads `"N"`. Returns `None`. (Node 2's right is null).
   5. Node 1's left is now fully built! Calls `dfs()` for right.
   6. `dfs()` reads `"3"`. Creates `Node(3)`. Calls `dfs()` for left.
      7. `dfs()` reads `"N"`. Returns `None`.
      8. `dfs()` reads `"N"`. Returns `None`.
   9. Node 1's right is fully built!
10. Returns `Node(1)`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(N)$ |
| **Average** | $O(N)$ | $O(N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

In both Serialization and Deserialization, we process every single node exactly once. Time complexity is strictly $O(N)$.
Space complexity requires $O(N)$ memory to physically store the massive serialized string and the split array. The recursive call stack also takes $O(H)$ space, but $O(N)$ dominates.

## Variants & optimizations

- **Level-Order Serialization (BFS):** LeetCode's actual visual representation of trees (e.g. `[1, 2, 3, null, null, 4, 5]`) uses BFS! You can serialize using a Queue. Instead of pushing just valid nodes, you push `null` pointers too. During deserialization, you use a Queue to reconstruct the tree level by level!
- **BST Serialization ($O(N)$ Time, $O(1)$ String Space!):** If the tree is GUARANTEED to be a Binary Search Tree, you DO NOT need to store `"N"` null markers! You just output a standard Pre-Order string (`"5,3,2,4,7,6"`). Because of the BST bounds property (`tree_06`), the deserializer mathematically knows EXACTLY when to stop building the left branch and switch to the right branch by passing a `max_bound` down the recursive stack! This saves massive amounts of disk space.

## Real-world applications

- **Network Payloads (JSON):** Every time a Web API sends a complex nested hierarchical JSON object to a frontend client, it undergoes this exact architectural process of converting a memory graph into a 1D string, and parsing it back into memory!

## Related algorithms in cOde(n)

- **[tree_01 - Pre-order Traversal](tree_01_preorder-traversal.md)** — The foundational traversal strategy used in this specific implementation.
- **[tree_05 - Level Order Traversal](tree_05_level-order-traversal.md)** — The foundational traversal strategy if you choose to implement the BFS variant instead.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
