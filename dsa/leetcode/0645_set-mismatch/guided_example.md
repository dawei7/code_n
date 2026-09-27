# Guided Example: Set Mismatch

We trace the step-by-step arithmetic series expected sum ($s_1 = \frac{n(n+1)}{2}$), observed multiset sum ($s = \sum nums$), deduplicated set sum ($s_2 = \sum \text{set}(nums)$), closed-form algebraic difference extraction ($dup = s - s_2$ and $miss = s_1 - s_2$), and linear-time defect detection on representative corrupted permutation arrays:

- **Input:** $nums = [1, 2, 2, 4]$
- **Required output:** `[2, 3]`
  - Problem definitions:
    - An array originally contained all integers from $1$ to $n$ exactly once.
    - Due to a data transmission corruption, one number became duplicated ($dup$), displacing one number that is now missing ($miss$).
    - Goal: Return $[dup, \; miss]$ in that exact order.
- **Algebraic Set-Sum Triple Invariant:**
  - Let $n = |nums|$.
  - **1. Ideal Expected Sum ($s_1$):**
    - The sum of all numbers from $1$ to $n$:
      $$
      s_1 = \sum_{i=1}^n i = \frac{n(n + 1)}{2}
      $$
  - **2. Observed Raw Array Sum ($s$):**
    - In $nums$, the missing number is absent, and the duplicate number appears twice:
      $$
      s = \sum_{x \in nums} x = s_1 + dup - miss
      $$
  - **3. Deduplicated Unique Set Sum ($s_2$):**
    - Taking the unique set of elements eliminates the second occurrence of $dup$. The set contains all numbers from $1$ to $n$ **except $miss$**:
      $$
      s_2 = \sum_{x \in \text{set}(nums)} x = s_1 - miss
      $$
  - **Direct Closed-Form Solution:**
    - From $s_2 = s_1 - miss$, we immediately isolate $miss$:
      $$
      miss = s_1 - s_2
      $$
    - From $s = s_2 + dup$, we immediately isolate $dup$:
      $$
      dup = s - s_2
      $$
    - Both answers are computed directly via arithmetic differences without sorting or frequency hash map lookups!
- **Step-by-Step Worked Execution Trace on $[1, 2, 2, 4]$:**
  - Array length: $n = 4$.
  - **Step 1: Compute Ideal Expected Sum ($s_1$):**
    $$
    s_1 = \frac{4 \times (4 + 1)}{2} = \frac{4 \times 5}{2} = \mathbf{10}
    $$
    - (The ideal set $\{1, 2, 3, 4\}$ sums to $1 + 2 + 3 + 4 = 10$).
  - **Step 2: Compute Observed Multiset Sum ($s$):**
    $$
    s = 1 + 2 + 2 + 4 = \mathbf{9}
    $$
  - **Step 3: Compute Deduplicated Set Sum ($s_2$):**
    - Unique elements present in array:
      $$
      \text{set}(nums) = \{1, 2, 4\}
      $$
    - Sum of unique elements:
      $$
      s_2 = 1 + 2 + 4 = \mathbf{7}
      $$
  - **Step 4: Solve for $dup$ and $miss$:**
    - **Find Duplicate:**
      - The difference between the raw multiset sum and the unique set sum is precisely the extra copy of the duplicate:
        $$
        dup = s - s_2 = 9 - 7 = \mathbf{2}
        $$
    - **Find Missing:**
      - The difference between the ideal full sum and the unique set sum is precisely the absent number:
        $$
        miss = s_1 - s_2 = 10 - 7 = \mathbf{3}
        $$
  - **Step 5: Assemble Output:**
    $$
    [dup, \; miss] = [\mathbf{2}, \; \mathbf{3}]
    $$
- **Endpoint Missing Instance ($nums = [1, 1], n = 2$):**
  - $s_1 = 2 \times 3 / 2 = 3$.
  - $s = 1 + 1 = 2$.
  - $s_2 = \text{sum}(\{1\}) = 1$.
  - $dup = 2 - 1 = \mathbf{1}$.
  - $miss = 3 - 1 = \mathbf{2}$.
  - Result: `[1, 2]`.
- **Bitwise XOR Alternative ($O(1)$ Space):**
  - XORing all array elements with $1 \dots n$ yields $dup \oplus miss$.
  - Partitioning by the lowest set bit isolates $dup$ and $miss$ without any extra collection allocations.

