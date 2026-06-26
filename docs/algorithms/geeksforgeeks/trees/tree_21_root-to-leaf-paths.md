# Binary Tree Root-to-Leaf Paths

| | |
|---|---|
| **ID** | `tree_21` |
| **Category** | trees |
| **Complexity (required)** | $O(N)$ Time, $O(H)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/) |

## Problem statement

Given the `root` of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.
The paths should be formatted as strings, with nodes separated by `"->"`.

**Input:** A binary tree `root` node.
**Output:** An array of strings representing the paths.

## When to use it

- To demonstrate proficiency in Backtracking-style DFS state management.
- A foundational building block for any path-finding problem (e.g., Path Sum II).

## Approach

**1. The "String Accumulator" DFS:**
To build a path from the root down to a leaf, we need to pass our history down the tree!
We write a recursive DFS function that takes the `current_node` AND the `current_path_string` as parameters.
When we visit a node, we immediately append its value to the string: `new_path = current_path_string + str(node.val)`.

**2. The Leaf Trigger:**
How do we know when a path is finished? When we hit a Leaf!
A leaf is defined strictly as `!node.left and !node.right`.
If the current node is a leaf, we are done! We append `new_path` directly to our global `results` array. We DO NOT recurse any further.

**3. The Forking Paths:**
If the node is NOT a leaf, the path must continue.
We simply append `"->"` to our string, and recursively pass it down to both children!
`dfs(node.left, new_path + "->")`
`dfs(node.right, new_path + "->")`
Because strings in Python/Java are immutable, passing `new_path` down one branch creates a completely independent physical copy of the string in memory. When the DFS backtracks to go down the other branch, the original `new_path` is completely untainted!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for tree_21: Root-to-Leaf Paths.

Return every root-to-leaf path as a list of node-index
lists. DFS from the root, accumulating the path; record
a copy when a leaf is reached.
"""


def solve(children, root, n):
    if n == 0 or root == -1:
        return []
    out = []

    def dfs(i, path):
        if i == -1:
            return
        path.append(i)
        if children[i][0] == -1 and children[i][1] == -1:
            out.append(list(path))
        else:
            dfs(children[i][0], path)
            dfs(children[i][1], path)
        path.pop()
    dfs(root, [])
    return out
```

</details>

## Walk-through

Tree:
```text
      1
    /   \
   2     3
    \
     5
```

1. **`dfs(1, "")`:**
   - `path` becomes `"1"`.
   - Node 1 has children. `path` becomes `"1->"`.
   - Calls `dfs(2, "1->")`.
   - Calls `dfs(3, "1->")`.
2. **`dfs(2, "1->")`:**
   - `path` becomes `"1->2"`.
   - Node 2 has a child (5). `path` becomes `"1->2->"`.
   - Calls `dfs(5, "1->2->")`.
3. **`dfs(5, "1->2->")`:**
   - `path` becomes `"1->2->5"`.
   - Node 5 is a leaf!
   - `res.append("1->2->5")`.
   - Returns to 2, then returns to 1.
4. **`dfs(3, "1->")`:**
   - `path` becomes `"1->3"`.
   - Node 3 is a leaf!
   - `res.append("1->3")`.

Final Result: `["1->2->5", "1->3"]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(\log N)$ |
| **Average** | $O(N)$ | $O(\log N)$ |
| **Worst** | $O(N^2)$ | $O(N)$ |

The DFS traversal visits every single node exactly once.
However, string concatenation (`+`) physically creates a new string in memory! In a completely skewed tree (linked list shape), the string grows by 1 character each time. The time taken to copy the string is 1 + 2 + 3 ... + N = $O(N^2)$ in the absolute worst case!
To guarantee strictly $O(N)$ time regardless of language optimizations, you must pass down an Array of values, and only `.join("->")` the array when you hit a leaf!
Space complexity is bounded by the recursive call stack $O(H)$.

## Variants & optimizations

- **Path Sum II (Backtracking Array):** Instead of a string, you pass a running Sum and an Array. If `sum == target`, you add a deep copy of the array to your results. Because arrays are mutable, you MUST explicitly `.pop()` the node off the array at the very end of the DFS function before it returns! This is standard Backtracking (`backtracking_01`).

## Real-world applications

- **File System Crawling:** Given a hierarchical directory tree (like `C:/`), this exact algorithm generates the absolute file paths (e.g. `C:/Users/David/Documents/file.txt`) for every single file in the system!

## Related algorithms in cOde(n)

- **[tree_01 - Pre-order Traversal](tree_01_preorder-traversal.md)** — The foundational pattern used to carry state down the tree.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
