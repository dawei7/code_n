# Guided Example: Minimum Moves to Equal Array Elements II

We trace the step-by-step $L_1$ norm Manhattan distance minimization, subgradient balance theorem ($N_{left} == N_{right}$), median selection, and absolute deviation summation ($\sum |nums[i] - \text{median}|$) on representative numeric arrays:

- **Input:** $nums = [1, 2, 3]$
- **Required output:** `2`
  - Array length: $n = 3$ (Odd)
  - Sorted array: $[1, 2, 3]$
  - Median selection: Index $\lfloor 3 / 2 \rfloor = 1 \implies k = 2$
  - Absolute deviations to target $k = 2$:
    - For element $nums[0] = 1$: $|1 - 2| = \mathbf{1}$
    - For element $nums[1] = 2$: $|2 - 2| = \mathbf{0}$
    - For element $nums[2] = 3$: $|3 - 2| = \mathbf{1}$
  - Total minimum moves:
    $$
    1 + 0 + 1 = \mathbf{2}
    $$
- **Even-Length Array Instance:** $nums = [1, 10, 2, 9]$ ($n = 4$)
  - Sorted array: $[1, 2, 9, 10]$
  - Any target in the median interval $[2, 9]$ yields the identical optimal cost:
    - Choosing $k = 2$:
      $$
      |1 - 2| + |2 - 2| + |9 - 2| + |10 - 2| = 1 + 0 + 7 + 8 = \mathbf{16}
      $$
    - Choosing $k = 9$:
      $$
      |1 - 9| + |2 - 9| + |9 - 9| + |10 - 9| = 8 + 7 + 0 + 1 = \mathbf{16}
      $$
- **All Elements Equal Instance:** $nums = [5, 5, 5] \implies \text{median} = 5 \implies \mathbf{0}$ moves

This instance demonstrates median optimality for $L_1$ loss functions, mathematically proves why the mean minimizes squared errors ($L_2$) while the median minimizes absolute errors ($L_1$), and derives $O(N \log N)$ runtime (or $O(N)$ via Quickselect) and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums = [1, 2, 3]$:
In one move, you can **increment or decrement an element by 1**.
Find the **minimum number of moves** required to make all array elements equal.

```text
Array Elements on the Number Line:
  1 ------- 2 ------- 3
  ^         ^         ^
  nums[0]  median   nums[2]

Target: Median = 2
  Distance from 1 to 2: |1 - 2| = 1
  Distance from 2 to 2: |2 - 2| = 0
  Distance from 3 to 2: |3 - 2| = 1

Total Moves: 1 + 0 + 1 = 2
```

### The $L_1$ Minimization Principle
We want to choose a target integer $x$ that minimizes the total cost:
$$
f(x) = \sum_{i=0}^{n-1} |nums[i] - x|
$$
- If we choose the arithmetic mean $\bar{x}$, we minimize the sum of squared differences $\sum (nums[i] - x)^2$ ($L_2$ norm).
- But here, each step costs $1$, meaning we are minimizing the sum of **absolute differences** ($L_1$ norm).
- In mathematical statistics, the point that minimizes the sum of absolute deviations from a set of 1D points is unconditionally the **median**.

---

## 2. Conceptual Foundation & Invariants

### 1. Subgradient Balance Proof:
Consider shifting the target point $x$ by a small positive increment $\Delta > 0$:
- Every point $nums[i] < x$ sees its distance increase by $\Delta$.
- Every point $nums[i] > x$ sees its distance decrease by $\Delta$.
- The net change in total cost is:
  $$
  \Delta \cdot (\text{Count}(nums[i] < x) - \text{Count}(nums[i] > x))
  $$
- To minimize $f(x)$, the net slope must be zero:
  $$
  \text{Count}(nums[i] < x) == \text{Count}(nums[i] > x)
  $$
- This balance condition is satisfied precisely when $x$ divides the array into two equal halves, which is the definition of the **median**.

### 2. Pairing Outer Elements:
Alternatively, consider pairing the smallest and largest elements:
- To equalize $nums[0]$ and $nums[n-1]$ to any point $x \in [nums[0], nums[n-1]]$:
  $$
  |nums[0] - x| + |nums[n-1] - x| = nums[n-1] - nums[0]
  $$
  The cost for this outer pair is constant for any $x$ inside their interval!
- Moving inward, the next pair $(nums[1], nums[n-2])$ is minimized for any $x \in [nums[1], nums[n-2]]$.
- Nesting these intervals yields the intersection of all pairs, which narrows down to the median value $nums[\lfloor n/2 \rfloor]$.

