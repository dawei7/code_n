# Guided Example: Non-overlapping Intervals

We trace the step-by-step Interval Scheduling greedy reduction, end-time ascending sort ordering, compatibility frontier tracking ($start \ge pre$), greedy exchange argument, and minimum removal calculation on representative interval sets:

- **Input:** $intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]$
- **Required output:** `1`
  - Total intervals: $N = 4$
  - Step 1 (Sort ascending by end time $r$):
    - Interval A: $[1, 2]$ (end = $2$)
    - Interval B: $[1, 3]$ (end = $3$)
    - Interval C: $[2, 3]$ (end = $3$)
    - Interval D: $[3, 4]$ (end = $4$)
  - Step 2 (Greedy selection of compatible intervals):
    - Frontier initialization: $pre = -\infty, \; kept = 0$
    - Evaluate $[1, 2]$: $start = 1 \ge -\infty \implies$ **Retained**. Update $pre \leftarrow 2, kept \leftarrow 1$
    - Evaluate $[1, 3]$: $start = 1 < 2$ (Overlaps with $[1, 2]$) $\implies$ **Removed**. $kept$ stays $1$
    - Evaluate $[2, 3]$: $start = 2 \ge 2$ (Touches boundary, non-overlapping) $\implies$ **Retained**. Update $pre \leftarrow 3, kept \leftarrow 2$
    - Evaluate $[3, 4]$: $start = 3 \ge 3 \implies$ **Retained**. Update $pre \leftarrow 4, kept \leftarrow 3$
  - Step 3 (Duality subtraction):
    $$
    \text{Min Removals} = N - kept = 4 - 3 = \mathbf{1}
    $$
- **All Overlapping Identical Intervals:** $intervals = [[1, 2], [1, 2], [1, 2]] \implies kept = 1 \implies \text{Removals} = 3 - 1 = \mathbf{2}$
- **Already Non-Overlapping Set:** $intervals = [[1, 2], [2, 3]] \implies kept = 2 \implies \text{Removals} = 2 - 2 = \mathbf{0}$

This instance demonstrates the classical Interval Scheduling duality, proves by greedy exchange why sorting by earliest finish time strictly maximizes the number of mutually compatible intervals, and derives $O(N \log N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a collection of intervals $intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]$:
Find the **minimum number of intervals** you need to remove to make the rest of the intervals non-overlapping.
Intervals sharing only an endpoint (such as $[1, 2]$ and $[2, 3]$) are considered non-overlapping.

```text
Intervals along the Number Line:
  [1, 2]:  |---|
  [1, 3]:  |-------|          <- Conflict with [1, 2] and [2, 3]
  [2, 3]:      |---|
  [3, 4]:          |---|

Optimal Retention: [1, 2], [2, 3], [3, 4] (3 intervals kept)
Minimum Removals: 4 - 3 = 1 interval removed ([1, 3])
```

### The Complementary Duality Principle
Minimizing the number of removed intervals is mathematically equivalent to **maximizing the number of mutually non-overlapping intervals kept**:
$$
\min(\text{Removals}) = N - \max(\text{Mutually Compatible Intervals Kept})
$$
This reformulates the problem into the classic **Interval Scheduling Problem**, which is solved optimally by the earliest-deadline-first greedy strategy.

---

## 2. Conceptual Foundation & Invariants

### 1. Earliest Finish Time Greedy Policy:
To maximize the number of intervals we can accommodate:
- We always select the available compatible interval that **finishes earliest** (smallest end coordinate $r$).
- **Exchange Argument Proof:**
  Suppose an optimal solution $OPT$ chooses an interval $I_{first}$ that ends at $r_{opt}$.
  Our greedy strategy chooses $I_{greedy}$ that ends at $r_{greedy} \le r_{opt}$.
  Because $r_{greedy} \le r_{opt}$, replacing $I_{first}$ with $I_{greedy}$ cannot overlap with any subsequent interval in $OPT$ that began after $r_{opt}$.
  Thus, the greedy choice leaves at least as much remaining time as any alternative choice, guaranteeing global optimality.

### 2. Compatibility Test Invariant:
Let $pre$ be the end time of the most recently retained interval:
- An interval $[l, r]$ is compatible if and only if:
  $$
  l \ge pre
  $$
- If $l \ge pre$, we retain $[l, r]$ and advance $pre \leftarrow r$.
- If $l < pre$, $[l, r]$ conflicts with the current active set and must be eliminated.

> **Greedy Invariant.** At every step, the set of selected intervals represents the maximum possible count of mutually disjoint intervals that can fit within $[-\infty, pre]$.

---

## 3. Step-by-Step Worked Execution

We trace $intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]$ ($N = 4$):

