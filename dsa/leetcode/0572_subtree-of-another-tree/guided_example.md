# Guided Example: Subtree of Another Tree

We trace the step-by-step subtree candidate search traversal ($isSubtree$), structural isomorphism verification ($same(p, q)$), topological value comparison ($p.val == q.val$), nullability equivalence testing ($p \text{ is } q$), descendant completeness enforcement, and boolean disjunctive matching on representative binary trees:

- **Input:**
  - Main Tree $root = [3, 4, 5, 1, 2]$
    - Root $3$ has left child $4$ and right child $5$.
    - Node $4$ has left child $1$ and right child $2$.
    - Nodes $1, 2, 5$ are leaves.
  - Subtree Pattern $subRoot = [4, 1, 2]$
    - Root $4$ has left child $1$ and right child $2$.
- **Required output:** `true`
  - Subtree definition: A node in $root$ along with **all of its descendants**.
  - Strict isomorphism requirement: The candidate subtree must match $subRoot$ in node values, structure, and leaf terminations (extra descendants in $root$ disqualify the match).
- **Two-Tier Depth-First Search Trace:**
  - **Tier 1: Tree Traversal ($isSubtree(node, subRoot)$):**
    - Searches every candidate node in $root$ as a potential root for $subRoot$.
    - Rule:
      $$
      isSubtree(node) = same(node, subRoot) \lor isSubtree(node.left) \lor isSubtree(node.right)
      $$
  - **Tier 2: Exact Subtree Comparison ($same(p, q)$):**
    - Compares two trees rooted at $p$ and $q$:
      - If both are `None`: return `True`.
      - If exactly one is `None`: return `False`.
      - If $p.val \ne q.val$: return `False`.
      - Recurse: $same(p.left, q.left) \land same(p.right, q.right)$.
- **Execution trace on $root$ and $subRoot$:**
  - **Candidate 1: Test at Root Node 3:**
    - Call $same(\text{Node 3}, \text{Node 4})$:
      - Compare root values:
        $$
        p.val = 3, \quad q.val = 4 \implies 3 \ne 4 \implies \mathbf{False}
        $$
    - Node 3 does not match $subRoot$.
    - Recurse into children of Node 3: left child (Node 4) and right child (Node 5).
  - **Candidate 2: Test at Left Child Node 4:**
    - Call $same(\text{Node 4}, \text{Node 4})$:
      - **Check Root of Subtree:**
        - $p.val = 4, \; q.val = 4 \implies 4 == 4 \implies \mathbf{Match!}$
      - **Check Left Subtree ($p.left = \text{Node 1}, \; q.left = \text{Node 1}$):**
        - Compare values: $1 == 1 \implies \mathbf{Match!}$
        - Check children of Node 1:
          - Both have $left = None \implies \mathbf{True}$.
          - Both have $right = None \implies \mathbf{True}$.
        - Left branch is identical: $\mathbf{True}$.
      - **Check Right Subtree ($p.right = \text{Node 2}, \; q.right = \text{Node 2}$):**
        - Compare values: $2 == 2 \implies \mathbf{Match!}$
        - Check children of Node 2:
          - Both have $left = None \implies \mathbf{True}$.
          - Both have $right = None \implies \mathbf{True}$.
        - Right branch is identical: $\mathbf{True}$.
      - All sub-checks succeed:
        $$
        same(\text{Node 4}, \text{Node 4}) = \mathbf{True}
        $$
    - Valid subtree found at Node 4!
    - Short-circuit return: **`true`**.
- **Extra Descendant Disqualification Instance:**
  - Suppose in $root$, Node 2 has a left child $0$ ($root = [3, 4, 5, 1, 2, \text{null}, \text{null}, 0]$), while $subRoot = [4, 1, 2]$.
  - When comparing Node 2:
    - In $root$: $p.left = \text{Node 0}$.
    - In $subRoot$: $q.left = None$.
    - $same$ evaluates `p is q` $\implies False$.
    - The extra node $0$ prevents identity $\implies \mathbf{false}$.
- **Empty SubRoot vs Empty Root:**
  - If $root$ is exhausted (`None`) without finding a match, returns $\mathbf{false}$.
  - Every tree is a subtree of itself: $same(root, root) = \mathbf{true}$.

This instance demonstrates nested structural pattern matching across rooted directed acyclic graphs, mathematically proves why complete descendant validation is required for subtree isomorphism, and derives $O(M \cdot N)$ worst-case runtime and $O(H)$ space bounds.

---

## 1. Instance & Teaching Goal

Given two binary trees $root$ and $subRoot$:
Determine if there exists a node $u$ in $root$ such that the subtree rooted at $u$ is **structurally identical with the same node values** as $subRoot$.
Return `true` if such a subtree exists, otherwise `false`.

