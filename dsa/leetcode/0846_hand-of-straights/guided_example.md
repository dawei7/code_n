# Guided Example: Hand of Straights

We trace the step-by-step multiset cardinality divisibility test ($|hand| \bmod groupSize == 0$), card frequency counter mapping ($cnt[v]$), ascending greedy smallest-element anchoring ($x = \min(active)$), consecutive run decrementation ($cnt[x+k] \mathrel{-}= 1$), missing successor detection, and valid straight partition verification on representative card hands:

- **Input:**
  $$
  hand = [1, 2, 3, 6, 2, 3, 4, 7, 8], \quad groupSize = 3
  $$
- **Required output:** `true`
  - Hand partitioning rules:
    - We have a hand of cards, each bearing an integer value.
    - We must partition the entire hand into groups such that each group contains exactly $groupSize$ cards with **consecutive integer values**:
      $$
      [x, \; x + 1, \; x + 2, \; \dots, \; x + groupSize - 1]
      $$
    - Every card in $hand$ must be placed into exactly one group.
    - Objective: Return `true` if a valid partition exists, and `false` otherwise.
    - For $hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]$ ($n = 9, groupSize = 3$):
      - Cardinality check: $9 \bmod 3 = 0$ (valid group count $9 / 3 = 3$).
      - Sorted cards: $[1, 2, 2, 3, 3, 4, 6, 7, 8]$.
      - Group 1: take $[1, 2, 3]$ (consecutive).
      - Remaining cards: $[2, 3, 4, 6, 7, 8]$.
      - Group 2: take $[2, 3, 4]$ (consecutive).
      - Remaining cards: $[6, 7, 8]$.
      - Group 3: take $[6, 7, 8]$ (consecutive).
      - All cards successfully grouped into consecutive straights!
      - Result: **`true`**.
- **Greedy Minimum Element Invariant:**
  - **The Forcing Property of the Smallest Element:**
    - Let $x$ be the smallest card currently present in the multiset.
    - Since no card with value smaller than $x$ exists, **card $x$ cannot be placed in the middle or at the end of any straight**!
    - Therefore, card $x$ **must serve as the starting card** of a straight:
      $$
      [x, \; x + 1, \; \dots, \; x + groupSize - 1]
      $$
    - There is no ambiguity or choice: the required cards $x, x+1, \dots, x+groupSize-1$ are uniquely dictated.
  - **Greedy Consumption Algorithm:**
    1. Count occurrences of each card in a frequency table $cnt$.
    2. Iterate through cards $x$ in sorted ascending order:
       - If $cnt[x] > 0$:
         - Form a straight starting at $x$:
           - For each offset $k \in [0, groupSize - 1]$:
             - Check if card $y = x + k$ is available ($cnt[y] > 0$).
             - If $cnt[y] == 0$, a required consecutive card is missing $\implies$ return **`false`**.
             - Deduct one copy: $cnt[y] \leftarrow cnt[y] - 1$.
    3. If all cards are consumed without encountering a missing successor, return **`true`**.
- **Step-by-Step Worked Execution Trace on the 9-Card Hand:**
  - Initial frequency table:
    $$
    cnt = \{ 1: 1, \; 2: 2, \; 3: 2, \; 4: 1, \; 6: 1, \; 7: 1, \; 8: 1 \}
    $$
  - Sorted card order: $[1, 2, 2, 3, 3, 4, 6, 7, 8]$.
  - **Step 1: Process Smallest Card $x = 1$ ($cnt[1] = 1 > 0$):**
    - Must form straight of size 3 starting at 1: $[1, 2, 3]$.
    - Verify and decrement successors:
      - Offset $k = 0 \implies y = 1$: $cnt[1] = 1 > 0 \implies cnt[1] \leftarrow 0$.
      - Offset $k = 1 \implies y = 2$: $cnt[2] = 2 > 0 \implies cnt[2] \leftarrow 1$.
      - Offset $k = 2 \implies y = 3$: $cnt[3] = 2 > 0 \implies cnt[3] \leftarrow 1$.
    - Group formed: $\mathbf{[1, 2, 3]}.$
    - Remaining frequencies:
      $$
      cnt = \{ 1: 0, \; 2: 1, \; 3: 1, \; 4: 1, \; 6: 1, \; 7: 1, \; 8: 1 \}
      $$
  - **Step 2: Process Next Smallest Card $x = 2$ ($cnt[2] = 1 > 0$):**
    - Must form straight of size 3 starting at 2: $[2, 3, 4]$.
    - Verify and decrement successors:
      - Offset $k = 0 \implies y = 2$: $cnt[2] = 1 > 0 \implies cnt[2] \leftarrow 0$.
      - Offset $k = 1 \implies y = 3$: $cnt[3] = 1 > 0 \implies cnt[3] \leftarrow 0$.
      - Offset $k = 2 \implies y = 4$: $cnt[4] = 1 > 0 \implies cnt[4] \leftarrow 0$.
    - Group formed: $\mathbf{[2, 3, 4]}.$
    - Remaining frequencies:
      $$
      cnt = \{ 1: 0, \; 2: 0, \; 3: 0, \; 4: 0, \; 6: 1, \; 7: 1, \; 8: 1 \}
      $$
  - **Step 3: Process Next Active Card $x = 6$ ($cnt[6] = 1 > 0$):**
    - Must form straight of size 3 starting at 6: $[6, 7, 8]$.
    - Verify and decrement successors:
      - Offset $k = 0 \implies y = 6$: $cnt[6] = 1 > 0 \implies cnt[6] \leftarrow 0$.
      - Offset $k = 1 \implies y = 7$: $cnt[7] = 1 > 0 \implies cnt[7] \leftarrow 0$.
      - Offset $k = 2 \implies y = 8$: $cnt[8] = 1 > 0 \implies cnt[8] \leftarrow 0$.
    - Group formed: $\mathbf{[6, 7, 8]}.$
    - Remaining frequencies: all zero!
  - **All cards cleanly partitioned:**
    $$
    ans = \mathbf{\text{true}}
    $$
