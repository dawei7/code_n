# Guided Example: House Robber III

We trace the step-by-step tree dynamic programming formulation, bottom-up state tuple propagation `(rob_curr, skip_curr)`, parent-child exclusion constraints ($rob \implies \text{skip children}$), and subtree value maximization on representative binary tree instances:

- **Input:**
  $$
  \text{root} = [3, 2, 3, \text{null}, 3, \text{null}, 1]
  $$
- **Required output:** $7$
  - If root $3$ is robbed: cannot rob children ($2$ and $3$), but can rob grandchildren ($3$ and $1$):
    $$
    \text{Total} = 3 + 3 + 1 = \mathbf{7}
    $$
  - If root $3$ is skipped: can rob children ($2$ and $3$):
    $$
    \text{Total} = 2 + 3 = 5
    $$
  - Global maximum: $\max(7, 5) = \mathbf{7}$
- **Child Dominant Alternative:** $\text{root} = [3, 4, 5, 1, 3, \text{null}, 1] \implies 9$ (skipping root $3$ to rob children $4 + 5 = 9$)
- **Single Node Tree:** $\text{root} = [4] \implies 4$
- **Empty Tree Base Case:** $\text{root} = [] \implies 0$

This instance demonstrates tree DP on hierarchical independent sets, mathematically proves why returning a 2-element tuple eliminates redundant overlapping subproblem recalculations, contrasts $O(N)$ bottom-up DFS with exponential naive recursion, and analyzes $O(H)$ recursion stack space bounds.

---

## 1. Instance & Teaching Goal

Given houses connected in a binary tree hierarchy:
$$
\text{root} = [3, 2, 3, \text{null}, 3, \text{null}, 1]
$$
Find the maximum money that can be robbed without robbing any two directly-linked (parent-child) houses on the same night:

```text
Tree Topology:
          3  <-- Level 0 (Root)
        /   \
       2     3  <-- Level 1 (Children)
        \     \
         3     1  <-- Level 2 (Grandchildren)

Strategy Comparison:
Plan A (Rob Root):
- Rob Root (3)
- Must Skip Children (2 and 3)
- Can Rob Grandchildren (3 and 1)
- Total = 3 + 3 + 1 = 7

Plan B (Skip Root):
- Skip Root (3)
- Can Rob Children (2 and 3)
- Grandchildren are skipped
- Total = 2 + 3 = 5

Optimal Outcome: 7
```

---

## 2. Conceptual Foundation & Invariants

### 1. The 2-State Subtree Return Contract
For every node `u`, define `dfs(u) -> (rob_u, skip_u)`:
- `rob_u`: Maximum loot from the subtree at `u` **including** node `u`'s house.
- `skip_u`: Maximum loot from the subtree at `u` **excluding** node `u`'s house.

### 2. Base Case: `u is None`
$$
\text{return } (0, \; 0)
$$

### 3. State Transitions from Left $(la, lb)$ and Right $(ra, rb)$:
- $la$: max loot robbing left child, $lb$: max loot skipping left child.
- $ra$: max loot robbing right child, $rb$: max loot skipping right child.

#### Choice 1: Rob Current Node `u`
Because adjacent houses cannot both be robbed, both children MUST be skipped:
$$
rob\_u = u.\text{val} + lb + rb
$$

#### Choice 2: Skip Current Node `u`
Because `u` is skipped, each child is free to be either robbed or skipped, whichever yields more money:
$$
skip\_u = \max(la, lb) + \max(ra, rb)
$$

Return `(rob_u, skip_u)`.
Final Answer: $\max(dfs(\text{root}))$.

> **Invariant.** For each node `u`, `dfs(u)` computes the exact maximum loot attainable from `u`'s subtree under the two mutually exclusive decisions: robbing `u` or skipping `u`.

---

## 3. Step-by-Step Worked Execution

We trace the postorder traversal on `[3, 2, 3, null, 3, null, 1]`:

---

### Step 1: Evaluate Grandchildren (Leaves)
1. **Node 3 (Right child of Node 2):**
   - Left = None $\implies (0, 0)$, Right = None $\implies (0, 0)$.
   - $rob = 3 + 0 + 0 = 3$.
   - $skip = \max(0, 0) + \max(0, 0) = 0$.
   - $\text{dfs}(\text{Node } 3) = (3, 0)$.
2. **Node 1 (Right child of Node 3):**
   - Leaf node $\implies \text{dfs}(\text{Node } 1) = (1, 0)$.

---

### Step 2: Evaluate Child Node 2
- Left child: `None` $\implies (la, lb) = (0, 0)$.
- Right child: `Node 3` $\implies (ra, rb) = (3, 0)$.
- Decisions for Node 2:
  - $rob = 2 + lb + rb = 2 + 0 + 0 = \mathbf{2}$.
  - $skip = \max(la, lb) + \max(ra, rb) = \max(0, 0) + \max(3, 0) = 0 + 3 = \mathbf{3}$.
- $\text{dfs}(\text{Node } 2) = (2, 3)$.

---