---

### Step 1: Sort by End Time
Sort all intervals ascending by their end coordinate $r$:
$$
\text{Sorted List: } [[1, 2], [1, 3], [2, 3], [3, 4]]
$$
Initialize:
$$
pre = -\infty, \quad kept = 0
$$

---

### Step 2: Evaluate $[1, 2]$
- Start: $l = 1$, End: $r = 2$.
- Compatibility check:
  $$
  1 \ge -\infty \quad (\text{True})
  $$
- Action: Retain $[1, 2]$.
  $$
  kept \leftarrow 0 + 1 = 1, \quad pre \leftarrow 2
  $$

---

### Step 3: Evaluate $[1, 3]$
- Start: $l = 1$, End: $r = 3$.
- Compatibility check:
  $$
  1 \ge 2 \quad (\text{False! Overlap detected with previous interval})
  $$
- Action: Eliminate $[1, 3]$.
  $$
  kept \text{ stays } 1, \quad pre \text{ remains } 2
  $$

---

### Step 4: Evaluate $[2, 3]$
- Start: $l = 2$, End: $r = 3$.
- Compatibility check:
  $$
  2 \ge 2 \quad (\text{True! Endpoints touching is allowed})
  $$
- Action: Retain $[2, 3]$.
  $$
  kept \leftarrow 1 + 1 = 2, \quad pre \leftarrow 3
  $$

---

### Step 5: Evaluate $[3, 4]$
- Start: $l = 3$, End: $r = 4$.
- Compatibility check:
  $$
  3 \ge 3 \quad (\text{True})
  $$
- Action: Retain $[3, 4]$.
  $$
  kept \leftarrow 2 + 1 = 3, \quad pre \leftarrow 4
  $$

---

### Step 6: Compute Minimum Removals
Total intervals kept: $kept = 3$.
$$
\text{Removed Count} = N - kept = 4 - 3 = \mathbf{1}
$$

---

## 4. Complete Execution Trace

| Candidate Interval $[l, r]$ | Finish Time $r$ | Prior Finish $pre$ | Condition $l \ge pre$ | Decision | Retained Count | New $pre$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$[1, 2]$** | $2$ | $-\infty$ | $1 \ge -\infty$ (**True**) | **Retain** | $1$ | $2$ |
| **$[1, 3]$** | $3$ | $2$ | $1 \ge 2$ (False) | **Remove** | $1$ | $2$ |
| **$[2, 3]$** | $3$ | $2$ | $2 \ge 2$ (**True**) | **Retain** | $2$ | $3$ |
| **$[3, 4]$** | $4$ | $3$ | $3 \ge 3$ (**True**) | **Retain** | $3$ | $4$ |
| **Final** | — | — | — | **Result: $4 - 3 = \mathbf{1}$** | — | — |

---

## 5. Boundary Cases & Failure Modes

- **Single Interval ($intervals = [[1, 2]]$):** $N = 1, kept = 1 \implies 1 - 1 = \mathbf{0}$.
- **All Duplicates ($[[1, 2], [1, 2], [1, 2]]$):** First interval retained, subsequent two fail $1 \ge 2 \implies 3 - 1 = \mathbf{2}$ removed.
- **Touching Endpoints ($[[1, 2], [2, 3], [3, 4]]$):** Boundary condition $l \ge pre$ permits touching endpoints $\implies 0$ removed.
- **Negative Coordinates ($[[-10, -5], [-6, -2], [-4, 0]]$):** Standard end-time ordering correctly sequences negative values without modification.

---

## 6. Traps & Common Anti-Patterns

- **Sorting by Start Time Instead of End Time:** Sorting by start time causes greedy choices to pick long intervals that start early (e.g. $[0, 10]$ before $[1, 2]$ and $[2, 3]$), eliminating multiple viable future intervals. Sorting by *end time* is strictly required.
- **Strict Inequality on Touching Endpoints:** Using `l > pre` instead of `l >= pre` treats touching intervals like $[1, 2]$ and $[2, 3]$ as overlapping, discarding valid non-overlapping configurations.
- **Dynamic Array Removal ($O(N^2)$):** Physically mutating or deleting items from a list takes $O(N)$ per deletion. Simply keeping a running count of retained intervals completes in $O(1)$ auxiliary memory.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting $N$ intervals by end time takes $O(N \log N)$ time.
  - The linear greedy scan inspects each interval exactly once in $O(1)$ time.
  - Total Time: $\mathcal{O}(N \log N)$. For $N = 10^5$, sorting takes $\approx 1.7 \times 10^6$ operations, executing in under 20 ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ beyond the in-place sort storage (or $\mathcal{O}(N)$ depending on language sorting implementations).