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

The candidates that could answer this question differ by orders of magnitude in cost, so the choice is settled before any heap is analysed:

| Approach | How it decides | Time | Auxiliary space | Failure mode or tradeoff |
|:---|:---|:---:|:---:|:---|
| Exhaustive play-tree recursion | Expand every legal sequence of moves and check whether one of them wins | Exponential in $n$ | $O(n)$ for the recursion stack | Correct but hopeless once $n$ reaches the millions |
| Bottom-up dynamic programming | Fill a table from $1$ to $n$ where a heap is winning exactly when one of the three smaller heaps is losing | $O(n)$ | $O(n)$ | The domain reaches $2^{31} - 1$, so the table cannot be allocated at all |
| Memoized recursion on the same recurrence | Compute only the states actually reached | $O(n)$ states | $O(n)$ for the memo | Same allocation wall, masked by a smaller constant |
| Period inference from small heaps | Compute the first few states, notice the repeat every four, and extrapolate | $O(1)$ after a constant amount of work | $O(1)$ | The period has to be *proved*; an observed pattern is not yet a strategy |
| Modular complement argument (used here) | Report whether $n \bmod 4 \ne 0$ and pair every opponent move $x$ with $4 - x$ | $O(1)$ | $O(1)$ | Relies entirely on the induction that the losing set is exactly the multiples of $4$ |
| Greedy maximum removal | Always take $3$ stones | $O(1)$ | $O(1)$ | Loses on $n = 5$, where taking $3$ leaves $2$ for the opponent to finish, and on every heap congruent to $1$ or $2$ modulo $4$ |

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

Continuing the same two rules past $n = 4$ shows the block of four repeating, and records for each heap the single move that settles it:

| Heap $n$ | Status | Deciding move | State handed over (its status) | Why the decision is forced |
|:---:|:---:|:---:|:---|:---|
| 0 | $\mathcal{L}$ | none available | — | The player to move has no stone to take; never an input, but the base of the induction |
| 1 | $\mathcal{W}$ | remove 1 | $0$ ($\mathcal{L}$) | Taking the whole heap wins on the spot |
| 2 | $\mathcal{W}$ | remove 2 | $0$ ($\mathcal{L}$) | Same, with a larger first bite |
| 3 | $\mathcal{W}$ | remove 3 | $0$ ($\mathcal{L}$) | Same |
| **4** | **$\mathcal{L}$** | **none works** | $\{3, 2, 1\}$, all $\mathcal{W}$ | Every move leaves a heap the opponent can clear |
| 5 | $\mathcal{W}$ | remove 1 | $4$ ($\mathcal{L}$) | Removing $2$ leaves $3$ and removing $3$ leaves $2$, both winning for the opponent |
| 6 | $\mathcal{W}$ | remove 2 | $4$ ($\mathcal{L}$) | The winning move is exactly $n \bmod 4$, not the largest legal one |
| 7 | $\mathcal{W}$ | remove 3 | $4$ ($\mathcal{L}$) | Same |
| **8** | **$\mathcal{L}$** | **none works** | $\{7, 6, 5\}$, all $\mathcal{W}$ | The block repeats: every move lands exactly one, two or three stones above a multiple of $4$ |
| 9 | $\mathcal{W}$ | remove 1 | $8$ ($\mathcal{L}$) | Row-for-row the same reasoning as $n = 5$ |
| 10 | $\mathcal{W}$ | remove 2 | $8$ ($\mathcal{L}$) | Row-for-row the same reasoning as $n = 6$ |
| 11 | $\mathcal{W}$ | remove 3 | $8$ ($\mathcal{L}$) | Row-for-row the same reasoning as $n = 7$ |
| **12** | **$\mathcal{L}$** | **none works** | $\{11, 10, 9\}$, all $\mathcal{W}$ | The third losing heap in the sequence $0, 4, 8, 12$ |

The table contains exactly three losing heaps in the range $1 \dots 12$, and they are precisely $4$, $8$ and $12$; every other column position is winning. That is the periodic structure the closed form encodes.

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

### The Mirror Round at Scale ($n = 9999$)

The same reasoning survives when the heap is too large to enumerate, because after the opening move every round removes exactly four stones:

| Stage | Heap at the start of the turn | Player to move | Stones removed | Heap handed over | Multiple of $4$? |
|:---|:---:|:---:|:---:|:---:|:---|
| Opening | $9999$ | You | $r = 9999 \bmod 4 = 3$ | $9996$ | Yes: $4 \times 2499$ |
| Reply A | $9996$ | Opponent | $1$ | $9995$ | No — the invariant is temporarily broken |
| Mirror A | $9995$ | You | $3 = 4 - 1$ | $9992$ | Yes: $4 \times 2498$ |
| Reply B | $9996$ | Opponent | $2$ | $9994$ | No |
| Mirror B | $9994$ | You | $2 = 4 - 2$ | $9992$ | Yes: $4 \times 2498$ |
| Reply C | $9996$ | Opponent | $3$ | $9993$ | No |
| Mirror C | $9993$ | You | $1 = 4 - 3$ | $9992$ | Yes: $4 \times 2498$ |
| Terminal round | $4$ | Opponent | any $x \in \{1, 2, 3\}$ | $4 - x$ | No |
| Final mirror | $4 - x$ | You | $4 - x$ | $0$ | The last stone is yours |

Rows A, B and C are alternatives, not three consecutive rounds: whichever reply the opponent chooses at $9996$, your answer lands on the same heap $9992$. Every such round consumes four stones, so the descent passes through the multiples $9996, 9992, \dots, 4$ — exactly $2499$ of them — and the opponent is the player to move at each one, until the terminal round hands you the final stone.

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
