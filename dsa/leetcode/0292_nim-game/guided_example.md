# Guided Example: Nim Game

We trace the step-by-step backward induction analysis, combinatorial game theory partition between normal play winning ($\mathcal{W}$) and losing ($\mathcal{L}$) states, modular arithmetic complementation strategy ($4 - x$), and $O(1)$ decision evaluation on representative stone heap configurations:

- **Input:** $n = 4$
- **Required output:** `false` (Every legal first move of $1, 2,$ or $3$ stones leaves $3, 2,$ or $1$ stones, allowing the opponent to take all remaining stones and win)
- **Immediate Win Base Cases:** $n = 1, 2, 3 \implies \text{true}$ (Remove all $n$ stones in the first turn to win immediately)
- **Winning Reduction to Losing Position:** $n = 5 \implies \text{true}$ (Remove $1$ stone, forcing the opponent into the losing state $4$)
- **Complementary Mirror Counterplay:** $n = 8 \implies \text{false}$ (Opponent responds to any move $x$ by taking $4 - x$, perpetually maintaining multiples of $4$)
- **Large Arbitrary Instance:** $n = 9999 \implies \text{true}$ ($9999 \equiv 3 \pmod 4 \ne 0$; initial player removes $3$ stones to leave $9996$)

This instance demonstrates impartial combinatorial game analysis, mathematically proves why states with $n \equiv 0 \pmod 4$ are strictly losing while $n \not\equiv 0 \pmod 4$ are strictly winning under optimal play, contrasts $O(1)$ modulo arithmetic against redundant $O(N)$ dynamic programming, and operates in $O(1)$ time and auxiliary space.

---

## 1. Instance & Teaching Goal

Given a heap of $n = 4$ stones:
- Two players take turns removing $1, 2,$ or $3$ stones.
- The player who removes the last stone wins.
- You move first.

Determine whether you can guarantee a win assuming both players play optimally:

```text
Heap size: 4 stones
Your choices:
- Remove 1 -> 3 left -> Opponent removes 3 -> Opponent wins!
- Remove 2 -> 2 left -> Opponent removes 2 -> Opponent wins!
- Remove 3 -> 1 left -> Opponent removes 1 -> Opponent wins!

Every available move leads to immediate defeat -> Output: false
```

### The Inherent Periodicity of Nim(1, 2, 3)
A naive approach might use recursion or DP from $1$ to $n$.
However, because each turn permits removing $1, 2,$ or $3$ stones:
- Any player facing a **multiple of 4** is helpless: any move of $x \in \{1, 2, 3\}$ leaves $4k - x$, which is NOT a multiple of 4.
- The opponent can then always remove $4 - x \in \{1, 2, 3\}$ stones, forcing the heap back to $4(k - 1)$, another multiple of 4!
The game's outcome is completely determined by:
$$
n \pmod 4 \ne 0
$$

---

## 2. Conceptual Foundation & Invariants

### Game Theory Classification ($\mathcal{W}$ vs $\mathcal{L}$)
In an impartial normal-play game under optimal play:
1. **Losing State ($\mathcal{L}$):** Every legal move transitions to a Winning state ($\mathcal{W}$).
2. **Winning State ($\mathcal{W}$):** There exists **at least one** legal move transitioning to a Losing state ($\mathcal{L}$).

### Inductive Base Cases:
- $n = 0$: Game over (previous player won). $\implies \mathcal{L}$.
- $n = 1$: Remove 1 stone $\to 0 \in \mathcal{L} \implies \mathbf{\mathcal{W}}$.
- $n = 2$: Remove 2 stones $\to 0 \in \mathcal{L} \implies \mathbf{\mathcal{W}}$.
- $n = 3$: Remove 3 stones $\to 0 \in \mathcal{L} \implies \mathbf{\mathcal{W}}$.
- $n = 4$: Available moves lead to $3, 2, 1 \in \mathcal{W}$. Every move hands the opponent a win $\implies \mathbf{\mathcal{L}}$.

### The Modulo 4 Invariant:
For any $n$:
$$
n \in \mathcal{L} \iff n \equiv 0 \pmod 4
$$
$$
n \in \mathcal{W} \iff n \not\equiv 0 \pmod 4
$$

### Optimal Winning Strategy for Player 1:
If $n = 4k + r$ with remainder $r \in \{1, 2, 3\}$:
1. On your turn: Remove exactly $r$ stones.
   The remaining stones become $4k$ (a multiple of 4 handed to the opponent).
2. On opponent's turn: The opponent removes $x \in \{1, 2, 3\}$ stones.
3. On your subsequent turn: Remove $4 - x$ stones.
   The total stones removed across the round is $x + (4 - x) = 4$.
   The opponent faces $4(k - 1)$, again a multiple of 4!
By induction, you will eventually take the final stone and win.

