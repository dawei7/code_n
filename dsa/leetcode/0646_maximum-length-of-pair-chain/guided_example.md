# Guided Example: Maximum Length of Pair Chain

We trace the step-by-step interval scheduling reduction, right-endpoint ascending sorting ($\text{sort by } b$), greedy earliest finish time selection ($pre < a$), strict inequality boundary testing ($b < c$), overlapping candidate pruning, and chain length maximization on representative integer interval pairs:

- **Input:** $pairs = [[1, 2], \; [2, 3], \; [3, 4]]$
- **Required output:** `2`
  - Chaining rule: Pair $p_2 = [c, d]$ can follow pair $p_1 = [a, b]$ if and only if:
    $$
    b < c
    $$
    (Strictly greater: if $b == c$, they touch and cannot chain).
  - You may select pairs in any order and skip any pairs.
  - Objective: Maximize the total number of pairs in a valid chain.
- **Interval Scheduling Equivalence & Earliest Finish Time Invariant:**
  - This problem is mathematically isomorphic to the classic **Interval Scheduling Maximization Problem** (ISMP):
    - Each pair $[a, b]$ represents an activity starting at time $a$ and ending at time $b$.
    - We wish to schedule the maximum number of mutually non-overlapping activities.
  - **The Greedy Strategy:**
    - Always choose the pair that **finishes earliest** (smallest right endpoint $b$).
    - Finishing as early as possible leaves the maximum possible remaining timeline slack for future pairs.
    - Sorting by $b$ ascending guarantees that we consider endpoints in order of their termination:
      $$
      b_1 \le b_2 \le \dots \le b_n
      $$
    - If the next pair $[a, b]$ starts strictly after the end of the previous chosen pair ($a > pre$):
      - We greedily append it to our chain:
        $$
        ans \leftarrow ans + 1
        $$
        $$
        pre \leftarrow b
        $$
      - If $a \le pre$, the pair conflicts with our current choice and is discarded.
- **Step-by-Step Worked Execution Trace on $[[1, 2], [2, 3], [3, 4]]$:**
  - **Step 1: Sort by Right Endpoint $b$:**
    - Pair 0: $[1, 2]$ (end is $2$)
    - Pair 1: $[2, 3]$ (end is $3$)
    - Pair 2: $[3, 4]$ (end is $4$)
    - Sorted list: $[[1, 2], \; [2, 3], \; [3, 4]]$.
  - Initialize chain state:
    $$
    ans = 0, \quad pre = -\infty
    $$
  - **Step 2: Inspect Pair 0 ($[1, 2]$):**
    - $a = 1, \; b = 2$.
    - Check compatibility:
      $$
      pre < a \iff -\infty < 1 \implies \mathbf{True!}
      $$
    - Select Pair 0:
      $$
      ans \leftarrow 0 + 1 = \mathbf{1}
      $$
      $$
      pre \leftarrow b = \mathbf{2}
      $$
    - Chain currently contains: `[1, 2]`.
  - **Step 3: Inspect Pair 1 ($[2, 3]$):**
    - $a = 2, \; b = 3$.
    - Check compatibility:
      $$
      pre < a \iff 2 < 2 \implies \mathbf{False!}
      $$
    - Note: $2 == 2$ violates the strict inequality $b < c$ requirement!
    - Pair $[2, 3]$ overlaps with the finish boundary of $[1, 2]$.
    - Discard Pair 1. Chain remains at length $1$, $pre = 2$.
  - **Step 4: Inspect Pair 2 ($[3, 4]$):**
    - $a = 3, \; b = 4$.
    - Check compatibility:
      $$
      pre < a \iff 2 < 3 \implies \mathbf{True!}
      $$
    - Select Pair 2:
      $$
      ans \leftarrow 1 + 1 = \mathbf{2}
      $$
      $$
      pre \leftarrow b = \mathbf{4}
      $$
    - Chain now contains: `[1, 2] -> [3, 4]`.
  - **Step 5: Emit Result:**
    - All pairs processed.
    - Maximum chain length:
      $$
      ans = \mathbf{2}
      $$
- **Unsorted Full Chain Instance ($[[7, 8], [1, 2], [3, 4]]$):**
  - Sorted by right endpoint: `[[1, 2], [3, 4], [7, 8]]`.
  - Pair $[1, 2]$: $pre = 2, ans = 1$.
  - Pair $[3, 4]$: $2 < 3 \implies pre = 4, ans = 2$.
  - Pair $[7, 8]$: $4 < 7 \implies pre = 8, ans = 3$.
  - Result: `3`.
