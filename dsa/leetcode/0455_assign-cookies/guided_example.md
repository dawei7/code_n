# Guided Example: Assign Cookies

We trace the step-by-step greedy sorting of greed factors ($g$) and cookie sizes ($s$), two-pointer monotonic matching ($s[j] \ge g[i]$), cookie conservation exchange argument, and maximum content children accumulation on representative supply-and-demand instances:

- **Input:**
  - Children greed factors: $g = [1, 2, 3]$
  - Cookie sizes: $s = [1, 1]$
- **Required output:** `1`
  - Step 1: Sort both arrays ascending:
    - Sorted children: $g = [1, 2, 3]$
    - Sorted cookies: $s = [1, 1]$
  - Step 2: Greedy two-pointer matching:
    - Pointers: Child $i = 0$, Cookie $j = 0$
    - **Child 0 (Greed $g[0] = 1$):**
      - Inspect cookie $j = 0$ ($s[0] = 1$).
      - Test: $s[0] \ge g[0] \iff 1 \ge 1$ (**Satisfied!**)
      - Assign cookie $0$ to child $0$.
      - Advance both: $i \leftarrow 1, \; j \leftarrow 1$.
    - **Child 1 (Greed $g[1] = 2$):**
      - Inspect cookie $j = 1$ ($s[1] = 1$).
      - Test: $s[1] \ge g[1] \iff 1 \ge 2$ (False! Cookie is too small).
      - Skip cookie $1$: $j \leftarrow 2$.
    - Cookies exhausted ($j = 2 == \text{len}(s)$).
    - Loop halts. Number of content children is $i = \mathbf{1}$.
- **Abundant Supply Instance:** $g = [1, 2], s = [1, 2, 3] \implies$ Child $1$ gets cookie $1$, Child $2$ gets cookie $2 \implies \mathbf{2}$
- **Empty Cookie Supply:** $s = [] \implies \mathbf{0}$

This instance demonstrates the greedy interval matching principle, mathematically proves why assigning the smallest viable cookie to the least greedy child preserves capacity for more demanding children, and derives $O(N \log N + M \log M)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given children greed factors $g = [1, 2, 3]$ and cookie sizes $s = [1, 1]$:
Each child $i$ wants at least greed $g[i]$.
Each cookie $j$ has size $s[j]$.
A child is content if $s[j] \ge g[i]$.
Each child can receive at most one cookie, and each cookie can be assigned to at most one child.
Find the **maximum number of content children**.

```text
Children Greed (Demand):   [ 1,  2,  3 ]
Cookie Sizes   (Supply):   [ 1,  1 ]

Matching:
  Child 0 (Greed 1)  <--- Cookie 0 (Size 1)   [Satisfied]
  Child 1 (Greed 2)  <--- Cookie 1 (Size 1)   [Too Small: 1 < 2]

Maximum Content Children: 1
```

### The Greedy Conservation Principle
- If a child can be satisfied by multiple cookies, which one should we give them?
- We should give them the **smallest cookie** that satisfies their greed!
- Using a larger cookie when a smaller one suffices wastes the surplus capacity of the larger cookie, which could potentially satisfy a greedier child later.
- Symmetrically, we should attempt to satisfy the **least greedy child first**: if even the least greedy child cannot be satisfied by a cookie of size $s[j]$, no greedier child could possibly be satisfied by it either.

---

## 2. Conceptual Foundation & Invariants

### 1. Ascending Sort Ordering:
Sort both arrays:
$$
g_0 \le g_1 \le \dots \le g_{n-1}
$$
$$
s_0 \le s_1 \le \dots \le s_{m-1}
$$

### 2. Two-Pointer Matching Logic:
Let $i$ be the index of the child to satisfy, and $j$ be the current smallest available cookie:
- If $j == m$: All cookies are consumed. Terminate; exactly $i$ children were satisfied.
- While $j < m$ and $s[j] < g[i]$:
  - Cookie $j$ is strictly too small for child $i$.
  - Because children are sorted ($g_k \ge g_i$ for all $k > i$), cookie $j$ cannot satisfy any subsequent child either.
  - Discard cookie $j$ by advancing $j \leftarrow j + 1$.
