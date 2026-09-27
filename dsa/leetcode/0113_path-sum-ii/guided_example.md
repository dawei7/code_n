# Guided Example: Path Sum II

We trace the step-by-step backtracking search and path state rollback across all root-to-leaf paths on a representative binary tree:

- **Input:** $\text{root} = [5, 4, 8, 11, \text{null}, 13, 4, 7, 2, \text{null}, \text{null}, 5, 1]$, $\text{targetSum} = 22$
- **Required output:** `[[5, 4, 11, 2], [5, 8, 4, 5]]`
- **Single-Node Base:** $\text{root} = [1, 2], \text{targetSum} = 1 \implies []$ (Root 1 is not a leaf)

This instance demonstrates collecting all matching root-to-leaf paths using a single shared mutable path buffer, appending values during descent, creating snapshot copies (`list(path)`) at matching leaf nodes, popping elements upon backtracking, and avoiding memory copying overhead.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree:
$$
\begin{gathered}
5 \\
\swarrow \qquad \searrow \\
4 \qquad\qquad\quad 8 \\
\swarrow \qquad\qquad \swarrow \quad \searrow \\
11 \qquad\qquad\quad 13 \qquad\quad 4 \\
\swarrow \quad \searrow \qquad\qquad\qquad\qquad \swarrow \quad \searrow \\
7 \qquad\quad 2 \qquad\qquad\qquad\qquad\quad 5 \qquad\quad 1
\end{gathered}
$$
and $\text{targetSum} = 22$, return **all** root-to-leaf paths where the sum of node values equals $22$.

In contrast to LeetCode 112 (which returns a single boolean and short-circuits on the first match), LeetCode 113 requires exhaustive exploration of all leaf paths:
- Path 1 ($5 \to 4 \to 11 \to 7$): sum $= 27 \ne 22$
- Path 2 ($5 \to 4 \to 11 \to 2$): sum $= 22$ (**Match 1!**)
- Path 3 ($5 \to 8 \to 13$): sum $= 26 \ne 22$
- Path 4 ($5 \to 8 \to 4 \to 5$): sum $= 22$ (**Match 2!**)
- Path 5 ($5 \to 8 \to 4 \to 1$): sum $= 18 \ne 22$
Result: `[[5, 4, 11, 2], [5, 8, 4, 5]]`.

Copying arrays at every recursive call allocates $O(N^2)$ extra memory.
Using a single shared path list with `append` on entry and `pop` on exit maintains strictly $O(H)$ auxiliary space, only creating new list copies when a valid leaf is confirmed.

---

## 2. Conceptual Foundation & Invariants

### Backtracking Path DFS Protocol
We maintain a mutable list `path` and remaining sum `rem` (initially `rem = targetSum`).
Define $\text{dfs}(\text{node}, \text{rem})$:

1. **Empty Guard:**
   If $\text{node} == \emptyset$: return.
2. **Push Current Node:**
   - $\text{path.append}(\text{node.val})$
   - $\text{rem} \leftarrow \text{rem} - \text{node.val}$
3. **Leaf Node Verification:**
   If $\text{node.left} == \emptyset$ and $\text{node.right} == \emptyset$:
   - If $\text{rem} == 0$:
     Store a detached copy of the active path:
     $$
     \text{results.append}(\text{list}(\text{path}))
     $$
4. **Child Subtree Exploration:**
   - If $\text{node.left}$: $\text{dfs}(\text{node.left}, \, \text{rem})$
   - If $\text{node.right}$: $\text{dfs}(\text{node.right}, \, \text{rem})$
5. **Backtracking State Rollback:**
   - $\text{path.pop()}$

> **Invariant.** At any moment during traversal, `path` contains the exact sequence of node values from the root down to the current active node, and $\text{rem} + \sum \text{path} = \text{targetSum}$.

---

## 3. Step-by-Step Worked Execution

We trace the traversal on the binary tree with $\text{targetSum} = 22$:

### Step 1: Root Node 5
- `path = [5]`, `rem = 22 - 5 = 17`.
- Internal node. Branch left to Node 4.

---

### Step 2: Node 4
- `path = [5, 4]`, `rem = 17 - 4 = 13`.
- Internal node. Branch left to Node 11.

---

### Step 3: Node 11
- `path = [5, 4, 11]`, `rem = 13 - 11 = 2`.
- Internal node.
  - **Probe Left Leaf 7:**
    - `path = [5, 4, 11, 7]`, $\text{rem} = 2 - 7 = -5 \ne 0$.
    - Rollback: `path.pop()` $\implies [5, 4, 11]$.
  - **Probe Right Leaf 2:**
    - `path = [5, 4, 11, 2]`, $\text{rem} = 2 - 2 = 0$.
    - **Valid Leaf Match!**
    - Capture snapshot: `results.append([5, 4, 11, 2])`.
    - Rollback: `path.pop()` $\implies [5, 4, 11]$.
