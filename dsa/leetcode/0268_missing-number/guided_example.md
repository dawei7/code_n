# Guided Example: Missing Number

We trace the step-by-step Gauss arithmetic series summation, bitwise XOR self-cancellation, and single-pass index differential on representative integer array instances:

- **Input:** $\text{nums} = [3, 0, 1]$
- **Required output:** $2$ (Array has length $n = 3$, containing elements from range $[0, 3]$; the missing value is $2$)
- **Terminal Element Missing:** $\text{nums} = [0, 1] \implies 2$ ($n = 2$; range $[0, 2]$; $2$ is omitted)
- **Zero Missing Instance:** $\text{nums} = [1, 2] \implies 0$ ($n = 2$; range $[0, 2]$; $0$ is omitted)
- **Nine Elements Instance:** $\text{nums} = [9, 6, 4, 2, 3, 5, 7, 0, 1] \implies 8$ ($n = 9$; sum deficit reveals $8$)

This instance demonstrates arithmetic series conservation and bitwise XOR algebra, proves why subtracting the array sum from the expected Gauss sum $\frac{n(n + 1)}{2}$ yields the missing element in $O(N)$ time and $O(1)$ space, details the XOR cancellation alternative which eliminates integer overflow risk, and compares both against $O(N \log N)$ sorting.

---

## 1. Instance & Teaching Goal

Given an array of $n = 3$ distinct integers from the inclusive range $[0, 3]$:
$$
\text{nums} = [3, 0, 1]
$$
Find the single missing number from $[0, n]$.
- Full range: $\{0, 1, 2, 3\}$
- Present elements: $\{0, 1, 3\}$
- Missing element: $\mathbf{2}$

A hash set requires $O(N)$ auxiliary memory.
Sorting requires $O(N \log N)$ time.
We solve this in strictly **$O(N)$ linear time and $O(1)$ auxiliary space** using either:
1. **Gauss Closed-Form Summation:** $\frac{n(n + 1)}{2} - \sum \text{nums}$
2. **Bitwise XOR Cancellation:** $\bigoplus_{i=0}^n i \oplus \bigoplus_{x \in \text{nums}} x$

---

## 2. Conceptual Foundation & Invariants

### Method A: Gauss Arithmetic Series Sum
The sum of all integers from $0$ to $n$ is given by Gauss's formula:
$$
S_n = \sum_{i=0}^n i = \frac{n(n + 1)}{2}
$$
Let $A = \sum_{x \in \text{nums}} x$ be the sum of the $n$ distinct numbers present in the array.
Because exactly one integer $m \in [0, n]$ is absent:
$$
S_n - A = \left(\sum_{i=0}^n i\right) - \left(\sum_{i=0, i \ne m}^n i\right) = m
$$
The missing integer $m$ is simply $S_n - A$!

### Method B: Bitwise XOR Self-Cancellation
Bitwise XOR satisfies:
1. $x \oplus x = 0$ (Self-inverse)
2. $x \oplus 0 = x$ (Identity)
3. Commutative and associative: ordering does not matter.

Consider the combined XOR of all numbers in $[0, n]$ and all numbers in `nums`:
$$
\text{res} = \left( \bigoplus_{i=0}^n i \right) \oplus \left( \bigoplus_{x \in \text{nums}} x \right)
$$
Every number present in `nums` appears twice (once in the range $[0, n]$ and once in `nums`), canceling to $0$:
$$
x \oplus x = 0
$$
The missing number $m$ appears **only once** (in the range $[0, n]$), so it survives:
$$
0 \oplus m = m
$$
We can compute this in a single loop by initializing $\text{res} = n$ and XORing $i \oplus \text{nums}[i]$ for $i = 0 \dots n - 1$:
$$
\text{res} = n \oplus \bigoplus_{i=0}^{n-1} (i \oplus \text{nums}[i])
$$

> **Invariant.** After processing index $i$, all numbers present in both the range $[0, i]$ and the prefix $\text{nums}[0 \dots i]$ have canceled out, preserving the missing element's parity.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{nums} = [3, 0, 1]$ ($n = 3$):

### Execution via Method A: Gauss Summation
- Length: $n = 3$.
- Expected sum:
  $$
  S_3 = \frac{3 \times (3 + 1)}{2} = \frac{3 \times 4}{2} = \mathbf{6}
  $$
