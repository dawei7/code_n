# Guided Example: Word Search

We trace the step-by-step 2D grid DFS backtracking and in-place state rollback on a representative grid:

- **Input:**
  $$\text{board} = \begin{pmatrix} \text{'A'} & \text{'B'} & \text{'C'} & \text{'E'} \\ \text{'S'} & \text{'F'} & \text{'C'} & \text{'S'} \\ \text{'A'} & \text{'D'} & \text{'E'} & \text{'E'} \end{pmatrix}, \quad \text{word} = \text{"ABCCED"}$$
- **Required output:** $\text{True}$
- **Cell Reuse Disqualification:** $\text{word} = \text{"ABCB"} \implies \text{False}$ (cell $(0, 1)$ cannot be reused).

This instance demonstrates four-directional recursive exploration, in-place visited marking without extra memory (`board[r][c] = '#'`), state rollback upon backtracking, and search pruning via character frequency checks.

---

## 1. Instance & Teaching Goal

Given an $M \times N$ board of characters ($M = 3, N = 4$) and a string $\text{word} = \text{"ABCCED"}$, return `True` if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells (horizontally or vertically neighboring). The same letter cell may not be used more than once in a path.

On the board:
$$
\begin{pmatrix}
\mathbf{A} & \mathbf{B} & \mathbf{C} & \text{E} \\
\text{S} & \text{F} & \mathbf{C} & \text{S} \\
\text{A} & \mathbf{D} & \mathbf{E} & \text{E}
\end{pmatrix}
$$
The search discovers the path:
$$
(0, 0)\text{['A']} \longrightarrow (0, 1)\text{['B']} \longrightarrow (0, 2)\text{['C']} \longrightarrow (1, 2)\text{['C']} \longrightarrow (2, 2)\text{['E']} \longrightarrow (2, 1)\text{['D']}
$$

A naive search that copies a visited boolean matrix at each step wastes $O(M \cdot N)$ memory per recursive frame.
By mutating `board[r][c] = '#'` upon entry and restoring its original character upon exit, DFS backtracking runs in strictly $O(1)$ auxiliary space beyond the recursion stack.

---

## 2. Conceptual Foundation & Invariants

### DFS Backtracking Protocol
We define $\text{dfs}(r, c, k)$ where $(r, c)$ is the current cell and $k$ is the index of the letter being matched in $\text{word}$:

1. **Boundary & Mismatch Check:**
   If $r < 0$ or $r \ge M$ or $c < 0$ or $c \ge N$ or $\text{board}[r][c] \ne \text{word}[k]$:
   - Return $\text{False}$.
2. **Success Base Case:**
   If $k == |\text{word}| - 1$:
   - Return $\text{True}$ (final character matched).
3. **Visited Marking (In-Place):**
   Save original character: `temp = board[r][c]`.
   Mark cell as occupied: `board[r][c] = '#'`.
4. **4-Directional Search:**
   Explore neighbors $(r+1, c), (r-1, c), (r, c+1), (r, c-1)$:
   $$
   \text{found} = \text{dfs}(r+1, c, k+1) \lor \text{dfs}(r-1, c, k+1) \lor \text{dfs}(r, c+1, k+1) \lor \text{dfs}(r, c-1, k+1)
   $$
5. **Backtracking State Rollback:**
   Restore cell: `board[r][c] = temp`.
   Return $\text{found}$.

> **Invariant.** At depth $k$, exactly $k$ board cells are temporarily marked as `'#'`, representing the active non-reusable prefix path matching $\text{word}[0 \dots k-1]$.

---

## 3. Step-by-Step Worked Execution

We trace the matching of $\text{"ABCCED"}$:

### Start Cell Discovery
- Scan cells until finding $\text{word}[0] = \text{'A'}$.
- Cell $(0, 0)$ is `'A'`. Initiate $\text{dfs}(0, 0, k=0)$.

---

### Recursive Path Walk
- **Depth $k = 0$, Cell $(0, 0)$ (`'A'`):**
  - Matches $\text{word}[0] = \text{'A'}$.
  - Mark `board[0][0] = '#'`.
  - Probe neighbors:
    - Down $(1, 0)$ is `'S'` $\ne \text{'B'}$ (Mismatch).
    - Right $(0, 1)$ is `'B'`. Matches $\text{word}[1]$! Recurse.
- **Depth $k = 1$, Cell $(0, 1)$ (`'B'`):**
  - Matches $\text{word}[1] = \text{'B'}$.
  - Mark `board[0][1] = '#'`.
  - Probe neighbors:
    - Left $(0, 0)$ is `'#'` (Already visited).
    - Down $(1, 1)$ is `'F'` $\ne \text{'C'}$.
    - Right $(0, 2)$ is `'C'`. Matches $\text{word}[2]$! Recurse.
