# Guided Example: Card Flipping Game

We trace the step-by-step card flip orientation mechanics, identical face disqualification property ($fronts[i] == backs[i] \implies \text{disqualified}$), universal reachability of non-identical face values, set filtering over candidate numbers, and minimum feasible good integer selection on representative card hands:

- **Input:**
  $$
  fronts = [1, 2, 4, 4, 7], \quad backs = [1, 3, 4, 1, 3]
  $$
- **Required output:** `2`
  - Card flipping game rules:
    - There are $n$ cards laid out on a table. The $i$-th card has $fronts[i]$ facing up and $backs[i]$ facing down.
    - You may flip any subset of cards. Flipping a card swaps its front and back numbers.
    - A number $x$ is called **good** if, after an optimal assignment of card flips, $x$ is on the back of at least one card and **not on the front of any card**.
    - Objective: Find the **minimum good number**. If no number can be good, return 0.
    - For $fronts = [1, 2, 4, 4, 7]$ and $backs = [1, 3, 4, 1, 3]$:
      - Card 0 has $(1, 1)$: front is 1, back is 1. Flipping this card leaves 1 facing up. Thus, 1 can **never** be avoided on the front! $1$ is disqualified.
      - Card 2 has $(4, 4)$: front is 4, back is 4. Flipping leaves 4 facing up. $4$ is disqualified.
      - Examine number 2 (on Card 1):
        - Card 1 has front 2, back 3.
        - Flip Card 1: front becomes 3, back becomes 2.
        - Card 0: keep as is (front 1, back 1).
        - Card 2: keep as is (front 4, back 4).
        - Card 3: keep as is (front 4, back 1).
        - Card 4: keep as is (front 7, back 3).
        - Now fronts are: $[1, 3, 4, 4, 7]$. Number 2 appears on **zero** fronts!
        - Number 2 appears on the back of Card 1.
        - Therefore, 2 is a valid **good number**!
      - Since 2 is the smallest possible candidate, output is **`2`**.
- **Double-Sided Identity & Feasibility Invariant:**
  - **The Disqualification Invariant ($S$):**
    - If a card has identical numbers on both sides ($fronts[i] == backs[i] = v$):
      - Regardless of whether this card is flipped or not, number $v$ **always faces up**.
      - Therefore, $v$ can **never** be eliminated from all front faces!
      - Define the set of permanently disqualified numbers:
        $$
        S = \{ fronts[i] \mid fronts[i] = backs[i] \}
        $$
  - **The Independent Flipping Guarantee:**
    - For any number $x \notin S$:
      - No single card has $x$ on both sides.
      - Whenever a card has $x$ facing up on the front, we can **flip that specific card** so that $x$ moves to the back.
      - Since $x$ was not on the back of that card initially, flipping it does not place another $x$ on the front.
      - Cards that do not contain $x$ at all can be left unflipped.
      - Thus, **every number $x \in (fronts \cup backs) \setminus S$ is guaranteed to be achievable as a good number**!
  - **Optimal Integer Selection:**
    - The minimum good integer is simply:
      $$
      ans = \min \{ x \in (fronts \cup backs) \mid x \notin S \}
      $$
    - If every number appears on an identical-sided card, return $0$.
- **Step-by-Step Worked Execution Trace on the 5-Card Hand:**
  - Cards:
    - Card 0: $(front = 1, \; back = 1)$
    - Card 1: $(front = 2, \; back = 3)$
    - Card 2: $(front = 4, \; back = 4)$
    - Card 3: $(front = 4, \; back = 1)$
    - Card 4: $(front = 7, \; back = 3)$
  - **Phase 0: Identify Disqualified Numbers ($front == back$):**
    - Card 0: $1 == 1 \implies \mathbf{1\ is\ Disqualified!}$
    - Card 1: $2 \ne 3$
    - Card 2: $4 == 4 \implies \mathbf{4\ is\ Disqualified!}$
    - Card 3: $4 \ne 1$
    - Card 4: $7 \ne 3$
    - Disqualified set:
      $$
      S = \{1, \; 4\}
      $$
  - **Phase 1: Filter Candidate Numbers Across All Faces:**
    - All numbers appearing on cards: $\{1, 2, 3, 4, 7\}$.
    - Filter against $S$:
      - Number $1$: in $S \implies \mathbf{Invalid.}$
      - Number $2$: $2 \notin S \implies \mathbf{Valid\ Candidate!}$
      - Number $3$: $3 \notin S \implies \mathbf{Valid\ Candidate!}$
      - Number $4$: in $S \implies \mathbf{Invalid.}$
      - Number $7$: $7 \notin S \implies \mathbf{Valid\ Candidate!}$
    - Feasible good numbers:
      $$
      \{2, \; 3, \; 7\}
      $$
  - **Phase 2: Minimum Value Selection:**
    $$
    ans = \min(2, 3, 7) = \mathbf{2}
    $$
