# Guided Example: Most Profit Assigning Work

We trace the step-by-step worker ability and job difficulty monotonic sorting, two-pointer sweep, cumulative prefix maximum profit tracking ($mx = \max(mx, profit_i)$), independent greedy worker assignment, and global profit summation on representative job markets:

- **Input:**
  $$
  difficulty = [2, 4, 6, 8, 10], \quad profit = [10, 20, 30, 40, 50]
  $$
  $$
  worker = [4, 5, 6, 7]
  $$
- **Required output:** `100`
  - Job assignment specifications:
    - We have $n$ jobs and $m$ workers.
    - Each job $i$ requires difficulty $difficulty[i]$ and yields profit $profit[i]$.
    - A worker with skill level $w$ can undertake any job with $difficulty \le w$.
    - Crucially: **multiple workers can choose the exact same job**, and each worker chooses their job independently to maximize their own individual profit!
    - Objective: Calculate the maximum total profit earned by all workers combined.
    - For the input market:
      - Worker with ability 4: can do jobs with difficulty $\le 4$ (diff 2 pays 10, diff 4 pays 20) $\implies \mathbf{20}$.
      - Worker with ability 5: can do jobs with difficulty $\le 5$ (diff 2 pays 10, diff 4 pays 20) $\implies \mathbf{20}$.
      - Worker with ability 6: can do jobs with difficulty $\le 6$ (diffs 2, 4, 6) $\implies \mathbf{30}$.
      - Worker with ability 7: can do jobs with difficulty $\le 7$ (diffs 2, 4, 6) $\implies \mathbf{30}$.
      - Total maximum profit:
        $$
        20 + 20 + 30 + 30 = \mathbf{100}
        $$
- **Dual Sorting & Running Prefix Maximum Invariant:**
  - **Greedy Decoupling Principle:**
    - Because jobs have infinite capacity (any number of workers can complete the same job), workers **do not compete with each other**.
    - For any worker with ability $w$, their optimal choice is simply the highest profit among all feasible jobs:
      $$
      \text{best}(w) = \max \{ profit[i] \mid difficulty[i] \le w \} \cup \{0\}
      $$
  - **Monotonic Two-Pointer Sweep:**
    1. Pair and sort jobs in ascending order of difficulty:
       $$
       jobs = \text{sort}\big(\text{zip}(difficulty, profit)\big)
       $$
    2. Sort workers in ascending order of ability:
       $$
       worker = \text{sort}(worker)
       $$
    3. Maintain pointer $i$ in $jobs$ and running maximum profit $mx = 0$:
       - As worker ability $w$ increases monotonically, advance $i$ to absorb all newly qualified jobs ($jobs[i].diff \le w$):
         $$
         mx \leftarrow \max(mx, \; jobs[i].profit)
         $$
       - The current value of $mx$ is immediately the optimal profit for worker $w$!
       - Accumulate: $ans \leftarrow ans + mx$.
    - Because both arrays are sorted, pointer $i$ never retreats, guaranteeing an $\mathcal{O}(N \log N + M \log M)$ execution time.
- **Step-by-Step Worked Execution Trace on the 4-Worker Market:**
  - Jobs sorted by difficulty:
    $$
    jobs = [(2, 10), \; (4, 20), \; (6, 30), \; (8, 40), \; (10, 50)]
    $$
  - Workers sorted:
    $$
    worker = [4, \; 5, \; 6, \; 7]
    $$
  - Initialize state: $i = 0, mx = 0, ans = 0$.
  - **Worker 0 (Ability $w = 4$):**
    - Advance job pointer while $jobs[i].diff \le 4$:
      - Job 0 $(2, 10)$: $2 \le 4 \implies mx = \max(0, 10) = 10, i \leftarrow 1$.
      - Job 1 $(4, 20)$: $4 \le 4 \implies mx = \max(10, 20) = \mathbf{20}, i \leftarrow 2$.
      - Job 2 $(6, 30)$: $6 > 4 \implies \mathbf{Stop.}$
    - Worker 0 earns: $mx = \mathbf{20}$.
    - Cumulative profit: $ans = 0 + 20 = \mathbf{20}$.
  - **Worker 1 (Ability $w = 5$):**
    - Advance job pointer while $jobs[i].diff \le 5$:
      - Job 2 $(6, 30)$: $6 > 5 \implies \mathbf{Stop.}$
      - (No new jobs available; $mx$ remains 20).
    - Worker 1 earns: $mx = \mathbf{20}$.
    - Cumulative profit: $ans = 20 + 20 = \mathbf{40}$.
  - **Worker 2 (Ability $w = 6$):**
    - Advance job pointer while $jobs[i].diff \le 6$:
      - Job 2 $(6, 30)$: $6 \le 6 \implies mx = \max(20, 30) = \mathbf{30}, i \leftarrow 3$.
      - Job 3 $(8, 40)$: $8 > 6 \implies \mathbf{Stop.}$
    - Worker 2 earns: $mx = \mathbf{30}$.
    - Cumulative profit: $ans = 40 + 30 = \mathbf{70}$.
  - **Worker 3 (Ability $w = 7$):**
    - Advance job pointer while $jobs[i].diff \le 7$:
      - Job 3 $(8, 40)$: $8 > 7 \implies \mathbf{Stop.}$
    - Worker 3 earns: $mx = \mathbf{30}$.
    - Cumulative profit: $ans = 70 + 30 = \mathbf{100}$.
  - **All Workers Assigned:**
    $$
    ans = \mathbf{100}
    $$
