# Guided Example: Patching Array

We trace the step-by-step continuous coverage frontier maintenance ($[1, x-1]$), greedy gap resolution via doubling (`x <<= 1`), array element consumption ($x \mathrel{+}= \text{nums}[i]$), and minimum patch counting on representative sorted array instances:

- **Input:** $\text{nums} = [1, 5, 10], \quad n = 20$
- **Required output:** $2$
  - Initial state: $x = 1$ (smallest uncovered integer)
  - Consume $1 \implies x = 2$, coverage $[1, 1]$
  - Next array element is $5 > 2$ (Gap at $2$):
    - Patch with $2 \implies x$ doubles to $4$, coverage $[1, 3]$ ($\text{patches} = 1$)
  - Next array element is $5 > 4$ (Gap at $4$):
    - Patch with $4 \implies x$ doubles to $8$, coverage $[1, 7]$ ($\text{patches} = 2$)
  - Consume $5 \le 8 \implies x = 8 + 5 = 13$, coverage $[1, 12]$
  - Consume $10 \le 13 \implies x = 13 + 10 = 23$, coverage $[1, 22]$
  - $23 > 20$, covering all values in $[1, 20]$ with $\mathbf{2}$ patches
- **Zero Patches Needed:** $\text{nums} = [1, 2, 2], n = 5 \implies 0$ (all sums in $[1, 5]$ already formable)
- **Single Element Minimal:** $\text{nums} = [1, 3], n = 6 \implies 1$ (patch $2$)
- **Empty Array Base Case:** $\text{nums} = [], n = 7 \implies 3$ (must patch powers of two: $1, 2, 4$)

This instance demonstrates greedy range extension on sorted numeric multisets, mathematically proves why patching the missing value $x$ itself maximally extends the coverage interval from $[1, x-1]$ to $[1, 2x-1]$ without leaving internal gaps, and analyzes $O(M + \log N)$ time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a sorted integer array $\text{nums} = [1, 5, 10]$ and target integer $n = 20$:
Add the minimum number of positive integer patches to `nums` such that any integer in $[1, n]$ can be formed by summing a subset of elements:

```text
nums: [1, 5, 10], n = 20

Coverage Progression:
Start:              Can form []             -> Missing: 1
Use 1:              Can form [1]            -> Missing: 2
Array has 5 > 2!    Must PATCH 2!           -> Can form [1, 3] -> Missing: 4
Array has 5 > 4!    Must PATCH 4!           -> Can form [1, 7] -> Missing: 8
Use 5:              Can form [1, 12]        -> Missing: 13
Use 10:             Can form [1, 22]        -> Missing: 23 > 20 (DONE!)

Patches Added: {2, 4} -> Total Patches: 2
```

### The Infeasibility of Explicit Subset Sum Sets
- Tracking the set of all achievable subset sums using a boolean array or hash set takes $O(n)$ space and time.
- For $n = 2^{31} - 1$, storing $2 \times 10^9$ numbers is impossible.
- **The Continuous Frontier Invariant:**
  Because elements are positive integers, if we can form every integer in $[1, x - 1]$, adding an element $v \le x$ extends our reach to $[1, x - 1 + v]$ continuously without skipping any numbers!

---

## 2. Conceptual Foundation & Invariants

### Coverage Interval $[1, x - 1]$
Let $x$ denote the **smallest positive integer that cannot currently be formed**:
- All integers in the continuous range $[1, x - 1]$ are confirmed formable.
- Initially: $x = 1$. The covered range is $[1, 0]$ (empty).

### The Two Frontier Decisions:
At each iteration while $x \le n$:

#### Case 1: The next array element is usable ($i < \text{len}(nums)$ and $\text{nums}[i] \le x$)
Because $\text{nums}[i] \le x$, the existing covered range $[0, x - 1]$ shifted by $\text{nums}[i]$ is:
$$
[\text{nums}[i], \; x - 1 + \text{nums}[i]]
$$
Since $\text{nums}[i] \le x$, this shifted range touches or overlaps with $[0, x - 1]$.
Their union forms a seamless continuous range:
$$
[0, \; x + \text{nums}[i] - 1]
$$
The new smallest unformable value becomes:
$$
x \leftarrow x + \text{nums}[i], \quad i \leftarrow i + 1
$$

#### Case 2: Array exhausted OR next element is too large ($\text{nums}[i] > x$)
If $\text{nums}[i] > x$, using $\text{nums}[i]$ cannot help form $x$ (it is already larger than $x$).
Since all remaining array elements are $\ge \text{nums}[i] > x$, no available element can form $x$.
We **must patch** a new number:
- What is the optimal number to patch? **Patch $x$ itself!**
- Patching $x$ safely covers $x$ and maximally extends our reach to $[1, x - 1 + x] = [1, 2x - 1]$.
- The new smallest unformable integer becomes $2x$:
  $$
  ans \leftarrow ans + 1, \quad x \leftarrow x \ll 1
  $$

> **Invariant.** At every step, all integers in $[1, x - 1]$ can be formed. Patching $x$ doubles the coverage frontier, ensuring exponential expansion towards $n$.

---

## 3. Step-by-Step Worked Execution

We trace the execution on $\text{nums} = [1, 5, 10]$ and $n = 20$:
Initialized: $x = 1, ans = 0, i = 0$.

---

### Step 1: $x = 1$
- Check $nums[0] = 1 \le x = 1$ (**True**).
- Consume $nums[0] = 1$:
  $$
  x \leftarrow 1 + 1 = \mathbf{2}, \quad i \leftarrow 1
  $$
- Covered range: $[1, 1]$. Patches: $0$.

---