```text
Root Tree:                  SubRoot Tree:
      3                           4
     / \                         / \
    4   5                       1   2
   / \
  1   2

Subtree at Node 4 matches SubRoot exactly!
Result = true
```

### The Invariant of Complete Descendants
- A "subtree" is not just a subset of connected nodes; it must include **all descendants** down to the leaves.
- If $subRoot$ matches a portion of $root$, but that portion has additional children in $root$, it is **not** a valid subtree!
- The helper `same(p, q)` enforces this by ensuring both trees terminate simultaneously with `None` at corresponding positions.

---

## 2. Conceptual Foundation & Invariants

### 1. The Exact Tree Matcher `same(p, q)`:
1. If $p$ is `None` and $q$ is `None`: return `True`.
2. If $p$ is `None` or $q$ is `None`: return `False` (structural mismatch).
3. If $p.val \ne q.val$: return `False` (value mismatch).
4. Return $same(p.left, q.left) \land same(p.right, q.right)$.

### 2. The Outer Search `isSubtree(root, subRoot)`:
1. If $root$ is `None`: return `False`.
2. Check if the tree rooted here matches:
   $$
   same(root, subRoot)
   $$
3. If not, recurse into children:
   $$
   isSubtree(root.left, subRoot) \lor isSubtree(root.right, subRoot)
   $$

> **Structural Isomorphism Invariant.** Two binary trees are identical if and only if their root values match and their respective left and right subtrees are recursively identical.

---

## 3. Step-by-Step Worked Execution

We trace $root = [3, 4, 5, 1, 2]$ and $subRoot = [4, 1, 2]$:

---

### Step 1: Check Node 3
- $same(\text{Node 3}, \text{Node 4})$:
  - $p.val = 3, \; q.val = 4 \implies 3 \ne 4$.
  - Returns `False`.

---

### Step 2: Recurse on Left Child (Node 4)
- $same(\text{Node 4}, \text{Node 4})$:
  - Roots: $4 == 4$ (Match).
  - Left children: $same(\text{Node 1}, \text{Node 1})$:
    - $1 == 1$ (Match).
    - Children are $(None, None) \implies \mathbf{True}$.
  - Right children: $same(\text{Node 2}, \text{Node 2})$:
    - $2 == 2$ (Match).
    - Children are $(None, None) \implies \mathbf{True}$.
  - Returns $\mathbf{True}$.

---

### Step 3: Emit Output
Since $same(\text{Node 4}, subRoot)$ is True, $isSubtree$ returns **`True`**.

---

## 4. Complete Execution Trace

| Current Node in $root$ | Comparison Target | $same(p, q)$ Outcome | Subtree Search Status | Next Step |
|:---:|:---:|:---:|:---:|:---:|
| **Node 3** | $subRoot$ (Node 4) | **False** ($3 \ne 4$) | Continues search | Recurse left and right |
| **Node 4** | $subRoot$ (Node 4) | **True** (All nodes match) | **Match Found!** | Early exit with `True` |
| **Final** | — | — | — | **Result: `True`** |

---

## 5. Boundary Cases & Failure Modes

- **SubRoot Identical to Root:** Matches on the very first call at the root $\implies \mathbf{true}$.
- **Root Exhausted ($root = None$):** Base case triggers $\implies \mathbf{false}$.
- **Matching Values with Extra Child:**
  ```text
    Root: Node 4 -> Left 1, Right 2 (with child 0)
    SubRoot: Node 4 -> Left 1, Right 2
  ```
  `same(2, 2)` fails because Node 2 has a child in $root$ but no child in $subRoot \implies \mathbf{false}$.
- **Duplicate Node Values:** If multiple nodes have value 4, the disjunction `or` continues searching until an exact structural match is found.

---

## 6. Traps & Common Anti-Patterns

- **Searching Only Left When Values Match:** If $p.val == q.val$ but the subtrees differ, the search must NOT stop; it must continue searching in $root.left$ and $root.right$ for another matching candidate.
- **Ignoring Leaf Structure:** Verifying only that all nodes of $subRoot$ appear in $root$ without ensuring that $root$'s leaves terminate at the same level confuses a subtree with a general subgraph.
- **String Serialization Pitfalls:** Serializing trees (e.g. pre-order string `"3,4,1,2,5"`) without unique delimiters or null markers fails on prefixes (e.g. `"12"` vs `"2"`). Explicit node-by-node DFS is structurally foolproof.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $M$ be the number of nodes in $root$ ($\le 2000$) and $N$ be the number of nodes in $subRoot$ ($\le 1000$).
  - For each of the $M$ nodes in $root$, `same` traverses at most $N$ nodes.
  - Worst-case time: $\mathcal{O}(M \cdot N)$ (e.g. trees with all identical values).
  - For $M = 2000, N = 1000$, worst-case operations $\approx 2 \times 10^6$, completing in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H_M + H_N)$ call stack space proportional to the tree heights.