- Rollback Node 11 $\implies [5, 4]$.
- Rollback Node 4 $\implies [5]$.

---

### Step 4: Node 8 (Right Branch of Root)
- `path = [5, 8]`, $\text{rem} = 17 - 8 = 9$.
- Internal node.
  - **Probe Left Leaf 13:**
    - `path = [5, 8, 13]`, $\text{rem} = 9 - 13 = -4 \ne 0$.
    - Rollback: `path.pop()` $\implies [5, 8]$.
  - **Probe Right Node 4:**
    - `path = [5, 8, 4]`, $\text{rem} = 9 - 4 = 5$.
    - **Probe Left Leaf 5:**
      - `path = [5, 8, 4, 5]`, $\text{rem} = 5 - 5 = 0$.
      - **Valid Leaf Match!**
      - Capture snapshot: `results.append([5, 8, 4, 5])`.
      - Rollback: `path.pop()` $\implies [5, 8, 4]$.
    - **Probe Right Leaf 1:**
      - `path = [5, 8, 4, 1]`, $\text{rem} = 5 - 1 = 4 \ne 0$.
      - Rollback: `path.pop()` $\implies [5, 8, 4]$.
    - Rollback Node 4 $\implies [5, 8]$.
- Rollback Node 8 $\implies [5]$.
- Rollback Root 5 $\implies []$.

Traversal concludes.
Returned result: `[[5, 4, 11, 2], [5, 8, 4, 5]]`.

---

## 4. Complete Execution Trace

```text
                                [5] (rem=17)
                               /            \
                     [5,4] (rem=13)        [5,8] (rem=9)
                      /                     /           \
             [5,4,11] (rem=2)       [5,8,13] (rem=-4)   [5,8,4] (rem=5)
              /            \             [Reject]        /           \
     [5,4,11,7]         [5,4,11,2]                 [5,8,4,5]       [5,8,4,1]
      (rem=-5)            (rem=0)                   (rem=0)         (rem=4)
      [Reject]          [SNAPSHOT 1]              [SNAPSHOT 2]      [Reject]
```

| Step | Active Leaf | Candidate Path | Sum | Remaining Target | Target Match? | Action Taken | Emitted Paths |
|:---:|:---:|:---|:---:|:---:|:---:|:---|:---|
| 1 | Node 7 | `[5, 4, 11, 7]` | 27 | -5 | No | Backtrack | `[]` |
| 2 | Node 2 | `[5, 4, 11, 2]` | 22 | 0 | **Yes** | **Capture snapshot** | `[[5, 4, 11, 2]]` |
| 3 | Node 13 | `[5, 8, 13]` | 26 | -4 | No | Backtrack | `[[5, 4, 11, 2]]` |
| 4 | Node 5 | `[5, 8, 4, 5]` | 22 | 0 | **Yes** | **Capture snapshot** | `[[5, 4, 11, 2], [5, 8, 4, 5]]` |
| 5 | Node 1 | `[5, 8, 4, 1]` | 18 | 4 | No | Backtrack | `[[5, 4, 11, 2], [5, 8, 4, 5]]` |

### Shared Buffer Rollback Trace

The candidate table above shows only the leaves. The table below shows the single mutable buffer that produced those candidates, event by event, so that the push/pop pairing and the exact moment of each snapshot are visible:

