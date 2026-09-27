# Guided Example: 4Sum

We trace the step-by-step nested two-pointer search on a representative array instance:

- **Input:** $\text{nums} = [1, 0, -1, 0, -2, 2]$, $\text{target} = 0$
- **Required output:** `[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]`

This instance demonstrates sorting, fixing dual outer anchors to reduce $4\text{Sum}$ to $2\text{Sum}$, bidirectional two-pointer scanning, duplicate pruning, and early-pruning bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums}$ and an integer $\text{target}$, we must return all unique quadruplets $[a, b, c, d]$ such that:
1. $a, b, c, d$ come from four distinct indices.
2. $a + b + c + d = \text{target}$.
3. No duplicate value quadruplets are returned.

For $\text{nums} = [1, 0, -1, 0, -2, 2]$ and $\text{target} = 0$:
- Sorting yields $\text{nums} = [-2, -1, 0, 0, 1, 2]$.
- Three distinct value quadruplets sum to $0$:
  - $[-2, -1, 1, 2] \implies -2 + (-1) + 1 + 2 = 0$
  - $[-2, 0, 0, 2] \implies -2 + 0 + 0 + 2 = 0$
  - $[-1, 0, 0, 1] \implies -1 + 0 + 0 + 1 = 0$

A naive search evaluates all $\binom{N}{4} = O(N^4)$ quadruplets. Sorting the array allows us to fix two anchor indices $i < j$ and find all valid pairs $(k, l)$ in the remaining suffix in linear time using two pointers, reducing the overall time complexity to $O(N^3)$.

---

## 2. Conceptual Foundation & Invariants

### Problem Reduction Hierarchy
We decompose the 4Sum problem hierarchically:
- Outer loop fixes index $i$ ($0 \le i \le N - 4$).
- Middle loop fixes index $j$ ($i + 1 \le j \le N - 3$).
- Inner loop runs a two-pointer scan with $k = j + 1$ and $l = N - 1$ on the sorted subsegment.

At each step, we evaluate the sum:
$$
S = \text{nums}[i] + \text{nums}[j] + \text{nums}[k] + \text{nums}[l]
$$

### Duplicate Elimination Rules
To ensure the output contains only unique quadruplets without hashing overhead:
1. **Outer loop duplicate skip:** If $i > 0$ and $\text{nums}[i] = \text{nums}[i-1]$, skip $i$.
2. **Middle loop duplicate skip:** If $j > i + 1$ and $\text{nums}[j] = \text{nums}[j-1]$, skip $j$.
3. **Inner two-pointer duplicate skip:** Upon finding $S = \text{target}$, record the quadruplet, then advance $k$ past any duplicate elements ($\text{nums}[k] = \text{nums}[k+1]$) and decrement $l$ past duplicate elements ($\text{nums}[l] = \text{nums}[l-1]$).

> **Invariant.** At each outer state $(i, j)$, all quadruplets beginning with lexicographically earlier pairs have been recorded. Pointers $k$ and $l$ explore the remaining suffix monotonically so that no valid configuration is skipped.

---

## 3. Step-by-Step Worked Execution

We sort the array:
$$
\text{nums} = [-2, -1, 0, 0, 1, 2] \quad (N = 6)
$$

### Anchor 1: $i = 0$ ($\text{nums}[0] = -2$)

#### Sub-anchor: $j = 1$ ($\text{nums}[1] = -1$)
We need suffix pair sum $\text{nums}[k] + \text{nums}[l] = \text{target} - (\text{nums}[0] + \text{nums}[1]) = 0 - (-3) = 3$.
Pointers initialize at $k = 2$ ($\text{nums}[2] = 0$) and $l = 5$ ($\text{nums}[5] = 2$).

- **Step 1 ($k=2, l=5$):**
  - Sum $S = -2 + (-1) + 0 + 2 = -1 < 0$.
  - Sum too small $\implies$ advance $k \leftarrow 3$.
- **Step 2 ($k=3, l=5$):**
  - Sum $S = -2 + (-1) + 0 + 2 = -1 < 0$.
  - Sum too small $\implies$ advance $k \leftarrow 4$.
- **Step 3 ($k=4, l=5$):**
  - Elements: $\text{nums}[4] = 1, \text{nums}[5] = 2$.
  - Sum $S = -2 + (-1) + 1 + 2 = 0$. Match!
  - Record quadruplet: `[-2, -1, 1, 2]`.
  - Shift pointers: $k \leftarrow 5, l \leftarrow 4$. Pointers cross; terminate sub-anchor.

---

#### Sub-anchor: $j = 2$ ($\text{nums}[2] = 0$)
We need suffix pair sum $0 - (-2 + 0) = 2$.
Pointers initialize at $k = 3$ ($\text{nums}[3] = 0$) and $l = 5$ ($\text{nums}[5] = 2$).

- **Step 4 ($k=3, l=5$):**
  - Sum $S = -2 + 0 + 0 + 2 = 0$. Match!
  - Record quadruplet: `[-2, 0, 0, 2]`.
  - Shift pointers: $k \leftarrow 4, l \leftarrow 4$. Pointers cross; terminate sub-anchor.

---

#### Sub-anchor: $j = 3$ ($\text{nums}[3] = 0$)
Since $\text{nums}[3] = \text{nums}[2] = 0$ and $j > i + 1$, this duplicate sub-anchor is skipped.

