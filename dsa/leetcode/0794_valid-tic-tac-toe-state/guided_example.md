# Guided Example: Valid Tic-Tac-Toe State

We trace the step-by-step Tic-Tac-Toe game mechanics (alternating turns, 'X' moves first), token count balance invariants ($x == o \lor x == o + 1$), 8-line three-in-a-row winning predicates (rows, columns, diagonals), game-over terminal state constraints, and invalid board configuration rejection on representative $3 \times 3$ boards:

- **Input:**
  $$
  board = \begin{bmatrix}
  \text{"O  "} \\
  \text{"   "} \\
  \text{"   "}
  \end{bmatrix}
  $$
- **Required output:** `false`
  - Tic-Tac-Toe game rules & legality constraints:
    - Players place marks alternately on a $3 \times 3$ grid.
    - Player 1 always plays `'X'` and **always takes the first turn**.
    - Player 2 always plays `'O'`.
    - Marks cannot be removed or overwritten once placed.
    - The game ends **immediately** when a player achieves 3 marks in a line (any row, column, or diagonal), or when the board is completely full (9 marks).
    - **No further moves may occur after a player wins.**
    - Objective: Determine whether the given board state can arise during a legitimate game.
    - For the sample board:
      - Contains zero `'X'` marks and one `'O'` mark ($x = 0, o = 1$).
      - Because `'X'` must move first, it is impossible for `'O'` to have moved before `'X'`.
      - State is illegal $\implies$ return **`false`**.
- **Turn Alternation & Terminal Victory Invariants:**
  - **Count Balance Invariant:**
    - Let $x$ be the total number of `'X'` marks and $o$ be the total number of `'O'` marks on the board.
    - Because `'X'` plays first and turns alternate:
      1. If `'O'` just played: $x == o$.
      2. If `'X'` just played: $x == o + 1$.
      3. Any other count ($x < o$ or $x > o + 1$) violates turn alternation!
  - **The Winning Move Timing Invariant:**
    - Examine all 8 lines (3 rows, 3 columns, 2 diagonals) for 3-in-a-row:
      1. **If `'X'` Wins:**
         - `'X'` must have placed the final, winning mark.
         - Therefore, the game terminated immediately on an `'X'` turn.
         - `'O'` could not have moved afterward.
         - Consequently, we must have:
           $$
           x == o + 1
           $$
           *(If `'X'` has won but $x == o$, `'O'` illegally moved after `'X'` already won!)*
      2. **If `'O'` Wins:**
         - `'O'` must have placed the final, winning mark.
         - The game terminated immediately on an `'O'` turn.
         - Consequently, we must have:
           $$
           x == o
           $$
           *(If `'O'` has won but $x == o + 1$, `'X'` illegally moved after `'O'` already won!)*
      3. **Simultaneous Win Exclusion:**
         - Can both `'X'` and `'O'` win?
         - If `'X'` wins, $x == o + 1$. If `'O'` wins, $x == o$.
         - Since $x == o + 1$ and $x == o$ are mutually exclusive, both players cannot simultaneously hold winning lines in a valid game.
- **Step-by-Step Worked Execution Trace on Sample 1 ($board = [\text{"O  "}, \text{"   "}, \text{"   "}]$):**
  - Count token marks:
    - Count of `'X'`: $x = 0$.
    - Count of `'O'`: $o = 1$.
  - Evaluate Count Balance:
    $$
    x == o \iff 0 == 1 \quad (\text{False})
    $$
    $$
    x == o + 1 \iff 0 == 2 \quad (\text{False})
    $$
  - Condition $x == o \lor x == o + 1$ fails!
  - Return:
    $$
    ans = \mathbf{false}
    $$
- **Step-by-Step Worked Execution Trace on Sample 2 ($board = [\text{"XOX"}, \text{" X "}, \text{"   "}]$):**
  - Token counts:
    - Row 0 has `X`, `O`, `X` (two `'X'`, one `'O'`).
    - Row 1 has `X` (one `'X'`).
    - Total: $x = 3, o = 1$.
  - Evaluate Count Balance:
    - Difference: $x - o = 3 - 1 = \mathbf{2}$.
    - Expected difference is 0 or 1.
    - Too many `'X'` marks placed $\implies$ return **`false`**.
- **Post-Victory Illegal Move Trace ($board = [\text{"XXX"}, \text{"OO "}, \text{"OO "}]$):**
  - Token counts: $x = 3, o = 4$.
  - Balance fails immediately ($3 < 4$).
- **Post-Victory Move with Correct Token Parity ($board = [\text{"XXX"}, \text{"OOO"}, \text{"   "}]$):**
  - $x = 3, o = 3$.
  - Balance check passes ($x == o$).
  - Win check:
    - Row 0: `XXX` $\implies$ `'X'` won!
    - Row 1: `OOO` $\implies$ `'O'` won!
  - Because `'X'` won, we require $x == o + 1$. But $3 \ne 3 + 1 = 4$!
  - Caught by `'X'` victory rule: `'O'` placed the second row after `'X'` already completed row 0!
  - Return **`false`**.