- **Underqualified Workers Trace ($difficulty = [85, 47, 57], worker = [24, 66, 99]$):**
  - Worker 24: $24 < 47 \implies$ cannot do any job $\implies$ earns $0$.
  - Worker 66: can do jobs up to 57 $\implies$ takes maximum profit among 47 and 57.
  - Handled seamlessly with initial $mx = 0$.
- **Higher Difficulty Pays Less (Non-Monotonic Profits):**
  - E.g. Job A $(diff = 2, profit = 50)$, Job B $(diff = 5, profit = 10)$.
  - $mx$ tracks $\max(50, 10) = 50$, ensuring a worker with skill 5 still takes the easier, higher-paying job!

This instance demonstrates monotone capacity allocation and online prefix maximum tracking on partially ordered reward sets, mathematically proves why sorting eliminates bipartite matching augmentations on infinite capacity graphs, and derives $O(N \log N + M \log M)$ execution time and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given jobs with $(difficulty, profit)$ and workers with skills:
Each worker can pick **any** job with $difficulty \le ability$.
Jobs can be picked multiple times.
Find the **maximum total profit**.

```text
Jobs: (2, 10), (4, 20), (6, 30), (8, 40), (10, 50)
Workers: [ 4, 5, 6, 7 ]

Worker 4: can do jobs <= 4 -> picks (4, 20) -> profit 20
Worker 5: can do jobs <= 5 -> picks (4, 20) -> profit 20
Worker 6: can do jobs <= 6 -> picks (6, 30) -> profit 30
Worker 7: can do jobs <= 7 -> picks (6, 30) -> profit 30

Total profit = 20 + 20 + 30 + 30 = 100
Result: 100
```

### The Invariant of the Prefix Maximum
- Because jobs can be repeated without limit, each worker greedily takes the job with the highest profit among all jobs they can do.
- Sorting both jobs and workers allows maintaining a running maximum profit $mx$ in a single forward pass.

---

## 2. Conceptual Foundation & Invariants

### 1. Optimal Worker Policy:
$$
\text{profit}^*(w) = \max \{ profit_i \mid difficulty_i \le w \} \cup \{0\}
$$

### 2. Monotone Sweep Algorithm:
$$
mx(w) = \max_{j \le i(w)} jobs[j].profit, \quad \text{where } i(w) = \max \{ k \mid jobs[k].diff \le w \}
$$
$$
ans = \sum_{w \in worker} mx(w)
$$

> **Independent Agent Invariant.** The allocation problem on complete multi-agent graphs with uncapacitated resources factors into independent 1D supremum queries. Sorting worker abilities aligns queries monotonically with the cumulative upper envelope of the step function $P(x) = \sup_{d \le x} \text{profit}(d)$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Sort Jobs and Workers
- $jobs = [(2, 10), (4, 20), (6, 30), (8, 40), (10, 50)]$.
- $worker = [4, 5, 6, 7]$.

---

### Step 2: Worker 4
- Absorb $(2, 10)$ and $(4, 20) \implies mx = 20$.
- Add $20 \implies ans = 20$.

---

### Step 3: Worker 5
- No new jobs $\le 5 \implies mx = 20$.
- Add $20 \implies ans = 40$.

---

### Step 4: Worker 6
- Absorb $(6, 30) \implies mx = 30$.
- Add $30 \implies ans = 70$.

---

### Step 5: Worker 7
- No new jobs $\le 7 \implies mx = 30$.
- Add $30 \implies ans = \mathbf{100}$.

---

## 4. Complete Execution Trace

| Worker Ability $w$ | Eligible Jobs Absorbed | Running Max Profit $mx$ | Worker Profit Added | Running Total $ans$ |
|:---:|:---:|:---:|:---:|:---:|
| $4$ | $(2, 10), (4, 20)$ | $20$ | $20$ | $20$ |
| $5$ | None | $20$ | $20$ | $40$ |
| $6$ | $(6, 30)$ | $30$ | $30$ | $70$ |
| **$7$** | **None** | **$30$** | **$30$** | **`100`** |

---

## 5. Boundary Cases & Failure Modes

- **All Workers Underqualified:** No worker meets the easiest job difficulty $\implies ans = 0$.
- **All Workers Overqualified:** Every worker takes the single highest-paying job in the market $\implies m \times \max(profit)$.
- **Harder Jobs Pay Less:** Handled automatically by $mx = \max(mx, profit)$; the running maximum never decreases.
- **Single Job, Many Workers:** All capable workers take that single job.

---

## 6. Traps & Common Anti-Patterns

- **Searching All Jobs for Each Worker ($O(N \cdot M)$):** For $N, M = 10,000$, an unsorted search takes $10^8$ operations. Sorting reduces this to $O(N \log N + M \log M)$.
- **Assuming Harder Jobs Always Pay More:** Never assume profit is monotonic with difficulty; always update $mx = \max(mx, profit)$ rather than picking the job with the highest difficulty.
- **Thinking Jobs Have Limited Capacity:** Jobs can be taken by any number of workers; no matching bipartite network flow is required.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting jobs: $\mathcal{O}(N \log N)$ where $N \le 10,000$.
  - Sorting workers: $\mathcal{O}(M \log M)$ where $M \le 10,000$.
  - Two-pointer scan: each job and worker visited once $\implies \mathcal{O}(N + M)$.
  - Total Time: strictly $\mathcal{O}(N \log N + M \log M)$. Completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory to store the zipped sorted jobs array.