| # | Event | Active Buffer After the Event | Cumulative Sum | $\text{rem}$ | Consequence |
|:---:|:---|:---|:---:|:---:|:---|
| 1 | Push $5$ | `[5]` | 5 | 17 | Root is not a leaf, so the descent continues left. |
| 2 | Push $4$ | `[5, 4]` | 9 | 13 | Node $4$ has only a left child, so only one continuation exists. |
| 3 | Push $11$ | `[5, 4, 11]` | 20 | 2 | Both children of $11$ are leaves and will be probed separately. |
| 4 | Push $7$ | `[5, 4, 11, 7]` | 27 | $-5$ | Leaf reached with a nonzero remainder, so nothing is stored. |
| 5 | Pop $7$ | `[5, 4, 11]` | 20 | 2 | The buffer returns to the state of event 3 before the sibling is tried. |
| 6 | Push $2$ | `[5, 4, 11, 2]` | 22 | 0 | Leaf reached with remainder $0$, so a detached copy of `[5, 4, 11, 2]` is stored. |
| 7 | Pop $2$ | `[5, 4, 11]` | 20 | 2 | The stored copy survives this pop because it was detached at event 6. |
| 8 | Pop $11$ | `[5, 4]` | 9 | 13 | The whole left subtree of node $4$ is finished. |
| 9 | Pop $4$ | `[5]` | 5 | 17 | Back at the root, ready for the right subtree. |
| 10 | Push $8$ | `[5, 8]` | 13 | 9 | Right subtree descent begins. |
| 11 | Push $13$ | `[5, 8, 13]` | 26 | $-4$ | Leaf reached with a nonzero remainder. |
| 12 | Pop $13$ | `[5, 8]` | 13 | 9 | Sibling node $4$ is tried next. |
| 13 | Push $4$ | `[5, 8, 4]` | 17 | 5 | Node $4$ has two leaf children. |
| 14 | Push $5$ | `[5, 8, 4, 5]` | 22 | 0 | Second match; a detached copy of `[5, 8, 4, 5]` is stored. |
| 15 | Pop $5$ | `[5, 8, 4]` | 17 | 5 | The second stored copy also survives its own pop. |
| 16 | Push $1$ | `[5, 8, 4, 1]` | 18 | 4 | Final leaf of the tree; no match. |
| 17 | Pop $1$ | `[5, 8, 4]` | 17 | 5 | Both children of node $4$ are exhausted. |
| 18 | Pop $4$ | `[5, 8]` | 13 | 9 | Right subtree of $8$ finished. |
| 19 | Pop $8$ | `[5]` | 5 | 17 | Back at the root once more. |
| 20 | Pop $5$ | `[]` | 0 | 22 | The buffer is empty again, while the result list still holds both detached copies. |

Two properties are visible only in this view. First, pushes and pops are perfectly balanced: every value pushed at some event is removed before the traversal finishes, which is what keeps the buffer at $O(H)$ size instead of growing with $N$. Second, the cumulative sum and $\text{rem}$ always satisfy $\text{rem} = 22 - \text{cumulative sum}$, and both return to their parent's values at every pop, so a sibling never inherits state from a branch that has already been abandoned.

---

## 5. Algorithmic Correctness

**Soundness.** A path is saved to `results` if and only if both children are null (confirming the endpoint is a true leaf) and $\text{rem} == 0$ (confirming the cumulative sum matches $\text{targetSum}$). Because `list(path)` makes a shallow copy of the active path, subsequent pop mutations do not corrupt previously captured answers.

**Completeness.** Preorder DFS exhaustively tests every root-to-leaf path. State rollback (`path.pop()`) guarantees that siblings explore independent path buffers without interference.

---

## 6. Traps This Instance Exposes

- **Storing References Instead of Copies:** Writing `results.append(path)` stores a reference to the mutable list. When the search backtracks to the root, `path` becomes empty `[]`, leaving `results` filled with empty lists `[[], []]`. A copy `list(path)` or `path[:]` is strictly mandatory.
- **Premature Pruning on Negative Remainder:** Tree values can be negative. Even if $\text{rem} < 0$, deeper nodes can have negative values that bring the sum back to $\text{targetSum}$. No branches may be pruned based on intermediate sign.
- **Stopping at First Match:** Unlike Path Sum I, the search must continue across the entire tree to find all matching paths.

**Boundary instances and the condition that decides each result.**

| Scenario | Input and $\text{targetSum}$ | Leaves that exist | Result | Why that result is forced |
|:---|:---|:---|:---|:---|
| Empty tree | $\text{root} = [\,]$, $\text{targetSum} = 0$ | None | `[]` | With no node there is no root-to-leaf path, so the empty result is returned even though the target $0$ would be met by an empty sum. |
| Single leaf path | $\text{root} = [1, 2]$, $\text{targetSum} = 3$ | Only $2$ | `[[1, 2]]` | The root has a child, so the sole path is $1 \to 2$ and it sums to $3$. |
| No matching leaf | $\text{root} = [1, 2, 3]$, $\text{targetSum} = 5$ | $2$ and $3$ | `[]` | The two candidate sums are $3$ and $4$; every leaf is rejected and the result list stays empty. |
| Mixed signs along one path | $\text{root} = [1, -2, -3, 1, 3, -2, \text{null}, -1]$, $\text{targetSum} = -1$ | $-1$, $3$, and $-2$ | `[[1, -2, 1, -1]]` | Only the path $1 \to -2 \to 1 \to -1$ sums to $-1$; the other leaves give $1 - 2 + 3 = 2$ and $1 - 3 - 2 = -4$, so the remainder dips below zero at intermediate nodes without invalidating the surviving path. |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot H)$, where $N$ is the number of nodes and $H$ is the tree height. In the worst case (e.g. a full binary tree where every leaf matches), there are $O(N)$ leaves, and copying a path of length $H$ into results takes $O(H)$ time.
- **Auxiliary Space Complexity:** $O(H)$ for the recursion stack and the shared `path` buffer.
