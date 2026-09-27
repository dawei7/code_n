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

### Why the Block Count Is Exact

The single block addition at $i = 0$, $L = 1$, $R = 3$ claims two qualifying
triplets in one operation. Expanding that block element by element shows that
the shortcut is not an approximation: the sorted order makes each interior
third index valid for the same reason as the right endpoint.

| Fixed $i$ | Left $L$ (value) | Right $R$ (value) | Third indices in the block | Sum for each interior $k$ | Block size $R - L$ | Running total |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|
| 0 | 1 (0) | 3 (3) | $k = 2, 3$ | $k = 2$: $-2 + 0 + 1 = -1 < 2$; $k = 3$: $-2 + 0 + 3 = 1 < 2$ | 2 | 2 |
| 0 | 2 (1) | 3 (3) | none: $S \ge \text{target}$ | $k = 3$ alone gives $-2 + 1 + 3 = 2$, which is not $< 2$ | 0 | 2 |
| 1 | 2 (1) | 3 (3) | none: $S \ge \text{target}$ | $0 + 1 + 3 = 4$, far above the bound | 0 | 2 |

Row one is the whole method in miniature: the right endpoint passes the test, so
every index strictly between $L$ and $R$ passes it too, and the count $R - L$
enumerates the block without touching the interior elements. Row two shows the
other half of the search: once the smallest available third index (here $k = 3$,
which is $R$ itself) already meets the bound, no larger $k$ can help, so the
right pointer must retreat instead.

---

## 5. Algorithmic Correctness

**Soundness.** For any fixed $i$ and $L$, if $\text{nums}[i] + \text{nums}[L] + \text{nums}[R] < \text{target}$, then for every $k \in [L+1, R]$, $\text{nums}[k] \le \text{nums}[R]$, which implies $\text{nums}[i] + \text{nums}[L] + \text{nums}[k] < \text{target}$. Every counted triplet is mathematically guaranteed to have sum strictly less than `target`.

**Completeness.** Sorting does not destroy triplet combinations because choice of indices is unordered. At each step where $S \ge \text{target}$, any triplet $(i, j, R)$ with $j \ge L$ would have sum $\ge S \ge \text{target}$. Thus, decrementing $R$ safely eliminates no valid triplet. Every valid triplet is accounted for.

---

## 6. Traps This Instance Exposes

- **Strict Inequality Trap ($<$ vs $\le$):** If the sum equals `target` (e.g. $-2 + 1 + 3 = 2 == 2$), it does **not** count. The comparison must strictly be $S < \text{target}$. An equality condition ($S \le \text{target}$) would falsely add invalid triplets.
- **Enumerating Elements Individually:** Looping through $k$ from $L+1$ to $R$ one-by-one degrades the algorithm back to $O(N^3)$. The formula `count += R - L` counts all valid third indices in $O(1)$ time.
- **Handling Multiplicities / Duplicates:** Unlike LeetCode 15 (3Sum), which requires unique value triplets, this problem counts **index triplets**. Duplicate values are distinct choices and must be included; skipping duplicate elements is a bug here.

### Multiplicity Check on an All-Equal Instance

A second instance makes the index-versus-value distinction measurable. Take
$\text{nums} = [0, 0, 0, 0, 0]$ with $\text{target} = 1$, where every index
triple sums to $0$ and therefore every one of the $\binom{5}{3} = 10$ triples
qualifies. Counting by value would report a single triplet; counting by index
must report ten, and the block additions have to sum to exactly that.

| Fixed $i$ | Pointer walk inside this $i$ | Additions from blocks | Subtotal for this $i$ | Running total |
|:---:|:---|:---:|:---:|:---:|
| 0 | $(L = 1, R = 4) \to +3$; $(L = 2, R = 4) \to +2$; $(L = 3, R = 4) \to +1$ | $3 + 2 + 1$ | 6 | 6 |
| 1 | $(L = 2, R = 4) \to +2$; $(L = 3, R = 4) \to +1$ | $2 + 1$ | 3 | 9 |
| 2 | $(L = 3, R = 4) \to +1$ | $1$ | 1 | **10** |

The outer loop stops at $i = 2$ because a first index needs two larger indices
after it, and the three subtotals $6 + 3 + 1$ reproduce
$\binom{5}{3} = \frac{5 \cdot 4 \cdot 3}{3 \cdot 2 \cdot 1} = 10$. Each block
addition is triggered by the left pointer advancing, so the walk never revisits
a pair $(i, L)$ and never counts an index triple twice.

### Boundary Map of Strictness and Length

Every row below is an authored case for this problem. The fourth column records
what the same two-pointer sweep would return if the comparison were relaxed to
$S \le \text{target}$, which is the cheapest way to break the solution.

| Instance | Edge condition | Correct count | Count under a relaxed $S \le \text{target}$ | What makes the strict count correct |
|:---|:---|:---:|:---:|:---|
| `[]`, target 0 | No elements | 0 | 0 | The outer loop spans $n - 2$ values, so an empty array never enters the sweep |
| `[-100, 100]`, target 0 | Fewer than three indices | 0 | 0 | Three distinct indices are impossible, and no block can be added before $L < R$ fails |
| `[-1, 1, 2, 2]`, target 3 | Equality at the bound plus a repeated value | 2 | 3 | The value triple $(-1, 2, 2)$ sums to exactly 3 and is excluded; the two index triples valued $(-1, 1, 2)$ are both kept |
| `[-100, -100, -100, 100]`, target -100 | Minimum target boundary | 1 | 4 | Choosing the $100$ makes the sum exactly $-100$; only the all-$(-100)$ triple is strictly smaller |
| `[-100, 0, 100, 100]`, target 100 | Maximum value against a mid target | 2 | 3 | The triple $(-100, 100, 100)$ sits exactly on 100, and only the two triples containing $0$ fall below it |
| `[0, 0, 0, 0, 0]`, target 1 | Five equal values | 10 | 10 | Equality never arises here, so strictness is not the hazard; multiplicity is |
| `[-5, -4, -3, -2]`, target 100 | Target above every sum | 4 | 4 | The very first pair $(L, R)$ already qualifies, so one block of size 2 plus one more pair records all $\binom{4}{3} = 4$ triples |

Rows three through five differ only in whether a sum lands exactly on the
bound, and each one shifts the relaxed count upward by one or more. That is the
signature of an inclusive comparison: it silently inflates the answer exactly at
the boundary, never in the interior.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$, where $N$ is the number of elements in `nums`. Sorting takes $O(N \log N)$ time. The outer loop runs $N - 2$ times. In each outer iteration, the two pointers $L$ and $R$ advance toward each other at most $N$ times, executing in $O(N)$ time. Total time is $O(N \log N) + O(N^2) = O(N^2)$.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary memory (sorting in-place), using only three integer loop pointers.
