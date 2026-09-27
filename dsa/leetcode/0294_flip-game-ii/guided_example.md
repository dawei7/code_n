# Guided Example: Flip Game II

We trace the step-by-step Minimax game theory recurrence, bitmask state encoding ($'+' \to 1, \; '-' \to 0$), XOR bit-clearing transitions, and memoized combinatorial search on representative game strings:

- **Input:** $\text{currentState} = \text{"++++"}$
- **Required output:** `true` (The starting player can guarantee a win by flipping the middle pair at index 1 to produce `"+--+"`, leaving the opponent with zero legal moves)
- **Immediate Defeat Base Case:** $\text{currentState} = \text{"+"} \implies \text{false}$ (No adjacent pairs; first player loses immediately)
- **Minimal Winning Pair:** $\text{currentState} = \text{"++"} \implies \text{true}$ (Flip to `"--"`; opponent has no moves)
- **Overlapping Three Pluses:** $\text{currentState} = \text{"+++"} \implies \text{true}$ (Flipping either pair leaves `"--+"` or `"+--"`, leaving opponent with zero moves)
- **Symmetric Non-Winning State:** Strings where every initial move allows the second player to counter with a winning move return `false`

This instance demonstrates impartial normal-play game theory (Sprague-Grundy / Minimax), explains why an existential quantifier over the player's choices couples with a universal negation of the opponent's responses ($\exists \text{ move s.t. } \neg \text{canWin}(\text{successor})$), details $O(1)$ bitwise consecutive pair checking via integer masks, and applies memoized backtracking to eliminate redundant subproblem re-evaluations.

---

## 1. Instance & Teaching Goal

Given string $\text{currentState} = \text{"++++"}$:
Two players take turns flipping two adjacent `"++"` into `"--"`. The first player unable to make a move loses.
Determine whether the **first player can guarantee a win** assuming both players play optimally:

```text
Starting state: "++++" (4 pluses)

Player 1 choices:
- Option A: Flip index 0 -> "--++" (Opponent can flip index 2 to "----" and win!)
- Option B: Flip index 1 -> "+--+" (Zero consecutive pluses left for Opponent!)
- Option C: Flip index 2 -> "++--" (Opponent can flip index 0 to "----" and win!)

By choosing Option B, Player 1 forces Opponent into "+--+" with 0 legal moves.
Player 1 wins! Output: true
```

### The Game-Theoretic Minimax Axiom
In a finite impartial two-player game with no ties:
- A player in state $S$ can **guarantee a win** ($\text{canWin}(S) = \text{True}$) if and only if there exists **at least one valid move** to a state $S'$ from which the opponent **cannot win**:
  $$
  \text{canWin}(S) \iff \exists S' \in \text{Next}(S) \quad \text{such that} \quad \neg \text{canWin}(S')
  $$
- Conversely, if every legal move leads to a state from which the opponent can win, or if no legal moves exist, the current player loses ($\text{canWin}(S) = \text{False}$).

---

## 2. Conceptual Foundation & Invariants

### Integer Bitmask Representation
Since no more than $20$ consecutive `'+'` may appear and every reachable state is a subset of the pluses of `currentState` ($\text{currentState.length} \le 60$), the state can be mapped to a compact integer `mask` held in a 64-bit word:
- Bit $i$ is $1$ if $\text{currentState}[i] == \text{'+'}$.
- Bit $i$ is $0$ if $\text{currentState}[i] == \text{'-'}$.

#### Operations:
1. **Consecutive Pair Test at index $i$:**
   $$
   (\text{mask} \ \& \ (1 \ll i)) \ne 0 \quad \text{and} \quad (\text{mask} \ \& \ (1 \ll (i + 1))) \ne 0
   $$
2. **State Transition (Flipping bits $i$ and $i + 1$ to $0$):**
   $$
   \text{next\_mask} = \text{mask} \oplus (1 \ll i) \oplus (1 \ll (i + 1))
   $$
3. **Memoization:**
   Cache computed outcomes in a hash map `memo[mask] -> bool` to avoid re-evaluating equivalent subgames reached via different move sequences (e.g. flipping positions 0 then 4 vs 4 then 0).

> **Invariant.** For any evaluated `mask`, `dfs(mask)` returns `True` if and only if there exists at least one legal move leading to a `next_mask` where `dfs(next_mask)` is `False`.

---

## 3. Step-by-Step Worked Execution

We trace the game search on $\text{currentState} = \text{"++++"}$ ($N = 4$):
Initial bitmask:
$$
\text{mask} = (1 \ll 0) + (1 \ll 1) + (1 \ll 2) + (1 \ll 3) = 1 + 2 + 4 + 8 = \mathbf{15} \quad (0\text{b}1111)
$$

---

### Step 1: Root Search $\text{dfs}(15)$
Player 1 evaluates all adjacent pair flips $i \in [0, 2]$:

#### Branch A: Flip Index $i = 0$
- Flip bits $0$ and $1$:
  $$
  \text{next\_mask} = 15 \oplus (1 \ll 0) \oplus (1 \ll 1) = 15 \oplus 3 = \mathbf{12} \quad (0\text{b}1100, \text{"--++"})
  $$
- Recursive evaluation: What can Player 2 do from $\text{dfs}(12)$?
  - In mask $12$ ($0\text{b}1100$), bits $2$ and $3$ are set.
  - Player 2 flips index $i = 2$:
    $$
    12 \oplus (1 \ll 2) \oplus (1 \ll 3) = 12 \oplus 12 = \mathbf{0} \quad (0\text{b}0000, \text{"----"})
    $$
  - In mask $0$, no adjacent bits are set $\implies \text{dfs}(0) = \mathbf{\text{False}}$.
  - Because Player 2 can transition to state $0$ (which is False for Player 1), Player 2 wins from state 12:
    $$
    \text{dfs}(12) = \mathbf{\text{True}}
    $$
- Since Player 2 wins from mask 12, Branch A ($i = 0$) does **not** guarantee a win for Player 1. Search continues.

---

#### Branch B: Flip Index $i = 1$ (The Winning Move)
- Flip bits $1$ and $2$:
  $$
  \text{next\_mask} = 15 \oplus (1 \ll 1) \oplus (1 \ll 2) = 15 \oplus 6 = \mathbf{9} \quad (0\text{b}1001, \text{"+--+"})
  $$
- Recursive evaluation: What can Player 2 do from $\text{dfs}(9)$?
  - Inspect mask $9$ ($0\text{b}1001$):
    - $i = 0$: Bit 0 is 1, Bit 1 is 0 (No).
    - $i = 1$: Bit 1 is 0, Bit 2 is 0 (No).
    - $i = 2$: Bit 2 is 0, Bit 3 is 1 (No).
  - There are **zero legal moves** available in mask $9$!
  - The loop completes without finding any valid move:
    $$
    \text{dfs}(9) = \mathbf{\text{False}}
    $$
- Since Player 2 loses from state $9$ ($\text{dfs}(9) == \text{False}$), Player 1 can force this state!
- Immediate victory condition met:
  $$
  \text{return True}
  $$

Player 1 wins!

#### Every Root Candidate, Including the Branch the Short-Circuit Never Reaches
The search returns the moment one child reports a loss for the player about to move, so move $i = 2$ is never generated in the actual run. Evaluating it afterwards shows it would have been rejected for the same reason as $i = 0$:

| Root move $i$ | `next_mask` | Resulting state | What the opponent can do from there | `dfs(next_mask)` | Verdict |
|:---:|:---:|:---:|:---:|:---:|:---|
| $i = 0$ | $15 \oplus 3 = 12$ | `"--++"` | flip $i = 2$: $12 \oplus 12 = 0$, and the mover at mask $0$ has no move | `True` — the opponent on move wins | Eliminated |
| $i = 1$ | $15 \oplus 6 = 9$ | `"+--+"` | nothing: bits $0$ and $3$ are never adjacent | `False` — the opponent on move loses | **Chosen: Player 1 wins** |
| $i = 2$ | $15 \oplus 12 = 3$ | `"++--"` | flip $i = 0$: $3 \oplus 3 = 0$, and the mover at mask $0$ has no move | `True` — the opponent on move wins | Eliminated |

Both outer moves fail for one structural reason: neither destroys the pluses, so each leaves exactly one live adjacent pair and the opponent's single reply empties the board.

---

## 4. Complete Execution Trace

```text
State: "++++" (mask 15)

Player 1 tries i = 0 -> next_mask = 12 ("--++"):
  Opponent evaluates dfs(12):
    Opponent plays i = 2 -> next_mask = 0 ("----") -> dfs(0) = False
    Opponent wins from 12 -> dfs(12) = True
  Move i = 0 fails for Player 1.

Player 1 tries i = 1 -> next_mask = 9 ("+--+"):
  Opponent evaluates dfs(9):
    No adjacent pair in mask 9 -> Opponent has 0 moves -> dfs(9) = False
  Opponent loses from 9!
  Player 1 wins by choosing i = 1!

Result: true
```

| Recursion Node | String State | Bitmask | Move Tried | Resulting Sub-State | Child Result | Decision at Current State |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Root | `"++++"` | 15 | $i = 0$ | `"--++"` (Mask 12) | Opponent Wins (`True`) | Try next move |
| Subgame | `"--++"` | 12 | $i = 2$ | `"----"` (Mask 0) | `False` (0 moves) | Current Player Wins (`True`) |
| **Root** | **`"++++"`** | **15** | **$i = 1$** | **`"+--+"` (Mask 9)** | **Opponent Loses (`False`)** | **`true` (Player 1 Wins!)** |