- Actual array sum:
  $$
  A = 3 + 0 + 1 = \mathbf{4}
  $$
- Difference:
  $$
  \text{missing} = S_3 - A = 6 - 4 = \mathbf{2}
  $$

---

### Execution via Method B: Bitwise XOR
Initialize $\text{res} = n = 3$.

- **Iteration $i = 0$ ($\text{nums}[0] = 3$):**
  $$
  \text{res} \leftarrow \text{res} \oplus 0 \oplus \text{nums}[0] = 3 \oplus 0 \oplus 3 = (3 \oplus 3) \oplus 0 = 0 \oplus 0 = \mathbf{0}
  $$

- **Iteration $i = 1$ ($\text{nums}[1] = 0$):**
  $$
  \text{res} \leftarrow \text{res} \oplus 1 \oplus \text{nums}[1] = 0 \oplus 1 \oplus 0 = \mathbf{1}
  $$

- **Iteration $i = 2$ ($\text{nums}[2] = 1$):**
  $$
  \text{res} \leftarrow \text{res} \oplus 2 \oplus \text{nums}[2] = 1 \oplus 2 \oplus 1 = (1 \oplus 1) \oplus 2 = 0 \oplus 2 = \mathbf{2}
  $$

Loop terminates. Result: $\mathbf{2}$.

---

## 4. Complete Execution Trace

```text
nums = [3, 0, 1], n = 3

Gauss Method:
  Expected: 3 * (3 + 1) / 2 = 6
  Actual:   3 + 0 + 1 = 4
  Missing:  6 - 4 = 2

Bitwise XOR Method:
  Initial res = 3
  i = 0: res = 3 ^ 0 ^ 3 = 0
  i = 1: res = 0 ^ 1 ^ 0 = 1
  i = 2: res = 1 ^ 2 ^ 1 = 2

Output: 2
```

| Step $i$ | Range Index $i$ | Array Element $\text{nums}[i]$ | XOR Term ($i \oplus \text{nums}[i]$) | Cumulative XOR ($\text{res}$) | Cumulative Sum ($A$) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Initial | - | - | - | $n = 3$ | 0 |
| **0** | 0 | 3 | $0 \oplus 3 = 3$ | $3 \oplus 3 = 0$ | $0 + 3 = 3$ |
| **1** | 1 | 0 | $1 \oplus 0 = 1$ | $0 \oplus 1 = 1$ | $3 + 0 = 3$ |
| **2** | 2 | 1 | $2 \oplus 1 = 3$ | $1 \oplus 3 = \mathbf{2}$ | $3 + 1 = \mathbf{4}$ |
| **End** | - | - | - | **$\mathbf{2}$ (Final Answer)** | $S_3 - 4 = 6 - 4 = \mathbf{2}$ |

---

## 5. Algorithmic Correctness

**Soundness.** Because the array contains $n$ distinct integers from the $(n + 1)$-element set $\{0, 1, \dots, n\}$, exactly one element $m$ is missing. Both addition and XOR are commutative and associative. Subtracting the actual sum from the complete sum leaves $m$. In the XOR approach, $x \oplus x = 0$ guarantees that all $n$ present numbers vanish, leaving $0 \oplus m = m$.

**Completeness.** No index or value is omitted. Every index $0 \dots n - 1$ and the final value $n$ are included in the calculation.

---

## 6. Traps This Instance Exposes

- **Integer Overflow in Gauss Summation:** In languages with fixed 32-bit signed integers (like Java or C++), if $n = 10^5$, $\frac{n(n + 1)}{2} \approx 5 \times 10^9 > 2^{31} - 1$, causing 32-bit integer overflow! The XOR approach operates strictly within bit positions $[0, 17]$ and never overflows, making XOR safer in fixed-width languages.
- **Missing Boundary Values ($0$ or $n$):** If `nums = [0, 1]` ($n = 2$), the missing number is $n = 2$. If `nums = [1, 2]` ($n = 2$), the missing number is $0$. The Gauss sum and XOR methods handle both extremes seamlessly.
- **Modifying the Input Array:** Cycle sort can place elements in-place (`nums[nums[i]]`), but it mutates the input. Summation and XOR are read-only and preserve input integrity.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of `nums`. A single linear pass reads all $N$ elements, performing $O(1)$ operations per element.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space. Only scalar variables (`res`, `expected_sum`, `actual_sum`) are stored.
