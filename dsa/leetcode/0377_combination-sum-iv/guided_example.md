# Guided Example: Combination Sum IV

We trace the step-by-step ordered combination dynamic programming recurrence ($f[i] = \sum_{x \in nums} f[i - x]$), target-outer/number-inner loop arrangement for sequence sensitivity, base case anchoring ($f[0] = 1$), and cumulative path counting on representative integer instances:

- **Input:** $nums = [1, 2, 3], \quad target = 4$
- **Required output:** $7$
  - The 7 valid ordered sequences summing to 4:
    1. $(1, 1, 1, 1)$
    2. $(1, 1, 2)$
    3. $(1, 2, 1)$
    4. $(2, 1, 1)$
    5. $(1, 3)$
    6. $(3, 1)$
    7. $(2, 2)$
  - Step-by-step sub-target counts:
    - $f[0] = 1$ (Empty sequence)
    - $f[1] = f[0] = 1$ (Sequence: `(1)`)
    - $f[2] = f[1] + f[0] = 1 + 1 = 2$ (Sequences: `(1, 1)`, `(2)`)
    - $f[3] = f[2] + f[1] + f[0] = 2 + 1 + 1 = 4$ (Sequences: `(1,1,1)`, `(2,1)`, `(1,2)`, `(3)`)
    - $f[4] = f[3] + f[2] + f[1] = 4 + 2 + 1 = \mathbf{7}$
  - Total combinations: $\mathbf{7}$
- **Single Element Array:** $nums = [9], target = 3 \implies 0$ (Target unreachable)
- **Target Equal to Smallest Element:** $nums = [2, 4], target = 2 \implies 1$ (`(2)`)

This instance demonstrates counting ordered compositions of an integer using a restricted set of parts, contrasts outer-target loops (permutations/sequences) with outer-item loops (un-ordered coin change combinations), and analyzes $O(T \cdot N)$ runtime and $O(T)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an array of distinct positive integers $nums = [1, 2, 3]$ and a target integer $target = 4$:
Find the number of possible combinations that add up to $target$.
Different sequences of the same elements are counted as distinct combinations (e.g. $(1, 2, 1)$ and $(1, 1, 2)$ are counted separately):

```text
Target: 4, Available Numbers: {1, 2, 3}

All 7 Ordered Sequences:
End with 1: (1, 1, 1, 1), (2, 1, 1), (1, 2, 1), (3, 1)  -> 4 sequences
End with 2: (1, 1, 2),    (2, 2)                         -> 2 sequences
End with 3: (1, 3)                                       -> 1 sequence

Total Sequences = 4 + 2 + 1 = 7
```

### Ordered Sequences vs Unordered Combinations
- In standard Unbounded Knapsack / Coin Change, the outer loop iterates over coin denominations. This forces coins to be chosen in a fixed non-decreasing order, counting **unordered multisets** (combinations).
- Here, **order matters**. By placing the **target sum on the outer loop** ($i \in [1, target]$) and iterating over all possible last elements ($x \in nums$) in the inner loop, any number can be placed at any position in the sequence, counting **ordered permutations**.

---

## 2. Conceptual Foundation & Invariants

### 1. DP State Definition:
Let $f[i]$ denote the total number of ordered combinations whose sum is exactly $i$:
- **Base Case:**
  $$
  f[0] = 1
  $$
  There is exactly $1$ way to achieve a sum of $0$: the empty sequence $()$.
- **Recurrence:**
  For any target $i \ge 1$, a valid sequence must end with some number $x \in nums$ where $x \le i$.
  The prefix preceding $x$ must sum to $i - x$:
  $$
  f[i] = \sum_{x \in nums, \; x \le i} f[i - x]
  $$

### 2. Tabulation Order:
Compute $f[i]$ strictly for $i = 1, 2, \dots, target$ in ascending order.
When evaluating $f[i]$, all subproblems $f[i - x]$ for $x \ge 1$ are already computed.

> **Invariant.** For each $i \le target$, $f[i]$ accurately stores the count of all distinct ordered sequences of integers from $nums$ that sum to $i$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 2, 3]$ with $target = 4$:
Initialized: $f = [1, 0, 0, 0, 0]$ for indices $0 \dots 4$.

---

### Step 1: Sub-target $i = 1$
Evaluate each $x \in [1, 2, 3]$:
- $x = 1$: $1 \le 1 \implies f[1] \mathrel{+}= f[1 - 1] = f[0] = 1$.
- $x = 2$: $2 > 1$ (skipped).
- $x = 3$: $3 > 1$ (skipped).
- Result: $f[1] = \mathbf{1}$ (Sequence: `(1)`).

---

