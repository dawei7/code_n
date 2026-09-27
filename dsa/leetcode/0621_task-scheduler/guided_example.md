# Guided Example: Task Scheduler

We trace the step-by-step CPU task frequency histogram aggregation ($cnt$), bottleneck frequency identification ($x = \max(cnt)$), co-leader tie count tracking ($s = \sum [v == x]$), slotted time-frame matrix packing ($(x - 1) \cdot (n + 1) + s$), idle cooling slot calculation, and total execution time minimization on representative processor workloads:

- **Input:** $tasks = [\text{"A"}, \text{"A"}, \text{"A"}, \text{"B"}, \text{"B"}, \text{"B"}], \quad n = 2$
- **Required output:** `8`
  - Cooldown rule: Between any two executions of the **same task**, there must be at least $n$ units of cooldown time (filled by other tasks or idle CPU cycles).
  - Objective: Find the minimum total CPU intervals to complete all tasks.
- **Frame-Packing Mathematical Formulation:**
  - Let $x$ be the maximum frequency among all task types:
    $$
    x = \max_{t} cnt[t]
    $$
  - Let $s$ be the number of distinct task types that appear with this maximal frequency $x$.
  - **The Grid / Frame Concept:**
    - The most frequent task must appear $x$ times.
    - Each of the first $x - 1$ instances of this task must be followed by at least $n$ cooling slots.
    - This partitions the timeline into **$x - 1$ complete frames**, each of length $n + 1$:
      $$
      \text{Frame Size} = n + 1
      $$
    - The final $x$-th instance of the maximal tasks requires only their single execution without subsequent cooldown trailing slots.
    - If there are $s$ tasks tied for the maximal frequency, each complete frame holds 1 of each, and the final tail frame holds all $s$ of them:
      $$
      \text{Lower Bound} = (x - 1) \cdot (n + 1) + s
      $$
  - **No-Idle Lower Bound:**
    - The CPU cannot take less time than the total number of tasks:
      $$
      \text{Time} \ge |tasks|
      $$
    - If there are enough other diverse tasks to fill all idle slots across frames, the total time simply equals $|tasks|$.
  - **Closed-Form Minimum Duration:**
    $$
    \text{Ans} = \max(|tasks|, \; (x - 1) \cdot (n + 1) + s)
    $$
- **Step-by-Step Worked Execution Trace:**
  - Input: $tasks = [\text{"A"}, \text{"A"}, \text{"A"}, \text{"B"}, \text{"B"}, \text{"B"}], \quad n = 2$.
  - **Step 1: Compute Frequency Map:**
    - `'A'`: $3$ occurrences
    - `'B'`: $3$ occurrences
    - Frequency map: $\{'A': 3, \; 'B': 3\}$.
    - Total task count: $|tasks| = 6$.
  - **Step 2: Identify Maximal Frequency $x$ and Ties $s$:**
    - Maximum frequency:
      $$
      x = \max(3, 3) = \mathbf{3}
      $$
    - Number of tasks with frequency $x = 3$:
      - Both `'A'` and `'B'` have frequency 3:
      $$
      s = \mathbf{2}
      $$
  - **Step 3: Compute Frame Structure:**
    - Number of complete frames:
      $$
      x - 1 = 3 - 1 = \mathbf{2}
      $$
    - Frame length:
      $$
      n + 1 = 2 + 1 = \mathbf{3}
      $$
    - Complete frame slots:
      $$
      (x - 1) \times (n + 1) = 2 \times 3 = \mathbf{6}
      $$
    - Final tail row size:
      $$
      s = \mathbf{2}
      $$
    - Frame capacity required:
      $$
      \text{Capacity} = 6 + 2 = \mathbf{8}
      $$
  - **Step 4: Visualize the CPU Schedule:**
    ```text
    Frame 1:  [ A ]  [ B ]  [ idle ]   (Length 3)
    Frame 2:  [ A ]  [ B ]  [ idle ]   (Length 3)
    Tail:     [ A ]  [ B ]             (Length 2)
    ```
    - Complete sequential execution order:
      $$
      A \to B \to \text{idle} \to A \to B \to \text{idle} \to A \to B
      $$
    - Between the 1st A (pos 0) and 2nd A (pos 3): exactly 2 slots ($B$, idle) $\implies$ satisfies $n = 2$.
    - Between the 2nd A (pos 3) and 3rd A (pos 6): exactly 2 slots ($B$, idle) $\implies$ satisfies $n = 2$.
    - Total intervals elapsed:
      $$
      3 + 3 + 2 = \mathbf{8}
      $$
  - **Step 5: Apply Capacity Bound:**
    $$
    ans = \max(|tasks|, \; \text{Capacity}) = \max(6, 8) = \mathbf{8}
    $$
- **Zero Cooldown Instance ($n = 0$):**
  - No idle slots needed at all:
    $$
    (3 - 1) \cdot (0 + 1) + 2 = 4
    $$
    $$
    \max(6, 4) = \mathbf{6} \quad (\text{Runs continuously without idle: } A B A B A B)
    $$
