# Guided Example: Binary Tree Paths

We trace the step-by-step root-to-leaf DFS descent, path string formatting, and backtracking unwinding on representative binary trees:

- **Input:** $\text{root} = [1, 2, 3, \text{null}, 5]$
- **Required output:** `["1->2->5", "1->3"]` (The two complete paths from the root to all leaf nodes)
- **Single Node Instance:** $\text{root} = [1] \implies \text{["1"]}$ (The root itself is a leaf; path contains no arrows)
- **Balanced Binary Tree:** $\text{root} = [1, 2, 3] \implies \text{["1->2", "1->3"]}$
- **Linear Skewed Tree:** $\text{root} = [1, 2, \text{null}, 3] \implies \text{["1->2->3"]}$ (Only one path terminating at the lone leaf)

This instance demonstrates depth-first search path aggregation, explains the exact leaf definition ($\text{left is None and right is None}$), contrasts mutable list backtracking with immutable string concatenation, and guarantees $O(N)$ node visits with $O(H)$ auxiliary call-stack memory.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree:
```text
        1
       / \
      2   3
       \
        5
```
Return all **root-to-leaf paths** formatted with `->` separators.
- Path 1: Root $1 \to$ Left child $2 \to$ Right child $5$ (Terminal leaf) $\implies \mathbf{\text{"1->2->5"}}$
- Path 2: Root $1 \to$ Right child $3$ (Terminal leaf) $\implies \mathbf{\text{"1->3"}}$
Output: `["1->2->5", "1->3"]`.

### The True Leaf Node Condition
A path must terminate at a **leaf node** (a node with **no left and no right child**):
$$
\text{is\_leaf}(\text{node}) \iff (\text{node.left is None}) \land (\text{node.right is None})
$$
Node $2$ has a null left child, but it is **not a leaf** because its right child ($5$) exists! We cannot stop at node $2$; we must descend until reaching node $5$.

---

## 2. Conceptual Foundation & Invariants

### DFS Path Construction Protocol `dfs(node, path)`
`path` maintains the sequence of node values from the root to the current node.
For each visited `node`:
1. **Append Current Value:**
   $$
   \text{path}.\text{append}(\text{str}(\text{node.val}))
   $$
2. **Leaf Node Base Check:**
   If $\text{node.left is None}$ and $\text{node.right is None}$:
   A complete root-to-leaf trajectory has matured!
   $$
   \text{results}.\text{append}(\text{"->"}.\text{join}(\text{path}))
   $$
3. **Recursive Subtree Branching:**
   - If $\text{node.left is not None}$:
     $$
     \text{dfs}(\text{node.left}, \; \text{path})
     $$
   - If $\text{node.right is not None}$:
     $$
     \text{dfs}(\text{node.right}, \; \text{path})
     $$
4. **Backtracking Restoration:**
   Remove current node from path before returning to ancestor:
   $$
   \text{path}.\text{pop}()
   $$

> **Invariant.** Inside `dfs(node, path)`, `path` contains the exact ordered sequence of nodes from the root down to `node`. When `node` is a leaf, joining `path` with `"->"` produces a complete and valid root-to-leaf path.

---

## 3. Step-by-Step Worked Execution

We trace the DFS execution on $\text{root} = [1, 2, 3, \text{null}, 5]$:
Initial call: `dfs(node = 1, path = [])`.

### Step 1: Visit Node 1 (Root)
- Append value: $\text{path} = [\text{"1"}]$.
- Leaf check: Left is 2, Right is 3 $\implies$ Not a leaf.
- Branch to Left Child: call `dfs(2, ["1"])`.

---

### Step 2: Visit Node 2
- Append value: $\text{path} = [\text{"1"}, \text{"2"}]$.
- Leaf check: Left is None, but Right is 5 $\implies$ Not a leaf!
- Branch to Right Child: call `dfs(5, ["1", "2"])`.

---

### Step 3: Visit Node 5 (Leaf Detected!)
- Append value: $\text{path} = [\text{"1"}, \text{"2"}, \text{"5"}]$.
- Leaf check:
  $$
  \text{left is None} \land \text{right is None} \implies \mathbf{\text{True (Leaf!)}}
  $$
- Format path:
  $$
  \text{"->"}.\text{join}([\text{"1"}, \text{"2"}, \text{"5"}]) = \mathbf{\text{"1->2->5"}}
  $$
  $\text{results}.\text{append}(\text{"1->2->5"})$.