- **Depth $k = 2$, Cell $(0, 2)$ (`'C'`):**
  - Matches $\text{word}[2] = \text{'C'}$.
  - Mark `board[0][2] = '#'`.
  - Probe neighbors:
    - Left $(0, 1)$ is `'#'`.
    - Right $(0, 3)$ is `'E'` $\ne \text{'C'}$.
    - Down $(1, 2)$ is `'C'`. Matches $\text{word}[3]$! Recurse.
- **Depth $k = 3$, Cell $(1, 2)$ (`'C'`):**
  - Matches $\text{word}[3] = \text{'C'}$.
  - Mark `board[1][2] = '#'`.
  - Probe neighbors:
    - Up $(0, 2)$ is `'#'`.
    - Left $(1, 1)$ is `'F'` $\ne \text{'E'}$.
    - Right $(1, 3)$ is `'S'` $\ne \text{'E'}$.
    - Down $(2, 2)$ is `'E'`. Matches $\text{word}[4]$! Recurse.
- **Depth $k = 4$, Cell $(2, 2)$ (`'E'`):**
  - Matches $\text{word}[4] = \text{'E'}$.
  - Mark `board[2][2] = '#'`.
  - Probe neighbors:
    - Up $(1, 2)$ is `'#'`.
    - Right $(2, 3)$ is `'E'` $\ne \text{'D'}$.
    - Left $(2, 1)$ is `'D'`. Matches $\text{word}[5]$! Recurse.
- **Depth $k = 5$, Cell $(2, 1)$ (`'D'`):**
  - Matches $\text{word}[5] = \text{'D'}$.
  - Base check: $k = 5 == |\text{word}| - 1$.
  - **Terminal Success!** Return $\text{True}$.

The success propagates up through the call stack, restoring marked cells and returning $\text{True}$.

---

## 4. Complete Execution Trace

| Recursion Depth $k$ | Target Letter $\text{word}[k]$ | Candidate Cell $(r, c)$ | Cell Value | Action Taken | Board In-Place Mark |
|:---:|:---:|:---:|:---:|:---|:---:|
| 0 | `'A'` | $(0, 0)$ | `'A'` | Match. Branch right to $(0, 1)$ | `board[0][0] = '#'` |
| 1 | `'B'` | $(0, 1)$ | `'B'` | Match. Branch right to $(0, 2)$ | `board[0][1] = '#'` |
| 2 | `'C'` | $(0, 2)$ | `'C'` | Match. Branch down to $(1, 2)$ | `board[0][2] = '#'` |
| 3 | `'C'` | $(1, 2)$ | `'C'` | Match. Branch down to $(2, 2)$ | `board[1][2] = '#'` |
| 4 | `'E'` | $(2, 2)$ | `'E'` | Match. Branch left to $(2, 1)$ | `board[2][2] = '#'` |
| 5 | `'D'` | $(2, 1)$ | `'D'` | **Match. Final Letter!** | **Return True** |

### Rejected Instance: $\text{word} = \text{"ABCB"}$
From $(0, 2)$ (`'C'`), searching for second `'B'` finds $(0, 1)$ containing `'#'` (already on active path). All other neighbors fail $\implies$ returns $\text{False}$.

---

## 5. Algorithmic Correctness

**Soundness.** Marking the current cell with `'#'` prevents any descendant call from revisiting the same cell in the active path, strictly enforcing the rule that each grid cell can be used at most once per path. Restoring the character upon backtrack ensures uncommitted paths leave the board unmodified for future exploration.

**Completeness.** Testing all cells as potential starts and exploring all four cardinal directions from matching prefixes guarantees that if any valid sequence of adjacent cells spells out $\text{word}$, DFS will encounter it.

---

## 6. Traps This Instance Exposes

- **Cell Re-use Prevention:** Failing to mark visited cells allows loops (e.g. bouncing back and forth between `'A'` and `'B'` to match `"ABABAB"` on a board with only one `'A'` and one `'B'`).
- **Pruning by Character Frequency:** If the frequency of any character in `word` exceeds its total occurrences on `board`, return `False` immediately without running any DFS.
- **Start Search from Rarer End:** If `word[0]` occurs 50 times on the board but `word[-1]` occurs only once, reversing `word` before searching dramatically reduces the branching factor.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \cdot N \cdot 3^L)$, where $M \times N$ is the grid size and $L = |\text{word}|$. From each cell, we explore at most 3 directions (since the parent cell is blocked by `'#'`).
- **Auxiliary Space Complexity:** $O(L)$ to store the recursion call stack up to depth $L$. No extra 2D arrays are created.
