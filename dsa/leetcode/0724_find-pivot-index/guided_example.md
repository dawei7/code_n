# Guided Example: Find Pivot Index

We trace the step-by-step array total sum aggregation ($S = \sum nums$), dual prefix-suffix sliding equilibrium tracking ($left, right$), sequential element extraction ($right \leftarrow right - nums[i]$), prefix equality evaluation ($left == right$), and leftmost equilibrium index selection on representative integer sequences:

- **Input:** $nums = [1, 7, 3, 6, 5, 6]$
- **Required output:** `3`
  - Pivot index criteria:
    - The pivot index is an index $i$ where the sum of numbers strictly to the left of $i$ equals the sum of numbers strictly to the right of $i$:
      $$
      \sum_{j=0}^{i-1} nums[j] = \sum_{j=i+1}^{n-1} nums[j]
      $$
    - If $i = 0$, the left sum is defined as $0$.
    - If $i = n - 1$, the right sum is defined as $0$.
    - If multiple pivot indices exist, return the **leftmost** index.
    - If no such index exists, return $-1$.
    - For $[1, 7, 3, 6, 5, 6]$:
      - At index $3$ ($nums[3] = 6$):
        - Left sum: $nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11$.
        - Right sum: $nums[4] + nums[5] = 5 + 6 = 11$.
        - Left sum strictly equals right sum ($11 == 11$).
      - Output is **3**.
- **Sliding Balance & Running Prefix Invariant:**
  - **The Conservation of Total Sum:**
    - The total sum $S = \sum_{j=0}^{n-1} nums[j]$ is constant.
    - For any candidate pivot $i$, the array partitions into three disjoint components:
      $$
      S = \text{LeftSum}(i) + nums[i] + \text{RightSum}(i)
      $$
    - Therefore, the equilibrium condition $\text{LeftSum}(i) == \text{RightSum}(i)$ is mathematically equivalent to:
      $$
      2 \times \text{LeftSum}(i) + nums[i] = S
      $$
  - **Dynamic Sliding Pointer Protocol:**
    - Initialize $left = 0$ and $right = S$.
    - For each index $i$ from $0$ to $n - 1$ with element $x = nums[i]$:
      1. Exclude the pivot element $x$ from the right sum:
         $$
         right \leftarrow right - x
         $$
      2. At this instant, $left$ holds the exact sum of elements $0 \dots i-1$, and $right$ holds the exact sum of elements $i+1 \dots n-1$.
      3. If $left == right$: return $i$ immediately (guarantees leftmost pivot).
      4. Add $x$ to the left sum before advancing:
         $$
         left \leftarrow left + x
         $$
- **Step-by-Step Worked Execution Trace on $nums = [1, 7, 3, 6, 5, 6]$:**
  - Compute total sum:
    $$
    S = 1 + 7 + 3 + 6 + 5 + 6 = \mathbf{28}
    $$
  - Initial state:
    $$
    left = 0, \quad right = 28
    $$
  - **Index $i = 0$ ($nums[0] = 1$):**
    - Subtract current element from right:
      $$
      right \leftarrow 28 - 1 = \mathbf{27}
      $$
    - Test equality:
      $$
      left = 0 \ne right = 27 \quad \mathbf{(No\ Match)}
      $$
    - Accumulate into left:
      $$
      left \leftarrow 0 + 1 = \mathbf{1}
      $$
  - **Index $i = 1$ ($nums[1] = 7$):**
    - Subtract from right:
      $$
      right \leftarrow 27 - 7 = \mathbf{20}
      $$
    - Test equality:
      $$
      left = 1 \ne right = 20 \quad \mathbf{(No\ Match)}
      $$
    - Accumulate into left:
      $$
      left \leftarrow 1 + 7 = \mathbf{8}
      $$
  - **Index $i = 2$ ($nums[2] = 3$):**
    - Subtract from right:
      $$
      right \leftarrow 20 - 3 = \mathbf{17}
      $$
    - Test equality:
      $$
      left = 8 \ne right = 17 \quad \mathbf{(No\ Match)}
      $$
    - Accumulate into left:
      $$
      left \leftarrow 8 + 3 = \mathbf{11}
      $$
  - **Index $i = 3$ ($nums[3] = 6$):**
    - Subtract from right:
      $$
      right \leftarrow 17 - 6 = \mathbf{11}
      $$
    - Test equality:
      $$
      left = \mathbf{11} == right = \mathbf{11} \quad \mathbf{(Equilibrium\ Reached!)}
      $$
    - Halts immediately and returns index:
      $$
      ans = \mathbf{3}
      $$
- **Boundary Pivot at Index 0 ($nums = [2, 1, -1]$):**
  - Total sum $S = 2$.
  - $i = 0, x = 2 \implies right = 2 - 2 = 0$.
  - $left = 0 == right = 0 \implies$ returns index **`0`**.