- **Single Identical Card Trace ($fronts = [1], backs = [1]$):**
  - Card 0 has $(1, 1)$.
  - $S = \{1\}$.
  - No valid numbers remain $\implies ans = \mathbf{0}$.
- **All Distinct Numbers Trace ($fronts = [1, 2], backs = [3, 4]$):**
  - $S = \emptyset$.
  - Minimum number is $\min(1, 2, 3, 4) = \mathbf{1}$.

This instance demonstrates 2-SAT independence reduction on Boolean flip variables and obstruction set characterization, mathematically proves why single-variable obstructions $x = \bar{x}$ form the only forbidden certificates on decoupled 1-card constraints, and derives $O(N)$ execution time and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given cards with $fronts$ and $backs$:
Flip any cards so that a number $x$ appears on the back of some card, but on **zero** fronts.
Find the **minimum** such number $x$.

```text
fronts: [ 1, 2, 4, 4, 7 ]
backs:  [ 1, 3, 4, 1, 3 ]

Card 0: (1, 1) -> 1 is on BOTH sides! 1 can NEVER be avoided -> DISQUALIFIED!
Card 2: (4, 4) -> 4 is on BOTH sides! 4 can NEVER be avoided -> DISQUALIFIED!

Disqualified numbers: { 1, 4 }

Other numbers on cards: { 2, 3, 7 }
Smallest valid number = 2
Result: 2
```

### The Invariant of the Unavoidable Numbers
- A number $v$ can never be good if any card has $v$ on **both front and back** ($fronts[i] == backs[i]$).
- Any other number on the cards can always be made good by flipping cards so that $x$ always faces down.
- The answer is the minimum number among all card values not in the disqualified set.

---

## 2. Conceptual Foundation & Invariants

### 1. Obstruction Set:
$$
S = \{ fronts[i] \mid fronts[i] = backs[i] \}
$$

### 2. Feasible Minimum Selection:
$$
ans = \min \big( \{ x \in fronts \cup backs \mid x \notin S \} \cup \{0\} \big)
$$

> **Boolean Decomposability Invariant.** The condition that value $x$ is absent from all card fronts is a collection of decoupled constraints on each card $i$. The clause for card $i$ is satisfiable unless $fronts[i] = backs[i] = x$. Thus, global satisfiability factors into independent local non-identity tests.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Find Disqualified Set
- Card 0: $1 == 1 \implies 1 \in S$.
- Card 2: $4 == 4 \implies 4 \in S$.
- $S = \{1, 4\}$.

---

### Step 2: Check Candidates
- Candidates: 1, 2, 3, 4, 7.
- Filter out $\{1, 4\} \implies \{2, 3, 7\}$.

---

### Step 3: Find Minimum
- $\min(2, 3, 7) = \mathbf{2}$.

---

### Step 4: Output
$$
\mathbf{2}
$$

---

## 4. Complete Execution Trace

| Card Index $i$ | Front Value | Back Value | $front == back$? | Added to Disqualified Set $S$? |
|:---:|:---:|:---:|:---:|:---:|
| $0$ | $1$ | $1$ | **Yes** | **Add $1$ to $S$** |
| $1$ | $2$ | $3$ | No | — |
| $2$ | $4$ | $4$ | **Yes** | **Add $4$ to $S$** |
| $3$ | $4$ | $1$ | No | — |
| **$4$** | **$7$** | **$3$** | **No** | — |
| **Candidate Evaluation** | — | — | — | **$S = \{1, 4\} \implies \min(\{2, 3, 7\}) = \mathbf{2}$** |

---

## 5. Boundary Cases & Failure Modes

- **Single Card with Same Number ($fronts = [1], backs = [1]$):** Only number 1 is disqualified $\implies$ returns 0.
- **No Card with Same Number:** All numbers are eligible $\implies$ minimum of all numbers.
- **Large Arrays ($N = 2000$):** Set filtering processes $2000$ elements in $< 0.5$ ms.
- **No Feasible Number Exists:** Returns default 0.

---

## 6. Traps & Common Anti-Patterns

- **Simulating All $2^N$ Card Flips:** For $N = 2000$, checking all flip configurations takes $2^{2000}$ operations (impossible). Mathematical reduction to the obstruction set $S$ solves the problem in linear time.
- **Thinking Multiple Cards with the Same Number Interact:** Cards are flipped independently. Flipping card $i$ has zero effect on card $j$.
- **Ignoring Back Values as Candidates:** Numbers on the backs can also be good (they will face down after other cards flip). Consider all numbers from both $fronts$ and $backs$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Finding identical-face pairs to build set $S$: $\mathcal{O}(N)$.
  - Iterating over all $2N$ front and back values to find the minimum unbanned value: $\mathcal{O}(N)$.
  - Total Time: strictly linear $\mathcal{O}(N)$ where $N \le 2000$. Completes in $< 0.2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory for the disqualified set $S$.
