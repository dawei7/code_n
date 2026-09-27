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
Since string length $N \le 20$, the string can be mapped to a compact 32-bit integer `mask`:
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
- **Bitmask Size Limit:** Using integer bitmasks requires that $N$ fits within machine integer sizes. Here $N \le 20$, which comfortably fits in a standard 32-bit integer with fast bitwise operations.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot 2^N)$ in the worst case, where $N$ is the length of `currentState`. There are at most $2^N$ unique bitmasks. For each mask, the loop performs $N - 1$ bitwise tests. With memoization, each state is evaluated at most once.
- **Auxiliary Space Complexity:** $O(2^N)$ auxiliary memory for the memoization cache and $O(N)$ stack frames for the recursion depth.