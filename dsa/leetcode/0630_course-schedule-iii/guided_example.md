# Guided Example: Course Schedule III

We trace the step-by-step deadline-driven course sequencing ($\text{sort by } lastDay$), cumulative timeline expansion ($s \leftarrow s + duration$), deadline violation detection ($s > lastDay$), greedy longest-duration course replacement via max-heap ($\text{heappop}(pq)$), time-slack maximization, and maximal course cardinality evaluation on representative training schedules:

- **Input:** $courses = [[100, 200], \; [200, 1300], \; [1000, 1250], \; [2000, 3200]]$
- **Required output:** `3`
  - Course contract:
    - Course $i$ requires $duration_i$ days of non-preemptive continuous study.
    - Course $i$ must finish **on or before** its deadline $lastDay_i$ ($finish\_time \le lastDay_i$).
    - Only one course can be studied at any time.
    - Start day is $t = 0$.
  - Objective: Maximize the **total number of courses** completed.
- **Earliest Deadline First & Greedy Replacement Invariant:**
  - **Sorting Order:**
    - To avoid premature commitment to tighter deadlines later in the timeline, process courses in ascending order of their deadlines:
      $$
      lastDay_1 \le lastDay_2 \le \dots \le lastDay_n
      $$
  - **The Regret / Replacement Principle:**
    - Suppose we add a course with $(duration, lastDay)$, causing total elapsed study time $s$ to exceed $lastDay$ ($s > lastDay$).
    - To restore feasibility, we must drop one of the courses currently accepted in our schedule.
    - Which course should we drop?
      - Every course currently in our schedule has a deadline $\le lastDay$.
      - Dropping **any single course** reduces our course count by 1.
      - But dropping the course with the **largest duration** frees the maximum amount of timeline slack $\Delta s$, making it easiest to fit future courses!
    - Using a **max-priority queue (max-heap)** allows us to identify and evict the longest duration in $\mathcal{O}(\log k)$ time.
- **Step-by-Step Worked Execution Trace:**
  - Input courses:
    - $C_A = [100, 200]$
    - $C_B = [200, 1300]$
    - $C_C = [1000, 1250]$
    - $C_D = [2000, 3200]$
  - **Step 1: Sort by Deadline ($lastDay$):**
    1. $C_1 = [100, 200]$ ($lastDay = 200$)
    2. $C_2 = [1000, 1250]$ ($lastDay = 1250$)
    3. $C_3 = [200, 1300]$ ($lastDay = 1300$)
    4. $C_4 = [2000, 3200]$ ($lastDay = 3200$)
  - Initialize schedule:
    $$
    s = 0, \quad pq = [] \quad (\text{Max-Heap of durations})
    $$
  - **Course 1 ($[100, 200]$):**
    - Add to timeline: $s \leftarrow 0 + 100 = \mathbf{100}$.
    - Push duration $100$ into heap: $pq = [100]$.
    - Check feasibility: $s = 100 \le 200 \implies \mathbf{Feasible!}$
  - **Course 2 ($[1000, 1250]$):**
    - Add to timeline: $s \leftarrow 100 + 1000 = \mathbf{1100}$.
    - Push duration $1000$ into heap: $pq = [1000, 100]$.
    - Check feasibility: $s = 1100 \le 1250 \implies \mathbf{Feasible!}$
  - **Course 3 ($[200, 1300]$):**
    - Add to timeline: $s \leftarrow 1100 + 200 = \mathbf{1300}$.
    - Push duration $200$ into heap: $pq = [1000, 200, 100]$.
    - Check feasibility: $s = 1300 \le 1300 \implies \mathbf{Feasible!}$
  - **Course 4 ($[2000, 3200]$):**
    - Add to timeline: $s \leftarrow 1300 + 2000 = \mathbf{3300}$.
    - Push duration $2000$ into heap: $pq = [2000, 1000, 200, 100]$.
    - Check feasibility:
      $$
      s = 3300 > 3200 \implies \mathbf{Overdue!}
      $$
    - Total time exceeds deadline by $100$ days.
    - We must drop the longest course in the heap:
      - Max duration in heap is $\mathbf{2000}$ (Course 4 itself!).
      - Evict $2000$ from heap:
        $$
        s \leftarrow 3300 - 2000 = \mathbf{1300}
        $$
      - Heap state: $pq = [1000, 200, 100]$.
  - **Step 5: Final Course Count:**
    - Active courses remaining in heap: $\{100, 200, 1000\}$.
    - Cardinality:
      $$
      |pq| = \mathbf{3}
      $$
- **Better Replacement Scenario ($C_{new}$ shorter than an earlier course):**
  - Suppose at $t = 1100$ (holding $100$ and $1000$), we encounter a course $[300, 1200]$.
  - $s \leftarrow 1100 + 300 = 1400 > 1200$.
  - Evict max duration $1000$:
    $$
    s \leftarrow 1400 - 1000 = \mathbf{400}
    $$
  - We retain 2 courses, but our timeline shrunk from $1100$ to $400$, saving $700$ days of slack for future courses!