### Step 2: Sub-target $i = 2$
Evaluate each $x \in [1, 2, 3]$:
- $x = 1$: $1 \le 2 \implies f[2] \mathrel{+}= f[2 - 1] = f[1] = 1$.
- $x = 2$: $2 \le 2 \implies f[2] \mathrel{+}= f[2 - 2] = f[0] = 1$.
- $x = 3$: $3 > 2$ (skipped).
- Result: $f[2] = 1 + 1 = \mathbf{2}$ (Sequences: `(1, 1)`, `(2)`).

---

### Step 3: Sub-target $i = 3$
Evaluate each $x \in [1, 2, 3]$:
- $x = 1$: $1 \le 3 \implies f[3] \mathrel{+}= f[3 - 1] = f[2] = 2$.
- $x = 2$: $2 \le 3 \implies f[3] \mathrel{+}= f[3 - 2] = f[1] = 1$.
- $x = 3$: $3 \le 3 \implies f[3] \mathrel{+}= f[3 - 3] = f[0] = 1$.
- Result: $f[3] = 2 + 1 + 1 = \mathbf{4}$ (Sequences: `(1,1,1)`, `(2,1)`, `(1,2)`, `(3)`).

---

### Step 4: Final Target $i = 4$
Evaluate each $x \in [1, 2, 3]$:
- $x = 1$: $1 \le 4 \implies f[4] \mathrel{+}= f[4 - 1] = f[3] = 4$.
- $x = 2$: $2 \le 4 \implies f[4] \mathrel{+}= f[4 - 2] = f[2] = 2$.
- $x = 3$: $3 \le 4 \implies f[4] \mathrel{+}= f[4 - 3] = f[1] = 1$.
- Result:
  $$
  f[4] = 4 + 2 + 1 = \mathbf{7}
  $$

---

## 4. Complete Execution Trace

```text
nums = [1, 2, 3], target = 4
f = [1, 0, 0, 0, 0]

i = 1:
  x = 1: f[1] += f[0] = 1 -> f[1] = 1
i = 2:
  x = 1: f[2] += f[1] = 1
  x = 2: f[2] += f[0] = 1 -> f[2] = 2
i = 3:
  x = 1: f[3] += f[2] = 2
  x = 2: f[3] += f[1] = 1
  x = 3: f[3] += f[0] = 1 -> f[3] = 4
i = 4:
  x = 1: f[4] += f[3] = 4
  x = 2: f[4] += f[2] = 2
  x = 3: f[4] += f[1] = 1 -> f[4] = 7

Output: f[4] = 7
```

| Target Sum $i$ | Branch $x = 1$ ($f[i - 1]$) | Branch $x = 2$ ($f[i - 2]$) | Branch $x = 3$ ($f[i - 3]$) | Total Ways $f[i]$ | Concrete Sequence Set |
|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | - | - | - | 1 | `()` |
| 1 | $+1$ | - | - | **1** | `(1)` |
| 2 | $+1$ | $+1$ | - | **2** | `(1, 1), (2)` |
| 3 | $+2$ | $+1$ | $+1$ | **4** | `(1,1,1), (2,1), (1,2), (3)` |
| **4** | **$+4$** | **$+2$** | **$+1$** | **$\mathbf{7}$** | **All 7 sequences listed above** |

---

## 5. Algorithmic Correctness

**Soundness.** Any non-empty sequence summing to $i$ has a unique final element $x \in nums$. Removing $x$ produces a sequence of non-negative integers summing to $i - x$. Since every valid sequence of sum $i$ is partitioned into disjoint subsets based on its final element $x$, the sum $\sum_{x} f[i - x]$ counts each sequence exactly once without duplicates.

**Completeness.** Every available number $x \in nums$ that does not exceed $i$ is considered as a potential ending element. Since sub-targets are processed from $1$ up to $target$, all valid predecessor states are fully accumulated.

---

## 6. Traps This Instance Exposes

- **Loop Order Confusion:** Swapping the loops (putting `for x in nums:` on the outside) changes the problem to standard Coin Change 2, counting unordered combinations (which would yield 4 instead of 7 for target 4). The target loop must be on the outside to count ordered sequences.
- **Negative Numbers Follow-Up:** If $nums$ contained negative numbers, an arbitrary number of $+x$ and $-x$ pairs could cancel out, creating an infinite number of sequences (e.g. $1 + (-1) + 1 + (-1) \dots$). Negative numbers require bounding the maximum sequence length.
- **Base Case $f[0] = 0$ Error:** Setting $f[0] = 0$ would cause all subsequent $f[i]$ to remain 0. A single element $x$ summing to $x$ relies on $f[x - x] = f[0] = 1$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(T \cdot N)$, where $T = target$ and $N = \text{len}(nums)$.
  - The outer loop runs $T$ times.
  - The inner loop iterates over all $N$ elements.
  - Total arithmetic additions: $T \times N$, running well under $10^6$ operations for $T \le 1000, N \le 200$.
- **Auxiliary Space Complexity:** $O(T)$ auxiliary space to store the 1D DP table $f$ of size $target + 1$.