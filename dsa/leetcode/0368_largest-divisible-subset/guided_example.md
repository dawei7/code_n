# Guided Example: Largest Divisible Subset

We trace the step-by-step array pre-sorting, transitivity of integer divisibility, dynamic programming chain length formulation ($f[i] = \max(f[j] + 1)$), and backwards path reconstruction on representative integer sets:

- **Input:** `nums = [1, 2, 3]`
- **Required output:** `[2, 1]` (or `[1, 2]` / `[1, 3]`)
  - Sorted array: `[1, 2, 3]`
  - Pairwise divisibility constraints:
    - $1 \mid 2$ (2 is divisible by 1)
    - $1 \mid 3$ (3 is divisible by 1)
    - $2 \nmid 3$ (3 is not divisible by 2)
  - Longest divisible chains:
    - Path A: $1 \to 2$ (Length 2, subset $\{1, 2\}$)
    - Path B: $1 \to 3$ (Length 2, subset $\{1, 3\}$)
  - DP array computed: $f = [1, 2, 2]$, peak at index $k = 1$ with length $m = 2$
  - Backtracking reconstruction:
    - At index 1: emits $nums[1] = 2$, remaining length $m = 1$
    - At index 0: $2 \% 1 == 0$ and $f[0] == 1 \implies$ emits $nums[0] = 1$
    - Emitted subset: `[2, 1]`
- **Four-Element Chain Instance:** `nums = [1, 2, 4, 8] \implies [8, 4, 2, 1]`
- **Prime Numbers Set:** `nums = [2, 3, 5, 7] \implies [2]` (Any single element, length 1)

This instance demonstrates dynamic programming over partially ordered sets (posets), mathematically proves why sorting enables the transitivity condition $a \mid b \land b \mid c \implies a \mid c$, explains backwards path recovery, and analyzes $O(N^2)$ time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a set of distinct positive integers $\text{nums} = [1, 2, 3]$:
Find the largest subset such that for every pair of elements $(u, v)$ in the subset:
$$
u \mid v \quad \text{or} \quad v \mid u \quad (u \pmod v == 0 \lor v \pmod u == 0)
$$

```text
Input: [1, 2, 3]

Pairwise Divisibility Graph:
  1 ----> 2
   \
    \---> 3
(No edge between 2 and 3 because 3 is not divisible by 2)

Candidate Divisible Subsets:
{1, 2} -> Size 2 (1|2)
{1, 3} -> Size 2 (1|3)
{2, 3} -> INVALID (2 does not divide 3, 3 does not divide 2)

Largest Subset Size: 2 (Output: [2, 1] or [1, 2])
```

### The Transitivity Principle via Sorting
If an array is sorted in strictly increasing order $a_1 < a_2 < \dots < a_k$:
If $a_k$ is divisible by $a_{k-1}$, and $a_{k-1}$ is divisible by $a_{k-2}$, then by mathematical transitivity:
$$
a_{k-1} \mid a_k \quad \land \quad a_{k-2} \mid a_{k-1} \implies a_{k-2} \mid a_k
$$
Therefore, to extend an existing valid chain ending at $a_{k-1}$ with a new larger integer $a_k$, we **only need to verify that $a_k$ is divisible by the largest element $a_{k-1}$**!
This converts the subset problem into a 1D Longest Increasing Subsequence (LIS)-style DP.

---

## 2. Conceptual Foundation & Invariants

### 1. DP State Definition:
Let $f[i]$ denote the maximum size of a divisible subset whose largest element is `nums[i]`:
- Initialize: $f[i] = 1$ for all $i \in [0, n - 1]$.
- Recurrence:
  For each $i \in [0, n - 1]$ and all $j \in [0, i - 1]$:
  $$
  \text{if } \text{nums}[i] \pmod{\text{nums}[j]} == 0: \quad f[i] = \max(f[i], \; f[j] + 1)
  $$
- Peak Tracking: Let $k = \operatorname{argmax}_i f[i]$ be the index of the chain head.

### 2. Backwards Subset Reconstruction:
Starting at index $k$ with target remaining length $m = f[k]$:
Iterate $i$ backwards from $k$ down to $0$:
If $\text{nums}[k] \pmod{\text{nums}[i]} == 0$ and $f[i] == m$:
1. Append $\text{nums}[i]$ to $ans$.
2. Update predecessor reference: $k \leftarrow i$.
3. Decrement target length: $m \leftarrow m - 1$.

> **Invariant.** For every element $a_j$ chosen during reconstruction, $a_j$ divides the previously chosen element $a_k$, preserving mutual divisibility across all collected numbers.

---

## 3. Step-by-Step Worked Execution

We trace `nums = [1, 2, 3]` ($n = 3$):
Sorted array: `nums = [1, 2, 3]`.

---

### Step 1: Forward DP Table Population
1. **Index $i = 0$ ($nums[0] = 1$):**
   - Base case: $f[0] = 1$.
   - Best so far: $k = 0, f[k] = 1$.
2. **Index $i = 1$ ($nums[1] = 2$):**
   - Inner loop $j = 0$: $nums[1] \pmod{nums[0]} = 2 \pmod 1 = 0$.
   - Transition:
     $$
     f[1] = \max(1, \; f[0] + 1) = \max(1, \; 1 + 1) = \mathbf{2}
     $$
   - Since $f[1] > f[k]$ ($2 > 1$), update best index: $k \leftarrow 1$.