- **Missing Consecutive Card Failure ($hand = [1, 2, 3, 4, 5], groupSize = 4$):**
  - $|hand| = 5 \bmod 4 = 1 \ne 0 \implies$ fails divisibility immediately $\implies \mathbf{\text{false}}.$
- **Missing Successor Value ($hand = [1, 2, 4], groupSize = 3$):**
  - Smallest is 1; requires $[1, 2, 3]$.
  - Card 3 has count $0 \implies$ cannot complete straight $\implies \mathbf{\text{false}}.$

This instance demonstrates multiset decomposition into bounded intervals over linearly ordered semirings, mathematically proves why the minimum-element greedy forcing rule guarantees finding a valid matching if one exists without backtracking, and derives $O(N \log N)$ execution time and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given card values and $groupSize$:
Can we partition all cards into groups of size $groupSize$ containing **consecutive numbers**?

```text
hand = [ 1, 2, 3, 6, 2, 3, 4, 7, 8 ], groupSize = 3

Cards:
  Take [1, 2, 3] -> remaining: [2, 3, 4, 6, 7, 8]
  Take [2, 3, 4] -> remaining: [6, 7, 8]
  Take [6, 7, 8] -> remaining: []

All cards used in valid straights!
Result: true
```

### The Invariant of the Smallest Element
- The smallest remaining card $x$ **cannot be anywhere except the start of a straight**.
- It forces the existence of $x, x+1, \dots, x+groupSize-1$.
- If any required successor has count 0, the hand is impossible to partition.

---

## 2. Conceptual Foundation & Invariants

### 1. Divisibility Necessary Condition:
$$
|hand| \equiv 0 \pmod{groupSize}
$$

### 2. Greedy Anchor Invariant:
For $x = \min \{ v \mid cnt[v] > 0 \}$:
$$
\forall k \in [0, groupSize - 1]: cnt[x + k] \ge 1
$$
$$
cnt[x + k] \leftarrow cnt[x + k] - 1
$$

> **Matroid Greedy Basis Invariant.** Interval graph decomposition of multisets into contiguous chains of uniform length admits a matroid structure. The greedy strategy of repeatedly matching the minimal element of the ground set yields the unique optimal base without branching.

---

## 3. Step-by-Step Worked Execution

We trace $hand = [1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize = 3$:

---

### Step 1: Divisibility Check
- $9 \bmod 3 = 0$. Pass!

---

### Step 2: Straight 1 ($x = 1$)
- Cards $1, 2, 3$ decremented $\implies$ straight $[1, 2, 3]$.

---

### Step 3: Straight 2 ($x = 2$)
- Cards $2, 3, 4$ decremented $\implies$ straight $[2, 3, 4]$.

---

### Step 4: Straight 3 ($x = 6$)
- Cards $6, 7, 8$ decremented $\implies$ straight $[6, 7, 8]$.

---

### Step 5: Output
- Multiset exhausted $\implies \mathbf{\text{true}}.$

---

## 4. Complete Execution Trace

| Straight Built | Anchor Card $x$ | Required Consecutive Cards | Counts Before Decrement | Counts After Decrement | Valid Straight? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Group $1$ | $1$ | $1, 2, 3$ | $cnt[1]=1, cnt[2]=2, cnt[3]=2$ | $cnt[1]=0, cnt[2]=1, cnt[3]=1$ | **Yes** |
| Group $2$ | $2$ | $2, 3, 4$ | $cnt[2]=1, cnt[3]=1, cnt[4]=1$ | $cnt[2]=0, cnt[3]=0, cnt[4]=0$ | **Yes** |
| **Group $3$** | **$6$** | **$6, 7, 8$** | **$cnt[6]=1, cnt[7]=1, cnt[8]=1$** | **$cnt[6]=0, cnt[7]=0, cnt[8]=0$** | **`Yes`** |
| **Complete** | — | — | — | All counts zero | **`true`** |

---

## 5. Boundary Cases & Failure Modes

- **Length Not Divisible ($|hand| \bmod groupSize \ne 0$):** Immediate return `false`.
- **$groupSize = 1$:** Every single card forms its own trivial group of length 1 $\implies$ always `true`.
- **Missing Middle Card ($[1, 2, 4]$ with $groupSize = 3$):** Card 3 is absent $\implies cnt[3] == 0 \implies$ returns `false`.
- **Multiple Identical Straights ($[1, 2, 3, 1, 2, 3]$):** Two independent $[1, 2, 3]$ groups processed sequentially $\implies \text{true}$.

---

## 6. Traps & Common Anti-Patterns

- **Trying to Start Straights from the Largest Element:** Starting from maximum elements is also valid, but arbitrary middle elements cause ambiguity. Always process from an extreme (strictly ascending from minimum).
- **Not Checking Cardinality Upfront:** If length is not divisible by `groupSize`, performing full frequency counting and sorting is wasted computation; check `len(hand) % groupSize` first.
- **Modifying Counter Keys During Iteration:** Iterate over the sorted unique keys or sorted input list to avoid dictionary mutation runtime errors.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Initial frequency counting: $\mathcal{O}(N)$.
  - Sorting $N$ elements: $\mathcal{O}(N \log N)$ where $N \le 10^4$.
  - For each card, decrementing $groupSize$ elements: each card is decremented once $\implies \mathcal{O}(N)$.
  - Total Time: strictly $\mathcal{O}(N \log N)$. Completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory for the frequency table.
