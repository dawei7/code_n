# Guided Example: IPO

We trace the step-by-step two-heap greedy priority queue architecture (min-heap capital thresholding vs max-heap profit extraction), dynamic capital unlocking ($capital \le w$), greedy profit accumulation ($w \leftarrow w + profit$), project budget decrement ($k$), and early stagnation termination on representative investment portfolios:

- **Input:**
  - Projects allowed: $k = 2$
  - Initial capital: $w = 0$
  - Project profits: $profits = [1, 2, 3]$
  - Required capitals: $capital = [0, 1, 1]$
- **Required output:** `4`
  - Available projects:
    - Project 0: capital required $0$, profit $1$
    - Project 1: capital required $1$, profit $2$
    - Project 2: capital required $1$, profit $3$
  - Constraints: You can complete at most $k = 2$ distinct projects. To start a project, current capital must satisfy $w \ge capital[i]$. Completing it increases capital by $profits[i]$.
- **Two-heap greedy execution trace:**
  - Min-heap $h_1$ (sorted by required capital ascending):
    $$
    h_1 = [(0, 1), \; (1, 2), \; (1, 3)]
    $$
  - Max-heap $h_2$ (available affordable profits): $h_2 = []$
  - **Round 1 ($k = 2, \; w = 0$):**
    - Unlock all projects in $h_1$ with $capital \le w (0)$:
      - Pop $(0, 1)$ from $h_1$: capital $0 \le 0 \implies$ push profit $1$ into $h_2$.
      - Next in $h_1$ is $(1, 2)$: capital $1 > 0 \implies$ locked! Stop unlocking.
    - Max-heap $h_2$ contains: $\{1\}$.
    - Greedily pick the project with maximum profit from $h_2$:
      - Pop maximum profit: $\mathbf{1}$
      - Update capital:
        $$
        w \leftarrow 0 + 1 = \mathbf{1}
        $$
      - Decrement project budget: $k \leftarrow 2 - 1 = 1$.
  - **Round 2 ($k = 1, \; w = 1$):**
    - Unlock all newly affordable projects in $h_1$ with $capital \le w (1)$:
      - Pop $(1, 2)$ from $h_1$: capital $1 \le 1 \implies$ push profit $2$ into $h_2$.
      - Pop $(1, 3)$ from $h_1$: capital $1 \le 1 \implies$ push profit $3$ into $h_2$.
      - $h_1$ is now empty.
    - Max-heap $h_2$ contains: $\{2, 3\}$.
    - Greedily pick the maximum profit from $h_2$:
      - Pop maximum profit: $\mathbf{3}$ (Project 2)
      - Update capital:
        $$
        w \leftarrow 1 + 3 = \mathbf{4}
        $$
      - Decrement project budget: $k \leftarrow 1 - 1 = 0$.
  - Project quota $k = 0$ reached.
  - Final maximized capital: **`4`**.
- **Complete All Projects ($k = 3, w = 0$):**
  - Unlocks Project 1 in Round 3 $\implies w \leftarrow 4 + 2 = \mathbf{6}$
- **Insufficient Initial Capital ($w = 0, capital = [5, 10]$):**
  - No project satisfies $capital \le 0 \implies h_2$ remains empty $\implies$ halts early with $w = \mathbf{0}$.