### Step 3: Evaluate Child Node 3 (Right Child of Root)
- Left child: `None` $\implies (la, lb) = (0, 0)$.
- Right child: `Node 1` $\implies (ra, rb) = (1, 0)$.
- Decisions for Node 3:
  - $rob = 3 + lb + rb = 3 + 0 + 0 = \mathbf{3}$.
  - $skip = \max(la, lb) + \max(ra, rb) = \max(0, 0) + \max(1, 0) = 0 + 1 = \mathbf{1}$.
- $\text{dfs}(\text{Node } 3) = (3, 1)$.

---

### Step 4: Evaluate Root Node 3
- Left child (Node 2) returns: $(la, lb) = (2, 3)$.
- Right child (Node 3) returns: $(ra, rb) = (3, 1)$.
- Decisions for Root:
  - **Rob Root:**
    $$
    rob = 3 + lb + rb = 3 + 3 + 1 = \mathbf{7}
    $$
  - **Skip Root:**
    $$
    skip = \max(la, lb) + \max(ra, rb) = \max(2, 3) + \max(3, 1) = 3 + 3 = \mathbf{6}
    $$
- $\text{dfs}(\text{Root}) = (7, 6)$.

---

### Step 5: Final Result Extraction
Take the maximum of the two options at root:
$$
\max(rob, \; skip) = \max(7, 6) = \mathbf{7}
$$

---

## 4. Complete Execution Trace

```text
Tree:
      3 (Root)
     / \
    2   3
     \   \
      3   1

dfs(grandchild 3): rob = 3 + 0 + 0 = 3, skip = 0        -> (3, 0)
dfs(child 2):      rob = 2 + 0 + 0 = 2, skip = 0 + 3 = 3-> (2, 3)
dfs(grandchild 1): rob = 1 + 0 + 0 = 1, skip = 0        -> (1, 0)
dfs(child 3):      rob = 3 + 0 + 0 = 3, skip = 0 + 1 = 1-> (3, 1)

dfs(root 3):
  rob  = 3 + lb + rb = 3 + 3 + 1 = 7
  skip = max(2, 3) + max(3, 1) = 3 + 3 = 6
  Result = max(7, 6) = 7
```

| Node Analyzed | Node Value | Left Child $(la, lb)$ | Right Child $(ra, rb)$ | Rob Option: $val + lb + rb$ | Skip Option: $\max(la, lb) + \max(ra, rb)$ | Subtree State $(rob, skip)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Grandchild 3 | 3 | $(0, 0)$ | $(0, 0)$ | $3 + 0 + 0 = 3$ | $0 + 0 = 0$ | $(3, 0)$ |
| Child 2 | 2 | $(0, 0)$ | $(3, 0)$ | $2 + 0 + 0 = 2$ | $0 + 3 = 3$ | $(2, 3)$ |
| Grandchild 1 | 1 | $(0, 0)$ | $(0, 0)$ | $1 + 0 + 0 = 1$ | $0 + 0 = 0$ | $(1, 0)$ |
| Child 3 | 3 | $(0, 0)$ | $(1, 0)$ | $3 + 0 + 0 = 3$ | $0 + 1 = 1$ | $(3, 1)$ |
| **Root 3** | **3** | **$(2, 3)$** | **$(3, 1)$** | **$3 + 3 + 1 = 7$** | **$3 + 3 = 6$** | **$(7, 6) \implies \mathbf{7}$** |

---

## 5. Algorithmic Correctness

**Soundness.** The restriction prohibits robbing two directly connected nodes. If node $u$ is robbed, its children must not be robbed, which is enforced by selecting $lb$ and $rb$. If node $u$ is skipped, no adjacent edges are activated, allowing each child to freely select its optimal local configuration ($\max(la, lb)$ and $\max(ra, rb)$). Every evaluated loot combination obeys all edge constraints.

**Completeness.** By evaluating both possibilities (robbing $u$ vs skipping $u$) at each node in postorder, the dynamic program considers all $2^N$ possible valid node subsets in the tree. Because optimal substructure holds, no better combination of houses can produce a higher sum.

---

## 6. Traps This Instance Exposes

- **Overlapping Subtree Recalculations:** A naive recursive approach that calls `rob(root.left.left) + rob(root.left.right) ...` branches into identical subtrees repeatedly, causing exponential $O(2^N)$ runtime. Bottom-up postorder caching solves this in $O(N)$.
- **Assuming Skip Mandates Robbing Children:** If a parent is skipped, it is NOT mandatory to rob its children; a child can also be skipped if its own grandchildren provide more value. The formulation $\max(la, lb)$ correctly handles this choice.
- **Null Safety in Tree Traversal:** Directly accessing `node.left.val` crashes when children are null. Returning $(0, 0)$ for null nodes normalizes boundary handling cleanly.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. Each node is visited once during postorder traversal, and calculations at each node take $O(1)$ arithmetic steps.
- **Auxiliary Space Complexity:** $O(H)$, where $H$ is the height of the binary tree ($O(\log N)$ for balanced trees, $O(N)$ for degenerate chains), bounded by the maximum depth of the call stack.
