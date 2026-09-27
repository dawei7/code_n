# Guided Example: Dota2 Senate

We trace the step-by-step party index queue partitioning ($qr$ for Radiant, $qd$ for Dire), cyclic round-robin turn order simulation ($i < j$), greedy earliest-threat opponent elimination, survivor re-queueing with round offset ($idx + n$), party exhaustion termination, and strategic majority victory determination on representative voting sequences:

- **Input:** $senate = \text{"RDD"}$
- **Required output:** `\text{"Dire"}`
  - Rules of procedure:
    - Voting proceeds in cyclic order from left to right.
    - Each senator with active voting rights can choose to **ban one opposing senator**, stripping them of all rights for the remainder of the game.
    - Optimal game-theoretic strategy: Each senator greedily bans the **earliest upcoming opponent** to preempt that opponent's turn and protect teammates.
    - The first party to completely eliminate the opposing faction wins.
- **Dual FIFO Queue Architecture:**
  - Track each party's active senators in two separate FIFO queues:
    - `qr`: Queue of turn indices for Radiant senators.
    - `qd`: Queue of turn indices for Dire senators.
  - **Turn Execution & Elimination Step:**
    - Peek at the front of both queues: $r = qr[0], \; d = qd[0]$.
    - The senator with the **smaller index** acts first in this round:
      - **Case 1: $r < d$ (Radiant acts first):**
        - Radiant senator at index $r$ exercises their right to ban Dire senator at index $d$.
        - Dire senator $d$ is permanently eliminated (popped from `qd`).
        - Radiant senator $r$ survives and re-enters the queue for the next round with updated turn timestamp:
          $$
          qr.\text{append}(r + n)
          $$
        - Both original front elements are popped: $qr.\text{popleft}(), \; qd.\text{popleft}()$.
      - **Case 2: $d < r$ (Dire acts first):**
        - Dire senator at index $d$ bans Radiant senator at index $r$.
        - Radiant senator $r$ is permanently eliminated.
        - Dire senator $d$ re-enters the queue with updated timestamp:
          $$
          qd.\text{append}(d + n)
          $$
  - **Termination:**
    - When either queue becomes empty, the party whose queue still holds active senators is declared the winner!
- **Step-by-Step Worked Execution Trace on $\text{"RDD"}$ ($n = 3$):**
  - Initial indices:
    - Index 0: `'R'` (Radiant)
    - Index 1: `'D'` (Dire 1)
    - Index 2: `'D'` (Dire 2)
  - Populate queues:
    $$
    qr = [0], \quad qd = [1, \; 2]
    $$
  - **Round 1, Action 1:**
    - Compare queue heads:
      $$
      r = 0, \quad d = 1 \implies 0 < 1 \implies \mathbf{Radiant\ acts\ first!}
      $$
    - Radiant senator 0 bans Dire senator 1.
    - Dire senator 1 is permanently eliminated.
    - Radiant senator 0 survives and is scheduled for the next cycle:
      $$
      r_{next} = r + n = 0 + 3 = \mathbf{3}
      $$
    - Queue states after Action 1:
      $$
      qr = [3], \quad qd = [2]
      $$
  - **Round 1, Action 2:**
    - Compare queue heads:
      $$
      r = 3, \quad d = 2 \implies 2 < 3 \implies \mathbf{Dire\ acts\ first!}
      $$
    - Notice that Dire senator 2 now has their turn in the first cycle ($t = 2$), which occurs **before** Radiant senator 0 can vote again in round 2 ($t = 3$)!
    - Dire senator 2 exercises their right to ban Radiant senator 3.
    - Radiant senator 3 is permanently eliminated!
    - Dire senator 2 survives and is scheduled for the next cycle:
      $$
      d_{next} = d + n = 2 + 3 = \mathbf{5}
      $$
    - Queue states after Action 2:
      $$
      qr = [], \quad qd = [5]
      $$
  - **Step 3: Victory Declaration:**
    - Radiant queue $qr$ is completely empty ($|qr| = 0$).
    - Dire queue $qd$ holds the sole surviving senator.
    - Dire party announces victory!
    - Emit:
      $$
      \mathbf{\text{"Dire"}}
      $$
- **Two-Senator Duel ($senate = \text{"RD"}$):**
  - $qr = [0], qd = [1]$.
  - $0 < 1 \implies$ Radiant 0 bans Dire 1.
  - $qd$ is exhausted immediately $\implies$ Returns **`"Radiant"`**.
- **Dire First Mover ($senate = \text{"DRD"}$):**
  - $qr = [1], qd = [0, 2]$.
  - $0 < 1 \implies$ Dire 0 bans Radiant 1.
  - Radiant has no remaining senators $\implies$ Returns **`"Dire"`**.