This instance demonstrates greedy choice selection under dynamic affordability constraints, mathematically proves why always executing the highest-profit available project is optimal via an exchange argument, and derives $O(N \log N + K \log N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given initial capital $w$, an integer $k$ (maximum projects allowed), and arrays $profits$ and $capital$:
To start project $i$, you must have at least $capital[i]$ capital.
When you finish project $i$, you receive pure profit $profits[i]$, increasing your total capital to $w + profits[i]$.
Find the **maximum capital** achievable after finishing at most $k$ distinct projects.

```text
Projects:
  P0: Needs 0 capital -> Yields +1 profit
  P1: Needs 1 capital -> Yields +2 profit
  P2: Needs 1 capital -> Yields +3 profit

Step 1 (w = 0):
  Only P0 is affordable (needs 0). Complete P0 -> w becomes 0 + 1 = 1.

Step 2 (w = 1):
  Both P1 and P2 are now affordable (need 1).
  Greedy choice: Pick P2 (+3) over P1 (+2) -> w becomes 1 + 3 = 4.

Maximized Capital after 2 projects: 4
```

### The Greedy Choice Property
At any point with current capital $w$:
- Any project requiring capital $\le w$ is immediately eligible to be executed.
- Once executed, capital **strictly increases** ($w \leftarrow w + profit$). Capital never decreases because required capital is only a gating threshold, not a spent cost.
- Therefore, completing any project only **unlocks more projects**, never fewer!
- Among all currently unlocked projects, it is always optimal to choose the one that yields the **largest profit**. This gives the greatest capital boost for future selections.

---

## 2. Conceptual Foundation & Invariants

### 1. The Dual-Heap Architecture:
We split projects into two heaps:
1. **$h_1$ (Locked Queue):** Min-heap ordered by required capital $(c, p)$. Stores projects that may or may not be affordable.
2. **$h_2$ (Unlocked Pool):** Max-heap ordered by profit. Stores all projects whose required capital is $\le w$.

### 2. The Two-Stage Selection Loop:
For each of the $k$ selections:
1. **Unlock Phase:** While $h_1$ is non-empty and its top element has $capital \le w$:
   Pop $(c, p)$ from $h_1$ and push $-p$ into $h_2$.
2. **Execution Phase:**
   - If $h_2$ is empty: No affordable projects remain. Terminate early.
   - Pop the largest profit from $h_2$: $w \leftarrow w + \text{pop}(h_2)$.
   - Decrement $k \leftarrow k - 1$.

> **Monotonic Capital Invariant.** Capital $w$ is non-decreasing over time, guaranteeing that once a project is pushed into $h_2$, it remains permanently affordable until chosen.

---

## 3. Step-by-Step Worked Execution

We trace $k = 2, w = 0, profits = [1, 2, 3], capital = [0, 1, 1]$:

---

### Step 1: Initialize Min-Heap $h_1$
Heapify capital-profit pairs:
$$
h_1 = [(0, 1), \; (1, 2), \; (1, 3)]
$$
Initialize max-heap $h_2 = []$.

---

### Step 2: Project Choice 1 ($k = 2$)
- Current capital: $w = 0$.
- **Unlock from $h_1$:**
  - Look at top of $h_1$: $(0, 1)$.
  - $0 \le w (0) \implies$ Pop $(0, 1)$, push profit $1$ to $h_2$.
  - Look at new top of $h_1$: $(1, 2)$.
  - $1 > w (0) \implies$ Stop unlocking.
- Pool of affordable profits: $h_2 = [1]$.
- **Execute best project:**
  - Pop maximum profit: $1$.
  - Update capital:
    $$
    w \leftarrow 0 + 1 = \mathbf{1}
    $$
  - Budget remaining: $k = 1$.

---

### Step 3: Project Choice 2 ($k = 1$)
- Current capital: $w = 1$.
- **Unlock from $h_1$:**
  - Look at top of $h_1$: $(1, 2)$.
  - $1 \le w (1) \implies$ Pop $(1, 2)$, push profit $2$ to $h_2$.
  - Look at top of $h_1$: $(1, 3)$.
  - $1 \le w (1) \implies$ Pop $(1, 3)$, push profit $3$ to $h_2$.
  - $h_1$ is empty.
- Pool of affordable profits: $h_2$ has $\{2, 3\}$.
- **Execute best project:**
  - Pop maximum profit: $\mathbf{3}$.
  - Update capital:
    $$
    w \leftarrow 1 + 3 = \mathbf{4}
    $$
  - Budget remaining: $k = 0$.

---

### Step 4: Termination
Project quota exhausted ($k = 0$).
Output: **`4`**.

---

## 4. Complete Execution Trace

| Choice Round | Current Capital $w$ | Projects Unlocked from $h_1$ | Available Profits in $h_2$ | Max Profit Popped | Capital After Execution | Remaining $k$ |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|
| **Init** | $0$ | — | `[]` | — | $0$ | $2$ |
| **Round 1** | $0$ | $(0, 1)$ | `[1]` | **$1$** | $0 + 1 = \mathbf{1}$ | $1$ |
| **Round 2** | $1$ | $(1, 2), (1, 3)$ | `[2, 3]` | **$3$** | $1 + 3 = \mathbf{4}$ | $0$ |
| **Final** | $4$ | — | — | — | **Result: $4$** | $0$ |

---

## 5. Boundary Cases & Failure Modes

- **Zero Projects Allowed ($k = 0$):** Loop never runs $\implies$ returns initial $w$.
- **Stagnation / Bankruptcy:** If $w = 0$ and all projects require $capital \ge 1$, $h_2$ remains empty $\implies$ loop breaks early and returns initial $w$.
- **All Projects Affordable Initially:** All $N$ projects immediately dump into $h_2$, which simply pops the $k$ largest profits.
- **$k \ge N$ (Can Do All Projects):** Executes every affordable project until none remain.

---

## 6. Traps & Common Anti-Patterns

- **Scanning All Projects Repeatedly ($O(K \cdot N)$):** Iterating through all $N$ projects on each of the $k$ rounds takes $O(K \cdot N)$ time. For $N, K = 10^5$, this requires $10^{10}$ operations (Time Limit Exceeded). The two-heap approach processes each project in $O(\log N)$ amortized time.
- **Deducting Capital for Projects:** Required capital is a prerequisite threshold, **not a cost**. You do not subtract $capital[i]$ from $w$; you only add $profits[i]$ to $w$.
- **Sorting Entire Array by Profit First:** Sorting by profit is invalid because high-profit projects with huge capital requirements cannot be started until smaller projects build up the necessary capital.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Heapifying $h_1$ with $N$ elements takes $O(N)$ time.
  - Each of the $N$ projects is popped from $h_1$ and pushed to $h_2$ at most once: $O(N \log N)$.
  - In each of the $K$ rounds, popping the maximum profit takes $O(\log N)$ time: $O(K \log N)$.
  - Total Time: $\mathcal{O}(N \log N + K \log N)$. For $N, K = 10^5$, executes in $< 60$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to store projects in heaps $h_1$ and $h_2$.
