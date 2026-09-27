# Guided Example: Design Tic-Tac-Toe

We trace the step-by-step $O(1)$ line-counter design, distinct player tracking dictionaries, row/column/diagonal key space partitioning (`row`, `n + col`, `2n`, `2n + 1`), and instant victory determination on representative $N \times N$ game instances:

- **Input:** $n = 2$, move sequence:
  1. `move(0, 0, 1)` (Player 1 marks `(0, 0)`)
  2. `move(1, 0, 2)` (Player 2 marks `(1, 0)`)
  3. `move(0, 1, 1)` (Player 1 marks `(0, 1)`)
- **Required output:** `[0, 0, 1]`
  - Move 1: Player 1 marks row 0, col 0, diag 0 $\implies$ max line count is $1 < 2 \implies 0$
  - Move 2: Player 2 marks row 1, col 0, anti-diag $\implies$ max line count is $1 < 2 \implies 0$
  - Move 3: Player 1 marks row 0, col 1 $\implies$ row 0 count reaches $2 == n$!
  - Player 1 completes row 0 and wins! Returns **$1$**
- **Anti-Diagonal Victory Instance:** On $n = 3$, marks at $(0, 2), (1, 1), (2, 0)$ trigger anti-diagonal count $= 3 \implies$ win
- **Main Diagonal Victory Instance:** Marks at $(0, 0), (1, 1), (2, 2)$ trigger diagonal count $= 3 \implies$ win

This instance demonstrates constant-time game state tracking, mathematically proves why tracking aggregate line occupancy replaces $O(N)$ row/column grid scans, explains disjoint integer key encodings, and achieves $O(1)$ time per move and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a Tic-Tac-Toe board of dimension $N = 2$:
Two players place marks alternately:
- Player 1 marks cells with `X`
- Player 2 marks cells with `O`
The first player to fill an entire row, column, or diagonal of length $n$ wins immediately.
Design a class where `move(row, col, player)` executes in **$O(1)$ time**:

```text
Board 2x2:
Move 1: Player 1 at (0, 0)
   [X, .]
   [., .]  -> No win (return 0)

Move 2: Player 2 at (1, 0)
   [X, .]
   [O, .]  -> No win (return 0)

Move 3: Player 1 at (0, 1)
   [X, X]  <-- ROW 0 COMPLETED BY PLAYER 1!
   [O, .]  -> Player 1 wins! (return 1)
```

### Why Matrix Grid Scanning is Suboptimal
- Storing an $N \times N$ matrix and scanning the affected row, column, and diagonals takes $O(N)$ time per move.
- Scanning the entire board takes $O(N^2)$ time.
- For $N = 10^3$ and $10^5$ moves, $O(N)$ per move results in Time Limit Exceeded.
- **The Line-Counter Principle:**
  Since each cell belongs to at most 4 lines (1 row, 1 column, at most 2 diagonals), incrementing 4 counters per move allows checking for a win in **$O(1)$ constant time**!

---

## 2. Conceptual Foundation & Invariants

### 1. Disjoint Key Space Encoding
We map each of the $2N + 2$ lines to a unique integer key:
- **Row $r$:** Key $r \in [0, N - 1]$.
- **Column $c$:** Key $N + c \in [N, 2N - 1]$.
- **Main Diagonal ($r == c$):** Key $2N$ (written as `n << 1`).
- **Anti-Diagonal ($r + c == N - 1$):** Key $2N + 1$ (written as `n << 1 | 1`).

### 2. Player-Specific Dictionaries
Maintain two separate counter dictionaries in a list:
$$
cnt = [\text{defaultdict}(int), \; \text{defaultdict}(int)]
$$
- Player 1 uses `cur = cnt[0]`
- Player 2 uses `cur = cnt[1]`

### 3. Move Protocol `move(row, col, player)`:
1. `cur = cnt[player - 1]`
2. Increment line counters:
   - $cur[row] \mathrel{+}= 1$
   - $cur[N + col] \mathrel{+}= 1$
   - If $row == col$: $cur[2N] \mathrel{+}= 1$
   - If $row + col == N - 1$: $cur[2N + 1] \mathrel{+}= 1$
3. Win condition check:
   If any of the lines through $(row, col)$ reaches count $N$:
   $$
   \text{return } player
   $$
   Otherwise, return $0$.

> **Invariant.** For any player and any line key, `cur[key]` is the exact number of cells marked by that player along that line. Since moves are unique, a count of $N$ guarantees that all $N$ cells on that line are owned by that player.

---

## 3. Step-by-Step Worked Execution

We trace $N = 2$ with moves: `(0, 0, 1)`, `(1, 0, 2)`, `(0, 1, 1)`:
Winning threshold: $n = 2$.
Line keys for $N = 2$:
- Rows: Row 0 $\to 0$, Row 1 $\to 1$
- Cols: Col 0 $\to 2 + 0 = 2$, Col 1 $\to 2 + 1 = 3$
- Main Diag ($r == c$): $2 \times 2 = 4$
- Anti-Diag ($r + c == 1$): $2 \times 2 + 1 = 5$

---