- Backtrack: $\text{path}.\text{pop}() \implies [\text{"1"}, \text{"2"}]$.
- Return to Node 2.

---

### Step 4: Backtrack from Node 2
- Both children of Node 2 handled.
- Backtrack: $\text{path}.\text{pop}() \implies [\text{"1"}]$.
- Return to Node 1.

---

### Step 5: Visit Node 3 (Leaf Detected!)
- Branch to Right Child of Node 1: call `dfs(3, ["1"])`.
- Append value: $\text{path} = [\text{"1"}, \text{"3"}]$.
- Leaf check:
  $$
  \text{left is None} \land \text{right is None} \implies \mathbf{\text{True (Leaf!)}}
  $$
- Format path:
  $$
  \text{"->"}.\text{join}([\text{"1"}, \text{"3"}]) = \mathbf{\text{"1->3"}}
  $$
  $\text{results}.\text{append}(\text{"1->3"})$.
- Backtrack: $\text{path}.\text{pop}() \implies [\text{"1"}]$.
- Return to Node 1.

---

### Step 6: Backtrack from Root
- Both children of Node 1 handled.
- Backtrack: $\text{path}.\text{pop}() \implies []$.
- Traversal complete!

Collected output:
$$
\mathbf{[\text{"1->2->5"}, \text{"1->3"}]}
$$

---

## 4. Complete Execution Trace

```text
dfs(1): path = ["1"]
  dfs(2): path = ["1", "2"]
    dfs(5): path = ["1", "2", "5"] -> LEAF! -> Record "1->2->5"
    pop -> path = ["1", "2"]
  pop -> path = ["1"]
  dfs(3): path = ["1", "3"] -> LEAF! -> Record "1->3"
  pop -> path = ["1"]
pop -> path = []

Final Paths: ["1->2->5", "1->3"]
```

| Step | Action | Visited Node | Current `path` State | Leaf Node? | Emitted Path String | Next Transition |
|:---:|:---|:---:|:---:|:---:|:---:|:---|
| **1** | Enter DFS | 1 | `["1"]` | No (Children 2, 3) | - | Descend Left to Node 2 |
| **2** | Enter DFS | 2 | `["1", "2"]` | No (Right child 5) | - | Descend Right to Node 5 |
| **3** | Enter DFS | 5 | `["1", "2", "5"]` | **Yes (Leaf)** | **`"1->2->5"`** | Backtrack to Node 2 |
| **4** | Backtrack | 2 | `["1"]` | - | - | Backtrack to Node 1 |
| **5** | Enter DFS | 3 | `["1", "3"]` | **Yes (Leaf)** | **`"1->3"`** | Backtrack to Node 1 |
| **6** | Backtrack | 1 | `[]` | - | - | **Terminates** |

---

## 5. Algorithmic Correctness

**Soundness.** Every recorded path is emitted only when a node satisfies $\text{node.left is None and node.right is None}$. Because the traversal begins at the tree root and only advances across parent-to-child edges, the sequence in `path` represents a continuous ancestor-to-descendant trajectory ending at a leaf.

**Completeness.** DFS visits every node reachable from the root. Every leaf node has a unique path from the root. Since every valid child pointer is traversed, every leaf node in the tree is reached, and its unique path is generated.

---

## 6. Traps This Instance Exposes

- **Premature Null Evaluation:** If the base case checks `if not node: record_path()`, every leaf node will hit the null base case twice (once for left child, once for right child), emitting duplicate paths! The leaf check must be performed on the node itself (`if not node.left and not node.right`).
- **Half-Leaf Confusion:** A node with one child (like node 2, which has a right child but no left child) is **not a leaf**. Emitting a path at node 2 (`"1->2"`) would be invalid because node 2 has an outgoing branch.
- **Path Copy Overhead:** Appending to a shared mutable list and popping takes $O(1)$ amortized time per step. In contrast, concatenating strings at every level (`path + "->" + str(node.val)`) creates a new string at each step, consuming $O(H^2)$ memory per branch.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot H)$, where $N$ is the number of nodes and $H$ is the tree height. DFS visits each node once ($O(N)$). When reaching a leaf, joining the path string takes $O(H)$ time. With $L$ leaves ($L \le N$), total string formatting time is $O(L \cdot H) = O(N \cdot H)$ in the worst case (or $O(N \log N)$ for balanced trees).
- **Auxiliary Space Complexity:** $O(H)$ auxiliary memory for the recursion call stack and `path` array, where $H \le N$ is the maximum depth of the tree.