3. **Index $i = 2$ ($nums[2] = 3$):**
   - Inner loop $j = 0$: $3 \pmod 1 = 0 \implies f[2] = \max(1, f[0] + 1) = \mathbf{2}$.
   - Inner loop $j = 1$: $3 \pmod 2 = 1 \ne 0 \implies$ cannot chain from $2$.
   - Final $f[2] = 2$.
   - $f[2] \not> f[k]$ ($2 \not> 2$), $k$ remains $1$.

DP Array Summary:
$$
f = [1, \; 2, \; 2], \quad \text{Optimal End Index } k = 1, \quad \text{Maximum Length } m = 2
$$

---

### Step 2: Backwards Path Reconstruction
Initialize: $k = 1, m = 2, i = 1, ans = []$.

1. **Step $i = 1$ ($nums[1] = 2$):**
   - Divisibility check: $nums[k] \pmod{nums[1]} = 2 \pmod 2 = 0$.
   - Length check: $f[1] == m \iff 2 == 2$ (**True**).
   - Append to subset:
     $$
     ans.\text{append}(2) \implies ans = [\mathbf{2}]
     $$
   - Update state: $k \leftarrow 1, \; m \leftarrow 2 - 1 = \mathbf{1}$.
   - Advance: $i \leftarrow 0$.

2. **Step $i = 0$ ($nums[0] = 1$):**
   - Divisibility check: $nums[k] \pmod{nums[0]} = 2 \pmod 1 = 0$.
   - Length check: $f[0] == m \iff 1 == 1$ (**True**).
   - Append to subset:
     $$
     ans.\text{append}(1) \implies ans = [2, \; \mathbf{1}]
     $$
   - Update state: $k \leftarrow 0, \; m \leftarrow 1 - 1 = \mathbf{0}$.
   - Target length $m = 0$ reached! While loop terminates.

---

### Step 3: Final Output
Subset contains 2 mutually divisible integers:
$$
ans = \mathbf{[2, 1]}
$$

---

## 4. Complete Execution Trace

```text
nums = [1, 2, 3] (Sorted)

DP Calculation:
i = 0: nums[0]=1 -> f[0]=1, peak k=0
i = 1: nums[1]=2 -> 2%1==0 -> f[1]=f[0]+1=2, peak k=1
i = 2: nums[2]=3 -> 3%1==0 -> f[2]=f[0]+1=2 (3%2!=0)

State: f = [1, 2, 2], peak index k = 1, max size m = 2

Backtracking:
i = 1: nums[1]=2, 2%2==0 and f[1]==2 -> ans=[2], k=1, m=1
i = 0: nums[0]=1, 2%1==0 and f[0]==1 -> ans=[2, 1], k=0, m=0

Result: [2, 1]
```

| Index $i$ | $nums[i]$ | Valid Predecessors $j < i$ | State Computation $f[i]$ | Is New Peak? | Peak Index $k$ | Peak Size $f[k]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | None | 1 | Initial | 0 | 1 |
| **1** | **2** | $j = 0$ ($2 \pmod 1 == 0$) | $\max(1, 1 + 1) = \mathbf{2}$ | **Yes** | **1** | **2** |
| 2 | 3 | $j = 0$ ($3 \pmod 1 == 0$) | $\max(1, 1 + 1) = 2$ | No | 1 | 2 |

---

## 5. Algorithmic Correctness

**Soundness.** Suppose subset $S = \{a_1, a_2, \dots, a_m\}$ is sorted ascending. By inductive construction, each $a_p$ divides $a_{p+1}$. If $x \mid y$ and $y \mid z$, then $x \mid z$. Hence, for any pair $a_p < a_q$, $a_p$ divides $a_q$. Thus every pair satisfies $a_q \pmod{a_p} == 0$, fulfilling the problem contract.

**Completeness.** Every possible predecessor $j < i$ where $nums[i] \pmod{nums[j]} == 0$ is considered in the inner loop. The optimal substructure property guarantees that $f[i]$ is the absolute maximal chain ending at $nums[i]$. Tracking the global maximum over all $i$ guarantees finding the largest divisible subset.

---

## 6. Traps This Instance Exposes

- **Order Requirement:** Pairwise divisibility must hold for **all** pairs in the subset, not just adjacent elements. Sorting beforehand is mandatory so that pairwise divisibility reduces to adjacent chain divisibility via transitivity.
- **Multiple Optimal Subsets:** For `[1, 2, 3]`, both `[1, 2]` and `[1, 3]` are optimal (size 2). Returning any valid maximum subset satisfies the problem.
- **Reconstruction Fallacy:** Simply selecting any element with $f[i] == m - 1$ without checking $nums[k] \pmod{nums[i]} == 0$ can attach an unrelated branch from another chain. Both condition checks are mandatory.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$, where $N$ is the number of integers in `nums`.
  - Sorting takes $O(N \log N)$ time.
  - The nested DP loops execute $\frac{N(N-1)}{2}$ modulo operations $\implies O(N^2)$ time.
  - Backtracking takes $O(N)$ time.
  - Total time is strictly $O(N^2)$, easily handling $N \le 1000$.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store the DP array $f$ and output list $ans$.