- **Unfeasible Single Course ($duration > lastDay$):**
  - e.g. $[100, 50]$: Pushed to heap, exceeds deadline, immediately evicted $\implies 0$ courses added.

This instance demonstrates matroid greedy optimization and replacement scheduling under interval deadlines, mathematically proves why evicting maximum-duration elements preserves schedule feasibility while maximizing remaining capacity, and derives $O(N \log N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given courses with `[duration, lastDay]`:
Find the **maximum number of courses** you can take without missing any deadline.

```text
Courses:
  C1: [100, 200]
  C2: [1000, 1250]
  C3: [200, 1300]
  C4: [2000, 3200]

Timeline:
  t = 0  -> start C1 -> finishes t = 100  (<= 200, OK)
  t = 100 -> start C2 -> finishes t = 1100 (<= 1250, OK)
  t = 1100 -> start C3 -> finishes t = 1300 (<= 1300, OK)
  t = 1300 -> start C4 -> finishes t = 3300 (> 3200, Missed deadline!)

Drop longest course (2000):
  Schedule retains C1, C2, C3. Total = 3 courses
```

### The Invariant of the Regret Exchange
- If an existing schedule of $K$ courses is valid, adding a $(K+1)$-th course might exceed its deadline.
- By evicting the **single longest duration** course among the $K+1$ courses:
  1. The new schedule retains $K$ courses.
  2. The total time $s$ is strictly smaller than or equal to what it was before.
  3. Every retained course still finishes before its deadline because courses were processed in increasing order of deadline.

---

## 2. Conceptual Foundation & Invariants

### 1. Algorithm Structure:
1. Sort courses by deadline `lastDay` ascending.
2. Initialize cumulative time $s = 0$ and max-heap $pq$.
3. For each `(duration, lastDay)`:
   - $s \leftarrow s + duration$
   - Push $duration$ into $pq$.
   - If $s > lastDay$:
     - $s \leftarrow s - \text{heappop}(pq)$.
4. Return $|pq|$.

> **Exchange Monotonicity Invariant.** If a schedule of $k$ courses is feasible, replacing any course with one of smaller duration preserves feasibility with respect to all subsequent deadlines.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Sort by Deadline
- C1: `[100, 200]`
- C2: `[1000, 1250]`
- C3: `[200, 1300]`
- C4: `[2000, 3200]`

---

### Step 2: Iterate Through Courses
- C1 `[100, 200]`: $s = 100 \le 200$. $pq = [100]$.
- C2 `[1000, 1250]`: $s = 1100 \le 1250$. $pq = [1000, 100]$.
- C3 `[200, 1300]`: $s = 1300 \le 1300$. $pq = [1000, 200, 100]$.
- C4 `[2000, 3200]`: $s = 3300 > 3200 \implies$ Evict max (2000).
  - $s \leftarrow 3300 - 2000 = 1300$.
  - $pq = [1000, 200, 100]$.

---

### Step 3: Result
$$
|pq| = \mathbf{3}
$$

---

## 4. Complete Execution Trace

| Course $(dur, last)$ | Cumulative $s$ Before | Add Duration | Cumulative $s$ | $s \le last$? | Evicted From Heap | Final $s$ | Active Count |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `[100, 200]` | $0$ | $+100$ | $100$ | **Yes** | None | $100$ | $1$ |
| `[1000, 1250]`| $100$ | $+1000$ | $1100$ | **Yes** | None | $1100$ | $2$ |
| `[200, 1300]` | $1100$ | $+200$ | $1300$ | **Yes** | None | $1300$ | $3$ |
| `[2000, 3200]`| $1300$ | $+2000$ | $3300$ | No ($> 3200$) | **$2000$** | **$1300$** | **`3`** |
| **Result** | — | — | — | — | — | — | **`3`** |

---

## 5. Boundary Cases & Failure Modes

- **Course Impossible Alone ($duration > lastDay$):** Evicted immediately upon insertion $\implies$ net 0 effect.
- **All Courses Feasible:** Zero evictions $\implies$ returns $N$.
- **Identical Deadlines:** Sorted stably; shorter courses accepted, longer courses evicted when budget is exhausted.
- **Empty Course List:** Returns 0.

---

## 6. Traps & Common Anti-Patterns

- **Sorting by Duration First:** Sorting by duration misses tight early deadlines, causing early courses to be skipped. Always sort by **deadline** first.
- **Dropping the Current Course Instead of Max-in-Heap:** If current course has duration 200 and causes an overflow with a previous course of duration 1000, dropping 1000 and keeping 200 saves 800 days! Always evict the heap maximum.
- **Using Min-Heap Instead of Max-Heap:** Evicting the smallest duration saves the least amount of time, failing the greedy objective.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting courses by deadline: $\mathcal{O}(N \log N)$.
  - Iterating over $N$ courses with heap push/pop: $\mathcal{O}(N \log N)$.
  - Total Time: $\mathcal{O}(N \log N)$. For $N = 10^4$, completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to store the max-heap.
