# Guided Example: Chalkboard XOR Game

We trace the step-by-step impartial combinatorial game rules, total bitwise XOR state sum ($S = \bigoplus nums$), instant victory zero-sum condition ($S == 0 \implies \text{win}$), parity pairing invariant ($n \equiv 0 \pmod 2$), vector space contradiction proof on fatal move existence, and deterministic Sprague-Grundy outcome classification on representative integer multisets:

- **Input:** $nums = [1, 1, 2]$
- **Required output:** `false`
  - Combinatorial game specifications:
    - An array $nums$ of length $n$ is written on a chalkboard.
    - Two players, Alice and Bob, take turns erasing one number per turn; Alice plays first.
    - Let $S$ be the bitwise XOR sum of all remaining numbers on the chalkboard:
      $$
      S = \bigoplus_{x \in nums} x
      $$
    - **Victory Condition:** If $S == 0$ at the start of a player's turn, that player **wins immediately**!
    - **Losing Condition:** If a player erases a number $x$ and the remaining XOR sum becomes $0$ ($S \oplus x == 0$), that player **loses immediately**.
    - Both players play with optimal strategy.
    - Objective: Return `true` if Alice wins, or `false` if Bob wins.
    - For $nums = [1, 1, 2]$ ($n = 3$):
      - Total initial XOR: $S = 1 \oplus 1 \oplus 2 = 0 \oplus 2 = \mathbf{2} \ne 0$.
      - Alice does not win on turn 0.
      - Alice must erase a number:
        - If Alice erases $1$: remaining is $[1, 2]$, XOR is $1 \oplus 2 = 3 \ne 0$. Safe for Alice.
          - On Bob's turn, board has $[1, 2]$ ($S = 3$).
          - If Bob erases $1$, remaining is $[2]$ (XOR $2 \ne 0$). Safe for Bob.
          - On Alice's turn, board has $[2]$ ($S = 2$).
          - Alice MUST erase $2$, leaving empty board with XOR $0 \implies$ Alice loses!
        - If Alice erases $2$: remaining is $[1, 1]$, XOR is $1 \oplus 1 = 0 \implies$ Alice loses immediately!
      - Every possible path results in Alice losing $\implies$ return **`false`**.
- **Even Parity & Non-Zero Move Existence Invariant:**
  - **Case 1: Initial Zero Sum ($S == 0$):**
    - By the explicit game rules, if $S == 0$ at the start of the game, Alice wins on turn 0 immediately without making any moves!
  - **Case 2: Initial Non-Zero Sum ($S \ne 0$):**
    - Suppose it is a player's turn with $n$ elements and XOR sum $S \ne 0$.
    - A move of erasing element $nums[i]$ is fatal if and only if the remaining XOR sum becomes 0:
      $$
      S \oplus nums[i] == 0 \iff nums[i] == S
      $$
    - A player is forced to lose if and only if **EVERY choice of $nums[i]$ is fatal** (i.e. $nums[i] == S$ for all $i \in [0, n - 1]$).
    - Can every choice be fatal?
      - Compute the XOR sum of all candidate remaining states:
        $$
        \bigoplus_{i = 1}^n (S \oplus nums[i]) = \left( \bigoplus_{i = 1}^n S \right) \oplus \left( \bigoplus_{i = 1}^n nums[i] \right)
        $$
      - Notice that $\bigoplus_{i=1}^n nums[i] = S$ by definition!
      - If $n$ is **even**, XORing $S$ an even number of times yields $0$:
        $$
        \bigoplus_{i = 1}^n (S \oplus nums[i]) = 0 \oplus S = \mathbf{S}
        $$
      - Because $S \ne 0$, the sum of all $(S \oplus nums[i])$ is non-zero ($S \ne 0$).
      - **A set of values whose XOR sum is non-zero CANNOT all be zero!**
      - Therefore, whenever $n$ is **even**, there **MUST exist at least one element** $nums[i]$ such that $S \oplus nums[i] \ne 0$!
  - **The Winning Strategy for Even $n$:**
    - When $n$ is even, Alice can ALWAYS pick an element that does not cause remaining XOR to become 0.
    - This leaves Bob with an **odd** number of elements and non-zero XOR.
    - Bob is unable to guarantee a safe move, and the game must terminate in a finite number of steps.
    - Thus, Alice wins if and only if:
      $$
      n \equiv 0 \pmod 2 \quad \lor \quad S == 0
      $$
- **Step-by-Step Worked Execution Trace on $nums = [1, 1, 2]$ ($n = 3$):**
  - **Step 1: Check Length Parity:**
    $$
    n = 3 \implies 3 \pmod 2 = 1 \quad \mathbf{(Odd\ Length)}
    $$
  - **Step 2: Compute Total XOR Sum $S$:**
    $$
    S = 1 \oplus 1 \oplus 2 = 0 \oplus 2 = \mathbf{2}
    $$
  - **Step 3: Evaluate Win Predicate:**
    $$
    (n \bmod 2 == 0) \lor (S == 0) \iff (1 == 0) \lor (2 == 0) \implies \mathbf{False}
    $$
  - Output:
    $$
    ans = \mathbf{false}
    $$
