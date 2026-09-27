# Guided Example: Binary Tree Longest Consecutive Sequence

We trace the step-by-step top-down recursive traversal, parent-child consecutive value verification ($\text{node.val} == \text{parent.val} + 1$), streak accumulator propagation and reset, and global maximum tracking on representative binary tree structures:

- **Input:** Binary tree $\text{root} = [1, \text{null}, 3, 2, 4, \text{null}, \text{null}, \text{null}, 5]$
- **Required output:** $3$ (The longest consecutive parent-to-child sequence is $3 \to 4 \to 5$, of length $3$)
- **Discontinuous Step Reset:** $1 \to 3$ skips value $2$ ($3 \ne 1 + 1$), resetting the streak length to $1$ at node $3$
- **Child-to-Parent Path Exclusion:** Path $2 \to 3$ cannot be linked because sequences must travel strictly in parent-to-child topological order
- **Single Node Base Case:** $\text{root} = [1] \implies 1$ (A single node forms a valid sequence of length $1$)
- **Zigzag Sequence:** Consecutive paths can branch left or right at any parent (e.g. left child then right child), provided each step increments by exactly $+1$

This instance demonstrates top-down tree path accumulation, explains why non-consecutive steps reset the local streak without invalidating previously recorded global maximums, formalizes the strict parent-to-child directional constraint, and achieves $O(N)$ linear time and $O(H)$ auxiliary stack space.

---

## 1. Instance & Teaching Goal

Given a binary tree:
```text
        1
         \
          3
         / \
        2   4
             \
              5
```
Find the length of the **longest consecutive sequence path**:
- The path must travel strictly from **parent to child**.
- Each consecutive step must increase in value by **exactly 1** ($\text{child.val} == \text{parent.val} + 1$).

Path candidates:
- $1 \to 3$: Step size is $+2 \ne +1$ (Not consecutive).
- $3 \to 2$: Step size is $-1 \ne +1$ (Not consecutive).
- $3 \to 4 \to 5$: Step size is $+1$ at each step ($3+1=4$, $4+1=5$). Length $= \mathbf{3}$.
Output: $\mathbf{3}$.

---

## 2. Conceptual Foundation & Invariants

### Top-Down Recursive State `dfs(node, parent_val, current_streak)`
To track sequences without backtracking or re-traversing subtrees:
We pass down the current path length `current_streak` from parent to child:
1. **Base Case:**
   If `node is None`, return immediately.
2. **Consecutive Evaluation:**
   - If `parent_val is not None` and `node.val == parent_val + 1`:
     The consecutive sequence continues!
     $$
     \text{streak} = \text{current\_streak} + 1
     $$
   - Else (first node or non-consecutive step):
     The previous sequence is broken; start a new sequence of length 1 at `node`:
     $$
     \text{streak} = 1
     $$
3. **Global Accumulation:**
   $$
   \text{max\_len} \leftarrow \max(\text{max\_len}, \; \text{streak})
   $$
4. **Recursive Descent:**
   Recursively evaluate both children:
   $$
   \text{dfs}(\text{node.left}, \; \text{node.val}, \; \text{streak})
   $$
   $$
   \text{dfs}(\text{node.right}, \; \text{node.val}, \; \text{streak})
   $$

> **Invariant.** At every visited node, `streak` represents the exact length of the unique contiguous increasing consecutive path ending at `node` from an ancestor. `max_len` stores the global supremum over all explored nodes.

### The Same Recurrence Read Bottom-Up
Nothing in the problem forces the running length to travel downward. A post-order reading computes, for each node, the longest valid sequence that **starts** at that node and descends: the value is `1` plus the child's own answer when the edge steps by exactly $+1$, and it collapses to `1` when the edge does not. Both readings describe the same five nodes, and the table below shows them side by side:

| Node | Left child (edge step) | Right child (edge step) | Longest run starting at this node (bottom-up) | Streak ending at this node (top-down view) |
|:---:|:---:|:---:|:---:|:---:|
| $1$ | none | $3$ (step $+2$) | $1$ — neither branch steps by $+1$ | $1$ — it is the root |
| $3$ | $2$ (step $-1$) | $4$ (step $+1$) | $3$ — the chain $3 \to 4 \to 5$ | $1$ — the edge from $1$ broke the chain |
| $2$ | none | none | $1$ — a leaf | $1$ |
| $4$ | none | $5$ (step $+1$) | $2$ — the chain $4 \to 5$ | $2$ — the chain $3 \to 4$ |
| $5$ | none | none | $1$ — a leaf | $3$ — the chain $3 \to 4 \to 5$ |

The two middle columns are why the bottom-up form needs no parent parameter: the edge test compares a node with its own child, which is already in hand. The last column is why the top-down form needs no combination step: the streak already counts the whole path behind the node. Both columns reach the same maximum of $3$, but note where that maximum lives — column four peaks at the internal node $3$, and the value returned for the root is only $1$. The global answer must therefore be accumulated separately from whatever a single call returns, whichever direction the recurrence runs.

