# Guided Example: Continuous Subarray Sum

We trace the step-by-step modular prefix sum congruence ($(P[i] - P[j]) \pmod k == 0 \iff P[i] \equiv P[j] \pmod k$), earliest-seen index preservation in hash map ($d[r] = \min(index)$), minimum length thresholding ($i - d[r] \ge 2$), and zero-remainder pre-grounding ($d[0] = -1$) on representative integer sequences:

- **Input:** $nums = [23, 2, 4, 6, 7], \quad k = 6$
- **Required output:** `true`
  - Good subarray definition:
    1. Length of contiguous segment is $\ge 2$ ($i - j \ge 2$).
    2. Sum of elements in the subarray is an integer multiple of $k$ ($\sum \pmod k == 0$).
- **Prefix Sum Modulo Congruence Trace:**
  - Let $P[i]$ be the prefix sum up to index $i$:
    $$
    \text{Sum}(j + 1 \dots i) = P[i] - P[j]
    $$
  - Divisibility by $k$:
    $$
    (P[i] - P[j]) \pmod k = 0 \iff P[i] \pmod k = P[j] \pmod k
    $$
  - Subarray length is $(i - j)$. Requirement: $i - j \ge 2 \iff i - j > 1$.
  - Initialize remainder dictionary with virtual base index:
    $$
    d = \{0: -1\}
    $$
    *(Remainder $0$ at index $-1$ allows a subarray starting at index $0$ to qualify if its prefix sum itself is a multiple of $k$)*
  - Running prefix accumulator: $s = 0$.
  - **Index 0 ($x = 23$):**
    - Update running sum modulo $k$:
      $$
      s \leftarrow (0 + 23) \pmod 6 = 23 \pmod 6 = \mathbf{5}
      $$
    - Is remainder $5$ in $d$? No.
    - Record earliest appearance:
      $$
      d[5] \leftarrow 0
      $$
    - State: $d = \{0: -1, \; 5: 0\}$.
  - **Index 1 ($x = 2$):**
    - Update running sum modulo $k$:
      $$
      s \leftarrow (5 + 2) \pmod 6 = 7 \pmod 6 = \mathbf{1}
      $$
    - Is remainder $1$ in $d$? No.
    - Record earliest appearance:
      $$
      d[1] \leftarrow 1
      $$
    - State: $d = \{0: -1, \; 5: 0, \; 1: 1\}$.
  - **Index 2 ($x = 4$):**
    - Update running sum modulo $k$:
      $$
      s \leftarrow (1 + 4) \pmod 6 = 5 \pmod 6 = \mathbf{5}
      $$
    - Is remainder $5$ in $d$? **Yes!**
    - Earliest seen index for remainder $5$: $d[5] = 0$.
    - Check length of span:
      $$
      \text{length} = i - d[5] = 2 - 0 = \mathbf{2}
      $$
    - Check constraint: $\text{length} = 2 \ge 2$ (Pass!).
    - Elements in this span: $nums[1 \dots 2] = [2, 4]$.
    - Sum: $2 + 4 = 6$, which is $1 \times 6$ (exact multiple of $k$).
    - Early return: **`true`**!
- **Zero Prefix Multiple Instance ($nums = [6, 12], k = 6$):**
  - Index 0: $s = 0 \implies 0 - (-1) = 1 < 2$.
  - Index 1: $s = 0 \implies 1 - (-1) = 2 \ge 2 \implies \mathbf{true}$.
- **Length 1 Failure Instance ($nums = [6], k = 6$):**
  - Single element: $i - d[0] = 0 - (-1) = 1 \ngtr 1 \implies \mathbf{false}$.
- **Zeros in Array ($nums = [0, 0], k = 1$):**
  - $s = 0 \implies 1 - (-1) = 2 \ge 2 \implies \mathbf{true}$ ($0$ is a multiple of any $k$).

This instance demonstrates hash-accelerated prefix difference congruence, mathematically proves why keeping the earliest index maximizes candidate span lengths, and derives $O(N)$ runtime and $O(\min(N, k))$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums = [23, 2, 4, 6, 7]$ and an integer $k = 6$:
A **good subarray** is a contiguous segment of $nums$ such that:
1. Its length is at least $2$.
2. The sum of the elements in the subarray is an integer multiple of $k$ ($n \times k$, including $0$).
Return `true` if a good subarray exists, and `false` otherwise.

```text
Array: [ 23,   2,   4,   6,   7 ],  k = 6

Prefix sums:
  Index -1: Sum =  0, Remainder = 0 mod 6 = 0
  Index  0: Sum = 23, Remainder = 23 mod 6 = 5
  Index  1: Sum = 25, Remainder = 25 mod 6 = 1
  Index  2: Sum = 29, Remainder = 29 mod 6 = 5  <- Remainder 5 repeated!

Between Index 0 and Index 2:
  Remainder 5 appeared at index 0 and reappeared at index 2.
  Subarray = nums[1..2] = [2, 4].
  Sum = 6 (multiple of 6!), Length = 2 - 0 = 2 >= 2.
Output: true
```

### The Modular Congruence Invariant
Why does matching remainders guarantee a multiple of $k$?
- Let $P[i] = \sum_{m=0}^i nums[m]$ be the prefix sum.
- The sum of the subarray between index $j + 1$ and index $i$ is:
  $$
  S(j + 1 \dots i) = P[i] - P[j]
  $$