---

### Anchor 2: $i = 1$ ($\text{nums}[1] = -1$)

#### Sub-anchor: $j = 2$ ($\text{nums}[2] = 0$)
We need suffix pair sum $0 - (-1 + 0) = 1$.
Pointers initialize at $k = 3$ ($\text{nums}[3] = 0$) and $l = 5$ ($\text{nums}[5] = 2$).

- **Step 5 ($k=3, l=5$):**
  - Sum $S = -1 + 0 + 0 + 2 = 1 > 0$.
  - Sum too large $\implies$ decrement $l \leftarrow 4$.
- **Step 6 ($k=3, l=4$):**
  - Elements: $\text{nums}[3] = 0, \text{nums}[4] = 1$.
  - Sum $S = -1 + 0 + 0 + 1 = 0$. Match!
  - Record quadruplet: `[-1, 0, 0, 1]`.
  - Shift pointers: $k \leftarrow 4, l \leftarrow 3$. Pointers cross; terminate sub-anchor.

---

#### Sub-anchor: $j = 3$ ($\text{nums}[3] = 0$)
Duplicate element ($\text{nums}[3] = \text{nums}[2] = 0$); skipped.

---

### Anchor 3: $i = 2$ ($\text{nums}[2] = 0$)
Minimum possible sum using $i = 2$ is $\text{nums}[2] + \text{nums}[3] + \text{nums}[4] + \text{nums}[5] = 0 + 0 + 1 + 2 = 3 > 0$.
Early exit: no further solutions can sum to $0$.

---

## 4. Complete Execution Trace

| Step | Anchor $i$ | Sub-anchor $j$ | Left $k$ | Right $l$ | Values $(a, b, c, d)$ | Quadruplet Sum $S$ | Comparison to Target (0) | Action Taken |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 0 | 1 | 2 | 5 | $(-2, -1, 0, 2)$ | $-1$ | Too small ($S < 0$) | Advance $k \leftarrow 3$ |
| 2 | 0 | 1 | 3 | 5 | $(-2, -1, 0, 2)$ | $-1$ | Too small ($S < 0$) | Advance $k \leftarrow 4$ |
| 3 | 0 | 1 | 4 | 5 | $(-2, -1, 1, 2)$ | $0$ | **Exact match** | **Emit `[-2, -1, 1, 2]`**; shift both |
| 4 | 0 | 2 | 3 | 5 | $(-2, 0, 0, 2)$ | $0$ | **Exact match** | **Emit `[-2, 0, 0, 2]`**; shift both |
| - | 0 | 3 | - | - | - | - | Duplicate sub-anchor | Skip $j = 3$ |
| 5 | 1 | 2 | 3 | 5 | $(-1, 0, 0, 2)$ | $1$ | Too large ($S > 0$) | Decrement $l \leftarrow 4$ |
| 6 | 1 | 2 | 3 | 4 | $(-1, 0, 0, 1)$ | $0$ | **Exact match** | **Emit `[-1, 0, 0, 1]`**; shift both |
| - | 1 | 3 | - | - | - | - | Duplicate sub-anchor | Skip $j = 3$ |
| - | 2 | - | - | - | - | - | Min sum $3 > 0$ | Early exit |

---

## 5. Algorithmic Correctness

**Soundness.** Every emitted quadruplet satisfies $a + b + c + d = \text{target}$. Because elements are picked from distinct sorted indices $i < j < k < l$, all four values represent four distinct array positions. Duplicate checks on adjacent equal elements guarantee that every emitted quadruplet is unique.

**Completeness.** Sorting orders the search space monotonically. For any pair of anchors $(i, j)$, the inner two-pointer search on $[j+1, N-1]$ scans from opposite ends. When $S < \text{target}$, discarding $k$ is sound because any inner right index $l' < l$ would only yield an even smaller sum. Symmetrically, when $S > \text{target}$, discarding $l$ is sound. Thus, no valid combinations are omitted.

---

## 6. Traps This Instance Exposes

- **Duplicate Subsets Without a Hash Set:** Relying on a hash set to filter duplicates incurs significant memory overhead. Skipping identical adjacent values ($s[i] == s[i-1]$ and $s[j] == s[j-1]$) suppresses duplicates naturally at zero extra space cost.
- **Integer Overflow in Fixed-Width Languages:** When summing four integers up to $10^9$, the intermediate sum can reach $4 \times 10^9$, overflowing signed 32-bit integers ($\approx 2.14 \times 10^9$). In languages like C++ or Java, 64-bit integers (`long long` or `long`) must be used for accumulator calculations.
- **Input Length Boundary ($N < 4$):** If the array has fewer than 4 elements, four distinct indices cannot be chosen. Guarding with `if len(nums) < 4: return []` prevents index out-of-bounds.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^3)$. Sorting takes $O(N \log N)$. The outer loop runs $O(N)$ times, the middle loop runs $O(N)$ times, and the inner two-pointer scan runs in $O(N)$ time. The total time is $O(N \log N + N^2 \cdot N) = O(N^3)$.
- **Auxiliary Space Complexity:** $O(1)$ beyond sorting. The algorithm maintains only a constant number of scalar index pointers.