- If $s[j] \ge g[i]$:
  - Cookie $j$ satisfies child $i$. Assign it: $i \leftarrow i + 1, \; j \leftarrow j + 1$.

> **Greedy Invariant.** At every step, the cookie assigned to child $i$ is the smallest available cookie in the entire supply capable of satisfying $g[i]$.

---

## 3. Step-by-Step Worked Execution

We trace $g = [1, 2, 3]$ and $s = [1, 1]$:

---

### Step 1: Sort Both Arrays
- Sorted greed: $g = [1, 2, 3]$ ($n = 3$).
- Sorted cookies: $s = [1, 1]$ ($m = 2$).
- Initialize pointers: $i = 0, \; j = 0$.

---

### Step 2: Evaluate Child 0 ($g[0] = 1$)
- Inspect cookie $j = 0$: $s[0] = 1$.
- Check satisfaction condition:
  $$
  s[0] \ge g[0] \iff 1 \ge 1 \quad (\text{True})
  $$
- Child 0 is content!
- Advance both child and cookie pointers:
  $$
  i \leftarrow 0 + 1 = \mathbf{1}, \quad j \leftarrow 0 + 1 = \mathbf{1}
  $$

---

### Step 3: Evaluate Child 1 ($g[1] = 2$)
- Inspect cookie $j = 1$: $s[1] = 1$.
- Check condition:
  $$
  s[1] \ge g[1] \iff 1 \ge 2 \quad (\text{False})
  $$
- Cookie 1 cannot satisfy child 1 (and cannot satisfy child 2).
- Discard cookie 1:
  $$
  j \leftarrow 1 + 1 = \mathbf{2}
  $$

---

### Step 4: Cookie Exhaustion
- Cookie pointer $j = 2 == m$.
- No more cookies remain.
- Loop terminates.
- Final satisfied children: $i = \mathbf{1}$.

---

## 4. Complete Execution Trace

| Child Pointer $i$ | Target Greed $g[i]$ | Cookie Pointer $j$ | Available Size $s[j]$ | Comparison $s[j] \ge g[i]$ | Action Taken | Next $(i, j)$ | Content Count |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|:---:|
| **$0$** | $1$ | $0$ | $1$ | $1 \ge 1$ (**True**) | **Assign cookie** | $(1, 1)$ | $1$ |
| **$1$** | $2$ | $1$ | $1$ | $1 \ge 2$ (False) | Discard small cookie | $(1, 2)$ | $1$ |
| **$1$** | $2$ | $2$ | EOF | — | **Exhausted** | Halt | **Result: $1$** |

---

## 5. Boundary Cases & Failure Modes

- **No Cookies ($s = []$):** Loop terminates immediately at $j = 0 == m \implies 0$.
- **All Cookies Smaller Than Minimum Greed ($g = [5, 6], s = [1, 2, 3]$):** Cookie pointer $j$ increments through all 3 cookies without matching $\implies 0$.
- **More Cookies Than Children ($g = [1, 2], s = [1, 2, 3, 4]$):** All children are satisfied. Pointer $i$ reaches $n = 2 \implies 2$.
- **Equal Sizes Throughout ($g = [2, 2, 2], s = [2, 2]$):** Matches first 2 children $\implies 2$.

---

## 6. Traps & Common Anti-Patterns

- **Trying to Satisfy the Greediest Child First:** Giving a large cookie of size 10 to a child needing 10 might leave a child needing 2 starved if only a cookie of size 1 is left. Sorting ascending and matching from smallest to largest guarantees optimal utilization.
- **Nested Loop Cookie Searching ($O(N \cdot M)$):** Scanning the cookie array from the beginning for every child causes quadratic runtime. Because both arrays are sorted, the cookie pointer $j$ moves strictly forward, achieving $O(N + M)$ traversal.
- **Forgetting to Advance Cookie Pointer on Discard:** If a cookie is too small, failing to increment $j$ creates an infinite loop.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting $g$ of size $N$ takes $O(N \log N)$ time.
  - Sorting $s$ of size $M$ takes $O(M \log M)$ time.
  - The two-pointer scan traverses each element in $g$ and $s$ at most once: $O(N + M)$.
  - Total Time: $\mathcal{O}(N \log N + M \log M)$. For $N, M \le 3 \times 10^4$, finishes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ beyond sorting memory.