---

## 3. Step-by-Step Worked Execution

We trace the DFS traversal on tree $[1, \text{null}, 3, 2, 4, \text{null}, \text{null}, \text{null}, 5]$:
Initial state: `max_len = 0`.

---

### Step 1: Visit Node 1 (Root)
- `node.val = 1, parent_val = None, current_streak = 0`.
- No parent exists $\implies \text{streak} = \mathbf{1}$.
- Update global max: $\text{max\_len} = \max(0, 1) = \mathbf{1}$.
- Left child is `None`.
- Recurse right: $\text{dfs}(\text{Node}(3), \; \text{parent} = 1, \; \text{streak} = 1)$.

---

### Step 2: Visit Node 3
- `node.val = 3, parent_val = 1, current_streak = 1`.
- Check consecutive condition:
  $$
  \text{node.val} == \text{parent\_val} + 1 \iff 3 == 1 + 1 \iff 3 == 2 \quad (\mathbf{\text{False}})
  $$
- Streak broken! Reset streak starting at Node 3:
  $$
  \text{streak} = \mathbf{1}
  $$
- Update global max: $\text{max\_len} = \max(1, 1) = 1$.
- Branch left: $\text{dfs}(\text{Node}(2), \; \text{parent} = 3, \; \text{streak} = 1)$.
- Branch right: $\text{dfs}(\text{Node}(4), \; \text{parent} = 3, \; \text{streak} = 1)$.

---

### Step 3: Visit Node 2 (Left Branch of 3)
- `node.val = 2, parent_val = 3, current_streak = 1`.
- Check condition:
  $$
  2 == 3 + 1 \iff 2 == 4 \quad (\mathbf{\text{False}})
  $$
- Reset streak: $\text{streak} = 1$.
- Update global max: $\text{max\_len} = \max(1, 1) = 1$.
- Both children of Node 2 are `None`. Returns.

---

### Step 4: Visit Node 4 (Right Branch of 3)
- `node.val = 4, parent_val = 3, current_streak = 1`.
- Check condition:
  $$
  \text{node.val} == \text{parent\_val} + 1 \iff 4 == 3 + 1 \iff 4 == 4 \quad (\mathbf{\text{True!}})
  $$
- Consecutive sequence extends!
  $$
  \text{streak} = 1 + 1 = \mathbf{2} \quad (\text{Path: } 3 \to 4)
  $$
- Update global max:
  $$
  \text{max\_len} = \max(1, 2) = \mathbf{2}
  $$
- Left child is `None`.
- Branch right: $\text{dfs}(\text{Node}(5), \; \text{parent} = 4, \; \text{streak} = 2)$.

---

### Step 5: Visit Node 5 (Right Branch of 4)
- `node.val = 5, parent_val = 4, current_streak = 2`.
- Check condition:
  $$
  \text{node.val} == \text{parent\_val} + 1 \iff 5 == 4 + 1 \iff 5 == 5 \quad (\mathbf{\text{True!}})
  $$
- Consecutive sequence extends!
  $$
  \text{streak} = 2 + 1 = \mathbf{3} \quad (\text{Path: } 3 \to 4 \to 5)
  $$
- Update global max:
  $$
  \text{max\_len} = \max(2, 3) = \mathbf{3}
  $$
- Both children of Node 5 are `None`. Returns.

---

### Traversal Completed
All nodes visited. Global maximum consecutive path length is $\mathbf{3}$.

---

## 4. Complete Execution Trace

```text
DFS Trace:
  dfs(1, parent=None, streak=0) -> streak = 1, max_len = 1
    dfs(3, parent=1, streak=1): 3 != 1 + 1 -> streak resets to 1
      dfs(2, parent=3, streak=1): 2 != 3 + 1 -> streak resets to 1
      dfs(4, parent=3, streak=1): 4 == 3 + 1 -> streak = 2, max_len = 2
        dfs(5, parent=4, streak=2): 5 == 4 + 1 -> streak = 3, max_len = 3

Final Result: 3
```

| Node Visited | Node Value | Parent Value | Consecutive? ($\text{val} == \text{parent} + 1$) | Path Streak | Global `max_len` | Active Path |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Root | 1 | None | Root (N/A) | 1 | 1 | $[1]$ |
| Right | 3 | 1 | $3 \ne 1 + 1$ (No) | 1 (Reset) | 1 | $[3]$ |
| Left | 2 | 3 | $2 \ne 3 + 1$ (No) | 1 (Reset) | 1 | $[2]$ |
| **Right** | **4** | **3** | **$4 == 3 + 1$ (Yes)** | **2** | **2** | $[3, 4]$ |
| **Right** | **5** | **4** | **$5 == 4 + 1$ (Yes)** | **3** | **$\mathbf{3}$** | **$[3, 4, 5]$ (Optimal)** |