- In modular arithmetic:
  $$
  (P[i] - P[j]) \equiv 0 \pmod k \iff P[i] \pmod k = P[j] \pmod k
  $$
- Therefore, whenever the running remainder $P[i] \pmod k$ repeats a value previously seen at $P[j] \pmod k$, the elements in between **must sum to a multiple of $k$**!

---

## 2. Conceptual Foundation & Invariants

### 1. Hash Map State Representation:
Maintain dictionary $d$ mapping `remainder -> earliest_index`:
- **Initial Sentinel:** $d[0] = -1$.
  If the prefix sum from index $0$ to $i$ is divisible by $k$, its remainder is $0$.
  The length is $i - (-1) = i + 1$. For $i \ge 1$, this subarray has length $\ge 2$.
- **Never Overwrite Existing Remainders:**
  If a remainder $s$ is already present in $d$, **do not update it**!
  Keeping the earliest index maximizes the distance $i - d[s]$, maximizing the likelihood that $i - d[s] \ge 2$.

### 2. The Verification Step:
For each element $nums[i]$:
1. $s \leftarrow (s + nums[i]) \pmod k$.
2. If $s \notin d$:
   $$
   d[s] = i
   $$
3. Elif $i - d[s] > 1$:
   $$
   \text{Return } \mathbf{True}
   $$

> **Earliest Index Invariant.** Retaining the first occurrence of each remainder in $d$ guarantees that any subsequent matching remainder evaluates the maximum possible subarray length.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [23, 2, 4, 6, 7]$ with $k = 6$:

---

### Step 1: Initialize
- $d = \{0: -1\}$
- $s = 0$

---

### Step 2: Index 0 ($nums[0] = 23$)
- Update remainder:
  $$
  s \leftarrow (0 + 23) \pmod 6 = \mathbf{5}
  $$
- Is $5 \in d$? No.
- Record: $d[5] = 0$.
- Hash map: $\{0: -1, \; 5: 0\}$.

---

### Step 3: Index 1 ($nums[1] = 2$)
- Update remainder:
  $$
  s \leftarrow (5 + 2) \pmod 6 = 7 \pmod 6 = \mathbf{1}
  $$
- Is $1 \in d$? No.
- Record: $d[1] = 1$.
- Hash map: $\{0: -1, \; 5: 0, \; 1: 1\}$.

---

### Step 4: Index 2 ($nums[2] = 4$)
- Update remainder:
  $$
  s \leftarrow (1 + 4) \pmod 6 = 5 \pmod 6 = \mathbf{5}
  $$
- Is $5 \in d$? **Yes!**
- Retrieve earliest appearance: $d[5] = 0$.
- Check length condition:
  $$
  i - d[5] = 2 - 0 = \mathbf{2} > 1
  $$
- Valid good subarray found ($nums[1 \dots 2] = [2, 4]$, sum $= 6$).
- Return **`True`**.

---

## 4. Complete Execution Trace

| Index $i$ | Value $nums[i]$ | Running Remainder $s = (s + x) \pmod k$ | $s$ in Hash Map $d$? | Earliest Index $d[s]$ | Span Length $i - d[s]$ | Length $\ge 2$? | Action / Return |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **Init** | — | $0$ | Yes (Sentinel) | $-1$ | — | — | $d[0] = -1$ |
| **$0$** | $23$ | $5$ | No | — | — | — | Store $d[5] = 0$ |
| **$1$** | $2$ | $1$ | No | — | — | — | Store $d[1] = 1$ |
| **$2$** | $4$ | **$5$** | **Yes** | $0$ | $2 - 0 = \mathbf{2}$ | **Yes** | **Return `True`** |

---

## 5. Boundary Cases & Failure Modes

- **Subarray Sum Exactly Zero ($nums = [0, 0], k = 1$):**
  - $0 + 0 = 0$, and $0$ is an integer multiple of $k$ ($0 = 0 \times k$) $\implies \mathbf{true}$.
- **Length 1 Single Element Divisible by $k$ ($nums = [6], k = 6$):**
  - $s = 0$, $d[0] = -1 \implies i - d[0] = 0 - (-1) = 1 \ngtr 1 \implies \mathbf{false}$ (requires length $\ge 2$).
- **No Divisible Subarray Exists ($nums = [23, 2, 6, 4, 7], k = 13$):**
  - Traverses entire array without any duplicate remainder $\implies \mathbf{false}$.

---

## 6. Traps & Common Anti-Patterns

- **Overwriting Existing Remainders:** Writing `d[s] = i` unconditionally resets the earliest index to the current index, shrinking the calculated distance $i - d[s]$ to 0 and missing valid length $\ge 2$ subarrays.
- **Forgetting Sentinel $d[0] = -1$:** If the subarray starting from index 0 itself is divisible (e.g. $[23, 1]$ with $k = 6 \implies 24$), omitting $d[0] = -1$ stores $d[0] = 1$ on the second element instead of recognizing that $nums[0 \dots 1]$ is valid.
- **Using $O(N^2)$ Nested Loops:** Checking all $\frac{N^2}{2}$ subarrays causes Time Limit Exceeded for $N = 10^5$. Modular prefix hashing runs in linear $O(N)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Single pass over the array of length $N$.
  - Each step performs one modular addition and one hash map lookup in $O(1)$ amortized time.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^5$, completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(\min(N, k))$ extra space to store at most $\min(N, k)$ distinct remainders in dictionary $d$.