### Step 1: Move 1 — `move(0, 0, player=1)`
- Current player dictionary: `cur = cnt[0]`.
- Update line counters:
  - Row 0: $cur[0] \leftarrow 0 + 1 = 1$.
  - Col 0: $cur[2] \leftarrow 0 + 1 = 1$.
  - Main Diag ($0 == 0$ holds): $cur[4] \leftarrow 0 + 1 = 1$.
  - Anti-Diag ($0 + 0 == 1$ is false): not updated.
- Check win:
  - Active keys checked: $\{0, 2, 4\}$.
  - Counts: $cur[0]=1, cur[2]=1, cur[4]=1$. None equals $n = 2$.
- Return: **$0$** (No winner).

---

### Step 2: Move 2 — `move(1, 0, player=2)`
- Current player dictionary: `cur = cnt[1]`.
- Update line counters:
  - Row 1: $cur[1] \leftarrow 0 + 1 = 1$.
  - Col 0: $cur[2] \leftarrow 0 + 1 = 1$.
  - Main Diag ($1 == 0$ is false): not updated.
  - Anti-Diag ($1 + 0 == 1$ holds): $cur[5] \leftarrow 0 + 1 = 1$.
- Check win:
  - Active keys checked: $\{1, 2, 5\}$.
  - Counts: $cur[1]=1, cur[2]=1, cur[5]=1$. None equals $n = 2$.
- Return: **$0$** (No winner).

---

### Step 3: Move 3 — `move(0, 1, player=1)`
- Current player dictionary: `cur = cnt[0]`.
- Update line counters:
  - **Row 0:** $cur[0] \leftarrow 1 + 1 = \mathbf{2}$!
  - Col 1: $cur[3] \leftarrow 0 + 1 = 1$.
  - Main Diag ($0 == 1$ is false): not updated.
  - Anti-Diag ($0 + 1 == 1$ holds): $cur[5] \leftarrow 0 + 1 = 1$.
- Check win:
  - Active keys checked: $\{0, 3, 5\}$.
  - $cur[0] == 2 == n$ (**Win Condition Satisfied!**).
- Player 1 has completed Row 0!
- Immediately return: **$1$**.

---

## 4. Complete Execution Trace

```text
n = 2, Winning Threshold = 2
Keys: Row 0=0, Row 1=1, Col 0=2, Col 1=3, Diag=4, Anti-Diag=5

Move 1: move(0, 0, 1)
  Player 1: cur[0]=1, cur[2]=1, cur[4]=1
  Max count = 1 < 2 -> return 0

Move 2: move(1, 0, 2)
  Player 2: cur[1]=1, cur[2]=1, cur[5]=1
  Max count = 1 < 2 -> return 0

Move 3: move(0, 1, 1)
  Player 1: cur[0]=2, cur[3]=1, cur[5]=1
  cur[0] == 2 == n -> WINNER: Player 1 -> return 1
```

| Move | Player | Cell $(r, c)$ | Lines Updated | Line Keys Updated | Updated Counts for Player | Win Detected? | Return Value |
|:---:|:---:|:---:|:---|:---:|:---|:---:|:---:|
| 1 | 1 | $(0, 0)$ | Row 0, Col 0, Diag | $0, 2, 4$ | $cur[0]=1, cur[2]=1, cur[4]=1$ | No | **0** |
| 2 | 2 | $(1, 0)$ | Row 1, Col 0, Anti-Diag | $1, 2, 5$ | $cur[1]=1, cur[2]=1, cur[5]=1$ | No | **0** |
| **3** | **1** | **$(0, 1)$** | **Row 0, Col 1, Anti-Diag** | **$0, 3, 5$** | **$cur[0]=2, cur[3]=1, cur[5]=1$** | **Yes (Row 0)** | **$\mathbf{1}$ (Winner)** |

---

## 5. Algorithmic Correctness

**Soundness.** A player wins if and only if all $n$ cells of a single row, column, or diagonal are filled by that player. Since each call specifies an unoccupied cell, a counter reaching $n$ proves that $n$ distinct cells along that line have been marked by that player. Evaluating only the lines intersecting the latest move $(row, col)$ is sufficient because untouched lines cannot change count.

**Completeness.** Every move increments all lines intersecting the placed cell. The check `any(cur[i] == n ...)` verifies all potentially winning lines immediately after the mark is placed, guaranteeing that a winning move is detected instantly without delay.

---

## 6. Traps This Instance Exposes

- **Re-Scanning Untouched Lines:** There is no need to check all $2N + 2$ lines on every move. Only the 2 to 4 lines that pass through $(row, col)$ could have increased. Checking only intersecting lines guarantees $O(1)$ work.
- **Center Cell on Odd Boards:** For odd $n$, the center cell $(n//2, n//2)$ lies on both the main diagonal and the anti-diagonal. Checking both conditions `row == col` and `row + col == n - 1` independently ensures both diagonal counters are properly updated.
- **Key Collisions:** Mixing row indices with column indices (e.g. using `col` instead of `n + col`) would blend vertical and horizontal counts. The offset $+ n$ ensures disjoint key sets.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$ per `move` call. Each move updates at most 4 dictionary entries and evaluates at most 4 equality checks.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory across all moves to store at most $2N + 2$ entries in each player's dictionary.
