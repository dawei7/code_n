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

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. Each node is visited exactly once during the DFS traversal, performing $O(1)$ arithmetic comparisons and assignments.
- **Auxiliary Space Complexity:** $O(H)$, where $H$ is the height of the binary tree, corresponding to the maximum recursion call stack frames. In balanced trees, $H = O(\log N)$; in the worst-case skewed tree, $H = O(N)$.