This instance demonstrates algebraic conservation laws over perturbed integer sets, mathematically proves why projection onto unique support partitions multiset mass into distinct defect coordinates, and derives $O(N)$ runtime and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an array $nums$ of length $n$ containing numbers from $1$ to $n$ with one duplicate and one missing:
Find `[duplicate, missing]` in that order.

```text
nums = [ 1, 2, 2, 4 ], n = 4

1. Expected sum s1 = 1 + 2 + 3 + 4 = 10
2. Actual sum   s  = 1 + 2 + 2 + 4 = 9
3. Unique sum   s2 = 1 + 2 + 4     = 7

Duplicate = s - s2  = 9 - 7  = 2
Missing   = s1 - s2 = 10 - 7 = 3

Result: [2, 3]
```

### The Invariant of Set Subtraction
- The raw array has one extra copy of the duplicate $\implies s - s2 = dup$.
- The unique set is missing only the absent number $\implies s1 - s2 = miss$.

---

## 2. Conceptual Foundation & Invariants

### 1. Algebraic Formulas:
$$
s_1 = \frac{n(n + 1)}{2}
$$
$$
s = \sum_{x \in nums} x
$$
$$
s_2 = \sum_{x \in \text{set}(nums)} x
$$
$$
\text{Ans} = [s - s_2, \; s_1 - s_2]
$$

### 2. Conservation Invariant:
$$
s - s_1 = dup - miss
$$

> **Set-Support Deficit Invariant.** Deduplication acts as the idempotent operator $\text{Supp}: \mathcal{M} \to \mathcal{P}$, isolating the multi-cardinality mass $dup$ while preserving the deficiency gap $miss$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 2, 2, 4]$:

---

### Step 1: Compute Ideal Sum
- $n = 4$.
- $s_1 = (4 \times 5) / 2 = 10$.

---

### Step 2: Compute Actual Sum
- $s = 1 + 2 + 2 + 4 = 9$.

---

### Step 3: Compute Unique Sum
- $\text{set}(nums) = \{1, 2, 4\}$.
- $s_2 = 1 + 2 + 4 = 7$.

---

### Step 4: Subtract
- $dup = 9 - 7 = 2$.
- $miss = 10 - 7 = 3$.
- Return **`[2, 3]`**.

---

## 4. Complete Execution Trace

| Metric | Formula | Evaluated Value | Meaning |
|:---:|:---:|:---:|:---:|
| $s_1$ | $n(n+1)/2$ | **$10$** | Sum of $\{1, 2, 3, 4\}$ |
| $s$ | $\sum nums$ | **$9$** | Sum of $[1, 2, 2, 4]$ |
| $s_2$ | $\sum \text{set}(nums)$ | **$7$** | Sum of $\{1, 2, 4\}$ |
| **$dup$** | $s - s_2$ | **`2`** | Extra duplicate value |
| **$miss$** | $s_1 - s_2$ | **`3`** | Value omitted from set |
| **Output** | $[dup, miss]$ | **`[2, 3]`** | Final result pair |

---

## 5. Boundary Cases & Failure Modes

- **$n = 2$ ($[1, 1]$ or $[2, 2]$):** Base case; computes flawlessly.
- **Missing Value is 1 ($[2, 2]$):** $s_1 = 3, s = 4, s_2 = 2 \implies dup = 4-2=2, miss = 3-2=1 \implies [2, 1]$.
- **Missing Value is $n$ ($[1, 1]$):** $dup = 1, miss = 2 \implies [1, 2]$.
- **Large Array ($n = 10^4$):** Sums easily fit inside standard integers.

---

## 6. Traps & Common Anti-Patterns

- **Returning in Wrong Order (`[miss, dup]`):** The problem strictly specifies returning `[duplicate, missing]`. Inverting the order fails validation.
- **Sorting First ($O(N \log N)$):** Sorting the array takes unnecessary extra time; set sum arithmetic runs in strictly linear $O(N)$ time.
- **Integer Overflow in Other Languages:** In C++, $n(n+1)/2$ for $n = 10^5$ can exceed 32-bit signed integer limits; use 64-bit integer (`long long`).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - One pass to compute $s = \text{sum}(nums)$: $\mathcal{O}(N)$.
  - One pass to insert into hash set and sum: $\mathcal{O}(N)$.
  - Total Time: strictly linear $\mathcal{O}(N)$. For $N = 10^4$, completes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to store the hash set of unique numbers.
