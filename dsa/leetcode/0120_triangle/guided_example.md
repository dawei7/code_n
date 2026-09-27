# Guided Example: Triangle

We trace the step-by-step bottom-up dynamic programming reduction and $O(N)$ rolling array collapse on a representative triangle:

- **Input:** $\text{triangle} = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]$
- **Required output:** $11$ (Path $2 \to 3 \to 5 \to 1 = 11$)
- **Single-Row Base:** $\text{triangle} = [[-10]] \implies -10$

This instance demonstrates why bottom-up DP eliminates boundary branch checks (every cell $(r, c)$ naturally has two child candidates $(r+1, c)$ and $(r+1, c+1)$), compresses space from $O(N^2)$ to a 1D vector of size $N$, converges to a single root scalar without a final minimum scan, and runs in $O(N^2)$ time.

---

## 1. Instance & Teaching Goal

Given a triangular array of numbers:
$$
\begin{matrix}
\text{Row 0:} & & & 2 & & \\
\text{Row 1:} & & 3 & & 4 & \\
\text{Row 2:} & 6 & & 5 & & 7 \\
\text{Row 3:} & 4 & 1 & & 8 & 3
\end{matrix}
$$
find the minimum path sum from the top of the triangle to the bottom. From index $c$ on row $r$, you may only step to either $c$ or $c + 1$ on row $r + 1$.

Consider path alternatives:
- $2 \to 4 \to 7 \to 3 = 16$
- $2 \to 3 \to 6 \to 4 = 15$
- $2 \to 3 \to 5 \to 8 = 18$
- $2 \to 3 \to 5 \to 1 = 11$ (**Minimum!**)

### Why Bottom-Up Trumps Top-Down
- **Top-Down:** Begins at $1$ root but diverges into $N$ endpoints at the bottom row. Boundary cells on the left ($c = 0$) and right ($c = r$) only have one parent, requiring conditional edge logic. A final $O(N)$ linear pass is required to find $\min(DP[N-1])$.
- **Bottom-Up:** Begins at the bottom row and converges upward toward the single top apex. **Every single interior and boundary cell $(r, c)$ has exactly two child options $(r+1, c)$ and $(r+1, c+1)$**. No boundary branching is needed, and the final answer resides directly in `dp[0]`.

---

## 2. Conceptual Foundation & Invariants

### Bottom-Up DP Recurrence
Let $N$ be the number of rows.
Let $DP[c]$ represent the minimum path sum from node $(r, c)$ down to the base of the triangle.

1. **Base Case (Bottom Row $r = N - 1$):**
   A path starting on the bottom row has cost equal to the cell itself:
   $$
   DP = \text{list}(\text{triangle}[N - 1])
   $$
2. **Bottom-Up State Transition:**
   For row $r$ iterating from $N - 2$ down to $0$:
   For column $c$ from $0$ up to $r$:
   $$
   DP[c] \leftarrow \text{triangle}[r][c] + \min(DP[c], \, DP[c + 1])
   $$
   Here:
   - $DP[c]$ represents the minimum path continuing downward to the left child $(r+1, c)$.
   - $DP[c+1]$ represents the minimum path continuing downward to the right child $(r+1, c+1)$.
3. **Termination:**
   At row $r = 0$, $DP[0]$ stores the globally minimal path sum from the triangle's apex to the base.

> **Invariant.** After processing row $r$, each entry $DP[c]$ holds the exact minimum path weight from node $(r, c)$ to any reachable cell on row $N - 1$.

---

## 3. Step-by-Step Worked Execution

We trace the 1D rolling array on $[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]$ ($N = 4$):

### Base Initialization ($r = 3$)
Initialize $DP$ with row 3:
$$
DP = [4, \, 1, \, 8, \, 3]
$$

---

### Step 1: Process Row $r = 2$ ($[6, 5, 7]$)
- Column $c = 0$ (Value $6$):
  $$
  DP[0] = 6 + \min(DP[0], DP[1]) = 6 + \min(4, 1) = 6 + 1 = 7
  $$
- Column $c = 1$ (Value $5$):
  $$
  DP[1] = 5 + \min(DP[1], DP[2]) = 5 + \min(1, 8) = 5 + 1 = 6
  $$
