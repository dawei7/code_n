# Boundary Traversal of Binary Tree

| | |
|---|---|
| **ID** | `tree_19` |
| **Category** | trees |
| **Complexity (required)** | $O(N)$ Time, $O(H)$ Space |
| **Difficulty** | 6/10 |
| **Interview relevance** | 5/10 |
| **GeeksForGeeks Equivalent** | [Boundary Traversal of binary tree](https://www.geeksforgeeks.org/boundary-traversal-of-binary-tree/) |

## Problem statement

Given a binary tree, print boundary nodes of the binary tree Anti-Clockwise starting from the root.
The boundary includes:
1. The Left Boundary (excluding leaves).
2. All the Leaf Nodes (from left to right).
3. The Right Boundary (excluding leaves, in reverse order).

**Input:** A binary tree `root` node.
**Output:** An array of integers representing the anti-clockwise boundary.

## When to use it

- To test your ability to break a complex problem into smaller, modular, highly-specific tree traversal functions.

## Approach

This problem seems overwhelming, but it becomes trivial if you break it into 4 distinct, sequential steps.

**1. The Root:**
Add the root to the result array (unless the root is a leaf itself, in which case we don't want to add it twice!).

**2. The Left Boundary (Top-Down):**
Create a function that starts at `root.left`.
We add the node to our result. We move to `node.left`.
What if `node.left` is null? The boundary doesn't end! It just zig-zags! We move to `node.right` instead.
We continue this until we hit a leaf node. We DO NOT add the leaf node (leaves are handled in step 3).

**3. The Leaves (Left-to-Right):**
Create a standard Pre-Order DFS function (`tree_01`).
If the node is a leaf (`!node.left and !node.right`), add it to the result!
Otherwise, recursively search `node.left` and `node.right`. This mathematically guarantees the leaves are added perfectly from left to right.

**4. The Right Boundary (Bottom-Up):**
Create a function that starts at `root.right`.
We move to `node.right`. If it's null, we zig-zag to `node.left`.
We continue until we hit a leaf (do not add it).
BUT WAIT! The boundary must be anti-clockwise! We are traveling DOWN the right boundary, but we need to print it UPWARDS!
How do we reverse it? We use a temporary array (or the recursive call stack) to collect the nodes as we go down, and then append them to our main result array in reverse!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for tree_19: Boundary Traversal.

Walk the boundary of a binary tree anti-clockwise:
left edge top-to-bottom, then leaves left-to-right, then
right edge bottom-to-top.
"""


def solve(children, root, n):
    """Boundary traversal: left edge + leaves + right edge (reversed)."""
    if root == -1:
        return []
    out = [root]

    def is_leaf(u):
        return children[u][0] == -1 and children[u][1] == -1

    def left_boundary(u):
        cur = children[u][0]
        while cur != -1:
            if not is_leaf(cur):
                out.append(cur)
            cur = children[cur][0] if children[cur][0] != -1 else children[cur][1]

    def leaves(u):
        if u == -1:
            return
        if is_leaf(u):
            out.append(u)
        else:
            leaves(children[u][0])
            leaves(children[u][1])

    def right_boundary(u):
        stack = []
        cur = children[u][1]
        while cur != -1:
            if not is_leaf(cur):
                stack.append(cur)
            cur = children[cur][1] if children[cur][1] != -1 else children[cur][0]
        while stack:
            out.append(stack.pop())

    if not is_leaf(root):
        left_boundary(root)
        leaves(root)
        right_boundary(root)
    # If root is a leaf, leaves() would only emit root; we
    # already added it. The contract: include the root exactly once.
    return out
```

</details>

## Walk-through

Tree:
```text
        1
      /   \
     2     3
    / \   / 
   4   5 6   
      / \
     7   8
```

1. **Root:** Add `1`. `res = [1]`.
2. **Left Boundary:** Start at `2`.
   - `2` is not a leaf. Add `2`. `res = [1, 2]`.
   - Go left to `4`.
   - `4` is a leaf. Stop!
3. **Leaves:** Start DFS from root `1`.
   - Hits `4` (leaf). Add `4`. `res = [1, 2, 4]`.
   - Hits `7` (leaf). Add `7`. `res = [1, 2, 4, 7]`.
   - Hits `8` (leaf). Add `8`. `res = [1, 2, 4, 7, 8]`.
   - Hits `6` (leaf). Add `6`. `res = [1, 2, 4, 7, 8, 6]`.
4. **Right Boundary:** Start at `3`.
   - `3` is not a leaf. Add `3` to `tmp = [3]`.
   - `3` has no right child! Zig-zag left to `6`.
   - `6` is a leaf. Stop!
   - Reverse `tmp`: `[3]`.
   - Append to res: `res = [1, 2, 4, 7, 8, 6, 3]`.

Result: `[1, 2, 4, 7, 8, 6, 3]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(H)$ |
| **Average** | $O(N)$ | $O(H)$ |
| **Worst** | $O(N)$ | $O(N)$ |

The left boundary takes $O(H)$ time. The right boundary takes $O(H)$ time. The leaf gathering traverses the entire tree taking $O(N)$ time.
Total time complexity is exactly $O(N)$.
Space complexity is bounded by the recursive call stack for gathering leaves, and the temporary array for the right boundary. The maximum space is proportional to the height of the tree $O(H)$, which degrades to $O(N)$ in the worst case.

## Variants & optimizations

- **Anti-Clockwise Matrix Spiral (`array_03`):** The exact conceptual equivalent of this problem applied to a 2D Array! You peel off the top, right, bottom, and left boundaries in a while loop.

## Real-world applications

- **Convex Hull Rendering:** In graphics, given a massive hierarchical layout of shapes, calculating the "Boundary" nodes allows the system to instantly draw the outer bounding silhouette without needing to process the thousands of interior shapes.

## Related algorithms in cOde(n)

- **[tree_18 - Right Side View](tree_18_right-side-view.md)** — A visually similar problem, but the "View" is strictly vertical, whereas the "Boundary" follows the structural edges even if they zig-zag inwards.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