---

## 5. Algorithmic Correctness

**Soundness.** A state is reported as `True` only when there exists at least one legal move leading to a state where the opposing player has no winning strategy (`not dfs(next_state)`). This matches the exact mathematical definition of a winning position in game theory.

**Completeness.** The search exhaustively explores all candidate moves. If a state has no moves, it returns `False`. If every possible move allows the opponent to win, it returns `False`. By memoizing subproblems on the immutable integer bitmask, the complete game tree is traversed without omissions.

---

## 6. Traps This Instance Exposes

- **Flipping an Outer vs Inner Pair:** In `"++++"`, flipping an outer pair (index 0 or 2) leaves two adjacent pluses (`"--++"` or `"++--"`), giving the opponent an immediate counter-win. Only flipping the center pair (index 1) isolates the pluses (`"+--+"`), denying the opponent any legal moves.
- **Missing Memoization:** Game trees branch exponentially. Without caching (`@cache` or memo dictionary), subgames with identical remaining pluses would be recalculated thousands of times, causing Time Limit Exceeded.
- **Bitmask Size Limit:** An integer bitmask needs one bit per index, so the encoding must hold up to $60$ bits — a 64-bit word, not a 32-bit one. What actually bounds the search is the separate constraint that no more than $20$ consecutive `'+'` may appear, which caps the length of any single playable run and keeps the memoized game tree small.

### Boundary Values and Composed Positions
The worked instance is one point in a small landscape of positions. Every verdict below is the exact `dfs` value for that state, and each one is forced by a structural reason rather than by a special case:

| Instance | Plus runs | Legal moves at the start | `dfs` | Why the value is forced |
|:---:|:---:|:---:|:---:|:---|
| `"+"` | $1$ | $0$ | `False` | A run of length $1$ holds no adjacent pair, so there is nothing to flip |
| `"++"` | $2$ | $1$ | `True` | The only move clears both bits and hands over a terminal state |
| `"+++"` | $3$ | $2$ | `True` | Either flip leaves a lone `'+'`, so the opponent's reply set is empty |
| `"++++"` | $4$ | $3$ | `True` | Only the centre flip isolates the survivors; the two outer flips lose |
| `"+++++"` | $5$ | $4$ | `False` | All $4$ moves leave a run of length $2$ or $3$, and each of those is a win for the opponent |
| `"++--++"` | $2, 2$ | $2$ | `False` | Two equal pair-games cancel: whatever the mover does to one run, the opponent mirrors it in the other |
| `"+++--++"` | $3, 2$ | $3$ | `False` | Different lengths, equal Grundy numbers ($1 \oplus 1 = 0$), so the mover is still lost |
| `"++++--++"` | $4, 2$ | $4$ | `True` | Grundy numbers $2$ and $1$ disagree ($2 \oplus 1 = 3 \ne 0$), so a winning reply exists |
| 60-character alternating state | $1, 1, \dots, 1$ | $0$ | `False` | The length ceiling is reached and no two `'+'` are adjacent, so the answer is a terminal loss |

### Why Equal Components Cancel
A maximal run of `'+'` is an independent subgame, because a flip can never cross a `'-'`. Its outcome is summarized by a Grundy number $g(L)$ built from the split recurrence
$$
g(L) = \operatorname{mex}\{\, g(a) \oplus g(b) : a + b = L - 2 \,\},
$$
since flipping a pair inside a run of length $L$ leaves two runs of lengths $a$ and $b$ with $a + b = L - 2$. A composed position loses for the mover exactly when the XOR of its component Grundy numbers is $0$:

| Run length $L$ | Legal opening moves | `dfs` for the run alone | Grundy number $g(L)$ |
|:---:|:---:|:---:|:---:|
| $1$ | $0$ | `False` | $0$ |
| $2$ | $1$ | `True` | $1$ |
| $3$ | $2$ | `True` | $1$ |
| $4$ | $3$ | `True` | $2$ |
| $5$ | $4$ | `False` | $0$ |
| $6$ | $5$ | `True` | $3$ |

Two runs of length $2$ therefore cancel ($1 \oplus 1 = 0$), and so do a run of length $3$ and a run of length $2$ ($1 \oplus 1 = 0$) despite their different lengths. The memoized search never needs this theory — it reaches the same verdicts by exhausting moves — but the component view explains in one line why positions such as `"++--++"` and `"+++--++"` are losing.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot 2^N)$ in the worst case, where $N$ is the length of `currentState`. There are at most $2^N$ unique bitmasks. For each mask, the loop performs $N - 1$ bitwise tests. With memoization, each state is evaluated at most once.
- **Auxiliary Space Complexity:** $O(2^N)$ auxiliary memory for the memoization cache and $O(N)$ stack frames for the recursion depth.