- **Abundant Low-Frequency Tasks (No Idles):**
  - Suppose $tasks = [A, A, A, B, C, D, E, F, G], n = 2$.
  - $x = 3, s = 1 \implies (3 - 1) \cdot 3 + 1 = 7$.
  - Total tasks $|tasks| = 9$.
  - $ans = \max(9, 7) = \mathbf{9}$. (The 6 other letters easily fill and overflow the idle slots).

This instance demonstrates periodic scheduling bounds on cooldown-constrained task systems, mathematically proves why max-frequency tasks define the frame lower bound, and derives $O(T)$ runtime and $O(|\Sigma|)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a list of CPU tasks and a cooldown period $n$:
Find the **minimum units of time** needed to execute all tasks such that identical tasks are separated by at least $n$ units.

```text
Tasks: A, A, A, B, B, B. Cooldown n = 2

Schedule Grid (width n + 1 = 3):
  Row 1:  A   B   idle
  Row 2:  A   B   idle
  Row 3:  A   B

Total time = 8 units
```

### The Invariant of the Max-Frequency Skeleton
- The most frequent task dictates the minimum structural framework of the timeline.
- If task $A$ appears 3 times with $n = 2$, it requires at least:
  `A _ _ A _ _ A` (7 slots).
- If multiple tasks tie for the maximum count, each adds 1 to the final row.
- All other less-frequent tasks can be slotted into the idle vacancies between the main tasks.

---

## 2. Conceptual Foundation & Invariants

### 1. Mathematical Formula:
$$
\text{Ans} = \max(|tasks|, \; (x - 1) \cdot (n + 1) + s)
$$
where:
- $x = \max_{k} cnt[k]$ is the highest task count.
- $s = \sum_{k} \mathbf{1}[cnt[k] == x]$ is the number of tasks having count $x$.

### 2. Why $\max(|tasks|, \dots)$?
- If the number of distinct low-frequency tasks is larger than the number of available idle slots, no idling is required.
- The schedule expands horizontally without ever violating cooldown constraints, taking exactly $|tasks|$ units.

> **Frame Packing Invariant.** Packing tasks in descending order of frequency into $x - 1$ columns of width $n + 1$ guarantees that no task with count $\le x$ is placed in the same column twice, satisfying the separation distance $n$.

---

## 3. Step-by-Step Worked Execution

We trace $tasks = [A, A, A, B, B, B], n = 2$:

---

### Step 1: Count Tasks
- $A: 3$
- $B: 3$
- $|tasks| = 6$.

---

### Step 2: Compute $x$ and $s$
- $x = 3$.
- $s = 2$ (both $A$ and $B$).

---

### Step 3: Evaluate Formula
$$
(x - 1) \cdot (n + 1) + s = (3 - 1) \cdot (2 + 1) + 2 = 2 \cdot 3 + 2 = 8
$$
$$
\max(6, 8) = \mathbf{8}
$$

---

## 4. Complete Execution Trace

| Time Slot | Scheduled Task / State | Active Cooldown Status |
|:---:|:---:|:---:|
| $0$ | **`A`** | $A$ enters cooldown until slot $3$ |
| $1$ | **`B`** | $B$ enters cooldown until slot $4$ |
| $2$ | **`idle`** | Waiting for $A$ cooldown |
| $3$ | **`A`** | $A$ enters cooldown until slot $6$ |
| $4$ | **`B`** | $B$ enters cooldown until slot $7$ |
| $5$ | **`idle`** | Waiting for $A$ cooldown |
| $6$ | **`A`** | All $A$s completed |
| $7$ | **`B`** | All $B$s completed |
| **Total Units** | — | **`8`** |

---

## 5. Boundary Cases & Failure Modes

- **$n = 0$ (No Cooldown):** Returns $|tasks|$ directly.
- **All Tasks Unique ($[A, B, C, D]$):** $x = 1, s = 4 \implies (0)(n+1) + 4 = 4 = |tasks|$.
- **One Dominant Task ($[A, A, A, A], n = 3$):** $(4 - 1) \cdot 4 + 1 = 13$ units ($A \dots A \dots A \dots A$).
- **Empty Task List:** Returns $0$.

---

## 6. Traps & Common Anti-Patterns

- **Simulating with a Priority Queue Step-by-Step ($O(T \log 26)$):** While a max-heap simulation works, it is unnecessary and far slower than computing the exact closed-form formula in $O(T)$ time.
- **Forgetting $s$ (Ties for Max Count):** Assuming only one task has the max count omits extra tasks in the final row, undercounting the total by $s - 1$.
- **Forgetting $\max(|tasks|, \dots)$:** When many different tasks exist, the frame formula can evaluate to less than $|tasks|$. Neglecting $\max$ gives an impossible answer smaller than total task count.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Counting task frequencies: $\mathcal{O}(T)$ where $T = |tasks|$.
  - Finding max and ties over alphabet size $|\Sigma| = 26$: $\mathcal{O}(|\Sigma|)$ operations.
  - Closed-form formula: $\mathcal{O}(1)$.
  - Total Time: strictly linear $\mathcal{O}(T)$. For $T = 10^4$, completes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(|\Sigma|) = \mathcal{O}(1)$ auxiliary space for the 26-letter frequency counter.