---

## 5. Algorithmic Correctness

**Soundness.** A streak increments if and only if the current node value is exactly 1 greater than its immediate topological parent. Because the recurrence follows parent-child pointers, any measured streak corresponds to a valid parent-to-child sequence.

**Completeness.** Tree DFS visits every node in the binary tree exactly once. Any maximal consecutive sequence must have a starting node and end at some descendant. The algorithm starts a new candidate streak at every node and extends it along all child branches as far as the consecutive condition holds, ensuring the global maximum is recorded.

---

## 6. Traps This Instance Exposes

- **Parent-to-Child vs Arbitrary Paths:** In LeetCode 298, the path **must** go from parent to child. In LeetCode 549 (Binary Tree Longest Consecutive Sequence II), paths can travel child-to-parent-to-child and can be either increasing or decreasing. Conflating the two problems leads to unnecessary post-order subtree combination logic.
- **Strict $+1$ Step Size:** A sequence like $1 \to 3$ is increasing, but NOT consecutive. The check must test `node.val == parent.val + 1`, not `node.val > parent.val`.
- **Streak Reset Invariant:** When a streak breaks, the path length resets to $1$ (the current node itself), NOT $0$. Every single node constitutes a valid sequence of length 1.

### Boundary Shapes and Their Exact Answers
Each row below is a verified answer for a small tree, chosen because it isolates one way the rule can be misread:

| Tree (array form) | Answer | Why that value is forced |
|:---|:---:|:---|
| `[-30000]` | $1$ | One node is a sequence of length $1$ whatever its value; the bottom of the value range changes nothing about the count |
| `[5,5,5,5,5,5,5]` | $1$ | Every edge steps by $0$, and the rule demands exactly $+1$, so all six edges reset |
| `[5,4,null,3,null,2]` | $1$ | Each edge steps by $-1$; a decreasing chain never extends, however long it is |
| `[2,1,3]` | $2$ | The edge $2 \to 3$ steps by $+1$ and gives length $2$; the tempting chain $1 \to 2 \to 3$ climbs through the root, which the parent-to-child rule forbids |
| `[1,3,2,4]` | $2$ | $1 \to 3$ skips the value $2$ and resets; what survives are $1 \to 2$ and $3 \to 4$, both of length $2$ |
| `[0,1,1,2,null,null,2,3,null,null,3]` | $4$ | Two parallel $0 \to 1 \to 2 \to 3$ chains run in the two child subtrees; they cannot be merged through the shared root, and either one alone already has length $4$ |
| `[-2,-1,10,0,null,null,11,1]` | $4$ | The chain $-2 \to -1 \to 0 \to 1$ crosses zero without special handling, while $10 \to 11$ stays separate |
| `[29999,-30000,30000,-29999]` | $2$ | A valid $+1$ edge exists at the top of the range ($29999 \to 30000$) and at the bottom ($-30000 \to -29999$), but the two runs are in different subtrees and cannot be joined |

Two conclusions follow. The parity or magnitude of the values never matters, only the difference across an edge; and the reset is local, so a broken edge never destroys a run that was already completed in another subtree.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. Each node is visited exactly once during the DFS traversal, performing $O(1)$ arithmetic comparisons and assignments.
- **Auxiliary Space Complexity:** $O(H)$, where $H$ is the height of the binary tree, corresponding to the maximum recursion call stack frames. In balanced trees, $H = O(\log N)$; in the worst-case skewed tree, $H = O(N)$.

### Alternatives and Their Costs
| Approach | Time | Space | Tradeoff |
|:---|:---|:---|:---|
| **Top-down with an inherited streak (the method traced here)** | $O(N)$ | $O(H)$ stack | Each call needs the parent value and the streak so far, but the global maximum can be updated the moment a node is visited |
| **Post-order returning "longest run starting here"** | $O(N)$ | $O(H)$ stack | The edge test compares a node with its own child, so no parent parameter is needed; the returned value for the root is not the answer, so the maximum must still be tracked separately |
| **Collect every root-to-leaf path, then scan each one** | $O(N \cdot H)$ time for copying the paths | $O(N \cdot H)$ | Correct but wasteful: the same chain is re-scanned once per path that contains it, and a skewed tree holds one path of $N$ nodes |
| **Bidirectional post-order combination (the LeetCode 549 rule)** | $O(N)$ | $O(H)$ stack | It also joins an increasing left run with a decreasing right run through their common parent, so the sibling tree `[2,1,3]` returns $3$ from the chain $1 \to 2 \to 3$ where this problem requires $2$ |
| **Breadth-first traversal with a queue carrying the streak** | $O(N)$ | $O(\text{width})$ queue | Removes the recursion-depth exposure on skewed trees, at the cost of storing the streak for every node of the current level |
