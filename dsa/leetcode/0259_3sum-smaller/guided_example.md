# Guided Example: 3Sum Smaller

We trace the step-by-step array sorting, dual-pointer inward convergence, and block cardinality addition ($R - L$) on representative integer triplet instances:

- **Input:** $\text{nums} = [-2, 0, 1, 3], \quad \text{target} = 2$
- **Required output:** $2$ (The qualifying triplets are $(-2, 0, 1)$ with sum $-1$, and $(-2, 0, 3)$ with sum $1$)
- **Empty / Small Array:** $\text{nums} = [], \quad \text{target} = 0 \implies 0$ (Requires at least 3 elements)
- **Target Equality Boundary:** $\text{nums} = [-2, 0, 1, 3]$ has triplet $(-2, 1, 3)$ with sum $2$; rejected because $2 \not< 2$
- **Duplicate Elements Instance:** $\text{nums} = [-1, -1, -1, 1], \quad \text{target} = -1 \implies 1$ (Index triplet $(0, 1, 2)$ with sum $-3 < -1$)

This instance demonstrates two-pointer search space optimization on sorted arrays, proves why finding one valid pair $(L, R)$ guarantees that all $R - L$ interior candidates are valid without individual inspection, reduces a cubic $O(N^3)$ search to $O(N^2)$ quadratic time, and uses $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums} = [-2, 0, 1, 3]$ and $\text{target} = 2$:
Count the number of index triplets $(i, j, k)$ with $i < j < k$ satisfying:
$$
\text{nums}[i] + \text{nums}[j] + \text{nums}[k] < \text{target}
$$

Examining all possible index triplets:
1. $(-2, 0, 1) \implies \text{sum} = -1 < 2$ (**Valid!**)
2. $(-2, 0, 3) \implies \text{sum} = 1 < 2$ (**Valid!**)
3. $(-2, 1, 3) \implies \text{sum} = 2 < 2$ (False: $2 == 2$, not strictly smaller)
4. $(0, 1, 3) \implies \text{sum} = 4 < 2$ (False)
Total qualifying triplets: $\mathbf{2}$.

- A naive triple loop evaluates $\binom{N}{3} = O(N^3)$ combinations, which causes Time Limit Exceeded for $N = 3,500$ ($N^3 \approx 4.2 \times 10^{10}$ operations).
- Sorting the array in $O(N \log N)$ time allows a **two-pointer sweep** for each fixed index $i$.
- Whenever $\text{nums}[i] + \text{nums}[L] + \text{nums}[R] < \text{target}$, sorted monotonicity proves that all intermediate elements between $L$ and $R$ also form valid triplets, adding **$R - L$ triplets in $O(1)$ time**. Total runtime becomes $O(N^2)$.

---

## 2. Conceptual Foundation & Invariants

### The Sorted Two-Pointer Block Invariant
Let $\text{nums}$ be sorted in non-decreasing order:
$$
\text{nums}[0] \le \text{nums}[1] \le \dots \le \text{nums}[N-1]
$$
Fix the first index $i$. Set left pointer $L = i + 1$ and right pointer $R = N - 1$.
Calculate the sum $S = \text{nums}[i] + \text{nums}[L] + \text{nums}[R]$:

1. **Case $S < \text{target}$:**
   Because the array is sorted, every position $k$ between $L + 1$ and $R$ satisfies:
   $$
   \text{nums}[k] \le \text{nums}[R]
   $$
   Therefore:
   $$
   \text{nums}[i] + \text{nums}[L] + \text{nums}[k] \le \text{nums}[i] + \text{nums}[L] + \text{nums}[R] = S < \text{target}
   $$
   Every index $k \in \{L+1, L+2, \dots, R\}$ is guaranteed to form a valid triplet with $(i, L)$!
   There are exactly **$R - L$** such valid third indices.
   We add $R - L$ to the cumulative total and advance $L \leftarrow L + 1$ to explore larger middle elements.

2. **Case $S \ge \text{target}$:**
   The sum is too large (or equal). Since $L$ cannot move left, we must decrease the sum by moving the right boundary inward:
   $$
   R \leftarrow R - 1
   $$

> **Invariant.** At every step, any discarded candidate triplet either has already been counted in a block addition ($R - L$) or is provably $\ge \text{target}$.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{nums} = [-2, 0, 1, 3]$ with $\text{target} = 2$:
Sorted array: $\text{nums} = [-2, 0, 1, 3]$ ($N = 4$).
Initialize $\text{count} = 0$.

---

### Outer Iteration: $i = 0$ ($\text{nums}[0] = -2$)
Initialize pointers: $L = 1$ ($\text{nums}[1] = 0$), $\quad R = 3$ ($\text{nums}[3] = 3$).

- **Step 1 ($L = 1, R = 3$):**
  - Compute sum:
    $$
    S = \text{nums}[0] + \text{nums}[1] + \text{nums}[3] = -2 + 0 + 3 = \mathbf{1}
    $$
  - Compare with target: $1 < 2$ (**True**).
  - All $k \in [L+1 \dots R] = [2 \dots 3]$ are valid!
    Number of valid third elements: $R - L = 3 - 1 = \mathbf{2}$.
    (Corresponding to triplets $(-2, 0, 1)$ and $(-2, 0, 3)$).
  - Update: $\text{count} \leftarrow 0 + 2 = \mathbf{2}$.
  - Advance left pointer: $L \leftarrow 1 + 1 = 2$.