> **Invariant.** A player who hands their opponent a multiple of 4 can always maintain the multiple-of-4 property on every subsequent round until reaching 0.

---

## 3. Step-by-Step Worked Execution

We trace the transitions for $n = 4$ and contrast with $n = 5$:

---

### Analysis of $n = 4$ (First Player Moving)
- Initial state: $n = 4$.
- Possible moves:
  - **Move 1:** Remove 1 stone $\implies$ Remaining: $3$.
    Opponent removes 3 stones $\implies$ Opponent takes last stone. (You lose).
  - **Move 2:** Remove 2 stones $\implies$ Remaining: $2$.
    Opponent removes 2 stones $\implies$ Opponent takes last stone. (You lose).
  - **Move 3:** Remove 3 stones $\implies$ Remaining: $1$.
    Opponent removes 1 stone $\implies$ Opponent takes last stone. (You lose).
- All reachable states $\{3, 2, 1\}$ are winning for the opponent.
- State $4$ is an $\mathcal{L}$-position.
- **Return `false`**.

---

### Analysis of $n = 5$ (Winning Counterpart)
- Initial state: $n = 5 = 4(1) + 1$ (Remainder $r = 1$).
- **Your Move:** Remove $r = 1$ stone.
  - Remaining stones: $5 - 1 = \mathbf{4}$.
  - Opponent is forced into state $4$ ($\mathcal{L}$-position).
- **Opponent's Move:**
  - If opponent takes 1 stone $\implies$ 3 left $\implies$ You take 3 and win!
  - If opponent takes 2 stones $\implies$ 2 left $\implies$ You take 2 and win!
  - If opponent takes 3 stones $\implies$ 1 left $\implies$ You take 1 and win!
- You win unconditionally.
- **Return `true`**.

---

## 4. Complete Execution Trace

```text
n = 4:
  4 % 4 == 0 -> Multiple of 4 -> Return False

n = 5:
  5 % 4 == 1 != 0 -> Non-multiple of 4 -> Return True

n = 9999:
  9999 % 4 == 3 != 0 -> Non-multiple of 4 -> Return True
```

| Stones $n$ | Remainder $n \pmod 4$ | Can Win Immediately? | Optimal First Move | Opponent State Handed | Resulting Status |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 1 | Yes | Remove 1 | 0 | **`true`** |
| 2 | 2 | Yes | Remove 2 | 0 | **`true`** |
| 3 | 3 | Yes | Remove 3 | 0 | **`true`** |
| **4** | **0** | **No** | **None (All lose)** | **$\{1, 2, 3\} \in \mathcal{W}$** | **`false`** |
| 5 | 1 | No | Remove 1 | 4 | **`true`** |
| 6 | 2 | No | Remove 2 | 4 | **`true`** |
| 7 | 3 | No | Remove 3 | 4 | **`true`** |
| **8** | **0** | **No** | **None (All lose)** | **$\{5, 6, 7\} \in \mathcal{W}$** | **`false`** |

---

## 5. Algorithmic Correctness

**Soundness.** If $n \equiv 0 \pmod 4$, any legal move removes $x \in \{1, 2, 3\}$ stones, leaving $n' = n - x \not\equiv 0 \pmod 4$. The second player can then remove $4 - x$ stones, returning the heap to a multiple of 4. Since the game is finite and must terminate, the second player is guaranteed to take the final stone. Thus, the first player must lose.

**Completeness.** If $n \not\equiv 0 \pmod 4$, let $r = n \pmod 4 \in \{1, 2, 3\}$. The first player can remove exactly $r$ stones on their first move, transitioning the heap to $n - r \equiv 0 \pmod 4$. By the soundness argument, the second player now occupies the losing state, guaranteeing victory for the first player.

---

## 6. Traps This Instance Exposes

- **Overcomplicating with Dynamic Programming ($O(N)$):** Constructing a DP array `dp[i] = not (dp[i-1] and dp[i-2] and dp[i-3])` for $n \le 2^{31} - 1$ causes immediate Memory Limit Exceeded and Time Limit Exceeded. The game-theoretic pattern is strictly periodic with period 4.
- **Removing Maximal Stones Blindly:** Assuming you should always greedily take 3 stones fails on $n = 5$ (removing 3 leaves 2, letting the opponent take 2 and win). You must remove $n \pmod 4$ stones to force the opponent into the multiple-of-4 trap.
- **Zero Stones Constraint:** The problem guarantees $1 \le n \le 2^{31} - 1$, so non-positive inputs do not need defensive branching.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$ constant time. The evaluation computes a single modulo operation $n \pmod 4 \ne 0$ (or bitwise `n & 3 != 0`).
- **Auxiliary Space Complexity:** $O(1)$ auxiliary memory. Zero additional variables or collections are allocated.