### Step 2: $x = 2$
- Check $nums[1] = 5 \le x = 2$ (**False**, $5 > 2$).
- Gap at 2 cannot be covered by array elements.
- **Action: Patch with $2$!**
  $$
  ans \leftarrow 0 + 1 = \mathbf{1}, \quad x \leftarrow 2 \ll 1 = \mathbf{4}
  $$
- Covered range: $[1, 3]$ (Formable: $\{1, 2, 3\}$). Patches: $1$.

---

### Step 3: $x = 4$
- Check $nums[1] = 5 \le x = 4$ (**False**, $5 > 4$).
- Gap at 4 cannot be covered by array elements.
- **Action: Patch with $4$!**
  $$
  ans \leftarrow 1 + 1 = \mathbf{2}, \quad x \leftarrow 4 \ll 1 = \mathbf{8}
  $$
- Covered range: $[1, 7]$ (Formable: $\{1, 2, \dots, 7\}$). Patches: $2$.

---

### Step 4: $x = 8$
- Check $nums[1] = 5 \le x = 8$ (**True**, $5 \le 8$).
- Consume $nums[1] = 5$:
  $$
  x \leftarrow 8 + 5 = \mathbf{13}, \quad i \leftarrow 2
  $$
- Covered range: $[1, 12]$. Patches: $2$.

---

### Step 5: $x = 13$
- Check $nums[2] = 10 \le x = 13$ (**True**, $10 \le 13$).
- Consume $nums[2] = 10$:
  $$
  x \leftarrow 13 + 10 = \mathbf{23}, \quad i \leftarrow 3
  $$
- Covered range: $[1, 22]$. Patches: $2$.

---

### Step 6: Termination
- Check loop condition: $x \le n \iff 23 \le 20$ (**False**).
- Range $[1, 20]$ is completely contained within $[1, 22]$.
- Return total patches:
  $$
  ans = \mathbf{2}
  $$

---

## 4. Complete Execution Trace

```text
nums = [1, 5, 10], n = 20
x = 1, ans = 0, i = 0

Iter 1: nums[0]=1 <= 1 -> consume 1  -> x becomes 2,  i = 1
Iter 2: nums[1]=5 >  2 -> PATCH 2    -> x becomes 4,  ans = 1
Iter 3: nums[1]=5 >  4 -> PATCH 4    -> x becomes 8,  ans = 2
Iter 4: nums[1]=5 <= 8 -> consume 5  -> x becomes 13, i = 2
Iter 5: nums[2]=10<=13 -> consume 10 -> x becomes 23, i = 3
Exit:   x = 23 > 20 -> Stop

Total Patches: 2
```

| Iteration | Current Frontier $x$ | Next Array Value $nums[i]$ | Decision | Reason | New $x$ | Covered Range | Total Patches $ans$ |
|:---:|:---:|:---:|:---|:---|:---:|:---:|:---:|
| 1 | 1 | $1$ | Consume $nums[0]$ | $1 \le 1$ | 2 | $[1, 1]$ | 0 |
| **2** | **2** | **$5$** | **Patch $2$** | **$5 > 2$ (Gap at 2)** | **4** | **$[1, 3]$** | **1** |
| **3** | **4** | **$5$** | **Patch $4$** | **$5 > 4$ (Gap at 4)** | **8** | **$[1, 7]$** | **2** |
| 4 | 8 | $5$ | Consume $nums[1]$ | $5 \le 8$ | 13 | $[1, 12]$ | 2 |
| 5 | 13 | $10$ | Consume $nums[2]$ | $10 \le 13$ | 23 | $[1, 22]$ | 2 |
| **End** | **23** | - | **Terminate** | **$x = 23 > 20$** | 23 | $[1, 22]$ | **$\mathbf{2}$ (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** If all numbers in $[1, x - 1]$ can be formed, adding a patch of value $x$ guarantees that $x$ itself is formable ($0 + x = x$), and adding $x$ to any previously formable number $k \in [1, x - 1]$ produces $k + x \in [x + 1, 2x - 1]$. The new formable range is strictly continuous $[1, 2x - 1]$ with no missing numbers. Every patch added is mathematically necessary to bridge the gap at $x$.

**Completeness.** Any patch smaller than $x$ would expand the frontier to less than $2x$, requiring equal or more patches overall. Any patch larger than $x$ would leave $x$ unformable because all existing numbers sum to at most $x - 1$. Thus, patching $x$ is uniquely optimal, guaranteeing the minimal patch count.

---

## 6. Traps This Instance Exposes

- **Greedy Patch Choice:** Patching $x - 1$ or a smaller number leaves a smaller expansion window. Patching larger than $x$ skips $x$. Patching $x$ itself is the unique greedy optimum.
- **Integer Overflow in Bit Shifting:** If $n = 2^{31} - 1$, $x$ can grow up to $2 \times 10^9$. Doubling $x$ can exceed 32-bit signed integer limits. In languages like C++ or Java, $x$ must be declared as a 64-bit integer (`long long` / `long`) to prevent negative overflow. Python handles arbitrary precision integers automatically.
- **Array Exhaustion:** When $i$ reaches $\text{len}(nums)$, remaining coverage up to $n$ must continue doubling via patches (`x <<= 1`) until $x > n$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M + \log N)$, where $M = \text{len}(nums)$ and $N$ is the target integer.
  - The pointer $i$ advances through `nums` at most $M$ times.
  - When patching, $x$ doubles at each step. Starting from $1$, $x$ can double at most $\lceil \log_2 N \rceil$ times before exceeding $N$.
  - Total time is bounded by $O(M + \log N)$.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory using only scalar state variables ($x, ans, i$).