> **Median Invariant.** For any $x$, $f(x) \ge f(nums[\lfloor n / 2 \rfloor])$. Any choice other than the median strictly increases the total cost.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 2, 3]$ ($n = 3$):

---

### Step 1: Sort the Array
Sort $nums$ in ascending order:
$$
nums = [1, 2, 3]
$$

---

### Step 2: Extract the Median
Find the element at middle index $k = \lfloor 3 / 2 \rfloor = 1$:
$$
x = nums[1] = \mathbf{2}
$$

---

### Step 3: Compute Absolute Deviations
Sum $|nums[i] - x|$ across all indices:
- At $i = 0$: $|nums[0] - 2| = |1 - 2| = \mathbf{1}$.
- At $i = 1$: $|nums[1] - 2| = |2 - 2| = \mathbf{0}$.
- At $i = 2$: $|nums[2] - 2| = |3 - 2| = \mathbf{1}$.

Total sum:
$$
f(2) = 1 + 0 + 1 = \mathbf{2}
$$

---

### Comparison with Suboptimal Target (Mean / Extreme):
- If we chose $x = 1$: $f(1) = |1-1| + |2-1| + |3-1| = 0 + 1 + 2 = 3 > 2$.
- If we chose $x = 3$: $f(3) = |1-3| + |2-3| + |3-3| = 2 + 1 + 0 = 3 > 2$.
Median $x = 2$ achieves the strictly minimal cost of **`2`**.

---

## 4. Complete Execution Trace

| Element $nums[i]$ | Sorted Index | Selected Median $k$ | Absolute Distance $\lvert nums[i] - k \rvert$ | Cumulative Moves |
|:---:|:---:|:---:|:---:|:---:|
| $1$ | $0$ | $2$ | $\lvert 1 - 2 \rvert = 1$ | $1$ |
| $2$ | $1$ (Middle) | $2$ | $\lvert 2 - 2 \rvert = 0$ | $1$ |
| $3$ | $2$ | $2$ | $\lvert 3 - 2 \rvert = 1$ | **$2$** |
| **Total** | — | — | $\sum \lvert nums[i] - 2 \rvert$ | **Result: $2$** |

---

## 5. Boundary Cases & Failure Modes

- **Single Element ($nums = [10]$):** Median is 10 $\implies |10 - 10| = \mathbf{0}$.
- **Even-Length Array ($nums = [1, 2, 9, 10]$):** Any point between $nums[1] = 2$ and $nums[2] = 9$ gives the identical minimal cost $16$. Choosing index $\lfloor 4 / 2 \rfloor = 2$ ($value = 9$) or $1$ ($value = 2$) gives the same answer.
- **Negative Elements ($nums = [-10, -5, 0, 5, 10]$):** Sorted order handles negatives seamlessly. Median is 0. Total moves: $10 + 5 + 0 + 5 + 10 = \mathbf{30}$.
- **Duplicate Elements ($nums = [1, 1, 1, 100]$):** Median is 1 $\implies 0 + 0 + 0 + 99 = \mathbf{99}$.

---

## 6. Traps & Common Anti-Patterns

- **Using the Arithmetic Mean Instead of the Median:** The mean minimizes $\sum (x_i - \mu)^2$. For $[1, 2, 9, 10]$, the mean is $5.5$. Rounding to 5 or 6 gives cost $|1-5| + |2-5| + |9-5| + |10-5| = 4 + 3 + 4 + 5 = 16$, but for asymmetric datasets (e.g. $[1, 1, 100]$, mean $= 34 \implies \text{cost } 132$, while median $= 1 \implies \text{cost } 99$), the mean fails dramatically.
- **Integer Overflow in Summation:** Sum of differences can exceed 32-bit signed integer capacity ($N \times 10^9 = 10^{14}$). Using 64-bit accumulators prevents overflow.
- **Sorting Unnecessarily When Quickselect is Available:** Sorting takes $O(N \log N)$. In performance-critical environments, Quickselect (`nth_element`) finds the median in $O(N)$ average time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting the array takes $O(N \log N)$ time (or $O(N)$ using linear-time median selection).
  - Computing the sum of deviations takes a single pass of $O(N)$ time.
  - Total Time: $\mathcal{O}(N \log N)$. For $N = 10^5$, finishes in under 20 ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ beyond language-level in-place sorting.
