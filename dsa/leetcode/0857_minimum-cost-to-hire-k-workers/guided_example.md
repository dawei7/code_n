# Guided Example: Minimum Cost to Hire K Workers

We trace the step-by-step wage-to-quality ratio sorting, bottleneck wage determination, greedy max-heap quality tracking, and total wage minimization on representative workforce pools:

- **Input:**
  $$
  quality = [10, 20, 5], \quad wage = [70, 50, 30], \quad k = 2
  $$
- **Required output:** `105.0`
  - Hiring and payment rules:
    - We must hire exactly $k = 2$ workers from the pool of $N = 3$ workers.
    - Every hired worker $i$ must be paid at least their minimum requested wage: $\text{pay}_i \ge wage_i$.
    - Within the hired group, payments must be strictly proportional to quality:
      $$
      \frac{\text{pay}_i}{quality_i} = R \quad \text{for all hired } i
      $$
    - Combining both conditions:
      $$
      R \cdot quality_i \ge wage_i \iff R \ge \frac{wage_i}{quality_i}
      $$
    - Therefore, the unit-quality rate $R$ must be at least the wage-to-quality ratio of every worker in the group:
      $$
      R = \max_{i \in \text{hired}} \frac{wage_i}{quality_i}
      $$
    - The total hiring cost for a group $S$ of $k$ workers is:
      $$
      \text{Total Cost} = \sum_{i \in S} \text{pay}_i = R \times \sum_{i \in S} quality_i
      $$
- **Dual Optimization Decomposition Invariant:**
  - **Fixing the Bottleneck Ratio:**
    - If we fix the bottleneck worker to be worker $j$ (meaning $R = wage_j / quality_j$), then all other $k - 1$ workers in the group must have $wage_i / quality_i \le R$.
    - To minimize the total cost $R \times \sum_{i \in S} quality_i$ under a fixed $R$, we must choose the $k - 1$ workers with the **smallest possible qualities** among those with ratio $\le R$.
  - **Ascending Ratio Scan with a Max-Heap:**
    - Sort all workers by ratio $r_i = wage_i / quality_i$ ascending.
    - As we iterate through each worker $j$, their ratio $r_j$ is the largest ratio seen so far.
    - Maintain a max-heap of qualities for the active candidates.
    - When the heap reaches size $k$, evaluate the candidate cost $r_j \times \text{sum}(qualities)$, and then pop the worker with the largest quality so the pool remains as light as possible for subsequent larger ratios!

---

## 1. Instance & Teaching Goal

Given $quality = [10, 20, 5]$, $wage = [70, 50, 30]$, and $k = 2$:
Find $2$ workers that minimize total payment while meeting wage expectations and proportionality.

```text
Worker 0: q = 10, w = 70 -> ratio = 70/10 = 7.0
Worker 1: q = 20, w = 50 -> ratio = 50/20 = 2.5
Worker 2: q = 5,  w = 30 -> ratio = 30/5  = 6.0

Sorted by ratio:
1. Worker 1 (ratio = 2.5, q = 20)
2. Worker 2 (ratio = 6.0, q = 5)  -> pool [20, 5], sum q = 25 -> cost = 6.0 * 25 = 150.0
3. Worker 0 (ratio = 7.0, q = 10) -> pool [5, 10], sum q = 15 -> cost = 7.0 * 15 = 105.0

Minimum Cost = 105.0
```

The goal is to demonstrate why sorting by wage-to-quality ratio decouples the two variables ($R$ and $\sum q$) and allows an $\mathcal{O}(N \log N)$ greedy heap algorithm.

---

## 2. Conceptual Foundation & Invariants

### 1. Wage-to-Quality Ratio:
For worker $i$:
$$
r_i = \frac{wage_i}{quality_i}
$$

### 2. Ordered Sequence:
Workers sorted such that:
$$
r_{(1)} \le r_{(2)} \le \dots \le r_{(N)}
$$
When considering worker $(j)$ as the group ratio setter ($R = r_{(j)}$), all available candidates are chosen from $\{(1), (2), \dots, (j)\}$.

### 3. Quality Sum Minimization:
Among indices $\{1, \dots, j\}$, we select worker $j$ plus $k - 1$ others that minimize $\sum q$.
A max-heap of size $k$ retains the $k$ smallest qualities encountered so far. When size exceeds $k$, discarding the maximum quality guarantees optimal prefix selection.

---

## 3. Step-by-Step Worked Execution

### Setup:
Sort workers by ratio $w / q$:
- Worker 1: $r = 50 / 20 = 2.5, \quad q = 20$
- Worker 2: $r = 30 / 5 = 6.0, \quad q = 5$
- Worker 0: $r = 70 / 10 = 7.0, \quad q = 10$