- **Step 2 ($L = 2, R = 3$):**
  - Compute sum:
    $$
    S = \text{nums}[0] + \text{nums}[2] + \text{nums}[3] = -2 + 1 + 3 = \mathbf{2}
    $$
  - Compare with target: $2 < 2$ (**False**; strict inequality required).
  - Sum is too large. Decrement right pointer:
    $$
    R \leftarrow 3 - 1 = 2
    $$

- **Step 3 Check:**
  - $L = 2, R = 2 \implies L < R$ is False. Inner loop terminates.

---

### Outer Iteration: $i = 1$ ($\text{nums}[1] = 0$)
Initialize pointers: $L = 2$ ($\text{nums}[2] = 1$), $\quad R = 3$ ($\text{nums}[3] = 3$).

- **Step 4 ($L = 2, R = 3$):**
  - Compute sum:
    $$
    S = \text{nums}[1] + \text{nums}[2] + \text{nums}[3] = 0 + 1 + 3 = \mathbf{4}
    $$
  - Compare with target: $4 < 2$ (**False**).
  - Sum too large. Decrement:
    $$
    R \leftarrow 3 - 1 = 2
    $$
  - $L = 2, R = 2 \implies L < R$ is False. Inner loop terminates.

---

### Outer Loop Termination
Outer loop terminates because $i$ reaches $N - 2$.
Total valid triplets: $\mathbf{2}$.

---

## 4. Complete Execution Trace

```text
nums = [-2, 0, 1, 3], target = 2

i = 0 (-2):
  L=1 (0), R=3 (3) -> sum = -2 + 0 + 3 = 1 < 2
    -> Add R - L = 3 - 1 = 2 -> count = 2
    -> L advances to 2
  L=2 (1), R=3 (3) -> sum = -2 + 1 + 3 = 2 >= 2
    -> R decrements to 2
  L == R -> Stop

i = 1 (0):
  L=2 (1), R=3 (3) -> sum = 0 + 1 + 3 = 4 >= 2
    -> R decrements to 2
  L == R -> Stop

Final Count: 2
```

| Fixed $i$ | $\text{nums}[i]$ | Left $L$ | Right $R$ | Triplet Evaluated | Triplet Sum $S$ | Condition $S < 2$? | Triplets Added ($R - L$) | Running Total |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **0** | -2 | 1 (0) | 3 (3) | $(-2, 0, 3)$ | 1 | **Yes ($1 < 2$)** | **$3 - 1 = 2$** | **2** |
| 0 | -2 | 2 (1) | 3 (3) | $(-2, 1, 3)$ | 2 | No ($2 \ge 2$) | 0 ($R \leftarrow 2$) | 2 |
| 1 | 0 | 2 (1) | 3 (3) | $(0, 1, 3)$ | 4 | No ($4 \ge 2$) | 0 ($R \leftarrow 2$) | 2 |
| **End** | - | - | - | - | - | - | - | **$\mathbf{2}$ (Final Answer)** |

---

## 5. Algorithmic Correctness

**Soundness.** For any fixed $i$ and $L$, if $\text{nums}[i] + \text{nums}[L] + \text{nums}[R] < \text{target}$, then for every $k \in [L+1, R]$, $\text{nums}[k] \le \text{nums}[R]$, which implies $\text{nums}[i] + \text{nums}[L] + \text{nums}[k] < \text{target}$. Every counted triplet is mathematically guaranteed to have sum strictly less than `target`.

**Completeness.** Sorting does not destroy triplet combinations because choice of indices is unordered. At each step where $S \ge \text{target}$, any triplet $(i, j, R)$ with $j \ge L$ would have sum $\ge S \ge \text{target}$. Thus, decrementing $R$ safely eliminates no valid triplet. Every valid triplet is accounted for.

---

## 6. Traps This Instance Exposes

- **Strict Inequality Trap ($<$ vs $\le$):** If the sum equals `target` (e.g. $-2 + 1 + 3 = 2 == 2$), it does **not** count. The comparison must strictly be $S < \text{target}$. An equality condition ($S \le \text{target}$) would falsely add invalid triplets.
- **Enumerating Elements Individually:** Looping through $k$ from $L+1$ to $R$ one-by-one degrades the algorithm back to $O(N^3)$. The formula `count += R - L` counts all valid third indices in $O(1)$ time.
- **Handling Multiplicities / Duplicates:** Unlike LeetCode 15 (3Sum), which requires unique value triplets, this problem counts **index triplets**. Duplicate values are distinct choices and must be included; skipping duplicate elements is a bug here.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$, where $N$ is the number of elements in `nums`. Sorting takes $O(N \log N)$ time. The outer loop runs $N - 2$ times. In each outer iteration, the two pointers $L$ and $R$ advance toward each other at most $N$ times, executing in $O(N)$ time. Total time is $O(N \log N) + O(N^2) = O(N^2)$.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary memory (sorting in-place), using only three integer loop pointers.