- **No Pivot Index ($nums = [1, 2, 3]$):**
  - $S = 6$.
  - $i = 0$: $left = 0, right = 5$.
  - $i = 1$: $left = 1, right = 3$.
  - $i = 2$: $left = 3, right = 0$.
  - Loop exhausts without match $\implies$ returns **`-1`**.

This instance demonstrates prefix-suffix conservation laws and one-dimensional sliding equilibrium detection, mathematically proves why left-to-right linear search identifies the minimal index satisfying prefix-suffix balance, and derives $O(N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums$:
Find the **leftmost pivot index** where the sum of numbers to its left equals the sum of numbers to its right.
Return $-1$ if no such index exists.

```text
nums = [ 1, 7, 3, 6, 5, 6 ]
Total sum = 28

i = 0 (1): left = 0,  right = 27 (unequal)
i = 1 (7): left = 1,  right = 20 (unequal)
i = 2 (3): left = 8,  right = 17 (unequal)
i = 3 (6): left = 11, right = 11 (EQUAL!)

Pivot found at index 3!
Result: 3
```

### The Invariant of the Conservation of Sum
- Total sum $S = \text{LeftSum} + nums[i] + \text{RightSum}$.
- By tracking $left$ starting at 0 and $right$ starting at $S$, we maintain both sides in $O(1)$ time per step.

---

## 2. Conceptual Foundation & Invariants

### 1. Pre-computation:
$$
S = \sum_{j=0}^{n-1} nums[j]
$$

### 2. Single-Pass Equilibrium Test:
Initialize $left = 0, right = S$.
For each $i \in [0, n - 1]$:
$$
right \leftarrow right - nums[i]
$$
$$
\text{if } left == right \implies \text{return } i
$$
$$
left \leftarrow left + nums[i]
$$

> **Bilateral Sum Invariant.** The pivot condition $\sum_{k < i} x_k = \sum_{k > i} x_k$ is invariant under total sum conservation $2 \cdot \text{prefix}_{i-1} + x_i = S$, which admits a unique leftmost solution via sequential prefix accumulation.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Precompute Total
- $S = 28, left = 0, right = 28$.

---

### Step 2: Index 0 to 2
- $i = 0$: $right = 27, left = 0 \implies left \leftarrow 1$.
- $i = 1$: $right = 20, left = 1 \implies left \leftarrow 8$.
- $i = 2$: $right = 17, left = 8 \implies left \leftarrow 11$.

---

### Step 3: Index 3
- $right = 17 - 6 = 11$.
- $left == right == 11 \implies$ Return **`3`**.

---

## 4. Complete Execution Trace

| Index $i$ | Element $nums[i]$ | Left Sum Before Step | Right Sum After Deduction | Balance Check | Action Taken |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $1$ | $0$ | $27$ | $0 \ne 27$ | Advance, $left \leftarrow 1$ |
| $1$ | $7$ | $1$ | $20$ | $1 \ne 20$ | Advance, $left \leftarrow 8$ |
| $2$ | $3$ | $8$ | $17$ | $8 \ne 17$ | Advance, $left \leftarrow 11$ |
| **$3$** | **$6$** | **$11$** | **$11$** | **$11 == 11$** | **Return Index `3`** |

---

## 5. Boundary Cases & Failure Modes

- **Pivot at Index 0 ($[2, 1, -1]$):** $left = 0$, $right = 0 \implies$ returns 0.
- **Pivot at Last Index ($[-1, 1, 2]$):** $left = 0$, $right = 0 \implies$ returns $n - 1$.
- **No Pivot Found ($[1, 2, 3]$):** Returns $-1$.
- **Negative Numbers and Zeros ($[0, 0, 0]$):** Returns 0 (the leftmost valid pivot).

---

## 6. Traps & Common Anti-Patterns

- **Computing Slices inside Loop ($O(N^2)$):** Calling `sum(nums[:i])` and `sum(nums[i+1:])` inside the loop takes $O(N)$ per iteration, resulting in quadratic time. Maintaining running scalars $left$ and $right$ runs in strictly linear $O(N)$ time.
- **Returning the Last Pivot Instead of Leftmost:** The problem specifically requests the **leftmost** pivot index; return immediately upon the first match.
- **Including Pivot Element in the Sums:** The pivot element $nums[i]$ itself is strictly excluded from both $left$ and $right$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - One pass to compute initial sum $S$: $\mathcal{O}(N)$.
  - One pass to inspect each index with constant scalar operations: $\mathcal{O}(N)$.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 2$ ms for $N = 10^4$.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (only scalar variables $left, right, S$).