- **Step-by-Step Worked Execution Trace on Sample 2 ($nums = [0, 1]$):**
  - Length $n = 2$ (even).
  - Total XOR: $S = 0 \oplus 1 = 1 \ne 0$.
  - Because $n$ is even, Alice is guaranteed a winning move:
    - Alice erases $0$.
    - Remaining board: $[1]$ (XOR is $1 \ne 0$).
    - On Bob's turn, Bob must erase $1$, leaving empty board with XOR $0$.
    - Bob loses immediately! Alice wins.
  - Parity check: $n \bmod 2 == 0 \implies \mathbf{True}$.
  - Output:
    $$
    ans = \mathbf{true}
    $$
- **Immediate Win Initial State ($nums = [1, 2, 3]$):**
  - $n = 3$ (odd).
  - XOR sum: $1 \oplus 2 \oplus 3 = 3 \oplus 3 = \mathbf{0}$.
  - Initial XOR is 0 $\implies$ Alice wins instantly on turn 0!
  - Returns **`true`**.

This instance demonstrates impartial games under normal play convention and boolean vector space parity conservation, mathematically proves why even dimensionality over $\mathbb{F}_2^b$ precludes uniform degeneracy of marginal hyperplanes, and derives $O(N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given numbers on a chalkboard:
Players take turns erasing one number.
If erasing a number makes total XOR $= 0$, that player loses.
If total XOR is already 0 at turn start, that player wins immediately.
Does Alice (first player) win?

```text
nums = [ 1, 1, 2 ]  (length 3 is ODD)
Total XOR = 1 ^ 1 ^ 2 = 2 (non-zero)

Odd length + non-zero XOR -> Alice LOSES!
Result: false

nums = [ 0, 1 ]      (length 2 is EVEN)
Total XOR = 0 ^ 1 = 1 (non-zero)

Even length -> Alice can ALWAYS find a safe move!
Alice WINS!
Result: true
```

### The Invariant of the Even-Length Guarantee
- If initial XOR sum $S == 0$, Alice wins instantly.
- If $S \ne 0$ and $n$ is even, the XOR sum of all possible next states is $S \ne 0$, proving a safe move **always exists**.
- Alice wins $\iff n \pmod 2 == 0 \lor S == 0$.

---

## 2. Conceptual Foundation & Invariants

### 1. Cumulative XOR Sum:
$$
S = \bigoplus_{x \in nums} x
$$

### 2. Parity Identity Theorem:
$$
\bigoplus_{i = 1}^n (S \oplus nums[i]) = (n \cdot S) \oplus S = \begin{cases} S & n \equiv 0 \pmod 2 \\ 0 & n \equiv 1 \pmod 2 \end{cases}
$$
$$
\text{AliceWins} \iff (n \equiv 0 \pmod 2) \;\lor\; (S == 0)
$$

> **Bouton-Nim Sum Parity Invariant.** In the affine quotient space $\mathbb{F}_2^k$, the sum of coordinate projections $\sum (S \oplus v_i) = S$ for even $n$ guarantees that the zero vector cannot be an absorbing point for all elementary coordinate deletions simultaneously.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 1, 2]$:

---

### Step 1: Check Length
- $n = 3$ (odd).

---

### Step 2: Compute XOR Sum
- $1 \oplus 1 \oplus 2 = 2 \ne 0$.

---

### Step 3: Evaluate Win Rule
- Neither $n$ is even nor $S == 0$.
- Alice loses.

---

### Step 4: Output
$$
\mathbf{false}
$$

---

## 4. Complete Execution Trace

| Chalkboard State $nums$ | Length $n$ | Length Parity | Total XOR $S$ | Immediate Win? ($S == 0$) | Alice Wins? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `[1, 1, 2]` | $3$ | Odd | $2$ | No | **`false`** |
| `[0, 1]` | $2$ | Even | $1$ | No | **`true`** |
| `[1, 2, 3]` | $3$ | Odd | $0$ | **Yes** | **`true`** |
| `[1, 2, 3, 4]` | $4$ | Even | $4$ | No | **`true`** |

---

## 5. Boundary Cases & Failure Modes

- **Initial XOR is 0:** Instant win on turn 0 for Alice regardless of length parity $\implies$ `true`.
- **Single Element ($[5]$):** $n = 1$ (odd), $S = 5 \ne 0 \implies$ Alice must erase 5, leaving 0, loses $\implies$ `false`.
- **Two Identical Elements ($[3, 3]$):** $S = 0 \implies$ `true`.
- **Large Array ($N = 1000$):** Single linear XOR fold runs in $< 0.05$ ms.

---

## 6. Traps & Common Anti-Patterns

- **Attempting Minimax Game Tree Search:** A full game search on 1000 elements has $1000!$ states, resulting in immediate TLE. The game-theoretic proof reduces the solution to a single parity check.
- **Forgetting the Immediate Zero-Sum Victory Rule:** If $S == 0$ initially, Alice wins immediately without needing even length.
- **Assuming Player Who Erases to 0 Wins:** The rules state that erasing to 0 causes that player to **lose**, not win.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Length check: $\mathcal{O}(1)$.
  - Single pass XOR fold across $N$ elements: $\mathcal{O}(N)$.
  - Total Time: strictly linear $\mathcal{O}(N)$ where $N \le 1000$. Completes in $< 0.05$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space.