Initialize:
- $ans = \infty$
- $tot = 0$ (sum of active qualities)
- Max-heap $H = [\,]$

---

### Step 1: Process Worker 1 ($r = 2.5, q = 20$)
- Add quality to sum: $tot \leftarrow 0 + 20 = 20$.
- Push $20$ onto max-heap: $H = [20]$.
- Check size: $|H| = 1 < k = 2$.
- More workers required before forming a valid team.

---

### Step 2: Process Worker 2 ($r = 6.0, q = 5$)
- Add quality to sum: $tot \leftarrow 20 + 5 = 25$.
- Push $5$ onto max-heap: $H = [20, 5]$.
- Check size: $|H| = 2 == k$.
- **Evaluate candidate cost:**
  $$
  \text{Cost} = r_2 \times tot = 6.0 \times 25 = \mathbf{150.0}
  $$
- Update best answer:
  $$
  ans = \min(\infty, 150.0) = \mathbf{150.0}
  $$
- **Pruning for next iterations:**
  - To prepare for larger ratios, discard the worker with the largest quality:
  - Pop $\max(H) = 20$.
  - Adjust total quality: $tot \leftarrow 25 - 20 = 5$.
  - Heap retains: $H = [5]$.

---

### Step 3: Process Worker 0 ($r = 7.0, q = 10$)
- Add quality to sum: $tot \leftarrow 5 + 10 = 15$.
- Push $10$ onto max-heap: $H = [10, 5]$.
- Check size: $|H| = 2 == k$.
- **Evaluate candidate cost:**
  $$
  \text{Cost} = r_0 \times tot = 7.0 \times 15 = \mathbf{105.0}
  $$
- Update best answer:
  $$
  ans = \min(150.0, 105.0) = \mathbf{105.0}
  $$
- Pop $\max(H) = 10$.
- Adjust total quality: $tot \leftarrow 15 - 10 = 5$.
- Heap retains: $H = [5]$.

---

### Termination:
All workers evaluated.
$$
\text{Minimum Cost} = \mathbf{105.0}
$$

---

## 4. Complete Execution Trace

| Step | Worker $(q, w)$ | Ratio $r = w/q$ | Running $tot$ | Max-Heap State $H$ | Team Size $|H|$ | Group Cost $r \times tot$ | Running Minimum $ans$ | Action After Evaluation |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| $1$ | $(20, 50)$ | $2.5$ | $20$ | $[20]$ | $1$ | — | $\infty$ | Await more workers |
| $2$ | $(5, 30)$ | $6.0$ | $25$ | $[20, 5]$ | $2$ | $6.0 \times 25 = 150.0$ | $150.0$ | Pop max $20$, $tot \to 5$ |
| $3$ | $(10, 70)$ | $7.0$ | $15$ | $[10, 5]$ | $2$ | $7.0 \times 15 = \mathbf{105.0}$ | **`105.0`** | Pop max $10$, $tot \to 5$ |

---

## 5. Boundary Cases & Failure Modes

- **$k = 1$:** The team consists of a single worker. The cost is simply $\min(wage_i)$. The formula $r_i \times q_i = (w_i / q_i) \times q_i = w_i$ holds identically.
- **$k = N$:** All workers must be hired. The ratio is forced to be $\max(r_i)$ and total cost is $\max(r_i) \times \sum q_i$.
- **Identical Ratios:** Workers with identical ratios can be ordered arbitrarily; sorting order does not affect the optimal heap selection.

---

## 6. Traps & Common Anti-Patterns

- **Greedily Picking Smallest Wages:** Sorting by wage directly ignores quality efficiency. A worker with wage $50$ and quality $20$ is much cheaper per unit of quality than a worker with wage $30$ and quality $5$.
- **Greedily Picking Smallest Qualities:** Sorting purely by quality ignores wage expectations, which can force an excessively high bottleneck ratio $R$.
- **Omitting Max-Heap Eviction:** Failing to pop the largest quality worker leaves inferior large-quality workers in the pool, inflating subsequent costs for larger ratios.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting $N$ workers by ratio: $\mathcal{O}(N \log N)$.
  - Iterating through $N$ workers with heap operations of size $k$: $\mathcal{O}(N \log k)$.
  - Total Time: $\mathcal{O}(N \log N)$, easily handling $N \le 10^4$ in $< 20$ ms.
- **Auxiliary Space Complexity:**
  - Array of sorted worker pairs: $\mathcal{O}(N)$.
  - Priority queue storing at most $k$ elements: $\mathcal{O}(k)$.
  - Total Space: $\mathcal{O}(N)$.