- Column $c = 2$ (Value $7$):
  $$
  DP[2] = 7 + \min(DP[2], DP[3]) = 7 + \min(8, 3) = 7 + 3 = 10
  $$
- $DP$ vector after row 2: $[7, \, 6, \, 10]$

---

### Step 2: Process Row $r = 1$ ($[3, 4]$)
- Column $c = 0$ (Value $3$):
  $$
  DP[0] = 3 + \min(DP[0], DP[1]) = 3 + \min(7, 6) = 3 + 6 = 9
  $$
- Column $c = 1$ (Value $4$):
  $$
  DP[1] = 4 + \min(DP[1], DP[2]) = 4 + \min(6, 10) = 4 + 6 = 10
  $$
- $DP$ vector after row 1: $[9, \, 10]$

---

### Step 3: Process Row $r = 0$ ($[2]$)
- Column $c = 0$ (Value $2$):
  $$
  DP[0] = 2 + \min(DP[0], DP[1]) = 2 + \min(9, 10) = 2 + 9 = \mathbf{11}
  $$
- $DP$ vector after row 0: $[11]$

Termination. Apex minimum path sum: $DP[0] = \mathbf{11}$.

---

## 4. Complete Execution Trace

```text
Row 3 (Base):     4       1       8       3
                   \     / \     / \     /
Row 2:                7       6      10
                       \     / \     /
Row 1:                    9      10
                           \     /
Row 0 (Apex):                11
```

| Pass | Target Row $r$ | Column $c$ | Triangle Value | Child Options Evaluated | Optimal Choice $\min(L, R)$ | New $DP[c]$ Value |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Base | 3 | $0, 1, 2, 3$ | $[4, 1, 8, 3]$ | None (Terminal Leaves) | - | `[4, 1, 8, 3]` |
| 1 | 2 | 0 | 6 | $\min(DP[0]=4, DP[1]=1)$ | 1 | $6 + 1 = 7$ |
| 1 | 2 | 1 | 5 | $\min(DP[1]=1, DP[2]=8)$ | 1 | $5 + 1 = 6$ |
| 1 | 2 | 2 | 7 | $\min(DP[2]=8, DP[3]=3)$ | 3 | $7 + 3 = 10$ |
| 2 | 1 | 0 | 3 | $\min(DP[0]=7, DP[1]=6)$ | 6 | $3 + 6 = 9$ |
| 2 | 1 | 1 | 4 | $\min(DP[1]=6, DP[2]=10)$ | 6 | $4 + 6 = 10$ |
| **3** | **0** | **0** | **2** | **$\min(DP[0]=9, DP[1]=10)$** | **9** | **$2 + 9 = 11$ (Result)** |

---

## 5. Algorithmic Correctness

**Soundness.** Bellman's Principle of Optimality applies: the optimal path from $(r, c)$ to the base consists of the value at $(r, c)$ plus the minimum of the optimal path from $(r+1, c)$ and the optimal path from $(r+1, c+1)$. Because $DP[c]$ and $DP[c+1]$ are already solved optimally, choosing their minimum guarantees global optimality.

**Completeness.** Every allowable path from the apex down to any cell on the base must transition through adjacent indices. By checking all cells row by row, no valid path is omitted.

---

## 6. Traps This Instance Exposes

- **Greedy Choice Failure:** Making the greedy choice at each step from the top: $2 \to \min(3, 4) = 3 \to \min(6, 5) = 5 \to \min(1, 8) = 1$ happens to give 11 here, but if the bottom row was `[100, 1, 8, 0]`, a greedy step might pick the wrong branch early and miss an extremely small terminal value. Dynamic programming explores all options.
- **Top-Down Edge Cases:** In top-down DP, index $0$ has only parent $0$, and index $r$ has only parent $r-1$. Bottom-up DP eliminates all boundary special-casing.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$, where $N$ is the number of rows in the triangle. Total operations equal the number of cells: $\frac{N(N+1)}{2}$, with each cell taking $O(1)$ time.
- **Auxiliary Space Complexity:** $O(N)$ using a 1D rolling array of size $N$ (or strictly $O(1)$ if updating `triangle` in place).