- **Valid Terminal Victory Trace ($board = [\text{"XXX"}, \text{"XOO"}, \text{"OO "}]$):**
  - $x = 4, o = 3 \implies x == o + 1$ (valid count).
  - `'X'` wins (row 0).
  - Since $x == o + 1$, `'X'` placed the 7th mark and won $\implies$ return **`true`**.

This instance demonstrates finite state machine transition validation and game-theoretic reachability invariants on $3 \times 3$ combinatorial boards, mathematically proves why terminal state stopping rules constrain mark population parity, and derives $O(1)$ runtime and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a $3 \times 3$ Tic-Tac-Toe board:
Determine if this board could be reached in a **valid game** ('X' plays first, game ends on win).

```text
board:
  "O  "
  "   "
  "   "

Mark counts:
  Count of 'X' = 0
  Count of 'O' = 1

Rule: 'X' MUST move first!
'O' cannot have more marks than 'X'.
Result: false
```

### The Invariant of the Winning Move Parity
1. Token count must be balanced: $x == o$ or $x == o + 1$.
2. If `'X'` wins $\implies$ `'X'` made the last move $\implies x == o + 1$.
3. If `'O'` wins $\implies$ `'O'` made the last move $\implies x == o$.

---

## 2. Conceptual Foundation & Invariants

### 1. Population Parity Invariant:
$$
x \in \{o, \; o + 1\}
$$

### 2. Immediate Termination Axiom:
$$
\text{win}('X') \implies x == o + 1
$$
$$
\text{win}('O') \implies x == o
$$

> **Combinatorial Game Reachability Invariant.** The game tree of Tic-Tac-Toe forms a directed acyclic graph rooted at the empty board. The reachable configuration space $\mathcal{S}_{\text{valid}}$ is the union of terminal winning boards and intermediate non-terminal states strictly respecting alternating player parity.

---

## 3. Step-by-Step Worked Execution

We trace $board = [\text{"O  "}, \text{"   "}, \text{"   "}]$:

---

### Step 1: Count Marks
- $x = 0, o = 1$.

---

### Step 2: Check Balance
- $x \ne o$ ($0 \ne 1$).
- $x \ne o + 1$ ($0 \ne 2$).
- Invalid balance!

---

### Step 3: Output
$$
\mathbf{false}
$$

---

## 4. Complete Execution Trace

| Test Board | Count $x$ ('X') | Count $o$ ('O') | Parity Check ($x \in \{o, o+1\}$) | Win State Detected | Legally Reachable? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `["O  ", "   ", "   "]` | $0$ | $1$ | Failed ($0 < 1$) | None | **No (`false`)** |
| `["XOX", " X ", "   "]` | $3$ | $1$ | Failed ($3 - 1 = 2$) | None | **No (`false`)** |
| `["XXX", "OOO", "   "]` | $3$ | $3$ | Passed ($3 == 3$) | Both 'X' and 'O' win | **No (`false`)** |
| **`["XOX", "O O", "XOX"]`** | **$4$** | **$3$** | **Passed ($4 == 3 + 1$)** | **Neither wins** | **Yes (`true`)** |

---

## 5. Boundary Cases & Failure Modes

- **Empty Board (`"   "`):** $x = 0, o = 0 \implies$ valid initial state (`true`).
- **Full Board Draw (Cat's Game):** $x = 5, o = 4$, no winner $\implies$ valid (`true`).
- **Corner Diagonal Win:** Diagonals $(0,0)-(1,1)-(2,2)$ and $(0,2)-(1,1)-(2,0)$ are checked as lines.
- **Double Winning Line for Same Player:** In some configurations, a player forms two intersecting winning lines with a single move (e.g. corner placement completing both a row and column). This is valid as long as that player moved last ($x == o + 1$ for 'X').

---

## 6. Traps & Common Anti-Patterns

- **Checking Only Win Lines without Parity:** A board might have a valid single winning line, but if the mark counts don't match the winner's parity (e.g. 'O' moved after 'X' won), the board is illegal.
- **Allowing Both Players to Win:** If both 'X' and 'O' have 3-in-a-row, the game was illegally continued after the first player won.
- **Simulating All Possible Games (Tree Search):** The state space of Tic-Tac-Toe has $3^9 = 19,683$ boards. Instead of traversing the game tree, checking the 3 analytical conditions executes in $O(1)$ time with 0 recursion.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Board is fixed $3 \times 3$ (9 cells).
  - 8 possible winning lines checked in constant time: $\mathcal{O}(1)$.
  - Total Time: strictly $\mathcal{O}(1)$. Completes in $< 0.01$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space.