This instance demonstrates round-robin priority queuing and adversarial game-theoretic preemption, mathematically proves why offset index increments preserve cyclic causality without re-sorting, and derives $O(N)$ execution time and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a voting string of Radiant (`'R'`) and Dire (`'D'`) senators:
Senators vote in cyclic order, each greedily banning the next opponent.
Predict which party wins: `"Radiant"` or `"Dire"`.

```text
senate = "RDD" (length n = 3)

Queues:
  qr = [ 0 ]
  qd = [ 1, 2 ]

Turn 1: compare r=0, d=1
  0 < 1 -> Radiant 0 bans Dire 1!
  Radiant 0 moves to round 2: 0 + 3 = 3
  qr = [ 3 ], qd = [ 2 ]

Turn 2: compare r=3, d=2
  2 < 3 -> Dire 2 acts before Radiant's next turn!
  Dire 2 bans Radiant 3!
  Dire 2 moves to round 2: 2 + 3 = 5
  qr = [ ], qd = [ 5 ]

Radiant eliminated -> Dire Wins!
```

### The Invariant of the Cyclic Timeline
- Instead of resetting indices back to 0 at the end of each round, append surviving senators with index **$idx + n$**.
- This naturally models cyclic time: turn $k$ in round $r$ always happens before turn $j$ in round $r + 1$ because $k < j + n$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Dual Queue Step:
Pop $r$ from $qr$ and $d$ from $qd$:
- If $r < d$:
  - Radiant bans Dire: push $r + n$ to $qr$.
- If $d < r$:
  - Dire bans Radiant: push $d + n$ to $qd$.

### 2. Termination Invariant:
Loop terminates when $\min(|qr|, |qd|) == 0$.
Winner is `"Radiant"` if $qr$ has elements, else `"Dire"`.

> **Greedy Preemption Invariant.** Banning the opponent whose turn occurs nearest in the future eliminates an active opposing vote before it can be exercised, strictly dominating the elimination of any later opponent.

---

## 3. Step-by-Step Worked Execution

We trace $senate = \text{"RDD"}$:

---

### Step 1: Initialize
- $qr = [0]$.
- $qd = [1, 2]$.
- $n = 3$.

---

### Step 2: Turn 1
- $r = 0, d = 1$.
- $0 < 1 \implies$ R bans D1.
- R requeues as $0 + 3 = 3$.
- $qr = [3], qd = [2]$.

---

### Step 3: Turn 2
- $r = 3, d = 2$.
- $2 < 3 \implies$ D2 bans R.
- D2 requeues as $2 + 3 = 5$.
- $qr = [], qd = [5]$.

---

### Step 4: Outcome
- $qr$ is empty.
- Return **`"Dire"`**.

---

## 4. Complete Execution Trace

| Turn Event | Active $qr$ | Active $qd$ | Compared Pair $(r, d)$ | Actor | Banned Senator | Survivor Re-Queued As |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Initial | `[0]` | `[1, 2]` | — | — | — | — |
| Step 1 | `[0]` | `[1, 2]` | $(0, 1)$ | **Radiant 0** | Dire 1 | $r \to 0 + 3 = \mathbf{3}$ |
| Step 2 | `[3]` | `[2]` | $(3, 2)$ | **Dire 2** | Radiant 3 | $d \to 2 + 3 = \mathbf{5}$ |
| **Final** | **`[]`** | **`[5]`** | — | — | — | **`"Dire"` Wins** |

---

## 5. Boundary Cases & Failure Modes

- **All Radiant (`"RRR"`):** Dire queue empty at start $\implies$ Radiant wins immediately.
- **All Dire (`"DDD"`):** Dire wins immediately.
- **Alternating Pairs (`"RDRD"`):** Round 1 has R0 ban D1, R2 ban D3 $\implies$ Radiant sweeps.
- **Large Senate ($N = 10^4$):** Each comparison eliminates one senator $\implies$ terminates in at most $N$ steps.

---

## 6. Traps & Common Anti-Patterns

- **String Manipulation / Deletion ($O(N^2)$):** Modifying the string or searching forward with `s.find('D')` leads to quadratic slowdown. Two FIFO queues maintain constant-time $O(1)$ operations per turn.
- **Banning Arbitrary Opponents:** Banning an opponent who has already voted in the current round allows an upcoming opponent to vote and ban one of your teammates. The nearest upcoming opponent must always be banned.
- **Modulo Index Confusion:** Using $idx \pmod n$ without adding $n$ causes round 2 senators to collide with round 1 senators. Adding $+ n$ maintains chronological monotonicity.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Enqueueing initial indices: $\mathcal{O}(N)$.
  - In each step of the simulation, exactly one senator is permanently banned and removed from their queue.
  - At most $N$ eliminations can occur.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 2$ ms for $N = 10^4$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ auxiliary space for the two FIFO queues.