- **Negative Coordinates ($[[-10, -5], [-4, 0], [1, 6]]$):**
  - Sorted: ends at $-5, 0, 6$.
  - $-5 < -4 \implies$ Chains cleanly: length 3.

This instance demonstrates matroid greedy optimization on interval intersection graphs, mathematically proves why earliest finish time scheduling maximizes chain cardinality under strict order relations, and derives $O(N \log N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given pairs $[a, b]$:
A pair $[c, d]$ follows $[a, b]$ if and only if $b < c$.
Find the **maximum chain length**.

```text
Pairs: [1, 2], [2, 3], [3, 4]

Step 1: Pick [1, 2] -> pre = 2, length = 1
Step 2: Check [2, 3] -> 2 < 2 is FALSE (strict inequality!) -> Skip
Step 3: Check [3, 4] -> 2 < 3 is TRUE -> pre = 4, length = 2

Max Chain = [1, 2] -> [3, 4], Length = 2
```

### The Invariant of the Earliest Finish Time
- To maximize the number of non-overlapping intervals, you must always greedily take the interval that **ends first**.
- An interval ending earlier leaves strictly more time for remaining candidates than an interval ending later.

---

## 2. Conceptual Foundation & Invariants

### 1. The Greedy Sorting Protocol:
Sort pairs by the second coordinate:
$$
\text{pairs.sort}(key = \lambda x: x[1])
$$

### 2. The Acceptance Condition:
Initialize $pre = -\infty, ans = 0$.
For each $[a, b] \in pairs$:
$$
a > pre \implies ans \leftarrow ans + 1, \quad pre \leftarrow b
$$

> **Greedy Exchange Invariant.** If there exists an optimal schedule that deviates from the earliest finish time choice, replacing its first element with the earliest ending interval preserves mutual non-overlapping feasibility for all subsequent intervals.

---

## 3. Step-by-Step Worked Execution

We trace $pairs = [[1, 2], [2, 3], [3, 4]]$:

---

### Step 1: Sort by Right Endpoint
- Already sorted: `[1, 2], [2, 3], [3, 4]`.

---

### Step 2: Evaluate $[1, 2]$
- $pre = -\infty < 1 \implies$ Accept.
- $ans = 1, pre = 2$.

---

### Step 3: Evaluate $[2, 3]$
- $pre = 2 < 2$ is False $\implies$ Reject.

---

### Step 4: Evaluate $[3, 4]$
- $pre = 2 < 3 \implies$ Accept.
- $ans = 2, pre = 4$.

---

### Step 5: Output
$$
\mathbf{2}
$$

---

## 4. Complete Execution Trace

| Pair $[a, b]$ | Left Endpoint $a$ | Active $pre$ | Strict $pre < a$? | Decision | Running Length $ans$ | New $pre$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `[1, 2]` | $1$ | $-\infty$ | **Yes** | **Accept** | **$1$** | **$2$** |
| `[2, 3]` | $2$ | $2$ | No ($2 = 2$) | Discard | $1$ | $2$ |
| `[3, 4]` | $3$ | $2$ | **Yes** | **Accept** | **`2`** | **$4$** |
| **Final** | — | — | — | — | **`2`** | — |

---

## 5. Boundary Cases & Failure Modes

- **Single Pair ($N = 1$):** Always returns 1.
- **Identical Intervals ($[[1, 2], [1, 2]]$):** First accepted, second rejected $\implies 1$.
- **All Strictly Disjoint ($[[1, 2], [3, 4], [5, 6]]$):** All accepted $\implies N$.
- **Nested Intervals ($[[1, 10], [2, 3]]$):** Sorted: $[2, 3]$ comes before $[1, 10]$. Greedily selects $[2, 3]$, discarding the wasteful long interval $[1, 10]$.

---

## 6. Traps & Common Anti-Patterns

- **Sorting by Left Endpoint $a$ Instead of Right Endpoint $b$:** Sorting by $a$ fails when a long interval starts early and blocks multiple shorter intervals (e.g. $[1, 10]$ vs $[2, 3], [4, 5]$). Always sort by the **finish time** $b$.
- **Using Non-Strict Inequality ($pre \le a$):** The problem states $b < c$. If $pre = 2$ and $a = 2$, they cannot chain. You must use strict inequality $pre < a$.
- **$O(N^2)$ Dynamic Programming (LIS Style):** While $O(N^2)$ DP works, sorting + greedy runs in $O(N \log N)$ and is vastly simpler and faster.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting $N$ pairs by right endpoint: $\mathcal{O}(N \log N)$.
  - Single pass through pairs: $\mathcal{O}(N)$.
  - Total Time: $\mathcal{O}(N \log N)$. For $N = 1000$, completes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space (ignoring sorting stack).
